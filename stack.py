from collections import deque
class stack:
    def __init__(self):
        self.stack = deque()
        self.top = -1
    
    def push(self,data):
        if data is not None:
            self.stack.append(data)
            self.top += 1
            return
        print('Data cannot be empty')
    
    def pop(self):
        if self.top < 0:
            print('Stack is empty')
        else:
            print(f'Popped element is {self.stack.pop()}')
            self.top -= 1

    def peek(self):
        if self.top < 0:
            print('Stack is empty')
        else:
            print(f'Peek element is {self.stack[self.top]}')
    
    def display(self):
        for i in self.stack:
            print(i, end=" ")

def main():
    stack_ds = stack()
    stack_ds.push(10)
    stack_ds.pop()
    stack_ds.peek()
    stack_ds.push(10)
    stack_ds.push(120)
    stack_ds.display()

    for i in range(0,4):
        print(i)
    print(i)

if __name__ == '__main__':
    main()


