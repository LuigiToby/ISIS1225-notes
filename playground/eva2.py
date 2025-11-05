from DataStructures.List import array_list as lt # Importo mi implementación de lista para guardar la información

# Problema 1 eva2 de prueba

def best_par(list, target):
    if lt.size(list) < 2:
        return None
    lt.shell_sort(list, lt.default_sort_criteria)
    left = 0
    right = lt.size(list)-1

    best_pair = (lt.get_element(list, left), lt.get_element(list, right))
    best_diff = float("inf")

    while left < right: # Ojo mejor usar < y no <=
        s = lt.get_element(list, left)+lt.get_element(list, right)
        diff = abs(target-s) # El orden de esto no importa
        if diff < best_diff:
            best_pair = (lt.get_element(list, left), lt.get_element(list, right))
            best_diff  = diff
        if diff == 0:
            return best_pair
        if s > target:
            right -=1
        if s < target:
            left +=1
    return best_pair

# [1,2,3,4], busco el 8
# Entonces si 1+4 = 5 < 8, es decir tengo que aumentar, luego para aumentar me muevo a la derecha

list1 = lt.new_list()

lt.add_last(list1, 1)
lt.add_last(list1, 4)
lt.add_last(list1, 3)
lt.add_last(list1, 2)

list2 = lt.new_list()

list3 = lt.new_list()
lt.add_last(list3, 1)

list4 = lt.new_list()
lt.add_last(list4, -2)
lt.add_last(list4, 7)

list5 = lt.new_list()

lt.add_last(list5, 1)
lt.add_last(list5, 9)
lt.add_last(list5, -3)
lt.add_last(list5, 10)


list6 = lt.new_list()

lt.add_last(list6, 2)
lt.add_last(list6, 5)
lt.add_last(list6, 11)
lt.add_last(list6, -2)
lt.add_last(list6, 7)

list7 = lt.new_list()

lt.add_last(list7, 1)
lt.add_last(list7, 4)
lt.add_last(list7, 6)
lt.add_last(list7, 8)

print(best_par(list1, 6))
print(best_par(list2, 6))
print(best_par(list3, 6))
print(best_par(list4, 4))
print(best_par(list5, 6))
print(best_par(list6, 9))
print(best_par(list7, 11))


# Ejemplo 1 ChatGPT

def func1(list, target):
    if lt.size(list)<2:
        return(None)
    lt.shell_sort(list, lt.default_sort_criteria)
    best_diff = float('inf')
    left = 0
    right = lt.size(list) - 1
    best_pair = (lt.get_element(list, left), lt.get_element(list, right))
    while left < right:
        ad = abs(lt.get_element(list, left) - lt.get_element(list, right)) 
        diff = abs(ad-target)
        if diff < best_diff:
            best_diff=diff
            best_pair = (lt.get_element(list, left), lt.get_element(list, right))
        if diff == 0:
            return best_pair
        if ad > target:
            right-=1
        else:
            left+=1
    return best_pair

# Ejemplo 2 combinaciones en rango suma

def func2(list, range):
    if lt.size(list)<2:
        return(None)
    lt.shell_sort(list, lt.default_sort_criteria)
    left = 0
    right = lt.size(list) - 1
    contador = 0
    min_r, max_r = lt.get_element(range, 0), lt.get_element(range, 1)
    while left < right:
        s = lt.get_element(list, left) + lt.get_element(list, right)
        if min_r <= s <= max_r:
            contador += 1
            right-=1
        elif s > max_r:
            right-=1
        else:
            left+=1
    return contador


# Verifica si existe un par en la lista cuya diferencia absoluta sea exactamente igual a k.

def func3(list, k):
    if lt.size(list)<2: return None
    lt.shell_sort(list, lt.default_sort_criteria)
    l, r = 0, lt.size(list) - 1
    while l < r:
        s = abs(lt.get_element(list, l) - lt.get_element(list, r))
        if s == k: return True
        elif s > k: r-=1
        else: l+=1
    return False

# Calcular mediana de la lista

def mediana(list):
    s = lt.size(list)
    if s == 0: return None
    if s == 1: return lt.get_element(list,0)
    lt.shell_sort(list, lt.default_sort_criteria)
    
    if s%2 == 0: return (lt.get_element(list, (s//2)-1)+lt.get_element(list, s//2))/2
    
    else: return lt.get_element(list, s//2)        
    
# Distancia mínima entre dos elementos consecutivos en la lista

def dist_min(list):
    size = lt.size(list)
    if size < 2: return None
    lt.shell_sort(list, lt.default_sort_criteria)
    result = lt.new_list()
    best_dif = float('inf')
    for i in range(size-1):
        s = abs(lt.get_element(list, i) - lt.get_element(list, i+1))
        cp = (lt.get_element(list, i), lt.get_element(list, i+1))
        if s < best_dif:
            result = lt.new_list() 
            best_dif = s
        if s == best_dif:
            lt.add_last(result, cp)
    return result



        