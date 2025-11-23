estudiantes = int(input("Número de estudiantes: "))
materias = int(input("Número de materias: "))

matriz = []
for i in range(estudiantes):
    fila = []
    for j in range(materias):
        cal = float(input(f"Calificación del estudiante {i+1} en materia {j+1}: "))
        fila.append(cal)
    matriz.append(fila)

print("\n--- Promedio por estudiante ---")
for i in range(estudiantes):
    prom = sum(matriz[i]) / materias
    print(f"Estudiante {i+1}: {prom:.2f}")

print("\n--- Promedio por materia ---")
for j in range(materias):
    suma = 0
    for i in range(estudiantes):
        suma += matriz[i][j]
    prom = suma / estudiantes
    print(f"Materia {j+1}: {prom:.2f}")

maxima = matriz[0][0]
minima = matriz[0][0]

for i in range(estudiantes):
    for j in range(materias):
        if matriz[i][j] > maxima:
            maxima = matriz[i][j]
        if matriz[i][j] < minima:
            minima = matriz[i][j]

print("\n--- Resultados generales ---")
print("Calificación más alta:", maxima)
print("Calificación más baja:", minima)
