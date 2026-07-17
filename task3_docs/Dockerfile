# 1. Set the base image
FROM postman/newman:5.3-alpine

# 2. Set environment variables
ENV NODE_PATH=/usr/local/lib/node_modules

# 3. Update/upgrade packages, install extra system packages, and clean cache in a single layer
# We use Alpine's apk manager. --no-cache avoids saving local index files to keep the image small.
RUN apk update && \
    apk upgrade && \
    apk add --no-cache curl zip iputils

# 4. Install the custom Newman reporter globally and clean npm cache
RUN npm install -g newman-reporter-csvallinone && \
    npm cache clean --force

# 5. Set the working directory
WORKDIR /etc/newman

# 6. Set the default entrypoint
ENTRYPOINT ["newman"]
