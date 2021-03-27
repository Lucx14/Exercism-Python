def response(hey_bob):
    spoken = hey_bob.strip()
    question = spoken.endswith("?")
    shout = spoken.isupper()
    if not spoken:
        return "Fine. Be that way!"
    elif shout and question:
        return "Calm down, I know what I'm doing!"
    elif question:
        return "Sure."
    elif shout:
        return "Whoa, chill out!"
    else:
        return "Whatever."
