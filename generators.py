def num_generator():
    for i in range(100):
        yield i

def main():
    for i in num_generator():
        print(i)
    g = num_generator()
    print(next(g))
    print(next(g))

if __name__ == '__main__':
    main()