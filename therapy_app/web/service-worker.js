// Service Worker for The Bread Therapist Collective PWA
// Provides offline functionality, caching, and background sync

const CACHE_VERSION = 'v1.1.0';
const CACHE_NAME = `bread-therapy-${CACHE_VERSION}`;

// Assets to cache immediately on install
const STATIC_ASSETS = [
    '/',
    '/index.html',
    '/styles.css',
    '/app.js',
    '/manifest.json',
    '/assets/icon-192.png',
    '/assets/icon-512.png'
];

// Install event - cache static assets
self.addEventListener('install', (event) => {
    console.log('[Service Worker] Installing...', CACHE_VERSION);

    event.waitUntil(
        caches.open(CACHE_NAME)
            .then((cache) => {
                console.log('[Service Worker] Caching static assets');
                return cache.addAll(STATIC_ASSETS);
            })
            .then(() => {
                console.log('[Service Worker] Installation complete');
                return self.skipWaiting(); // Activate immediately
            })
            .catch((error) => {
                console.error('[Service Worker] Installation failed:', error);
            })
    );
});

// Activate event - clean up old caches
self.addEventListener('activate', (event) => {
    console.log('[Service Worker] Activating...', CACHE_VERSION);

    event.waitUntil(
        caches.keys()
            .then((cacheNames) => {
                return Promise.all(
                    cacheNames
                        .filter((name) => name !== CACHE_NAME)
                        .map((name) => {
                            console.log('[Service Worker] Deleting old cache:', name);
                            return caches.delete(name);
                        })
                );
            })
            .then(() => {
                console.log('[Service Worker] Activation complete');
                return self.clients.claim(); // Take control immediately
            })
    );
});

// Fetch event - network-first strategy for API calls, cache-first for assets
self.addEventListener('fetch', (event) => {
    const { request } = event;
    const url = new URL(request.url);

    // Skip cross-origin requests
    if (url.origin !== location.origin && !url.origin.includes('api.openai.com')) {
        return;
    }

    // Network-first strategy for API calls
    if (url.pathname.startsWith('/api/') || url.origin.includes('api.openai.com')) {
        event.respondWith(
            fetch(request)
                .then((response) => {
                    // Clone response for cache
                    const responseClone = response.clone();

                    // Cache successful responses
                    if (response.status === 200) {
                        caches.open(CACHE_NAME).then((cache) => {
                            cache.put(request, responseClone);
                        });
                    }

                    return response;
                })
                .catch(() => {
                    // Return cached version if available
                    return caches.match(request)
                        .then((cachedResponse) => {
                            if (cachedResponse) {
                                return cachedResponse;
                            }
                            // Return offline fallback
                            return new Response(
                                JSON.stringify({
                                    error: 'Offline',
                                    message: 'You are currently offline. Please check your connection.'
                                }),
                                {
                                    status: 503,
                                    headers: { 'Content-Type': 'application/json' }
                                }
                            );
                        });
                })
        );
        return;
    }

    // Cache-first strategy for static assets
    event.respondWith(
        caches.match(request)
            .then((cachedResponse) => {
                if (cachedResponse) {
                    return cachedResponse;
                }

                // Fetch from network and cache
                return fetch(request).then((response) => {
                    // Don't cache non-successful responses
                    if (!response || response.status !== 200 || response.type === 'error') {
                        return response;
                    }

                    const responseClone = response.clone();

                    caches.open(CACHE_NAME).then((cache) => {
                        cache.put(request, responseClone);
                    });

                    return response;
                });
            })
            .catch(() => {
                // Return offline fallback page
                if (request.destination === 'document') {
                    return caches.match('/');
                }
                return new Response('Offline', { status: 503 });
            })
    );
});

// Background sync for queued messages (when connection restored)
self.addEventListener('sync', (event) => {
    console.log('[Service Worker] Background sync triggered:', event.tag);

    if (event.tag === 'sync-messages') {
        event.waitUntil(syncQueuedMessages());
    }
});

// Push notification support (for future feature)
self.addEventListener('push', (event) => {
    console.log('[Service Worker] Push notification received');

    const options = {
        body: event.data ? event.data.text() : 'New notification',
        icon: '/assets/icon-192.png',
        badge: '/assets/icon-96.png',
        vibrate: [200, 100, 200],
        data: {
            dateOfArrival: Date.now(),
            primaryKey: 1
        },
        actions: [
            {
                action: 'open',
                title: 'Open App',
                icon: '/assets/icon-check.png'
            },
            {
                action: 'close',
                title: 'Dismiss',
                icon: '/assets/icon-close.png'
            }
        ]
    };

    event.waitUntil(
        self.registration.showNotification('Bread Therapy', options)
    );
});

// Notification click handler
self.addEventListener('notificationclick', (event) => {
    console.log('[Service Worker] Notification clicked:', event.action);

    event.notification.close();

    if (event.action === 'open') {
        event.waitUntil(
            clients.openWindow('/')
        );
    }
});

// Helper function: Sync queued messages
async function syncQueuedMessages() {
    try {
        // Get queued messages from IndexedDB
        const db = await openDatabase();
        const messages = await getQueuedMessages(db);

        // Send each message
        for (const message of messages) {
            try {
                await sendMessage(message);
                await removeQueuedMessage(db, message.id);
                console.log('[Service Worker] Synced message:', message.id);
            } catch (error) {
                console.error('[Service Worker] Failed to sync message:', error);
            }
        }

        // Notify client that sync is complete
        const clients = await self.clients.matchAll();
        clients.forEach((client) => {
            client.postMessage({
                type: 'SYNC_COMPLETE',
                count: messages.length
            });
        });

    } catch (error) {
        console.error('[Service Worker] Sync failed:', error);
    }
}

// Helper function: Open IndexedDB
function openDatabase() {
    return new Promise((resolve, reject) => {
        const request = indexedDB.open('bread-therapy-db', 1);

        request.onerror = () => reject(request.error);
        request.onsuccess = () => resolve(request.result);

        request.onupgradeneeded = (event) => {
            const db = event.target.result;
            if (!db.objectStoreNames.contains('messages')) {
                db.createObjectStore('messages', { keyPath: 'id', autoIncrement: true });
            }
        };
    });
}

// Helper function: Get queued messages
function getQueuedMessages(db) {
    return new Promise((resolve, reject) => {
        const transaction = db.transaction(['messages'], 'readonly');
        const store = transaction.objectStore('messages');
        const request = store.getAll();

        request.onerror = () => reject(request.error);
        request.onsuccess = () => resolve(request.result);
    });
}

// Helper function: Remove queued message
function removeQueuedMessage(db, id) {
    return new Promise((resolve, reject) => {
        const transaction = db.transaction(['messages'], 'readwrite');
        const store = transaction.objectStore('messages');
        const request = store.delete(id);

        request.onerror = () => reject(request.error);
        request.onsuccess = () => resolve();
    });
}

// Helper function: Send message to API
async function sendMessage(message) {
    const response = await fetch('/api/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(message)
    });

    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }

    return response.json();
}

// Listen for messages from clients
self.addEventListener('message', (event) => {
    console.log('[Service Worker] Message received:', event.data);

    if (event.data.type === 'SKIP_WAITING') {
        self.skipWaiting();
    }

    if (event.data.type === 'CACHE_URLS') {
        event.waitUntil(
            caches.open(CACHE_NAME)
                .then((cache) => cache.addAll(event.data.urls))
        );
    }
});

console.log('[Service Worker] Loaded', CACHE_VERSION);
