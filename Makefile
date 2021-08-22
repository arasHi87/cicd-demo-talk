PKG=api

.PHONY: clean init

service_up:
	docker-compose up -d

service_down:
	docker-compose down && docker volume rm cicd-talk-data

init: clean
	pipenv --python 3.8
	pipenv install --dev

lint:
	pipenv run flake8 ${PKG}/ --max-line-length=120
	pipenv run pylint --rcfile=setup.cfg ${PKG}/*

format:
	pipenv run black ${PKG}/
	pipenv run isort .

analysis:
	pipenv run bandit ${PKG}/

test:
	pipenv run pytest -vv --cov-report=term-missing --cov=${PKG}/endpoints ${PKG}/tests

ci-bundle: analysis format lint test