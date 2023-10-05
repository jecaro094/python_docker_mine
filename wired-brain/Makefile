
SRC=$(CURDIR)/product_service

requirements:
	pip install -r $(SRC)/requirements.txt -r $(SRC)/requirements-dev.txt

format:
	isort $(SRC)
	black $(SRC)

test:
	python -m pytest -- $(CURDIR)/

all: requirements format test