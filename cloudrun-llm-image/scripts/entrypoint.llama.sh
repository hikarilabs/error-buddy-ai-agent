#!/bin/bash

ollama serve & OLLAMA_PID=$!

sleep 5

ollama pull llama3.2:1b

ollama stop llama3.2:1b

kill -9 $OLLAMA_PID

