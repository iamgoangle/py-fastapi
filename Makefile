.PHONY: run setup

setup:
	pipenv install
run:
	uvicorn main:app --reload 