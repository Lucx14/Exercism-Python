def grep(pattern: str, flags: str, files):
    result = []
    with open(files[0]) as reader:
        for i, line in enumerate(reader):
            if flags == "-i":
                if pattern.lower() in line.lower():
                    result.append(
                        {"file": files[0], "line_number": (i + 1), "line": line}
                    )
            else:
                if pattern in line:
                    result.append(
                        {"file": files[0], "line_number": (i + 1), "line": line}
                    )

    if flags == "-n":
        return "".join([f"{x['line_number']}:{x['line']}" for x in result])
    elif flags == "-i":
        return "".join([x["line"] for x in result])
    elif flags == "":
        return "".join([x["line"] for x in result])
    elif flags == "-l":
        return "".join([x["file"] for x in result]) + "\n"
    elif flags == "-x":
        return "".join([x["line"] for x in result])


# Return the line number and contents of each matching line.
# Flags

# As said earlier, the grep command should also support the following flags:

#     -n Print the line numbers of each matching line.
#     -l Print only the names of files that contain at least one matching line.
#     -i Match line using a case-insensitive comparison.
#     -v Invert the program -- collect all lines that fail to match the pattern.
#     -x Only match entire lines, instead of lines that contain a match.
