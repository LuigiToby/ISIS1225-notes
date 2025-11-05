from DataStructures import double_node as lt
import pprint


def remove_duplicates(my_list):
    if lt.is_empty(my_list) or my_list['size'] == 1:
        return my_list
    else:
        nodo1 = my_list['header']['next']    
        nodo2 = nodo1['next']    
                        
        while nodo2['info'] != None:
            if nodo1['info'] == nodo2['info']:               
                
                nodo1['next'] = nodo2['next']                         
                nodo2['next']['prev'] = nodo1

                nodo2 = nodo2['next']                   

                my_list['size'] -= 1
            else:  
                nodo1 = nodo2                         
                nodo2 = nodo2['next']                            
    
        return my_list
    
    
def remove_value(my_list, value):
    if lt.is_empty(my_list):
        return
    else: 
        current = my_list['header']['next']
        while current != my_list['trailer']:
            next_node = current['next']
            if current['info'] == value:
                current['prev']['next'] = current['next']
                current['next']['prev'] = current['prev']
                my_list['size'] -= 1
            current = next_node
            
def insert_after_value(my_list, value, new_value):
    if lt.is_empty(my_list):
        return
    else: 
        current=my_list['header']['next']
        while current != my_list['trailer']:
            next_node = current["next"]
            if value == current['info']:
                
                nuevo_nodo = lt.new_double_node(new_value)
                nuevo_nodo['next'] = current['next']
                nuevo_nodo['prev'] = current
                
                current['next']['prev'] = nuevo_nodo
                current['next'] = nuevo_nodo
                
                my_list['size'] += 1
                
            current = next_node

def remove_all_before_value(my_list, value):
    """
    Elimina todos los nodos que aparecen ANTES de la primera ocurrencia de `value`.
    Si `value` no está en la lista, no hacer nada.
    """
    
    if lt.is_empty(my_list):
        return
    else:
        current = my_list['header']['next']
        while current != my_list['trailer']:
            if current['info'] == value:
                current['prev'] = my_list['header']             #2
                my_list['header']['next'] = current             #1
                break
            current = current['next']


def remove_all_after_value(my_list, value):
    """
    Elimina todos los nodos que aparecen DESPUÉS de la primera ocurrencia de `value`.
    Si `value` no está en la lista, no hacer nada.
    """
    if lt.is_empty(my_list):
        return
    else:
        current = my_list['header']['next']
        while current != my_list['trailer']:
            
            if current['info'] == value:
                
                my_list['trailer']['prev'] = current
                current['next'] = my_list['trailer']
                break
            
            current = current['next']

def remove_between(my_list, start_value, end_value):
    """
    Elimina todos los nodos que están ENTRE la primera ocurrencia de `start_value`
    y la primera ocurrencia de `end_value` (sin borrar esos valores).
    Si alguno no está en la lista, no hacer nada.
    Si `start_value` aparece después de `end_value`, no hacer nada.
    """
    if lt.is_empty(my_list):
        return
    else:
        start_node = None
        end_node = None
        current = my_list['header']['next']
        while current != my_list['trailer']:
            if current['info'] == start_value:
                start_node = current
            if current['info'] == end_value:  
                          
                
            else:
                current=current["next"]
                
                
    
        
my_list = lt.new_double_list() # Creo lista vacía

lt.add_last(my_list, "1")

lt.add_last(my_list, "2")

lt.add_last(my_list, "3")

lt.add_last(my_list, "5")

lt.add_last(my_list, "1")


lt.add_last(my_list, "3")

lt.add_last(my_list, "5")

lt.add_last(my_list, "1")

lt.add_last(my_list, "3")

lt.add_last(my_list, "5")

lt.add_last(my_list, "1")

lt.add_last(my_list, "100")

lt.add_last(my_list, "2")

lt.add_last(my_list, "2")

# remove_duplicates(my_list)

lt.pprint_double_list(my_list)

# remove_value(my_list, "2")



# insert_after_value(my_list, "2", "wow un dos")

# remove_all_before_value(my_list, "100")

# remove_all_after_value(my_list, "100")

remove_between(my_list, "2", "100")

lt.pprint_double_list(my_list)



