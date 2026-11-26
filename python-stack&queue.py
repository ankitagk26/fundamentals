def is_empty(structure):
    return len(structure) == 0

"""Stack-LIFO"""
def push(stack, item):
    stack.append(item)
    print(f"Pushed {item} onto stack.")

def pop_item(stack):
    if is_empty(stack):
        print("Stack Underflow..stack is empty!")
        return None
    popped=stack.pop()
    print(f"Popped {popped} from stack.")
    return removed

def peek(stack):
    if is_empty(stack):
        print("Stack is empty..no top element.")
        return None
    print(f"Top element of stack: {stack[-1]}")
    return stack[-1]

def display_stack(stack):
    if is_empty(stack):
        print("Stack is empty.")
    else:
        print("Stack (top - bottom):", list(reversed(stack)))

"""Queue-FIFO"""
def enqueue(queue, item):
    queue.append(item)
    print(f"Enqueued {item} into queue.")
  
def dequeue(queue):
    if is_empty(queue):
        print("Queue Underflow..queue is empty!")
        return None
    removed=queue.pop(0)
    print(f"Dequeued {removed} from queue.")
    return removed

def queue_front(queue):
    if is_empty(queue):
        print("Queue is empty. No front element.")
        return None
    print(f"Front element of queue: {queue[0]}")
    return queue[0]

def display_queue(queue):
    if is_empty(queue):
        print("Queue is empty.")
    else:
        print("Queue (front -> rear):", queue)

def stack_menu():
    stack=[]
    while True:
        print("\nStack Menu:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Back to Main Menu")
        ch = int(input("Enter choice: "))
        if ch==1:
            element=int(input("Enter value to push: "))
            push(stack,element)
        elif ch==2:
            pop_item(stack)
        elif ch==3:
            peek(stack)
        elif ch==4:
            display_stack(stack)
        elif ch==5:
            break
        else:
            print("*invalid choice*")

def queue_menu():
    queue = []
    while True:
        print("\nQueue Menu:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Front")
        print("4. Display")
        print("5. Back to Main Menu")
        ch=int(input("Enter choice: "))
        if ch==1:
            element=int(input("Enter value to enqueue: "))
            enqueue(queue,element)
        elif ch==2:
            dequeue(queue)
        elif ch==3:
            queue_front(queue)
        elif ch==4:
            display_queue(queue)
        elif ch==5:
            break
        else:
            print("*invalid choice*")

while True:
    print("\nLinear Data Structures Menu:")
    print("1. Stack Operations")
    print("2. Queue Operations")
    print("3. Exit")
    choice = int(input("Enter choice: "))
    if choice==1:
        stack_menu()
    elif choice==2:
        queue_menu()
    elif choice==3:
        print("Program exited")
        break
    else:
        print("*invalid choice*")
