# Application image built by the Flow B build stage (requirement 8.3). The build
# project runs `docker build` at the repository root and tags the result with the
# commit SHA before pushing to the application ECR repository, where Inspector
# enhanced scanning scans it on push (AC-3, requirement 8.4). No deployment
# follows; the pipeline ends at the push (requirement 8.5).

FROM public.ecr.aws/docker/library/python:3.12-slim

WORKDIR /app
COPY src/ ./src/

ENV PYTHONPATH=/app/src
USER 1000

# A trivial entrypoint: the PoC validates that the image builds and is pushed,
# not that it does anything useful at runtime.
CMD ["python", "-c", "import example_service; print('example-service', example_service.__version__)"]
