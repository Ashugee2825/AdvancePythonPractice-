d = {}
n = int(input())
for i in range(n):
    # li = 'Malika 10 20 30'.split()
    name, *scores = input().split() # name = 'Malika', scores = ['10', '20', '30']
    scores = list(map(float, scores))
    d[name] = scores
target_name = input()
for name, score in d.items():
    if target_name in d:
        avg = sum(d[target_name]) / len(d[target_name])
        print(f"{avg:.2f}")
    else:
        print("Name not found")


d = {}
n = int(input())
for i in range(n):
    # li = 'Malika 10 20 30'.split()
    name, *scores = input().split() # name = 'Malika', scores = ['10', '20', '30']
    scores = list(map(float, scores))
    print(name)
    print(scores)
target_name = input()
for name, score in d.items():
    if name == target_name:
        avg = (sum(score)/len(score))
print(f"{avg:.2f}")