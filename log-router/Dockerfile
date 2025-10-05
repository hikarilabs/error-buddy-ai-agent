FROM cloudrun-base-python:1.0.0

# Docker has a dangerous behaviour when files are copied in a non-priviledged container
# MUST USE: --chown=user:group when using ADD or COPY

ADD --chown=mluser:mluser log_router ./log_router
ADD --chown=mluser:mluser main.py .

# run the container
CMD ["python", "./main.py"]