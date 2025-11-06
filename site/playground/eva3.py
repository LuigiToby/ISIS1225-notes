from DataStructures.List import array_list as lt # Importo mi implementación de lista para guardar la información

# EVA1 ej1

def equals(root1,root2):
    if root1 == None and root2 == None:
        return True
    if root1 == None or root2 == None:
        return False
    if root1["key"] != root2["key"] or root1["value"] != root2["value"]:
        return False
    # Warning, here it's habit to put first the comparison for the left node and then the comparison for the right node
    return (
        equals(root1["right"], root2["right"]) and equals(root1["left"], root2["left"])
    ) 
    
def is_mirror(root1,root2):
    if root1 == None and root2 == None:
        return True
    if root1 == None or root2 == None:
        return False
    if root1["key"] != root2["key"] or root1["value"] != root2["value"]:
        return False
    return (
        is_mirror(root1["right"], root2["left"]) and is_mirror(root1["left"], root2["right"])
    ) 
    
def is_subtree(root, sub):
    if sub is None:
        return True
    if root is None:
        return False
    if equals(root, sub):
        return True
    return is_subtree(root["left"], sub) or is_subtree(root["right"], sub)

def same_keys(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    if root1["key"] != root2["key"]: # Ojo el tema aquí es que si estamos verificando no podemos usar una verificación positiva
        # Aquí usamos el return para salir de la recursión y estamos asumiendo que el caso False es el que nos saca
        # Que tiene todo el sentido del mundo.
        # Warning! The problem here is that we are verifying with a False-assumption premise 
        # Thus we aim to return False to stop the recursion. This only works because we asume that the False case
        # is the one that gets us out of the recursion loop, wich in hintsight makes a lot of sense.
        return False
    return (
        same_keys(root1["left"], root2["left"]) and
        same_keys(root1["right"], root2["right"])
    )
    
def is_symetric(root):
    if root is None:
        return True
    return is_mirror(root["left"], root["right"])

