.SILENT: fmt check lint

fmt:
	find . -type d -name ".venv" -prune -o -print -type f -name "*.py" \
		-exec pyupgrade --exit-zero-even-if-changed --py310-plus {} \+ 1> /dev/null
	autoflake \
		--in-place \
		--remove-all-unused-imports \
		--ignore-init-module-imports \
		-r \
		<project-name>
	isort --profile black .
	black .

check:
	find . -type d -name ".venv" -prune -o -print -type f -name "*.py" \
		-exec pyupgrade --py310-plus {} \+ 1> /dev/null
	autoflake \
		--in-place \
		--remove-all-unused-imports \
		--ignore-init-module-imports \
		-r \
		-c \
		<project-name>
	isort --profile black -c .
	black --check .

lint:
	mypy <project-name>
	flake8 .

test:
	pytest -x --cov=core --cov=<project-name> --cov-fail-under=90
