# Therapy App Deployment Guide

Complete guide for deploying the Therapy App Progressive Web Application (PWA) to a secure production server using Docker, GitHub Actions, and Watchtower for automated continuous deployment.

---

## Table of Contents

1. [Architecture Overview](#architecture-overview)
2. [Prerequisites](#prerequisites)
3. [Local Testing](#local-testing)
4. [Docker Hub Setup](#docker-hub-setup)
5. [GitHub Secrets Configuration](#github-secrets-configuration)
6. [Server Setup](#server-setup)
7. [Deploy to Production](#deploy-to-production)
8. [Monitoring and Maintenance](#monitoring-and-maintenance)
9. [Troubleshooting](#troubleshooting)
10. [Best Practices](#best-practices)

---

## Architecture Overview

The Therapy App uses a fully automated CI/CD pipeline:

```
┌─────────────┐
│   Developer │
│  git push   │
└──────┬──────┘
       │
       ▼
┌─────────────┐     ┌──────────────┐
│   GitHub    │────▶│GitHub Actions│
│ Repository  │     │  • Run Tests │
└─────────────┘     │  • Build     │
                    │  • Push      │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │  Docker Hub  │
                    │  (Registry)  │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │  Watchtower  │◀─── Checks every 5 min
                    │ (Auto-deploy)│
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │  Production  │
                    │    Server    │
                    │104.131.191.83│
                    └──────────────┘
```

**Key Benefits:**
- ✅ **Automated Testing:** All tests run before deployment
- ✅ **Zero-Downtime:** Rolling updates with health checks
- ✅ **Auto-Deploy:** Push code → automatically deployed in ~5 minutes
- ✅ **Rollback Ready:** Previous images preserved for quick rollback
- ✅ **No SSH Required:** Watchtower handles all deployments

---

## Prerequisites

### Required Accounts
- [x] **GitHub Account:** Repository at `NizaJ27/IS218-AI-Demo`
- [x] **Docker Hub Account:** Free account for image hosting
- [ ] **Digital Ocean Server:** 104.131.191.83 (already provisioned)

### Required Software (Local)
- [x] **Docker Desktop:** For local testing
- [x] **Git:** Version control
- [x] **Python 3.13:** For running tests

### Server Requirements
- Ubuntu 20.04+ with Docker installed
- Minimum 1GB RAM, 1 CPU core
- Public IP: 104.131.191.83
- Ports 80/443 available

---

## Local Testing

Before deploying, test the Docker configuration locally.

### Step 1: Set Up Environment

```bash
# Navigate to therapy app directory
cd therapy_app/

# Create environment file
cp .env.example .env

# Edit environment variables (optional for local testing)
nano .env
```

### Step 2: Build Docker Image

```bash
# Build the image
docker build -t therapy-app:local .

# Verify image was created
docker images | grep therapy-app
```

Expected output:
```
therapy-app  local  abc123def456  2 minutes ago  25MB
```

### Step 3: Run Container Locally

```bash
# Run the container
docker run -d \
  --name therapy-app-test \
  -p 8080:80 \
  therapy-app:local

# Check container is running
docker ps | grep therapy-app
```

### Step 4: Test the Application

```bash
# Test health endpoint
curl http://localhost:8080/health
# Expected: healthy

# Test main application
curl http://localhost:8080/
# Expected: HTML response

# Or open in browser
open http://localhost:8080
```

### Step 5: Check Logs

```bash
# View nginx logs
docker logs therapy-app-test

# Follow logs in real-time
docker logs -f therapy-app-test
```

### Step 6: Stop Test Container

```bash
# Stop and remove test container
docker stop therapy-app-test
docker rm therapy-app-test

# Clean up test image (optional)
docker rmi therapy-app:local
```

✅ **Local testing complete!** If everything works, proceed to Docker Hub setup.

---

## Docker Hub Setup

### Step 1: Create Docker Hub Account

1. Go to https://hub.docker.com
2. Click **Sign Up** (or log in if you have an account)
3. Verify your email address

### Step 2: Create Repository

1. Click **Create Repository** button
2. Fill in details:
   - **Name:** `therapy-app`
   - **Visibility:** Public (recommended for free tier)
   - **Description:** "Therapy App Progressive Web Application - Bread Therapist Collective"
3. Click **Create**

Your repository path: `nizaj27/therapy-app`

### Step 3: Generate Access Token

1. Click your profile → **Account Settings**
2. Navigate to **Security** tab
3. Click **New Access Token**
4. Configure token:
   - **Description:** `github-actions-therapy-app`
   - **Access permissions:** **Read & Write**
5. Click **Generate**
6. **Copy the token immediately** (you won't see it again!)

Token format: `dckr_pat_xxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

⚠️ **Important:** Store this token securely - it's like a password!

---

## GitHub Secrets Configuration

### Step 1: Navigate to Repository Settings

1. Go to your GitHub repository: `github.com/NizaJ27/IS218-AI-Demo`
2. Click **Settings** tab
3. Click **Secrets and variables** → **Actions**

### Step 2: Add Docker Hub Credentials

Click **New repository secret** for each:

**Secret 1: DOCKER_USERNAME**
- Name: `DOCKER_USERNAME`
- Value: `nizaj27` (your Docker Hub username)
- Click **Add secret**

**Secret 2: DOCKER_TOKEN**
- Name: `DOCKER_TOKEN`
- Value: `dckr_pat_xxxxx...` (the access token from Docker Hub)
- Click **Add secret**

### Step 3: Verify Secrets

You should see:
- ✅ DOCKER_USERNAME
- ✅ DOCKER_TOKEN

✅ **GitHub secrets configured!** GitHub Actions can now push to Docker Hub.

---

## Server Setup

Connect to your server and set up the deployment environment.

### Step 1: SSH to Server

```bash
ssh youruser@104.131.191.83
```

### Step 2: Create Application Directory

```bash
# Create directory structure
mkdir -p ~/therapy-app
cd ~/therapy-app

# Verify Docker is installed
docker --version
# Expected: Docker version 20.10.x or higher
```

### Step 3: Create Environment File

```bash
nano .env
```

Add the following configuration:

```env
# Docker Configuration
DOCKER_IMAGE=nizaj27/therapy-app
DOCKER_USERNAME=nizaj27

# Web Server Configuration
WEB_PORT=80

# Watchtower Configuration
WATCHTOWER_POLL_INTERVAL=300
```

**Save and exit** (Ctrl+X, Y, Enter)

### Step 4: Create Docker Compose File

```bash
nano docker-compose.yml
```

Paste the following:

```yaml
version: '3.8'

services:
  web:
    image: ${DOCKER_IMAGE}:latest
    container_name: therapy_app_web
    restart: unless-stopped
    ports:
      - "${WEB_PORT:-80}:80"
    labels:
      - "com.centurylinklabs.watchtower.enable=true"
    healthcheck:
      test: ["CMD", "wget", "--quiet", "--tries=1", "--spider", "http://localhost:80/health"]
      interval: 30s
      timeout: 3s
      retries: 3
      start_period: 10s
    networks:
      - therapy_network

  watchtower:
    image: containrrr/watchtower
    container_name: therapy_app_watchtower
    restart: unless-stopped
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    environment:
      - WATCHTOWER_CLEANUP=true
      - WATCHTOWER_POLL_INTERVAL=${WATCHTOWER_POLL_INTERVAL:-300}
      - WATCHTOWER_LABEL_ENABLE=true
      - WATCHTOWER_INCLUDE_STOPPED=true
      - WATCHTOWER_REVIVE_STOPPED=false
    command: --interval ${WATCHTOWER_POLL_INTERVAL:-300} --cleanup
    networks:
      - therapy_network

networks:
  therapy_network:
    driver: bridge
```

**Save and exit** (Ctrl+X, Y, Enter)

### Step 5: Pull Initial Image (Optional)

If you want to test before setting up CI/CD:

```bash
# Pull the image manually
docker compose pull

# Start services
docker compose up -d

# Check status
docker compose ps

# View logs
docker compose logs -f
```

### Step 6: Configure Firewall

```bash
# Allow HTTP traffic
sudo ufw allow 80/tcp

# Allow HTTPS (for future SSL setup)
sudo ufw allow 443/tcp

# Check firewall status
sudo ufw status
```

### Step 7: Test Deployment

```bash
# Test from server
curl http://localhost/health
# Expected: healthy

# Test from external
curl http://104.131.191.83/
# Expected: HTML response
```

✅ **Server setup complete!** Watchtower is now monitoring for updates.

---

## Deploy to Production

### Step 1: Commit Deployment Configuration

From your local machine:

```bash
# Navigate to project root
cd ~/Desktop/NJIT\ 2025\ Fall/IS\ 218/AI\ Demo\ App/enterprise_ai_demo1_websearch/

# Check what's new
git status

# Add deployment files
git add therapy_app/Dockerfile
git add therapy_app/nginx.conf
git add therapy_app/docker-compose.yml
git add therapy_app/.env.example
git add .github/workflows/deploy.yml

# Commit
git commit -m "feat: add Docker deployment configuration for therapy app

- Add Dockerfile with Nginx for PWA serving
- Add nginx.conf with PWA-specific headers and caching
- Add docker-compose.yml with Watchtower auto-deployment
- Add GitHub Actions workflow for CI/CD pipeline
- Configure health checks and monitoring"

# Push to GitHub
git push origin main
```

### Step 2: Monitor GitHub Actions

1. Go to GitHub repository → **Actions** tab
2. Watch the workflow run:
   - ✅ **Test job:** Runs pytest (must pass 100% coverage)
   - ✅ **Build and push job:** Builds Docker image and pushes to Docker Hub
   - ⏱️ **Duration:** ~3-5 minutes

### Step 3: Verify Docker Hub

1. Go to https://hub.docker.com/r/nizaj27/therapy-app
2. Check **Tags** tab
3. Should see:
   - `latest` tag with recent timestamp
   - Git commit SHA tag

### Step 4: Watch Watchtower Deploy

On your server:

```bash
# Watch Watchtower logs
cd ~/therapy-app
docker compose logs -f watchtower
```

You should see (within 5 minutes):
```
time="2025-01-XX" level=info msg="Found new nizaj27/therapy-app:latest image"
time="2025-01-XX" level=info msg="Stopping /therapy_app_web"
time="2025-01-XX" level=info msg="Removing image"
time="2025-01-XX" level=info msg="Pulling new image"
time="2025-01-XX" level=info msg="Starting /therapy_app_web"
```

### Step 5: Verify Deployment

```bash
# Check container status
docker compose ps
# Should show: therapy_app_web (running)

# Test application
curl http://104.131.191.83/health
# Expected: healthy

curl http://104.131.191.83/
# Expected: HTML response

# Check application logs
docker compose logs web | tail -20
```

### Step 6: Test in Browser

Open in your browser:
- http://104.131.191.83/

You should see the Therapy App PWA! 🎉

---

## Monitoring and Maintenance

### View Logs

**All services:**
```bash
cd ~/therapy-app
docker compose logs -f
```

**Specific service:**
```bash
docker compose logs -f web        # Application logs
docker compose logs -f watchtower # Deployment logs
```

**Last N lines:**
```bash
docker compose logs --tail=50 web
```

### Check Container Status

```bash
# List running containers
docker compose ps

# Detailed stats (CPU, Memory)
docker stats

# Check health status
docker inspect therapy_app_web | grep -A 10 Health
```

### Manual Updates

Force immediate update:
```bash
# Pull latest image
docker compose pull web

# Recreate container
docker compose up -d web

# Verify
docker compose ps
```

### Restart Services

```bash
# Restart specific service
docker compose restart web

# Restart all services
docker compose restart

# Stop all services
docker compose down

# Start all services
docker compose up -d
```

### Disk Space Management

```bash
# Check Docker disk usage
docker system df

# Remove unused images
docker image prune -a

# Remove unused containers
docker container prune

# Remove unused volumes
docker volume prune

# Full cleanup (careful!)
docker system prune -a --volumes
```

### Update Watchtower Settings

Edit `.env` to change check frequency:

```bash
nano .env
```

```env
# Check every 1 minute (testing)
WATCHTOWER_POLL_INTERVAL=60

# Check every 5 minutes (default)
WATCHTOWER_POLL_INTERVAL=300

# Check every hour (production)
WATCHTOWER_POLL_INTERVAL=3600
```

Apply changes:
```bash
docker compose up -d watchtower
```

---

## Troubleshooting

### Issue 1: Watchtower Not Updating

**Check logs:**
```bash
docker compose logs watchtower | tail -50
```

**Common causes:**
- Wrong image name in `.env`
- Labels not set correctly
- Network connectivity issues
- Docker Hub rate limiting

**Solution:**
```bash
# Manually trigger update
docker compose pull web
docker compose up -d web

# Restart Watchtower
docker compose restart watchtower

# Verify image name
cat .env | grep DOCKER_IMAGE
```

### Issue 2: Container Won't Start

**Check logs:**
```bash
docker compose logs web | tail -50
```

**Common causes:**
- Port 80 already in use
- Nginx configuration error
- Health check failing

**Solution:**
```bash
# Check port usage
sudo lsof -i :80

# Check nginx configuration
docker compose exec web nginx -t

# Try different port
nano .env
# Change: WEB_PORT=8080
docker compose up -d
```

### Issue 3: GitHub Actions Build Fails

**Check workflow logs:**
1. Go to repository → **Actions**
2. Click failed workflow
3. Review error messages

**Common issues:**
- Tests failing → Fix tests locally first
- Docker build errors → Test `docker build` locally
- Authentication failed → Verify Docker Hub secrets

**Solution:**
```bash
# Run tests locally
pytest therapy_app/tests/ -v --cov=therapy_app/src

# Test Docker build locally
cd therapy_app/
docker build -t therapy-app:test .

# Verify secrets in GitHub
# Settings → Secrets → Actions
```

### Issue 4: Health Check Failing

**Check health status:**
```bash
docker inspect therapy_app_web | grep -A 20 Health
```

**Test health endpoint:**
```bash
docker compose exec web curl http://localhost:80/health
```

**Common causes:**
- Nginx not responding
- Wrong health check path
- Container crash loop

**Solution:**
```bash
# Check nginx error logs
docker compose exec web cat /var/log/nginx/error.log

# Test nginx configuration
docker compose exec web nginx -t

# Restart container
docker compose restart web
```

### Issue 5: Image Not Found on Docker Hub

**Verify image exists:**
```bash
docker pull nizaj27/therapy-app:latest
```

**If 404 error:**
- Check repository name is correct: `nizaj27/therapy-app`
- Verify repository is public (or Docker Hub credentials configured)
- Ensure GitHub Actions successfully pushed image

**Solution:**
```bash
# Re-push manually from local
cd therapy_app/
docker build -t nizaj27/therapy-app:latest .
docker push nizaj27/therapy-app:latest
```

---

## Best Practices

### 1. Always Test Locally First

Before pushing to GitHub:
```bash
# Run tests
pytest therapy_app/tests/ -v --cov=therapy_app/src

# Build Docker image
docker build -t therapy-app:test therapy_app/

# Test container
docker run -d -p 8080:80 therapy-app:test
curl http://localhost:8080/health
```

### 2. Use Meaningful Commit Messages

Follow conventional commits:
```bash
git commit -m "feat: add user profile functionality"
git commit -m "fix: resolve session storage issue"
git commit -m "docs: update deployment guide"
```

### 3. Monitor Deployments

After pushing:
1. Watch GitHub Actions (3-5 minutes)
2. Watch Watchtower logs (5-10 minutes)
3. Verify deployment in browser
4. Check application logs for errors

### 4. Set Up Alerts

Configure Watchtower notifications:
```env
# Slack notifications
WATCHTOWER_NOTIFICATIONS=slack
WATCHTOWER_NOTIFICATION_URL=https://hooks.slack.com/services/YOUR/WEBHOOK

# Email notifications
WATCHTOWER_NOTIFICATIONS=email
WATCHTOWER_NOTIFICATION_EMAIL_TO=you@example.com
```

### 5. Regular Backups

Although the PWA has no database, backup configuration:
```bash
# Backup server configuration
cd ~/therapy-app
tar -czf therapy-app-backup-$(date +%Y%m%d).tar.gz .env docker-compose.yml

# Download to local machine
scp youruser@104.131.191.83:~/therapy-app/therapy-app-backup-*.tar.gz ~/backups/
```

### 6. SSL/HTTPS Setup (Recommended)

For production, use Caddy for automatic HTTPS:

```bash
# Install Caddy
sudo apt install -y debian-keyring debian-archive-keyring apt-transport-https
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | sudo gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | sudo tee /etc/apt/sources.list.d/caddy-stable.list
sudo apt update
sudo apt install caddy

# Configure Caddyfile
sudo nano /etc/caddy/Caddyfile
```

Add:
```caddyfile
your-domain.com {
    reverse_proxy localhost:80
}
```

```bash
# Reload Caddy
sudo systemctl reload caddy
```

### 7. Resource Limits

Set Docker resource limits in production:
```yaml
services:
  web:
    deploy:
      resources:
        limits:
          cpus: '1'
          memory: 256M
        reservations:
          cpus: '0.5'
          memory: 128M
```

---

## Quick Reference

### Essential Commands

**Server:**
```bash
cd ~/therapy-app

# View logs
docker compose logs -f

# Restart service
docker compose restart web

# Pull updates manually
docker compose pull && docker compose up -d

# Check status
docker compose ps

# View Watchtower activity
docker compose logs watchtower --tail=50

# Stop all services
docker compose down
```

**Local:**
```bash
# Build and test
docker build -t therapy-app:test therapy_app/
docker run -d -p 8080:80 therapy-app:test

# Deploy
git add .
git commit -m "feat: update therapy app"
git push origin main

# Monitor GitHub Actions
# → Go to github.com/NizaJ27/IS218-AI-Demo/actions
```

---

## Summary

**What You've Accomplished:**

✅ Fully automated CI/CD pipeline  
✅ Docker containerization with Nginx  
✅ Automated testing before deployment  
✅ Zero-downtime deployments with Watchtower  
✅ Health checks and monitoring  
✅ Production-ready configuration  

**Your Deployment Workflow:**

1. Write code locally
2. Run tests: `pytest therapy_app/tests/`
3. Commit and push: `git push origin main`
4. ✨ **GitHub Actions builds and tests automatically**
5. ✨ **Docker image pushed to Docker Hub automatically**
6. ✨ **Watchtower deploys to server automatically (~5 min)**
7. Visit http://104.131.191.83/ to see changes live! 🎉

**Next Steps:**

- [ ] Configure custom domain with Caddy
- [ ] Set up SSL/HTTPS
- [ ] Configure monitoring alerts
- [ ] Add staging environment
- [ ] Set up automated backups

---

**Need Help?**

- Docker documentation: https://docs.docker.com
- GitHub Actions docs: https://docs.github.com/actions
- Watchtower docs: https://containrrr.dev/watchtower/

---

*Generated for Therapy App PWA - Bread Therapist Collective*  
*Server: 104.131.191.83 | Repository: NizaJ27/IS218-AI-Demo*
