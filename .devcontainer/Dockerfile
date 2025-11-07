FROM mcr.microsoft.com/vscode/devcontainers/base:ubuntu

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 python3-pip python3-venv \
    curl wget git vim netcat-openbsd nmap socat \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# workspace
RUN mkdir -p /workspace && chown vscode:vscode /workspace
WORKDIR /workspace
USER vscode
SHELL ["/bin/bash", "-lc"]
