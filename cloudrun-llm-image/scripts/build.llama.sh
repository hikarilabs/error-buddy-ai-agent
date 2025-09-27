#!/usr/bin/env bash

source .env

docker build -t vllm-llama-3.2-1b:1.0.0 --build-arg HF_TOKEN=${HF_TOKEN} -f ../Dockerfile.llama.3.2.1b .