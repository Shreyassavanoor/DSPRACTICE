def reverse_func(tuple_param):
    reversed_tuple = tuple(reversed(tuple_param))
    print(f'Tuple before reversing {tuple_param}')
    print(f'Tuple of reversing {reversed_tuple}')

def copy_func(tuple_param):
    tuple_copy = tuple_param[:]
    print(f'Tuple copy {tuple_copy}')

def sort_func(tuple_param):
    sorted_tuple = tuple(sorted(tuple_param))
    print(f'Tuple sorted {sorted_tuple}')

def index_func(tuple_param):
    index = tuple_param.index(3)
    print(f'index of 3 is {index}')

def count_func(tuple_param):
    count = tuple_param.count(3)
    print(f'count of 3 is {count}')


def clear_func(tuple_param):
    print(f'Tuple before clearing {tuple_param}')
    tuple_param = ()
    print(f'Tuple after clearing {tuple_param}')


def tuple_practice():

    #declaring type 1
    my_tuple = 1,2,3,4,5

    #declaring type 2
    my_tuple2 = (5,4,3,2,1)

    #append X
    #extend X
    #insert X
    #remove X
    #pop X

    reverse_func(my_tuple)
    copy_func(my_tuple)
    sort_func(my_tuple2)
    index_func(my_tuple)
    count_func(my_tuple)
    clear_func(my_tuple)


def main():
    tuple_practice()

if __name__ == '__main__':
    main()