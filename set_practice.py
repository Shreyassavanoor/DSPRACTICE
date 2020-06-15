def disjoint_func(set1, set2):
    #if intersection is empty then set1 is disjoint

    is_disjoint = set1.isdisjoint(set2)
    print(f'Is Set1 disjoint? {is_disjoint} ')

def subset_func(set1, set2):
    #if every element of set1 is present in set2 then set1 is subset of set2.. set1 can also be equal to set2
    is_subset = set1.issubset(set2)
    print(f'Is Set1 subset of set2? {is_subset} ')

    #aliter for subset
    is_subset = set1 <= set2
    print(f'Is Set1 subset of set2? {is_subset} ')

    #proper subset means if all of elements of set1 present in set2 and set1 not equal to set2
    proper_subset = set1 < set2
    print(f'Is Set1 proper subset of set2? {proper_subset} ')

def superset_func(set1, set2):
    #Test whether every element in set2 is in the set1.
    is_superset = set1.issuperset(set2)
    print(f'Is Set1 superset of set2? {is_superset} ')

    #aliter for subset
    is_superset = set1 >= set2
    print(f'Is Set1 superset of set2? {is_superset} ')

    #proper superset means if all of elements of set2 present in set1 and set1 not equal to set2
    proper_superset = set1 > set2
    print(f'Is Set1 proper superset of set2? {proper_superset} ')

def setunion_func(set1, set2):
    #Return a new set with elements from the set and all others.
    union_set = set1.union(set2)
    print(f'Union set of set1 and set2 is {union_set}')

    #aliter for union
    union_set = set1 | set2
    print(f'Union set of set1 and set2 is {union_set}')

def setintersection_func(set1, set2):
    #Return a new set with elements common to the set and all others..
    intersection_set = set1.intersection(set2)
    print(f'Intersection set of set1 and set2 is {intersection_set}')

    #aliter for Intersection
    intersection_set = set1 & set2
    print(f'Intersection set of set1 and set2 is {intersection_set}')

def setdifference_func(set1, set2):
    #Return a new set with elements in the set that are not in the others.
    difference_set = set1.difference(set2)
    print(f'Difference set of set1 and set2 is {difference_set}')

    #aliter for Difference
    difference_set = set1 - set2
    print(f'Difference set of set1 and set2 is {difference_set}')

def setsymdifference_func(set1, set2):
    #Return a new set with elements in either the set or other but not both.
    sym_difference_set = set1.symmetric_difference(set2)
    print(f'Symmetric Difference set of set1 and set2 is {sym_difference_set}')

    #aliter for Difference
    sym_difference_set = set1 ^ set2
    print(f'Symmetric Difference set of set1 and set2 is {sym_difference_set}')

def setcopy_func(set1):
    copy_set = set1.copy()
    print(f'Copy of set1 is {copy_set}')

def setadd_func(set1):
    #Add element elem to the set.
    set1.add(100)
    print(f'Set1 after adding 100 {set1}')

def setremove_func(set1):
    #Remove element elem from the set. Raises KeyError if elem is not contained in the set.
    set1.remove(100)
    print(f'Set1 after removing 100 {set1}')

def setdiscard_func(set1):
    #Remove element elem from the set if it is present..
    set1.discard(100)
    print(f'Set1 after removing 100 {set1}')

def setpop_func(set1):
    #Remove and return an arbitrary element from the set. Raises KeyError if the set is empty.
    popped_value = set1.pop()
    print(f'Set1 after popping random element {set1}')
    print(f'Popped value is {popped_value}')

def setupdate_func(set1, set2):
    #Update the set, adding elements from all others.
    set1.update(set2)
    print(f'Set1 after updating {set1}')

    #aliter for update
    set1 |= set2
    print(f'Set1 after updating {set1}')

def setintersection_update(set1, set2):
    #Update the set, keeping only elements found in it and all others.
    set1.intersection_update(set2)
    print(f'Set1 after updating intersection {set1}')

    #aliter for intersection update
    set1 &= set2
    print(f'Set1 after updating intersection {set1}')

def setdifference_update(set1, set2):
    #Update the set, removing elements found in others.
    set1.difference_update(set2)
    print(f'Set1 after updating difference {set1}')

    #aliter for difference update
    set1 -= set2
    print(f'Set1 after updating difference {set1}')

def setsymdifference_update(set1, set2):
    #Update the set, keeping only elements found in either set, but not in both.
    set1.symmetric_difference_update(set2)
    print(f'Set1 after updating sym difference {set1}')

    #aliter for sym difference update
    set1 ^= set2
    print(f'Set1 after updating sym difference {set1}')

def setclear_func(set1):
    print(f'Set before clearing {set1}')
    set1.clear()
    print(f'Set after clearing {set1}')

def set_practice():
    my_set1 = {1, 2, 3, 4, 5, 10}
    my_set2 = {1, 2, 3, 4, 5,6, 7, 8, 9}
    my_set3 = {10,200,300}
    
    disjoint_func(my_set1, my_set2)
    subset_func(my_set1, my_set2)
    superset_func(my_set1, my_set2)
    setunion_func(my_set1, my_set2)
    setintersection_func(my_set1, my_set2)
    setdifference_func(my_set1, my_set2)
    setsymdifference_func(my_set1, my_set2)
    setcopy_func(my_set1)

    #data update functions
    setadd_func(my_set1)
    setremove_func(my_set1)
    setdiscard_func(my_set1)
    setpop_func(my_set1)
    setupdate_func(my_set1, my_set3)
    setintersection_update(my_set1, my_set3)
    setdifference_update(my_set1, my_set3)
    setsymdifference_update(my_set1, my_set3)
    setclear_func(my_set2)

def main():
    set_practice()

if __name__ == '__main__':
    main()
