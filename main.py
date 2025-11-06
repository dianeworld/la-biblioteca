
# ------------------------------------------------------------
# Projecte 05-11-2025: Gestió de Biblioteca (PAC-1)
# Fitxer: main.py
# Autors: Oscar Fouz Robles i Diana Urbano Fernández
# Data: 05 Novembre de 2025
# Descripció: - Primer commit
# Mostrar menú senzill per interactuar amb la biblioteca.
# Permet afegir llibres i alumnes per fer préstecs, retorns...
# i consultar la informació desada als fitxers JSON.
# ------------------------------------------------------------


from model import biblioteca

# Crear una instància de la biblioteca
biblio = Biblioteca()

# Funció per mostrar el menú d'opcions
def mostrar_menu():    
    print("1. Afegir llibre")
    print("2. Prestar llibre")
    print("3. Retornar llibre")
    print("4. Buscar per autor")
    print("5. Mostrar tots els llibres")
    print("0. Sortir!!!")


# Funció per llegir l'opció de l'usuari amb gestió bàsica d'errors
def get_option():
    try:
        return int(input("Tria opció: "))
    except ValueError:
        print("Si us plau, introdueix un número.")
        return -1  # Opció no vàlida


# Bucle principal del programa
while True:
    mostrar_menu()                          # Mostrar menú cada vegada
    op = get_option()                       # Llegir opció de l'usuari

    match op:                               # és la sintaxi de pattern matching introduïda a Python 3.10.
        case 1:
            # Anem a afegir un llibre
            t = input("Títol: ")
            a = input("Autor: ")
            biblio.afegir_llibre(t, a)      # Cridar la funció de biblioteca
            # pass

        case 2:
            # Prestar un llibre
            t = input("Títol a prestar: ")
            biblio.prestar_llibre(t)        # Cridar la funció de biblioteca
            # pass
            
        case 3:
            # Retornar un llibre
            t = input("Títol a retornar: ")
            biblio.retornar_llibre(t)       # Cridar la funció de biblioteca
            # pass
        
        case 4:
            # Buscar llibres per autor
            a = input("Autor: ")
            for l in biblio.llibres:        # Recórrer tots els llibres
                if l.autor.lower() == a.lower():  # Comparar noms ignorants majúscules/minúscules
                    print(l)
        case 5:
            # Mostrar tots els llibres
            for l in biblio.llibres:
                print(l)
        case 0:
            # Sortir del programa
            break

