import tkinter as tk
from gui.question2 import Question2


class Question1:
    def __init__(self, root):
        self.root = root
        self.root.title("Alzheimer Predictor")
        self.root.geometry("600x700")

        # Tytuł sekcji
        tk.Label(root, text="Dane demograficzne", font=("Arial", 16, "bold")).pack(pady=10)

        # Pytanie o płeć
        tk.Label(root, text="1. Proszę wybrać płeć:", font=("Arial", 14)).pack(pady=10)
        self.sex_var = tk.IntVar()

        tk.Radiobutton(root, text="Mężczyzna", variable=self.sex_var, value=1, font=("Arial", 12)).pack()
        tk.Radiobutton(root, text="Kobieta", variable=self.sex_var, value=0, font=("Arial", 12)).pack()

        # Pytanie o wiek
        tk.Label(root, text="2. Proszę wybrać wiek:", font=("Arial", 14)).pack(pady=10)
        self.age_var = tk.IntVar(value=60)

        self.age_slider = tk.Scale(root, from_=60, to=100, orient="horizontal", variable=self.age_var,
                                   font=("Arial", 12))
        self.age_slider.pack()

        # Pytanie o pochodzenie etniczne
        tk.Label(root, text="3. Proszę wybrać najbardziej adekwatne pochodzenie etniczne:", font=("Arial", 14)).pack(
            pady=10)
        self.ethnicity_var = tk.IntVar()
        tk.Radiobutton(root, text="Kaukaskie", variable=self.ethnicity_var, value=0, font=("Arial", 12)).pack()
        tk.Radiobutton(root, text="Afroamerykańskie", variable=self.ethnicity_var, value=1, font=("Arial", 12)).pack()
        tk.Radiobutton(root, text="Azjatyckie", variable=self.ethnicity_var, value=2, font=("Arial", 12)).pack()
        tk.Radiobutton(root, text="Inne", variable=self.ethnicity_var, value=3, font=("Arial", 12)).pack()

        # Pytanie o wykształcenie
        tk.Label(root, text="4. Proszę wybrać posiadane wykształcenie:", font=("Arial", 14)).pack(pady=10)
        self.education_var = tk.IntVar()
        tk.Radiobutton(root, text="Podstawowe", variable=self.education_var, value=0, font=("Arial", 12)).pack()
        tk.Radiobutton(root, text="Średnie", variable=self.education_var, value=1, font=("Arial", 12)).pack()
        tk.Radiobutton(root, text="Wyższe Licencjackie/Inżynierskie", variable=self.education_var, value=2,
                       font=("Arial", 12)).pack()
        tk.Radiobutton(root, text="Wyższe Magisterskie lub powyżej", variable=self.education_var, value=3,
                       font=("Arial", 12)).pack()

        # Przycisk Wstecz i Dalej
        button_frame = tk.Frame(root)
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="Wstecz", font=("Arial", 14), command=self.previous_window).pack(side="left",
                                                                                                      padx=10)
        tk.Button(button_frame, text="Dalej", font=("Arial", 14), command=self.next_question).pack(side="right",
                                                                                                   padx=10)

    def next_question(self):
        """Zapisuje dane i przechodzi do Question2"""
        sex = self.sex_var.get()
        age = self.age_var.get()
        ethnicity = self.ethnicity_var.get()
        education = self.education_var.get()

        self.root.destroy()  # Zamykamy bieżące okno

        # Otwieramy kolejne pytanie
        root = tk.Tk()
        app = Question2(root)
        root.mainloop()

    def previous_window(self):
        """Cofa do ekranu głównego"""
        self.root.destroy()

        from gui.main_window import MainWindow  # Opóźniony import (rozwiązuje circular import)
        root = tk.Tk()
        app = MainWindow(root)
        root.mainloop()
