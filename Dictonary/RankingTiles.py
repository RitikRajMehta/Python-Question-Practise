results = {
    "Aarav": 86,
    "Meera": 94,
    "Kabir": 94,
    "Tara": 81,
    "Ishaan": 88,
    "Diya": 81
}

marks = []

for mark in results.values():
    if mark not in marks:
        marks.append(mark)

# Manual descending sort
for i in range(len(marks)):
    for j in range(i + 1, len(marks)):
        if marks[i] < marks[j]:
            marks[i], marks[j] = marks[j], marks[i]

ranking = {}
rank = 1

for mark in marks:
    count = 0

    for student, score in results.items():
        if score == mark:
            ranking[student] = rank
            count += 1

    rank += count

print("Ranking:", ranking)

print("Rank 1 Students:")
for student, rank in ranking.items():
    if rank == 1:
        print(student)