# Chapter 22: Module 14 Deployment with CI/CD

[← Previous: Chapter 21 - CI/CD with GitHub Actions](21-cicd-github-actions.md)

---

## Overview

This chapter guides you through deploying **Module 14** - a FastAPI web application with JWT authentication, PostgreSQL database, and calculation BREAD operations - using automated CI/CD. You'll set up:

1. **Docker Hub** for image storage
2. **GitHub Actions** for automated build and push
3. **Watchtower** on your server for auto-deployment
4. Complete CI/CD pipeline from code to production

**Time Requirement:** 60-90 minutes

**Prerequisites:**
- Completed Chapters 1-21
- Secure web server running (Digital Ocean droplet at 104.131.191.83)
- Domain name configured (optional but recommended)
- GitHub account (NizaJ27)
- Docker Hub account (free)
- Module 14 repository: https://github.com/NizaJ27/IS218-Module-14

---

## Architecture Overview

```
Developer Flow:
┌─────────────────────────────────────────────────────────────┐
│ 1. Push code to GitHub                                       │
│    ↓                                                          │
│ 2. GitHub Actions triggers                                   │
│    ├─ Run tests                                             │
│    ├─ Build Docker image                                    │
│    └─ Push image to Docker Hub                              │
│                                                               │
│ 3. Watchtower on server                                      │
│    ├─ Detects new image on Docker Hub                       │
│    ├─ Pulls latest image                                    │
│    ├─ Stops old container                                   │
│    └─ Starts new container                                  │
│                                                               │
│ 4. Application is live! ✅                                   │
└─────────────────────────────────────────────────────────────┘
```

**Key Benefits:**
- ✅ Push code → Automatic deployment
- ✅ Zero manual SSH to server
- ✅ Automatic rollout of updates
- ✅ Always running latest version
- ✅ Easy to rollback if needed

---

## Step 1: Set Up Module 14 Locally

### Clone Module 14

**Your repository is already set up at:**
```
https://github.com/NizaJ27/IS218-Module-14
```

**Clone to your local machine:**

```bash
cd ~/Code
git clone git@github.com:NizaJ27/IS218-Module-14.git
cd IS218-Module-14
```

**Verify you have the correct repository:**

```bash
git remote -v
# Should show:
# origin  git@github.com:NizaJ27/IS218-Module-14.git (fetch)
# origin  git@github.com:NizaJ27/IS218-Module-14.git (push)
```

### Test Locally

**Step 1:** Verify project structure

```bash
ls -la
# Should see:
# - docker-compose.yml (main compose file)
# - docker-compose.postgres.yml (PostgreSQL setup)
# - Dockerfile
# - main.py (FastAPI application entry point)
# - app/ (application code)
# - templates/ (HTML templates for frontend)
# - tests/ (unit, integration, e2e tests)
# - requirements.txt
# - sql/ (database scripts)
```

**Step 2:** Start with Docker Compose

```bash
# Use the PostgreSQL compose file for full setup
docker compose -f docker-compose.postgres.yml up --build

# Or run in background
docker compose -f docker-compose.postgres.yml up --build -d

# For development without external database:
docker compose up --build
```

**Step 3:** Verify it works

```bash
# Check running containers
docker compose ps

# Should see containers like:
# - is218-module-14-web-1 (FastAPI application)
# - is218-module-14-db-1 (PostgreSQL database)
```

**Step 4:** Test the application

Open browser to:
- `http://localhost:8000` - Main application
- `http://localhost:8000/docs` - Swagger API documentation
- `http://localhost:8000/register` - User registration
- `http://localhost:8000/login` - User login
- `http://localhost:8000/calculations-page` - Calculations BREAD interface

Test key features:
- ✅ Home page loads
- ✅ Can register new user
- ✅ Can login with credentials
- ✅ JWT authentication works
- ✅ Can create/read/update/delete calculations
- ✅ Database persists data

**Step 5:** Check logs

```bash
# View all logs
docker compose logs

# View specific service
docker compose logs web
docker compose logs db

# Follow logs in real-time
docker compose logs -f web
```

**Step 6:** Stop when done testing

```bash
# Stop and remove containers
docker compose down

# Stop and remove with volumes (clean slate)
docker compose down -v
```

---

## Step 2: Configure Docker Hub

### Create Docker Hub Account

1. Go to https://hub.docker.com
2. Sign up for free account
3. Verify your email

### Create Repository

**Step 1:** Click "Create Repository"

**Step 2:** Fill in details:
- **Name:** `is218-module-14`
- **Visibility:** Public (free) or Private (requires paid plan)
- **Description:** "FastAPI application with JWT auth and calculation BREAD operations"

**Step 3:** Note your repository path:
```
nizaj27/is218-module-14
```

(Use your actual Docker Hub username if different)

### Generate Access Token

**Step 1:** Go to Account Settings > Security

**Step 2:** Click "New Access Token"

**Step 3:** Configure token:
- **Description:** `github-actions-deploy`
- **Access permissions:** Read & Write
- Click "Generate"

**Step 4:** Copy token immediately (you won't see it again!)

```
dckr_pat_xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

**Security Note:** This token is like a password - keep it secret!

---

## Step 3: Configure GitHub Secrets

### Add Docker Hub Credentials

**Step 1:** Go to your GitHub repository

**Step 2:** Click **Settings** > **Secrets and variables** > **Actions**

**Step 3:** Add the following secrets:

**Secret 1: DOCKER_USERNAME**
- Click "New repository secret"
- Name: `DOCKER_USERNAME`
- Value: Your Docker Hub username
- Click "Add secret"

**Secret 2: DOCKER_TOKEN**
- Click "New repository secret"
- Name: `DOCKER_TOKEN`
- Value: The access token you copied earlier
- Click "Add secret"

**Secret 3: DOCKER_IMAGE**
- Name: `DOCKER_IMAGE`
- Value: `nizaj27/is218-module-14` (or your Docker Hub username)
- Click "Add secret"

### Add Server Credentials (Optional)

If you want GitHub Actions to also trigger deployment:

**Secret 4: SERVER_HOST**
- Value: `104.131.191.83` (your Digital Ocean server)

**Secret 5: SERVER_USER**
- Value: Your Ubuntu username on the server

**Secret 6: SSH_PRIVATE_KEY**
- Value: Your SSH private key for server access (from Chapter 21)

---

## Step 4: Create GitHub Actions Workflow

### Prepare Docker Configuration

**Step 1:** Update `docker-compose.yml` for production

Make sure your `docker-compose.yml` is production-ready:

```yaml
version: '3.8'

services:
  web:
    image: ${DOCKER_IMAGE:-nizaj27/is218-module-14}:latest
    restart: unless-stopped
    environment:
      - DATABASE_URL=${DATABASE_URL}
      - SECRET_KEY=${SECRET_KEY}
    ports:
      - "8000:8000"
    depends_on:
      - db
    labels:
      - "com.centurylinklabs.watchtower.enable=true"

  db:
    image: postgres:16
    restart: unless-stopped
    environment:
      - POSTGRES_DB=${POSTGRES_DB:-fastapi_db}
      - POSTGRES_USER=${POSTGRES_USER:-postgres}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
    volumes:
      - postgres-data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

volumes:
  postgres-data:
```

### Create Workflow File

**Create:** `.github/workflows/deploy.yml`

```yaml
name: Build, Test, and Deploy

on:
  push:
    branches:
      - master
      - main
  pull_request:
    branches:
      - master
      - main

env:
  DOCKER_IMAGE: ${{ secrets.DOCKER_USERNAME }}/is218-module-14

jobs:
  test:
    name: Run Tests
    runs-on: ubuntu-latest

    services:
      postgres:
        image: postgres:16
        env:
          POSTGRES_DB: test_db
          POSTGRES_USER: postgres
          POSTGRES_PASSWORD: postgres
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 5432:5432

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
          cache: 'pip'

      - name: Install dependencies
        run: |
          pip install -r requirements.txt

      - name: Run unit tests
        run: |
          pytest tests/unit/ -v
        env:
          DATABASE_URL: postgresql://postgres:postgres@localhost:5432/test_db

      - name: Run integration tests
        run: |
          pytest tests/integration/ -v
        env:
          DATABASE_URL: postgresql://postgres:postgres@localhost:5432/test_db

      - name: Install Playwright
        run: |
          playwright install --with-deps chromium

      - name: Run E2E tests
        run: |
          pytest tests/e2e/ -v
        env:
          DATABASE_URL: postgresql://postgres:postgres@localhost:5432/test_db

  build-and-push:
    name: Build and Push Docker Image
    needs: test
    runs-on: ubuntu-latest
    if: github.event_name == 'push' && (github.ref == 'refs/heads/master' || github.ref == 'refs/heads/main')

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Log in to Docker Hub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_TOKEN }}

      - name: Extract metadata
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ${{ env.DOCKER_IMAGE }}
          tags: |
            type=raw,value=latest
            type=sha,prefix={{branch}}-

      - name: Build and push image
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=registry,ref=${{ env.DOCKER_IMAGE }}:buildcache
          cache-to: type=registry,ref=${{ env.DOCKER_IMAGE }}:buildcache,mode=max

      - name: Image digest
        run: echo "Image pushed with digest ${{ steps.meta.outputs.digest }}"

  notify:
    name: Notify on Completion
    needs: [test, build-and-push]
    runs-on: ubuntu-latest
    if: always()

    steps:
      - name: Check job status
        run: |
          if [ "${{ needs.build-and-push.result }}" == "success" ]; then
            echo "✅ Build and push successful!"
            echo "🚀 Watchtower will deploy automatically"
          else
            echo "❌ Build or push failed"
            exit 1
          fi
```

### Commit and Push Workflow

```bash
git add .github/workflows/deploy.yml
git commit -m "Add CI/CD workflow for Docker Hub deployment"
git push origin master
```

### Verify Workflow

**Step 1:** Go to GitHub repository → **Actions** tab

**Step 2:** Watch workflow run:
- ✅ Test job runs
- ✅ Build and push job runs (if tests pass)
- ✅ Images pushed to Docker Hub

**Step 3:** Check Docker Hub:
- Go to https://hub.docker.com
- Navigate to your repository
- See the latest tag and timestamp

---

## Step 5: Set Up Watchtower on Server

### What is Watchtower?

**Watchtower** is a container that monitors your running Docker containers and automatically updates them when new images are available on Docker Hub.

**How it works:**
```
1. Watchtower runs as a container
2. Periodically checks Docker Hub for image updates
3. If new image found:
   - Pull new image
   - Stop old container
   - Start new container with same config
   - Remove old image
```

### Install Watchtower

**Step 1:** SSH to your server

```bash
ssh youruser@your-server-ip
```

**Step 2:** Create directory for your application

```bash
mkdir -p ~/IS218-Module-14
cd ~/IS218-Module-14
```

**Step 3:** Create `.env` file

```bash
nano .env
```

Add your environment variables:

```env
# Database Configuration
POSTGRES_DB=fastapi_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_secure_password_here

# Application Configuration
DATABASE_URL=postgresql://postgres:your_secure_password_here@db:5432/fastapi_db
SECRET_KEY=your_jwt_secret_key_here_change_in_production

# Docker
DOCKER_IMAGE=nizaj27/is218-module-14
DOCKER_USERNAME=nizaj27
```

**Generate a secure SECRET_KEY:**
```bash
python3 -c "import secrets; print(secrets.token_urlsafe(32))"
# Use this output for SECRET_KEY
```

**Step 4:** Create production `docker-compose.yml`

```bash
nano docker-compose.yml
```

```yaml
version: '3.8'

services:
  web:
    image: ${DOCKER_IMAGE}:latest
    restart: unless-stopped
    environment:
      - DATABASE_URL=${DATABASE_URL}
      - SECRET_KEY=${SECRET_KEY}
    ports:
      - "8000:8000"
    depends_on:
      - db
    labels:
      - "com.centurylinklabs.watchtower.enable=true"

  db:
    image: postgres:16
    restart: unless-stopped
    environment:
      - POSTGRES_DB=${POSTGRES_DB}
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
    volumes:
      - postgres-data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  watchtower:
    image: containrrr/watchtower
    restart: unless-stopped
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    environment:
      - WATCHTOWER_CLEANUP=true
      - WATCHTOWER_POLL_INTERVAL=300  # Check every 5 minutes
      - WATCHTOWER_LABEL_ENABLE=true  # Only watch labeled containers
      - WATCHTOWER_INCLUDE_STOPPED=true
      - WATCHTOWER_REVIVE_STOPPED=false
    command: --interval 300 --cleanup

volumes:
  postgres-data:
```

**Step 5:** Pull images and start services

```bash
# Pull the latest images
docker compose pull

# Start all services
docker compose up -d

# View logs
docker compose logs -f
```

**Step 6:** Verify Watchtower is running

```bash
docker compose ps

# Should see:
# - web (running)
# - db (running)
# - watchtower (running)
```

### Test Automatic Deployment

**Step 1:** Make a change in your local project

```bash
# On your local machine
cd ~/Code/IS218-Module-14

# Make a visible change to a template or add a comment
echo "# Updated $(date)" >> main.py
```

**Step 2:** Commit and push

```bash
git add .
git commit -m "Test automatic deployment"
git push origin master
```

**Step 3:** Watch GitHub Actions

- Go to repository → Actions tab
- Watch workflow build and push new image

**Step 4:** Watch server logs

```bash
# On your server
docker compose logs -f watchtower

# You should see:
# - Checking for updates...
# - Found new image for web
# - Pulling new image...
# - Stopping old container...
# - Starting new container...
```

**Step 5:** Verify deployment

```bash
# Check container was updated
docker compose ps

# Check application logs
docker compose logs web | tail -20

# Test the application
curl http://localhost:8000
curl http://localhost:8000/docs
```

**Success!** Your application automatically deployed! 🎉

---

## Step 6: Configure Caddy Reverse Proxy

### Why Use Caddy?

Instead of accessing your app at `http://your-ip:5000`, use Caddy to:
- Enable HTTPS automatically
- Use your domain name
- Proxy requests to Docker containers

### Update Caddyfile

**Step 1:** Edit Caddyfile

```bash
sudo nano /etc/caddy/Caddyfile
```

**Step 2:** Add configuration

```caddyfile
# Module 14 FastAPI Application
your-domain.com {
    reverse_proxy localhost:8000
}

# Or if you want www subdomain
www.your-domain.com {
    redir https://your-domain.com{uri}
}

# If you want API on subdomain
api.your-domain.com {
    reverse_proxy localhost:8000
}
```

**Step 3:** Reload Caddy

```bash
sudo systemctl reload caddy

# Check status
sudo systemctl status caddy
```

**Step 4:** Test

```bash
# Should get automatic HTTPS!
curl https://your-domain.com
curl https://your-domain.com/docs  # Swagger UI
curl https://your-domain.com/register
```

---

## Step 7: Monitoring and Maintenance

### View Logs

**All services:**
```bash
cd ~/IS218-Module-14
docker compose logs -f
```

**Specific service:**
```bash
docker compose logs -f web
docker compose logs -f watchtower
docker compose logs -f db
```

**Last N lines:**
```bash
docker compose logs --tail=50 web
```

### Check Container Status

```bash
docker compose ps

# Detailed info
docker stats
```

### Database Backups

**Manual backup:**
```bash
# Backup database
docker compose exec db pg_dump -U postgres fastapi_db > backup.sql

# Or with timestamp
docker compose exec db pg_dump -U postgres fastapi_db > backup-$(date +%Y%m%d-%H%M%S).sql
```

**Automated backup script:**

```bash
nano ~/backup-db.sh
```

```bash
#!/bin/bash
BACKUP_DIR="$HOME/backups"
mkdir -p "$BACKUP_DIR"

cd ~/IS218-Module-14
docker compose exec -T db pg_dump -U postgres fastapi_db \
  > "$BACKUP_DIR/fastapi_db-$(date +%Y%m%d-%H%M%S).sql"

# Keep only last 7 days
find "$BACKUP_DIR" -name "fastapi_db-*.sql" -mtime +7 -delete

echo "Backup completed: $(date)"
```

```bash
chmod +x ~/backup-db.sh

# Test
~/backup-db.sh

# Add to crontab for daily backups
crontab -e
# Add line:
0 2 * * * /home/youruser/backup-db.sh
```

### Restore from Backup

```bash
# Stop web service
docker compose stop web

# Restore database
cat backup.sql | docker compose exec -T db psql -U postgres fastapi_db

# Start web service
docker compose start web
```

### Update Watchtower Configuration

**Check more frequently (every 1 minute):**
```yaml
environment:
  - WATCHTOWER_POLL_INTERVAL=60
```

**Check less frequently (every 1 hour):**
```yaml
environment:
  - WATCHTOWER_POLL_INTERVAL=3600
```

**Enable notifications:**
```yaml
environment:
  - WATCHTOWER_NOTIFICATIONS=slack
  - WATCHTOWER_NOTIFICATION_SLACK_HOOK_URL=https://hooks.slack.com/services/YOUR/WEBHOOK/URL
```

---

## Troubleshooting

### Issue 1: Watchtower Not Updating

**Check Watchtower logs:**
```bash
docker compose logs watchtower
```

**Common causes:**
- Wrong image name in docker-compose.yml
- Labels not set correctly
- Network issues

**Solution:**
```bash
# Manually trigger update
docker compose pull
docker compose up -d

# Restart Watchtower
docker compose restart watchtower
```

### Issue 2: Database Connection Failed

**Check database is running:**
```bash
docker compose ps db

# Check logs
docker compose logs db
```

**Solution:**
```bash
# Verify DATABASE_URL in .env
cat .env | grep DATABASE_URL

# Should be: postgresql://postgres:password@db:5432/fastapi_db
# Note: Use service name "db", not "localhost"
```

### Issue 3: Port Already in Use

**Error:**
```
Error: Bind for 0.0.0.0:8000 failed: port is already allocated
```

**Solution:**
```bash
# Find what's using the port
sudo lsof -i :8000

# Kill the process
sudo kill -9 PID

# Or change port in docker-compose.yml
ports:
  - "8001:8000"  # Use different external port
```

### Issue 4: GitHub Actions Build Fails

**Check workflow logs:**
- Go to repository → Actions
- Click on failed workflow
- Review error messages

**Common issues:**
- Tests failing → Fix tests
- Docker build errors → Fix Dockerfile
- Authentication failed → Check Docker Hub credentials

### Issue 5: Containers Keep Restarting

**Check logs:**
```bash
docker compose logs web | tail -50
```

**Common causes:**
- Environment variables missing
- Database not ready
- Port conflicts
- Application crashes

**Solution:**
```bash
# Check all environment variables
docker compose config

# Verify .env file
cat .env

# Check container health
docker inspect is218-module-14-web-1 | grep -A 20 State
```

---

## Best Practices

### 1. Use Environment Variables

Never hardcode secrets in code:

```javascript
// ❌ DON'T
const password = 'my-secret-password';

// ✅ DO
const password = process.env.DB_PASSWORD;
```

### 2. Health Check Endpoints

Module 14 should have a health check endpoint:

```python
# In your FastAPI app
@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring"""
    try:
        # Check database connection
        db.execute("SELECT 1")
        return {
            "status": "healthy",
            "timestamp": datetime.utcnow().isoformat(),
            "database": "connected"
        }
    except Exception as e:
        return JSONResponse(
            status_code=503,
            content={
                "status": "unhealthy",
                "error": str(e)
            }
        )
```

### 3. Database Migrations

Always use migrations for database changes:

```bash
# backend/migrations/001_initial_schema.sql
# backend/migrations/002_add_users_table.sql

# Run migrations on startup
npm run migrate
```

### 4. Proper Logging

Use structured logging:

```javascript
const winston = require('winston');

const logger = winston.createLogger({
  level: 'info',
  format: winston.format.json(),
  transports: [
    new winston.transports.File({ filename: 'error.log', level: 'error' }),
    new winston.transports.File({ filename: 'combined.log' })
  ]
});

logger.info('Server started', { port: 5000 });
logger.error('Database error', { error: err.message });
```

### 5. Security Headers

Add security headers to your backend:

```javascript
const helmet = require('helmet');
app.use(helmet());

// CORS
const cors = require('cors');
app.use(cors({
  origin: process.env.FRONTEND_URL,
  credentials: true
}));
```

### 6. Resource Limits

Set resource limits in docker-compose.yml:

```yaml
services:
  backend:
    deploy:
      resources:
        limits:
          cpus: '1'
          memory: 512M
        reservations:
          cpus: '0.5'
          memory: 256M
```

---

## Testing Your Setup

### Complete Deployment Test

**Step 1: Make a visible change**

```bash
# Update a template or add a feature
echo "<!-- Last deployed: $(date) -->" >> templates/base.html
```

**Step 2: Commit and push**

```bash
git add .
git commit -m "Test deployment pipeline"
git push origin master
```

**Step 3: Watch the magic happen**

```bash
# 1. GitHub Actions starts (check Actions tab)
# 2. Tests run
# 3. Docker image builds
# 4. Image pushes to Docker Hub
# 5. Watchtower detects update (wait ~5 mins)
# 6. Application updates automatically
```

**Step 4: Verify**

```bash
# Check your website
curl https://your-domain.com

# Check API documentation
curl https://your-domain.com/docs

# Should see your changes!
```

**🎉 Congratulations! Your CI/CD pipeline is working!**

---

## Advanced: Multiple Environments

### Staging Environment

**Create staging branch:**
```bash
git checkout -b staging
git push -u origin staging
```

**Update workflow to deploy staging:**

```yaml
on:
  push:
    branches:
      - master
      - staging

jobs:
  build-and-push:
    steps:
      # ... existing steps ...

      - name: Determine environment
        id: env
        run: |
          if [ "${{ github.ref }}" == "refs/heads/master" ]; then
            echo "tag=production" >> $GITHUB_OUTPUT
          else
            echo "tag=staging" >> $GITHUB_OUTPUT
          fi

      - name: Build and push
        uses: docker/build-push-action@v5
        with:
          context: ./backend
          push: true
          tags: |
            ${{ env.DOCKER_IMAGE }}:${{ steps.env.outputs.tag }}
            ${{ env.DOCKER_IMAGE }}:${{ github.sha }}
```

**Run staging on different ports:**

```yaml
# docker-compose.staging.yml
services:
  backend:
    image: your-username/project-14:staging
    ports:
      - "5001:5000"  # Different port
  frontend:
    ports:
      - "3001:80"
```

---

## Summary

**What You've Accomplished:**

✅ Set up complete CI/CD pipeline
✅ Automated testing on every commit
✅ Automated Docker image builds
✅ Automatic deployment with Watchtower
✅ Zero-downtime deployments
✅ HTTPS with Caddy
✅ Database persistence
✅ Monitoring and logging

**Your Workflow Now:**

1. Write code locally
2. Commit and push to GitHub
3. ✨ **Everything else happens automatically!** ✨
4. Check your live site to see changes

**Next Steps:**

- Add monitoring (Chapter 20)
- Set up alerts for failures
- Implement backup automation
- Add staging environment
- Configure rolling deployments

---

## Quick Reference

### Essential Commands

```bash
# On Server
cd ~/IS218-Module-14

# View all logs
docker compose logs -f

# Restart specific service
docker compose restart web

# Pull latest images manually
docker compose pull

# Rebuild and restart
docker compose up -d --build

# Check container status
docker compose ps

# View Watchtower activity
docker compose logs watchtower --tail=50

# Backup database
docker compose exec db pg_dump -U postgres fastapi_db > backup.sql

# Stop all services
docker compose down

# Stop and remove volumes (careful!)
docker compose down -v
```

### Useful Docker Commands

```bash
# View all containers
docker ps -a

# View all images
docker images

# Remove unused images
docker image prune -a

# Remove unused volumes
docker volume prune

# View disk usage
docker system df

# Clean up everything (careful!)
docker system prune -a --volumes
```

---

[← Previous: Chapter 21 - CI/CD with GitHub Actions](21-cicd-github-actions.md) | [Home](../README.md)
