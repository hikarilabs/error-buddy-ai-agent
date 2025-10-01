#!/bin/bash

ollama serve & OLLAMA_PID=$!

sleep 5

ollama pull gemma3:1b

ollama stop gemma3:1b

kill -9 $OLLAMA_PID

