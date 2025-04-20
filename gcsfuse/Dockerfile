FROM debian:bullseye-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    lsb-release \
    tini \
    fuse \
    && rm -rf /var/lib/apt/lists/*

# Install gcsfuse
RUN export GCSFUSE_REPO=gcsfuse-`lsb_release -c -s` \
    && echo "deb https://packages.cloud.google.com/apt $GCSFUSE_REPO main" | tee /etc/apt/sources.list.d/gcsfuse.list \
    && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - \
    && apt-get update \
    && apt-get install -y gcsfuse \
    && rm -rf /var/lib/apt/lists/*

# Use tini as entrypoint to handle signals properly
ENTRYPOINT ["/usr/bin/tini", "--"]

# Default command (can be overridden)
CMD ["gcsfuse", "--version"]
