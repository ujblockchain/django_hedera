.PHONY:install
install:
	poetry install


.PHONY:install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall; poetry run pre-commit install 


.PHONY: lint
lint:
	poetry run pre-commit run --all-files



.PHONY:check-settings
check-settings:
	poetry run python -m core.manage check --settings=core.project.settings.split_settings


.PHONY:migrate
migrate:
	poetry run python -m core.manage migrate


.PHONY:migrations
migrations:
	poetry run python -m core.manage makemigrations


.PHONY:runserver
runserver:
	poetry run python -m core.manage runserver


.PHONY:superuser
run-server:
	poetry run python -m core.manage createsuperuser


.PHONY:setup
setup: install migrate install-pre-commit ;
