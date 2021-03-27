from itertools import groupby
import re

GROUPS_RE = re.compile(r"(\d*)([A-Za-z ])")


def decode(string):
    groups = re.findall(GROUPS_RE, string)

    return "".join(int(count) * letter if count else letter for count, letter in groups)


def encode(string):
    groups = [list(g) for _, g in groupby(string)]

    return "".join(
        [str(len(group)) + group[0] if len(group) > 1 else group[0] for group in groups]
    )
