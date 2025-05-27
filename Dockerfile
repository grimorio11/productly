FROM grimorio11/nginx-helm
RUN apk add --no-cache \
    curl \
    bash 

VOLUME . /data