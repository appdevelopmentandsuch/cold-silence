# cold-silence

[![CodeFactor](https://www.codefactor.io/repository/github/appdevelopmentandsuch/cold-silence/badge)](https://www.codefactor.io/repository/github/appdevelopmentandsuch/cold-silence)

[![codecov](https://codecov.io/gh/appdevelopmentandsuch/cold-silence/branch/main/graph/badge.svg?token=7Q2WY19HEA)](https://codecov.io/gh/appdevelopmentandsuch/cold-silence)

Start a new Django project sans boilerplate code.

# Setup

```bash
cd [project_dir]/src/cold_silence
pip install -r requirements.txt

OR

cd [project_dir]
make install
```

# Quickstart

```bash
cd [project_dir]/src/cold_silence
python3 main.py

OR

cd [project_dir]
make build_default_project
```

```bash
cd [project_dir]/src/cold_silence
python3 main.py --server_port 8080 --project_name my_project --service_name my_service --project_directory my_project --verbose
```

# Output

```bash
├── project_output
│   ├── dev.env
│   ├── docker-compose.yaml
│   ├── local.env
│   ├── nginx
│   │   ├── Dockerfile
│   │   └── nginx.conf
│   ├── prod.env
│   ├── project
│   │   ├── Dockerfile
│   │   ├── Dockerfile.prod
│   │   ├── manage.py
│   │   └── project
│   │       ├── asgi.py
│   │       ├── __init__.py
│   │       ├── settings.py
│   │       ├── urls.py
│   │       └── wsgi.py
│   └── staging.env
```

# Testing

To run tests, run the following

```bash
cd [project_dir]
pytest --cov cold_silence --cov-report=xml

OR

make test # This will generate several artifacts, along with a project, which can be removed with make clean

OR

make test_clean # This will automatically remove the generated artifacts and generated project
```

# Info

Python Version: 3.8.5
OS: Ubuntu 20.04
