max= 20
stack= [max]

top= 0

def push(stack, item):
    if top< max:
        top+= 1
        stack[top]= item
    else:
        return "Stack owerflow"    


def pop(stack,):
    if not is_empty(stack):
        popped_item= stack.pop()
        return popped_item
    else:
        return "Stack is empty"


def peek(stack,):
    if not is_empty(stack):
        return stack[top]
    else:
        return "Stack is empty!"

    
def is_empty(stack):
    return stack is None



push(stack, 10)
push(stack, 20)
pop(stack)
print(f"Top element is {peek(stack)}")