def _init():
    global res
    global sen
    global error
    sen = None
    res = None
    error = None

def set_res(value):
    global res
    res = value

def get_res():
    global res
    try:
        return res
    except KeyError as e:
        return e

def set_sen(value):
    global sen
    sen = value
def get_sen():
    global sen
    try:
        return sen
    except KeyError as e:
        return e

def set_error(value):
    global error
    error = value

def get_error():
    global error
    try:
        return error
    except KeyError as e:
        return e