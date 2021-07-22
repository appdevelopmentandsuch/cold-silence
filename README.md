# cold-silence

[![CodeFactor](https://www.codefactor.io/repository/github/appdevelopmentandsuch/cold-silence/badge)](https://www.codefactor.io/repository/github/appdevelopmentandsuch/cold-silence)
[![codecov](https://codecov.io/gh/appdevelopmentandsuch/cold-silence/branch/main/graph/badge.svg?token=7Q2WY19HEA)](https://codecov.io/gh/appdevelopmentandsuch/cold-silence)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/appdevelopmentandsuch/cold-silence/graphs/commit-activity)
[![GitHub license](https://img.shields.io/github/license/appdevelopmentandsuch/cold-silence.svg)](https://github.com/appdevelopmentandsuch/cold-silence/blob/master/LICENSE)
[![GitHub release](https://img.shields.io/github/release/appdevelopmentandsuch/cold-silence.svg)](https://GitHub.com/appdevelopmentandsuch/cold-silence/releases/)
[![GitHub tag](https://img.shields.io/github/tag/appdevelopmentandsuch/cold-silence.svg)](https://GitHub.com/appdevelopmentandsuch/cold-silence/tags/)
[![Github all releases](https://img.shields.io/github/downloads/appdevelopmentandsuch/cold-silence/total.svg)](https://GitHub.com/appdevelopmentandsuch/cold-silence/releases/)
[![GitHub stars](https://img.shields.io/github/stars/appdevelopmentandsuch/cold-silence.svg?style=social&label=Star&maxAge=2592000)](https://GitHub.com/appdevelopmentandsuch/cold-silence/stargazers/)
[![GitHub issues](https://img.shields.io/github/issues/appdevelopmentandsuch/cold-silence.svg)](https://GitHub.com/appdevelopmentandsuch/cold-silence/issues/)
[![GitHub issues-closed](https://img.shields.io/github/issues-closed/appdevelopmentandsuch/cold-silence.svg)](https://GitHub.com/appdevelopmentandsuch/cold-silence/issues?q=is%3Aissue+is%3Aclosed)

Start a new Django project sans boilerplate code.

# Quickstart

```bash
cd src
python3 main.py
```

```bash
cd src
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

# Info

Python Version: 3.8.5
OS: Ubuntu 20.04
