import tkinter as tk
from gui.question3 import Question3

class Question2:
    def __init__(self, root):
        self.root = root
        self.root.title("Pytanie 2 - Czynniki stylu życia")
        self.root.geometry("600x900")

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
        tk.Label(root, text="3. Jakie jest Twoje tygodniowe spożycie alkoholu (w jednostkach):", font=("Arial", 14)).pack(pady=5)
        self.alcohol_var = tk.IntVar(value=0)
        self.alcohol_slider = tk.Scale(root, from_=0, to=20, orient="horizontal", variable=self.alcohol_var,
                                       font=("Arial", 12))
        self.alcohol_slider.pack()

        # Aktywność fizyczna
        tk.Label(root, text="4. Jaka jest Twoja tygodniowa aktywność fizyczna (w godzinach):", font=("Arial", 14)).pack(pady=5)
        self.physical_var = tk.StringVar()
        self.physical_dropdown = tk.OptionMenu(root, self.physical_var, *[str(i) for i in range(11)])
        self.physical_dropdown.pack()

        # Jakość diety
        tk.Label(root, text="5. Jak oceniasz jakość swojej diety? (0-10):", font=("Arial", 14)).pack(pady=5)
        self.diet_var = tk.StringVar()
        self.diet_dropdown = tk.OptionMenu(root, self.diet_var, *[str(i) for i in range(11)])
        self.diet_dropdown.pack()

        # Jakość snu
        tk.Label(root, text="6. Jak oceniasz swój sen? (4-10):", font=("Arial", 14)).pack(pady=5)
        self.sleep_var = tk.StringVar()
        self.sleep_dropdown = tk.OptionMenu(root, self.sleep_var, *[str(i) for i in range(4, 11)])
        self.sleep_dropdown.pack()

        # Przypis dotyczący jednostek alkoholu
        tk.Label(root, text="*jednostka alkoholu = 10 g czystego alkoholu, czyli ok. 500 ml piwa, 125 ml wina, 40ml wódki",
                 font=("Arial", 10), fg="gray").pack(pady=10)

        # Przycisk Dalej
        tk.Button(root, text="Dalej", font=("Arial", 14), command=self.next_question).pack(pady=20)

    def next_question(self):
        bmi = self.bmi_var.get()
        smoking = self.smoking_var.get()
        alcohol = self.alcohol_var.get()
        physical = self.physical_var.get()
        diet = self.diet_var.get()
        sleep = self.sleep_var.get()
        print(
            f"BMI: {bmi}, Palenie: {smoking}, Alkohol: {alcohol}, Aktywność fizyczna: {physical}, Dieta: {diet}, Sen: {sleep}")  # Można zapisać te wartości lub przekazać dalej
        self.root.destroy()
        # Otwórz kolejne pytanie
        root = tk.Tk()
        app = Question3(root)
        root.mainloop()
