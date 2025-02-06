import tkinter as tk
from tkinter import messagebox
from gui.question3 import Question3


def previous_window(root, responses):
    """Cofa do poprzedniego pytania"""
    root.destroy()
    from gui.question1 import Question1  # Opóźniony import (rozwiązuje circular import)
    new_root = tk.Tk()
    app = Question1(new_root, responses)
    new_root.mainloop()


class Question2:
    def __init__(self, root, responses):
        self.root = root
        self.root.title("Alzheimer Predictor")
        self.root.geometry("600x700")
        self.responses = responses  # Przechowywanie odpowiedzi z poprzedniego pytania

        # Tytuł sekcji
        tk.Label(root, text="Styl życia", font=("Arial", 16, "bold")).pack(pady=10)

        # BMI
        tk.Label(root, text="1. Proszę wybrać BMI:", font=("Arial", 14)).pack(pady=5)
        self.bmi_var = tk.IntVar(value=15)
        self.bmi_slider = tk.Scale(root, from_=15, to=40, orient="horizontal", variable=self.bmi_var,
                                   font=("Arial", 12))
        self.bmi_slider.pack()

        # Smoking
        tk.Label(root, text="2. Czy palisz papierosy?", font=("Arial", 14)).pack(pady=5)
        self.smoking_var = tk.IntVar()
        tk.Radiobutton(root, text="Nie", variable=self.smoking_var, value=0, font=("Arial", 12)).pack()
        tk.Radiobutton(root, text="Tak", variable=self.smoking_var, value=1, font=("Arial", 12)).pack()

        # Alkohol
        tk.Label(root, text="3. Jakie jest Twoje tygodniowe spożycie alkoholu (w jednostkach):",
                 font=("Arial", 14)).pack(pady=5)
        self.alcohol_var = tk.IntVar(value=0)
        self.alcohol_slider = tk.Scale(root, from_=0, to=20, orient="horizontal", variable=self.alcohol_var,
                                       font=("Arial", 12))
        self.alcohol_slider.pack()

        # Aktywność fizyczna
        tk.Label(root, text="4. Jaka jest Twoja tygodniowa aktywność fizyczna (w godzinach):", font=("Arial", 14)).pack(
            pady=5)
        self.physical_var = tk.StringVar(value="")
        self.physical_dropdown = tk.OptionMenu(root, self.physical_var, *[str(i) for i in range(11)])
        self.physical_dropdown.pack()

        # Jakość diety
        tk.Label(root, text="5. Jak oceniasz jakość swojej diety? (0-10):", font=("Arial", 14)).pack(pady=5)
        self.diet_var = tk.StringVar(value="")
        self.diet_dropdown = tk.OptionMenu(root, self.diet_var, *[str(i) for i in range(11)])
        self.diet_dropdown.pack()

        # Jakość snu
        tk.Label(root, text="6. Jak oceniasz swój sen? (4-10):", font=("Arial", 14)).pack(pady=5)
        self.sleep_var = tk.StringVar(value="")
        self.sleep_dropdown = tk.OptionMenu(root, self.sleep_var, *[str(i) for i in range(4, 11)])
        self.sleep_dropdown.pack()

        # Przypis dotyczący jednostek alkoholu
        tk.Label(root,
                 text="*jednostka alkoholu = 10 g czystego alkoholu, czyli ok. 500 ml piwa, 125 ml wina, 40ml wódki",
                 font=("Arial", 10), fg="gray").pack(pady=10)

        # Przycisk Wstecz i Dalej
        button_frame = tk.Frame(root)
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="Wstecz", font=("Arial", 14),
                  command=lambda: previous_window(self.root, self.responses)).pack(side="left", padx=10)
        tk.Button(button_frame, text="Dalej", font=("Arial", 14), command=self.next_question).pack(side="right",
                                                                                                   padx=10)

    def next_question(self):
        if not self.physical_var.get() or not self.diet_var.get() or not self.sleep_var.get():
            messagebox.showwarning("Błąd",
                                   "Proszę wybrać wartość dla aktywności fizycznej, jakości diety i jakości snu.")
            return

        self.responses["BMI"] = self.bmi_var.get()
        self.responses["Smoking"] = self.smoking_var.get()
        self.responses["AlcoholConsumption"] = self.alcohol_var.get()
        self.responses["PhysicalActivity"] = self.physical_var.get()
        self.responses["DietQuality"] = self.diet_var.get()
        self.responses["SleepQuality"] = self.sleep_var.get()

        self.root.destroy()
        # Otwórz kolejne pytanie
        root = tk.Tk()
        app = Question3(root, self.responses)
        root.mainloop()
