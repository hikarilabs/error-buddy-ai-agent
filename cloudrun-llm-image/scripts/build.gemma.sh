#!/usr/bin/env bash

source .env

docker build -t vllm-gemma-3-1b:1.0.0 --build-arg HF_TOKEN=${HF_TOKEN} -f ../Dockerfile.gemma.3.1b .