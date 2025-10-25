FROM node:20-alpine AS builder

WORKDIR /app

# Clone the happy-server repository
RUN apk add --no-cache git && \
    git clone https://github.com/slopus/happy-server.git . && \
    npm install && \
    npm run build

# Production stage
FROM node:20-alpine

WORKDIR /app

# Copy built application from builder
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./package.json

# Expose the application port
EXPOSE 3005

# Start the server
CMD ["node", "dist/index.js"]
