
## @ Tests Commands
.PHONY: test
test: ## Run tests
	pytest -v

.PHONY: pypi
pypi: ## update version in pypi
	poetry build
	poetry publish

