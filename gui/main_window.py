import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

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
