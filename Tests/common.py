import jsonpickle


def clear_file(filename):
    with open(filename, 'w') as f:
        f.write(jsonpickle.encode({}))
