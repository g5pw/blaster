from result import Result


def echo(query):
    """A plugin that echoes the query it was given. Used for testing."""
    r = Result(
        title=query,
        description="Just echoes the query",
        action=""
    )
    return [r]
