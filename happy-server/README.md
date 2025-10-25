# Happy Server Docker Image

Docker image for [Happy Server](https://github.com/slopus/happy-server) - encrypted sync backend for Claude Code.

## Image Details

- **Base Image**: node:20-alpine
- **Port**: 3005
- **Build**: Multi-stage build from upstream source

## Required Environment Variables

- `NODE_ENV`: Set to "production"
- `DATABASE_URL`: PostgreSQL connection string (e.g., `postgres://user:pass@host:5432/dbname`)
- `REDIS_URL`: Redis connection string (e.g., `redis://host:6379`)
- `SEED`: Secure random token (generate with: `openssl rand -hex 32`)
- `PORT`: Application port (default: 3005)

## Usage

```bash
docker run -d \
  -e NODE_ENV=production \
  -e DATABASE_URL=postgres://... \
  -e REDIS_URL=redis://... \
  -e SEED=your-random-seed \
  -e PORT=3005 \
  -p 3005:3005 \
  ghcr.io/yurifrl/dockerfiles/happy-server:latest
```

## Build

The image is automatically built by GitHub Actions on push to the main branch and published to GitHub Container Registry.

## Architecture

Supports both `linux/amd64` and `linux/arm64` platforms.
