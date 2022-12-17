VENV_NAME=venv
VENV_ACTIVATE=. ./$(VENV_NAME)/Scripts/activate
PYTHON=./${VENV_NAME}/Scripts/python.exe

.DEFAULT_GOAL=build

pyenv:
	poetry install

env_reset: env_down pyenv env_up

env_up:
	cd ./tests/infra && \
	docker-compose up -d && printf '\nWAITING FOR APIv3' && \
	until $$(curl --output /dev/null --silent --head --fail http://localhost:8080); do \
		printf '.'; \
		sleep 5; \
	done && printf '\n\n' && \
	printf '############################\n' && \
	printf '############################\n' && \
	printf '####### UP & RUNNING #######\n' && \
	printf '############################\n' && \
	printf '############################'


pytest:
	- poetry run python -m coverage run -m unittest discover -s ./tests/test_cases -t tests/test_cases -p *_test.py

env_down:
	cd ./tests/infra && \
	docker-compose down --volumes

test: pyenv env_up pytest env_down

build:
	- poetry build

clean:
	- rm -rf ./pyopenproject.egg-info ./build ./dist .coverage

vars:
	source ./.env && \
	export VERSION && \
	echo "$$VERSION"


help:
	@echo "    clean"
	@echo "        Remove all artifacts."
	@echo '    build'
	@echo '        Build the project package'
	@echo '    test'
	@echo '        Run tests '

.PHONY: clean help test build
