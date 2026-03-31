#takes a list of objects and returns a list of dictified objects
def get_dicts(objects):
    dicts = []
    for object in objects:
        dicts.append(object.__dict__)
    return dicts