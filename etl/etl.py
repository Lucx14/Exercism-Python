def transform(legacy_data):
    result = {}
    for k, v in legacy_data.items():
        for letter in v:
            result[letter.lower()] = k
    return result
