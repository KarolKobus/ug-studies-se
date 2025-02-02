import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from gui.question1 import Question1


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Alzheimer Predictor")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        # Pobranie ścieżki do katalogu projektu
        base_path = os.path.dirname(os.path.abspath(__file__))  # Katalog 'gui'
        image_path = os.path.join(base_path, "..", "assets", "logo.png")  # Przechodzimy do głównego katalogu

        try:
            image = Image.open(image_path)
            image = image.resize((200, 200), Image.LANCZOS)  # Zamiana ANTIALIAS na LANCZOS
            self.logo = ImageTk.PhotoImage(image)
            img_label = tk.Label(root, image=self.logo)
            img_label.pack(pady=10)
        except Exception as e:
            messagebox.showwarning("Błąd wczytywania obrazu", f"Nie udało się wczytać obrazka: {e}")

        # Dodanie tekstu pod grafiką
        description_label = tk.Label(root,
                                     text="Niniejszy program służy do szacowania ryzyka zachorowania na chorobę Alzheimera na podstawie informacji uzyskanych od pacjenta.",
                                     wraplength=500, justify="center", font=("Arial", 12))
        description_label.pack(pady=10)

        # Przycisk Rozpocznij
        start_button = tk.Button(root, text="Rozpocznij", font=("Arial", 14), command=self.open_question1)
        start_button.pack(pady=20)

    def open_question1(self):
        self.root.destroy()
        root = tk.Tk()
        app = Question1(root)
        root.mainloop()