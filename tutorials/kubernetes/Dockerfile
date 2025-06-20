FROM ubuntu:22.04

# Set environment variable to avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies and Python
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python3-pip \
        python3-venv \
        git \
        tini \
        build-essential \
        && rm -rf /var/lib/apt/lists/*

# Create a virtual environment to avoid system package conflicts
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Upgrade pip and install EasyVVUQ
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir easyvvuq

# Clone the repository for examples and tutorials
RUN git clone https://github.com/UCL-CCS/EasyVVUQ.git /opt/EasyVVUQ

# Set working directory
WORKDIR /opt/EasyVVUQ

ENTRYPOINT ["tini", "--"]
