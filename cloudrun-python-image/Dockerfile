FROM python:3.12.11-slim-trixie AS builder

# Set DEBIAN AND PYTHON environement variables for the way we want to behave at image build
# Supress interaction prompts
ENV DEBIAN_FRONTEND=noninteractive

# If a C binding crashes don't let it go silently
ENV PYTHONFAULTHANDLER=1

# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE=1

# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

# Run everything on the laest image and packages relases
RUN apt-get update && apt upgrade -y

# Install gcc compiler
RUN apt install -y --no-install-recommends gcc

# Add a non-root user with reduced priviledges
RUN useradd --create-home -s /bin/bash mluser

# Upgrade pip setuptools and wheel packages
RUN python3 -m pip install --upgrade pip && pip install --upgrade setuptools wheel

# Set working directory default to mluser home folder
WORKDIR /home/mluser

# Run everything from now on as a standard user
USER mluser

RUN pip wheel --no-cache-dir --no-deps --wheel-dir ~/build-wheels fastapi[standard]==0.116.1 uvicorn==0.35.0

RUN pip wheel --no-cache-dir --no-deps --wheel-dir ~/build-wheels google-cloud-storage==3.3.1 google-cloud-secret-manager==2.24.0 google-cloud-pubsub==2.31.1 google-cloud-logging==3.12.1


# final stage - build base docker image
FROM python:3.12.11-slim-trixie

# Similar as in the builder stage set DEBIAN AND PYTHON environement variables for the way we want to behave at image build
# Supress interaction prompts
ENV DEBIAN_FRONTEND=noninteractive

# If a C binding crashes don't let it go silently
ENV PYTHONFAULTHANDLER=1

# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE=1

# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

# Run everything on the laest image and packages relases
RUN apt-get update && apt upgrade -y

# Install shell script utilities
RUN apt install -y procps tini

# Cleanup installation and upgrade folders to keep the image size low
RUN apt-get -y clean && rm -rf /var/lib/apt/lists/*

# Add a non-root user with reduced priviledges to run ML apps
RUN useradd --create-home -s /bin/bash mluser

# Upgrade pip, setuptools and wheel packages
RUN python3 -m pip install --upgrade pip && pip install --upgrade setuptools wheel

# Set working directory to mluser home folder
WORKDIR /home/mluser

# Run everything from now on as a standard user
USER mluser

# create a local build wheel directory
RUN mkdir wheels

# Copy the builder wheels to the base image
COPY --from=builder /home/mluser/build-wheels /home/mluser/wheels

# Prevent Docker to use a cached layer when installing packages, we want everything to be re-built from 0.
RUN pip install --no-cache /home/mluser/wheels/*

# add .local/bin to the container path for newly installed python executable scripts
ENV PATH="${PATH}:/home/mluser/.local/bin"


