# This uses a local image tag.
# For GCP using Artifact Registry hosted in EU:
# FROM europe-west2-docker.pkg.dev/[PROJECT_ID]/common/[IMAGE_TAG]
FROM  cloudrun-image:1.0.0

# Docker has a dangerous behaviour even when files are copied in a non-priviledged container by changing
# the owner to root.
# To prevent this MUST USE: --chown=user:group when using ADD or COPY

ADD --chown=mluser:mluser app ./app
ADD --chown=mluser:mluser main.py .

# Expose port
EXPOSE 8000

# Run the container app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
