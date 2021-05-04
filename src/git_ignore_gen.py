from utils import write_to_file, DEFAULT_PATH


class GitIgnoreGen:
    # Methods

    def generate_gitignore_file(self, path=DEFAULT_PATH):
        content = """
*.env
*.log
*.pot
*.pyc
__pycache__
db.sqlite3
media
envs/
tmp/
"""

        write_to_file("{0}/.gitignore".format(path), contents=content)
