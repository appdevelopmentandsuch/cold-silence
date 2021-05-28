clean:
	rm -rf project_output
	rm -f .coverage
	rm -f coverage.xml
	rm -rf .pytest_cache

test:
	pytest --cov cold_silence --cov-report=xml

test_clean:
	make test
	make clean

build_default_project:
	python3 src/cold_silence/main.py

setup:
	pip install -r requirements.txt

format:
	black ./

install:
	pip install .