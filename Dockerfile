# Base image
FROM klakegg/hugo:0.83.1-ext-ubuntu

# General commands
RUN apt-get update && apt-get install -y \
    git \
    vim