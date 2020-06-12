def append_func(list):
    # adding element at end of list
    list.append(6)
    print(f'List after appending ---> {list}')

    # here first two elements are replaced by iterator values
    list[0: 2] = [11, 12, 13, 14, 15]
    print(f'List after replacing first two elements with iterator ---> {list}')

def extend_func(list):
    iterable = [10,11,12,13,14,15]
    list.extend(iterable)
    print(f'List after extending ---> {list}')

def insert_func(list):
    list.insert(4, 100)
    print(f'List after inserting before index 4 ---> {list}')

def remove_func(list):
    list.remove(11)
    print(f'List after removing 11 ---> {list}')

def pop_func(list):
    popped_value = list.pop(3)
    print(f'Popped value is {popped_value}')
    print(f'List after popping at index 3 ---> {list}')

def clear_func(list):
    list.clear()
    print(f'List after clearing ---> {list}')

def index_func(list):
    index_value = list.index(4)
    print(f'Index of value 4 is {index_value}')

def count_func(list):
    count_value = list.count(100)
    print(f'Count of value 100 is {count_value}')

def sort_func(list):
    list.sort()
    print(f'List after sorting {list}')

    def custom_func(value):
        return value % 2

    list.sort(key = custom_func)
    print(f'List after sorting {list}')

def reverse_func(list):
    list.reverse()
    print(f'List after reversing {list}')
 
def copy_func(list):
    shallow_copy = list.copy()
    print(f'Shallow copy is {shallow_copy}')

def list_practice():
    demo_list = [1, 2, 3, 4, 5]

    append_func(demo_list)
    extend_func(demo_list)
    insert_func(demo_list)
    remove_func(demo_list)
    pop_func(demo_list)
    index_func(demo_list)
    count_func(demo_list)
    sort_func(demo_list)
    reverse_func(demo_list)
    copy_func(demo_list)
    clear_func(demo_list)


def main():
    list_practice()


if __name__ == '__main__':
    main()
