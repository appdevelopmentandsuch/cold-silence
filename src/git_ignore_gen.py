class GitIgnoreGen:
    # Methods

    def __generate_file_content(self):
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

        return content

    def write_git_ignore(self):
        git_ignore = open(".gitignore", "w")

        git_ignore_contents = self.__generate_file_content()

        git_ignore.write(git_ignore_contents)
        git_ignore.close()
