clean:
	rm -r project_output
	rm .coverage
	rm coverage.xml
	rm -r .pytest_cache

test:
	pytest --cov cold_silence --cov-report=xml

test_clean:
	make test
	make clean

build_default_project:
	python3 src/cold_silence/main.py

install:
	pip install -r requirements.txt