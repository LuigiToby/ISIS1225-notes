def new_double_node(element):
    return {"info": element, "next": None, "prev": None}

def new_double_list():
    header = {"info": None, "next": None, "prev": None}
    trailer = {"info": None, "next": None, "prev": header}
    header["next"] = trailer

    return {"header": header, "trailer": trailer, "size": 0}

def is_empty(double_list):
    return double_list["size"] == 0

def size(my_list):
    return my_list["size"]

def add_last(my_list, element):
    trailer = my_list["trailer"]
    last = trailer["prev"]
    node = new_double_node(element)
    
    node["next"] = trailer
    node["prev"] = last
    last["next"] = node
    trailer["prev"] = node
    
    my_list["size"] += 1
    return my_list

# Lo agrego par facilitar mi vida

def pprint_double_list(my_list):
    """
    Imprime el contenido de una lista doblemente enlazada
    de forma legible (ignorando header y trailer).
    """
    if is_empty(my_list):
        print("DoubleList(size=0) -> []")
        return
    
    elements = []
    node = my_list["header"]["next"]
    while node is not my_list["trailer"]:
        elements.append(str(node["info"]))
        node = node["next"]
    
    print(f"DoubleList(size={my_list['size']}) -> [" + " <-> ".join(elements) + "]")
