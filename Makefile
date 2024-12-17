test:
	poetry run python -m pytest --html=report.html

install:
	poetry install && \
	poetry run python generate_docker_pull.py && \
	sh pull_images.sh