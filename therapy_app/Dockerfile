# Multi-stage build for therapy_app PWA
# Stage 1: Build stage (optional, for future JavaScript build steps)
FROM node:20-alpine AS builder

WORKDIR /app

# Copy PWA files
COPY web/ ./web/

# In the future, add build steps here if needed:
# RUN npm install && npm run build

# Stage 2: Production stage with Nginx
FROM nginx:alpine

# Copy custom nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy PWA files from builder stage
COPY --from=builder /app/web /usr/share/nginx/html

# Create directory for user data (if needed for future backend)
RUN mkdir -p /usr/share/nginx/html/user_data

# Set proper permissions
RUN chown -R nginx:nginx /usr/share/nginx/html && \
    chmod -R 755 /usr/share/nginx/html

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD wget --quiet --tries=1 --spider http://localhost:80/ || exit 1

# Expose port 80
EXPOSE 80

# Nginx runs as daemon off in official image
CMD ["nginx", "-g", "daemon off;"]
