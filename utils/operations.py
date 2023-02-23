from utils.constants import STRING10

def string_serializer(data, size): # Devolverá cadenas de tamaño 10
    data = str(data)
    leng = len(data)
    new_str = data
    if leng<=size:
        new_str = data+STRING10[leng:]
    else:
        new_str = data[:size]
    return new_str