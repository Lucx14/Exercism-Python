def value(colors):
    color = (
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white",
    )

    return int("".join(str(color.index(x)) for x in colors[:2]))
