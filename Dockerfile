FROM grimorio11/nginx-helm
RUN apk add --no-cache \
    curl \
    bash && mkdir -p /data

VOLUME /data