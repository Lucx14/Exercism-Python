def flatten(iter):
    flat_list = []

    def flatten_list(data):
        for element in data:
            if isinstance(element, list):
                flatten_list(element)
            else:
                if element is not None:
                    flat_list.append(element)

    flatten_list(iter)

    return flat_list
