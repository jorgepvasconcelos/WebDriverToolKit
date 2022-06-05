
.PHONY: pypi
pypi:
	poetry build
	poetry publish

