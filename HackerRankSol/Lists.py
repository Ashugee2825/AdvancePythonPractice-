li = []
n = int(input())
for i in range(n):
    command,*values = input().split()   #' insert 0 5'.split()
    values = list(map(int,values))    # values = [0, 5]
    if command == 'insert':            # command = 'insert'
        li.insert(values[0],values[1])      # li = [5]
    elif command == 'print':           # command = 'print'
        print(li)
    elif command == 'remove':
        li.remove(values[0])
    elif command == 'append':
        li.append(values[0])
    elif command == 'sort':
        li.sort()
    elif command == 'pop':
        li.pop()
    elif command == 'reverse':
        li.reverse()
    else:
        print('Command not found')
    print('command',command)
    print('values',values)
