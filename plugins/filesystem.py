import re
import os

from result import Result


def files(query):
    """A plugin that searches for a file in the current directory tree"""
    # TODO optimize this!
    pattern=re.compile(".*{}.*".format(query))
    results = []
    for (dirpath, dirnames, filenames) in os.walk('.'):
        results.extend([
            Result(
                title=filename,
                description="Files matching your query",
                action=""
            )
            for filename in filenames if pattern.search(filename)
        ])
    return results
