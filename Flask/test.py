import tkinter as tk
from tkinter import*
import threading

import requests

def main():
    nombre_points = [0]

    def placer_points(entry_nombre, label_info):
        try:
            nombre_points[0] = int(entry_nombre.get())
            if 1 <= nombre_points[0] <= 5:
                label_info.config(text=f"Nombre de points à placer : {nombre_points[0]}")
                canvas.bind("<Button-1>", lambda event: placer_point(event, canvas, nombre_points, label_info))
            else:
                label_info.config(text="Entrez un nombre entre 1 et 5.")
        except ValueError:
            label_info.config(text="Entrez un nombre valide.")

    
    def placer_point(event, canvas, nombre_points, label_info):
        if nombre_points[0] > 0:
        # Dessine un point à l'emplacement du clic
            rayon = 45
            canvas.create_oval(event.x - rayon, event.y - rayon, event.x + rayon, event.y + rayon, fill='blue')
            nombre_points[0] -= 1
            label_info.config(text=f"Points restants à placer : {nombre_points[0]}")
        else:
            label_info.config(text="Tous les points ont été placés.")
            canvas.unbind("<Button-1>")

    # Création de la fenêtre principale
    window = tk.Tk()
    window.title("Fenêtre de base")
    window.geometry("1000x1000")

    # Zone de texte pour entrer le nombre
    entry_nombre = tk.Entry(window)
    entry_nombre.pack()

    # Label pour afficher les informations
    label_info = tk.Label(window, text="")
    label_info.pack()

    # Bouton pour confirmer le nombre
    button_confirmer = tk.Button(window, text="Confirmer", command=lambda: placer_points(entry_nombre, label_info))
    button_confirmer.pack()
    
    canvas = tk.Canvas(window, width=1000, height=1000)
    canvas.pack()

    canvas.bind("<Button-1>", lambda event: placer_point(event, canvas, nombre_points, label_info))


    # Exécuter la boucle principale
    window.mainloop()



def lancer_application_tkinter():
    def placer_point(event):
        # Vous pouvez ici envoyer une requête à Flask pour mettre à jour la carte
        # Par exemple, envoi des coordonnées du clic
        requests.post('http://127.0.0.1:5000/update', json={'x': event.x, 'y': event.y})

        # Votre logique de placement de point dans l'interface Tkinter
        # ...
        nombre_points = [0]

        def placer_points(entry_nombre, label_info):
            try:
                nombre_points[0] = int(entry_nombre.get())
                if 1 <= nombre_points[0] <= 5:
                    label_info.config(text=f"Nombre de points à placer : {nombre_points[0]}")
                    canvas.bind("<Button-1>", lambda event: placer_point(event, canvas, nombre_points, label_info))
                else:
                    label_info.config(text="Entrez un nombre entre 1 et 5.")
            except ValueError:
                label_info.config(text="Entrez un nombre valide.")

    
    def placer_point(event, canvas, nombre_points, label_info):
        if nombre_points[0] > 0:
        # Dessine un point à l'emplacement du clic
            rayon = 5
            canvas.create_oval(event.x - rayon, event.y - rayon, event.x + rayon, event.y + rayon, fill='blue')
            nombre_points[0] -= 1
            label_info.config(text=f"Points restants à placer : {nombre_points[0]}")
        else:
            label_info.config(text="Tous les points ont été placés.")
            canvas.unbind("<Button-1>")


    # Création de la fenêtre principale Tkinter
    window = tk.Tk()
    window.title("Placement de Points")
    window.geometry("400x300")

    # Création d'un Canvas pour les dessins
    canvas = tk.Canvas(window, width=400, height=200)
    canvas.pack()
    canvas.bind("<Button-1>", placer_point)

    # Exécuter la boucle principale
    window.mainloop()

if __name__ == "__main__":
    main()
