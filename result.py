import subprocess


class Result():
    def __init__(self, **kwargs):
        self.title = kwargs["title"]
        self.description = kwargs["description"]
        self.action = kwargs["action"]

    def run(self):
        """run the associated action"""
        subprocess.call([self.action])

    def __str__(self):
        return "{} || {}".format(
            self.title,
            self.description
        )
