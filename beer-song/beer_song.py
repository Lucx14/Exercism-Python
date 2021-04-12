no_beers = "No more bottles of beer on the wall, no more bottles of beer."
buy_beers = "Go to the store and buy some more, 99 bottles of beer on the wall."
take_last_beer = "Take it down and pass it around, no more bottles of beer on the wall."


def count_beers(num):
    return f"{num} bottle{'s' if num != 1 else ''} of beer on the wall, {num} bottle{'s' if num != 1 else ''} of beer."


def take_beer(num):
    return f"Take one down and pass it around, {num - 1} bottle{'s' if num - 1 != 1 else ''} of beer on the wall."


def recite(start, take=1):
    result = []

    while take > 0:
        if start == 0:
            result.extend([no_beers, buy_beers])
        elif start == 1:
            result.extend([count_beers(start), take_last_beer])
        else:
            result.extend([count_beers(start), take_beer(start)])

        result.append("")
        start -= 1
        take -= 1

    result.pop()
    return result
