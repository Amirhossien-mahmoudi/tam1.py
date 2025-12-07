def calc_avg(scores):
    total = sum(scores)
    count = len(scores)
    return total / count

def check_status(moadel):
    if moadel >= 17:
        return "Aali"
    elif moadel >= 12:
        return "Ghabool"
    else:
        return "Mashroot"

dars_count = int(input("Chand ta dars dari? "))
nomarat = []

for idx in range(dars_count):
    nomre = float(input(f"Nomre dars {idx + 1}: "))
    nomarat.append(nomre)

moadel = calc_avg(nomarat)
vaz = check_status(moadel)

print(f"\nMoadel shoma: {moadel:.2f}")
print(f"Vaziyat shoma: {vaz}")