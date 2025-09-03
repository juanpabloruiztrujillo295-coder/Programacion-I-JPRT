#Juego de Subcadenas: Jugador A (vocales) vs Jugador B (consonantes)

def obtener_subcadenas(cadena, modo):
    vocales = "aeiouAEIOU"
    subcadenas = []
    for i in range(len(cadena)):
        if (modo == "vocal" and cadena[i] in vocales) or \
            (modo == "consonante" and cadena[i] not in vocales):
            for j in range(i + 1, len(cadena) + 1):
                subcadenas.append(cadena[i:j])
    return subcadenas


print("=" * 50)
print("  BIENVENIDO AL JUEGO DE SUBCADENAS")
print("=" * 50)

# Entrada del jugador
cadena_inicial = input("Ingrese la cadena de texto: ")

print("\n Generando subcadenas...\n")

# Subcadenas de cada jugador
subcadenas_A = obtener_subcadenas(cadena_inicial, "vocal")
subcadenas_B = obtener_subcadenas(cadena_inicial, "consonante")

# Conteo de subcadenas
A = len(subcadenas_A)
B = len(subcadenas_B)

print("=" * 50)
print(" RESULTADOS")
print("=" * 50)
print(f"Jugador A (vocales)     ➡  {A} subcadenas")
print(f"Jugador B (consonantes) ➡  {B} subcadenas")
print("-" * 50)

# Determinar ganador
if A > B:
    print(f" El ganador es el JUGADOR A con {A} subcadenas.")
elif B > A:
    print(f" El ganador es el JUGADOR B con {B} subcadenas.")
else:
    print(f" ¡Es un empate! Ambos tienen {A} subcadenas.")

print("\n" + "=" * 50)
print("  LISTA DE SUBCADENAS")
print("=" * 50)

print("\n Jugador A (vocales):")
print(", ".join(subcadenas_A))

print("\n Jugador B (consonantes):")
print(", ".join(subcadenas_B))

print("\n" + "=" * 50)
print("  FIN DEL JUEGO")
print("=" * 50)

