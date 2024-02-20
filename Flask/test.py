import tkinter as tk

def placer_points(entry_nombre, label_info):
    # Récupère le nombre entré dans la zone de texte
    try:
        nombre_points = int(entry_nombre.get())
        if 1 <= nombre_points <= 5:
            # Ici, vous pouvez gérer la logique pour placer les points
            label_info.config(text=f"Nombre de points à placer : {nombre_points}")
        else:
            label_info.config(text="Entrez un nombre entre 1 et 5.")
    except ValueError:
        label_info.config(text="Entrez un nombre valide.")

def main():
    # Création de la fenêtre principale
    window = tk.Tk()
    window.title("Fenêtre de base")
    window.geometry("400x300")

    # Zone de texte pour entrer le nombre
    entry_nombre = tk.Entry(window)
    entry_nombre.pack()

    # Label pour afficher les informations
    label_info = tk.Label(window, text="")
    label_info.pack()

    # Bouton pour confirmer le nombre
    button_confirmer = tk.Button(window, text="Confirmer", command=lambda: placer_points(entry_nombre, label_info))
    button_confirmer.pack()

    # Exécuter la boucle principale
    window.mainloop()

if __name__ == "__main__":
    main()
