import os
import sys
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from gui.question1 import Question1


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Alzheimer Predictor")
        self.root.geometry("600x500")
        self.root.resizable(False, False)

        # Funkcja do poprawiania ścieżek
        def resource_path(relative_path):
            """ Naprawia ścieżkę w przypadku uruchamiania jako .exe """
            if hasattr(sys, '_MEIPASS'):
                return os.path.join(sys._MEIPASS, relative_path)
            return os.path.join(os.path.abspath("."), relative_path)

        # Pobranie poprawnej ścieżki do obrazka
        image_path = resource_path("assets/logo.png")

        try:
            image = Image.open(image_path)
            image = image.resize((200, 200), Image.LANCZOS)
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

        # 📝 **Dodanie informacji o projekcie na dole**
        footer_label = tk.Label(root, text="Projekt zaliczeniowy na przedmiot Inżynieria Oprogramowania\n"
                                           "Autorzy: Michał Wroński, Karol Kobus\n"
                                           "v. 0.9   2025",
                                font=("Arial", 9), fg="gray")
        footer_label.pack(side="bottom", pady=5)

    def open_question1(self):
        self.root.destroy()
        root = tk.Tk()
        app = Question1(root)
        root.mainloop()
