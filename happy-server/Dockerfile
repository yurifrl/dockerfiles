FROM node:25-alpine

WORKDIR /app

# Clone the happy-server repository and install dependencies
RUN apk add --no-cache git && \
    git clone https://github.com/slopus/happy-server.git . && \
    npm install

# Expose the application port
EXPOSE 3005

# Start the server with tsx
CMD ["npm", "start"]
