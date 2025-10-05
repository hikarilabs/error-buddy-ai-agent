#!/usr/bin/env bash

# docker build for apple silicon chips
docker build --platform=linux/amd64 -t llm-llama-3.2-1b:1.0.0 --build-arg CONTAINER_OLLAMA_HOST="0.0.0.0:11434" -f ../Dockerfile.llama.3.2.1b .