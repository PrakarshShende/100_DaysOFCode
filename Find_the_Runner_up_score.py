n = int(input())
scores = map(int, input().split())

scores = list(set(scores))
scores.remove(max(scores))

print(max(scores))