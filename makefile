install:
	pip install -e .

uninstall:
	pip uninstall calculadora_cr

run:
	python main.py

test:
	pytest