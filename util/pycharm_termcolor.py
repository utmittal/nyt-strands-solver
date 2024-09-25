import termcolor


def colored(*args, **kwargs) -> str:
    return termcolor.colored(force_color=True, *args, **kwargs)


def cprint(*args, **kwargs) -> None:
    return termcolor.cprint(force_color=True, *args, **kwargs)
