# Without input and Without return Statement
def add():
    a = 10
    b = 20
    print('Addition is:', a+b)
add()

#with input and Without return statemnt
def sub(a,b):
    print('Subtraction is:', a-b)

# without input and with return statemnet
def mul():
    return 10*20

# with input and with return statemnt   
def div(a,b):
    return a/b
          
add()
sub(20,10)
print(mul())
print(div(200,10))
