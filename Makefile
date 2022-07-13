.SILENT: fmt check lint

generate:
	rm -rf grafana_loki_client

	openapi-python-client generate --meta none --path grafana_loki_openapi.yaml

	touch grafana_loki_client/py.typed
	make fmt

fmt:
	find . -type d -name ".venv" -prune -o -print -type f -name "*.py" \
		-exec pyupgrade --exit-zero-even-if-changed --py37-plus {} \+ 1> /dev/null
	autoflake \
		--in-place \
		--remove-all-unused-imports \
		--ignore-init-module-imports \
		-r \
		.
	isort --profile black .
	black .

check:
	find . -type d -name ".venv" -prune -o -print -type f -name "*.py" \
		-exec pyupgrade --py37-plus {} \+ 1> /dev/null
	autoflake \
		--in-place \
		--remove-all-unused-imports \
		--ignore-init-module-imports \
		-r \
		-c \
		.
	isort --profile black -c .
	black --check .

lint:
	mypy .
	flake8 .
