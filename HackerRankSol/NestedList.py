n = int(input())
li = []
for i in range(n):
    name = input()
    score = float(input())
    li.append([name,score])

    scores = []
    for name, score in li:
        scores.append(score)
    scores = sorted(set(scores))
    scores.sort()
    name_li = []
    second_smallest_score = scores[1]
    
    for name, score in li:
        if score == second_smallest_score:
            name_li.append(name)
            print(name)
    for name in sorted(name_li):
        print(name)

