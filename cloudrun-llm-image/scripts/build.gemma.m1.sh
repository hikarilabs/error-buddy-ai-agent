#!/usr/bin/env bash

# docker build for apple silicon chips
docker build --platform=linux/amd64 -t llm-gemma3-1b:1.0.0 --build-arg CONTAINER_OLLAMA_HOST="0.0.0.0:11436" -f ../Dockerfile.gemma.3.1b .