def serializetoDict(var) -> dict:
    return {**{i: str(var[i]) for i in var if i == "_id"}, **{i: var[i] for i in var if i != "_id"}}


def serializetoList(entity) -> list:
    return [serializetoDict(info) for info in entity]
