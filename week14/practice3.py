names = ["Alice", "Bob", "Charlie", "David", "Eve"]
gpas = [3.9, 3.2, 3.6, 3.7, 3.5]

hours = [10, 100, 60, 20, 40]

allinone = list(zip(names, gpas, hours))
eligible = [
    (name, gpa, hour) for name, gpa, hour in allinone
    if gpa >= 3.8 or (gpa >= 3.5 and hour > 50)
]


eligible.sort(key = lambda x: (x[0], x[2]))
eligiable = [f"{name}: {gpa} / {hour}" for name, gpa, hour in eligible ]
print(eligiable)