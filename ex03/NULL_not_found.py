import math

def NULL_not_found(object: any) -> int:

    if object is None:
        print(f"Nothing: {object} {type(object)}")
    elif isinstance(object, bool) and object is False:
        print(f"Fake: {object} {type(object)}")
    elif isinstance(object, int) and object == 0:
        print(f"Zero: {object} {type(object)}")
    elif isinstance(object, float) and math.isnan(object):
        print(f"Zero: {object} {type(object)}")
    elif isinstance(object, str) and object == '':
        print(f"Empty: {object} {type(object)}")
    else:
        print(f"Type not Found")
        return 1
    return 0