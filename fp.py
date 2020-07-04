def map_func():
    #Return an iterator that applies function to every item of iterable, yielding the results.
    #map can take any number of iterables

    my_list1 = [1,2,3,4,5]
    my_list2 = [10,20,30,40,50]

    def double_func(item1, item2):
        return item1 * item2

    for r in map(double_func, my_list1, my_list2):
        print(r)

def filter_func():
    #Construct an iterator from those elements of iterable for which function returns true.
    my_list = [1,2,3,4,5,6]

    def filter_greater2(item):
        return item > 2
    
    for r in filter(filter_greater2, my_list):
        print(r)

def zip_func():
    #Make an iterator that aggregates elements from each of the iterables.
    my_list1 = [1,2,3,4,5]
    my_list2 = [10,20,30,40,50]
    for r in zip(my_list1, my_list2):
        print(r)

def main():
    #map_func()
    #filter_func()
    zip_func()

if __name__ == '__main__':
    main()