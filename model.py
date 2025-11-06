import json  # Per guardar i llegir dades en fitxer JSON

class Biblioteca:
    def __init__(self, fitxer='cataleg.json'):
        self.fitxer = fitxer
        try:
            with open(fitxer, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.llibres = data.get('llibres', [])
                self.socis = data.get('socis', [])
        except FileNotFoundError:
            self.llibres = []
            self.socis = []

    def desar(self):
        with open(self.fitxer, 'w', encoding='utf-8') as f:
            json.dump({'llibres': self.llibres, 'socis': self.socis}, f, ensure_ascii=False, indent=4)


    def afegir_llibre(self, titol, autor):  # Afegeix un llibre nou
        llibre = {"titol": titol, "autor": autor, "prestat": False}  # Dades del llibre
        self.llibres.append(llibre)  # Afegim a la llista
        self.desar()  # Guardem els canvis
        print("Llibre afegit.")  # Missatge a l'usuari

    def prestar_llibre(self, titol):  # Marca un llibre com prestat
        for l in self.llibres:  # Recorrem tots els llibres
            if l["titol"].lower() == titol.lower():  # Busquem pel títol
                if not l["prestat"]:  # Si no està prestat
                    l["prestat"] = True  # El marquem com prestat
                    self.desar()  # Guardem
                    print("Llibre prestat.")  # Missatge
                else:
                    print("Ja està prestat.")  # Ja estava prestat
                return  # Sortim de la funció
        print("No s’ha trobat el llibre.")  # No trobat

    def retornar_llibre(self, titol):  # Marca un llibre com retornat
        for l in self.llibres:  # Recorrem tots els llibres
            if l["titol"].lower() == titol.lower():  # Busquem pel títol
                if l["prestat"]:  # Si estava prestat
                    l["prestat"] = False  # El marquem com disponible
                    self.desar()  # Guardem
                    print("Llibre retornat.")  # Missatge
                else:
                    print("Aquest llibre no estava prestat.")  # No estava prestat
                return
        print("No s’ha trobat el llibre.")  # No trobat

    def mostrar_llibres(self):  # Mostra tots els llibres
        if not self.llibres:  # Si la llista és buida
            print("No hi ha llibres al catàleg.")  # Missatge
        else:
            for l in self.llibres:  # Recorrem tots els llibres
                estat = "Prestat" if l["prestat"] else "Disponible"  # Text de l’estat
                print(f"{l['titol']} ({l['autor']}) - {estat}")  # Mostrem el llibre

    def mostrar_socis(self):  # Mostra tots els socis
        print("Socis de la biblioteca:")  # Títol
        for s in self.socis:  # Recorrem la llista de socis
            print("-", s)  # Mostrem cada nom
