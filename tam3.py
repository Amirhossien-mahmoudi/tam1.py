def get_avg(scores):
    jam = sum(scores)
    tedad = len(scores)
    return jam / tedad

students = [
    {"id": 101, "esm": "Ali", "nomarat": [18, 19, 20]},
    {"id": 102, "esm": "Amir", "nomarat": [15, 14, 16.5]},
    {"id": 103, "esm": "Reza", "nomarat": [17, 16, 18.5, 19]}
]

print("Moadel har daneshjo:")
for st in students:
    moadel = get_avg(st["nomarat"])
    print(f"{st['esm']} (ID: {st['id']}) --> Moadel: {moadel:.2f}")