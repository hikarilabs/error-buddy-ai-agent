#!/usr/bin/env bash

docker build --platform=linux/amd64 -t cloudrun-base-python:1.0.0  -f ../Dockerfile .