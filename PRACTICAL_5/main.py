# problem 1
class Stack:
    def __init__(self):
        self.item = []

    def is_empty(self):
        return len(self.item) == 0

    def push(self, i):
        self.item.append(i)
    
    def pop(self):
        if not self.is_empty():
            return self.item.pop()
        else:
            return "stack is empty"
        
    def peek(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            return "stack is empty"

    def size(self):
        return len(self.item)

# evaluate postfix expression 
def evaluate_postfix_expression(expression):
    # initializing stack 
    stack = Stack()

    # split the expression by space to get each number or operaration
    items = expression.split()

    # now loop through the expression 
    for i in items:
        if i.isdigit(): # if i is number
            stack.push(int(i))
        else: # if i is operation 
            # pop the top two item(number) from the stack
            first_number = stack.pop()
            second_number = stack.pop()

            # now do the calculation
            if i == "+": # if operation is addition
                result = second_number + first_number
            elif i == "-": # if operation is subtraction
                result = second_number - first_number
            elif i == "*": # multiplication
                result = second_number * first_number
            elif i == "/": # division
                result = second_number / first_number
            
            # now after performing calculation add the result to stack
            stack.push(result)

    # final result be remain at the last 
    return stack.pop()

expression = "4 5 + 2 * 7 -"
result = evaluate_postfix_expression(expression)
print(f"result: {result}")

# problem 2
class Queue_using_2stack:
    def __init__(self):
        # stack for enqueue
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        # push item to stack1
        self.stack1.append(item)

    def dequeue(self):
        # if stack2 is empty, move element from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        # if stack is still empty, queue is empty
        if not self.stack2:
            return "dequeue from empty queue"
        
        return self.stack2.pop()

    def is_empty(self):
        # return true if both stack is empty
        return not self.stack1 and not self.stack2

    def size(self):
        # return the number of items in queue
        return len(self.stack1) + len(stack2)

queue = Queue_using_2stack()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())
print(queue.dequeue())

# problem 3
import time

class task_scheduler:
    def __init__(self):
        # initialize a list to store task 
        self.tasks = []

    def add_task(self, task, *args):
        # add a task
        self.tasks.append((task, args))
        print(f"Task {task.__name__} added to queue with args {args}")
    
    def run_tasks(self):
        # proces the task in sequence
        while self.tasks:
            task, args = self.tasks.pop(0)  # retrieve task in first come first
            print(f"Running task {task.__name__} with args {args}")
            task(*args)  
            time.sleep(1)  # setting the time

# first of all treat the user
def greet(name):
    print(f"Hello, {name}!")

def add(x, y):
    print(f"The sum of {x} and {y} is {x + y}")

def todo_list(tasks):
    print("Here's your list of things to do:")
    for task in tasks:
        print(f"- {task}")
        time.sleep(1)  # display the task in specific time interval
    print("hooray!!! all tasks completed!")


scheduler = task_scheduler()
scheduler.add_task(greet, "Yeshi")
scheduler.add_task(todo_list, ["Buy groceries", "Write report", "Exercise", "Read a book"])

scheduler.run_tasks()

# problem 4
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop() if not self.is_empty() else None

    def peek(self):
        return self.stack[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.stack) == 0


def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = Stack()
    output = []

    for item in expression:
        if item.isdigit():  # if its 
            output.append(item)
        elif item in precedence:  # if its an operator
            while (not stack.is_empty() and stack.peek() != '(' and
                   precedence[item] <= precedence[stack.peek()]):
                output.append(stack.pop())
            stack.push(item)
        elif item == '(':  # push '(' to stack
            stack.push(item)
        elif item == ')':  # pop until '('
            while stack.peek() != '(':
                output.append(stack.pop())
            stack.pop()  # remove '(' from stack

    # pop all remaining operators in the stack
    while not stack.is_empty():
        output.append(stack.pop())

    return ''.join(output)

expression = "3+5*2/(1-4)" # add expression here
print("infix:", expression)
print("postfix:", infix_to_postfix(expression))
