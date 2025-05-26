# browsing_session = []
# browsing_session.append(1)
# browsing_session.append(2)
# browsing_session.append(3)
# print(browsing_session)
# browsing_session.pop()
# print(browsing_session)
# print("redirect", browsing_session[-1])
# browsing_session.pop()
# browsing_session.pop()

# if not browsing_session:
#     print("disable")
#     # browsing_session[-1]

# implementing stack

# create the stack
def create_stack():
    stack = []
    return stack

# create an empty stack
def check_empty(stack):
    return len(stack) == 0

# adding items to the stack
def push(item, stack):
    stack.append(item)
    print("pushed item: " + item)

# remove an element from the stack
def pop(stack):
    if check_empty(stack):
        return "stack is empty"
    return stack.pop()

stack = create_stack()
push(str(1), stack)
push(str(2), stack)
push(str(3), stack)
push(str(4), stack)
print("popped item: ", pop(stack))
print("stack after popping an element: " + str(stack))
