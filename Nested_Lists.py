records = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    records.append([name, score])
    
scores = sorted(set([record[1] for record in records]))
sec_lowest = scores[1]

names = sorted([record[0] for record in records if record[1] == sec_lowest])

for name in names:
    print(name)