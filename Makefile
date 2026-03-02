.PHONY: install run test

install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

run:
	uvicorn src.serving.app:app --reload --host 0.0.0.0 --port 8000

test:
	pip install pytest
	pytest
