from result import Result


def calculate(query):
    try:
        r = eval(query)
    except SyntaxError:
        return []

    action = "echo {} | xclip".format(r)
    r = Result(
        title=r,
        description="copy to clipboard",
        action=action
    )
    return [r]
