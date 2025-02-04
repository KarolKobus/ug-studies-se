# Zbiór danych pochodzi z: https://www.kaggle.com/datasets/rabieelkharoua/alzheimers-disease-dataset/data
# Autor: Rabie El Kharoua
# Digital Object Identifier: 10.34740/kaggle/dsv/8668279
# License: Attribution 4.0 International (CC BY 4.0)
#---------------------------------------------------------------------#

#----------------------Importowanie bibliotek-------------------------#
import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler  # Skalowanie cech (standaryzacja)
from sklearn.model_selection import train_test_split  # Podział zbioru danych na zbiór treningowy i testowy

#------------------Wczytanie zbioru danych-----------------------------#
# Ważne: plik .csv musi znajdować się w tym samym katalogu co plik .py

# Pobranie katalogu, w którym znajduje się ten skrypt
script_dir = os.path.dirname(os.path.abspath(__file__))

# Ścieżka do pliku CSV w tym samym folderze co skrypt
file_path = os.path.join(script_dir, "alzheimers_disease_data.csv")

# Sprawdzenie, czy plik istnieje
if not os.path.exists(file_path):
    print(f"Plik nie istnieje: {file_path}")
else:
    print(f"Odczyt danych z: {file_path}")

#---------------Wczytanie pliku CSV----------------------------#
dataset = pd.read_csv(file_path)

#---------------Pozbywamy się braków danych---------------------#

# Usuwanie kolumn z więcej niż 50% brakujących wartości
threshold = 0.5  # 50% brakujących danych

# Obliczenie procentu brakujących wartości w każdej kolumnie
missing_percentage = dataset.isna().sum() / len(dataset)

# Lista kolumn do usunięcia
columns_to_drop = missing_percentage[missing_percentage > threshold].index

# Usunięcie tych kolumn oraz 'PatientID' i 'DoctorInCharge'
a = dataset.drop(columns=columns_to_drop)
b = a.drop(columns=['PatientID','DoctorInCharge'])
dataset = b

#------------------Dzielimy zbiór na zmienne zależne i niezależne-----------------#

# Musimy to formatować do obiektu typu numpy.array
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

#------------------Standaryzacja zmiennych----------------------------------------#
# Tak aby różnorodne zmienne dało się ze sobą porównywać
sc = StandardScaler()
X = sc.fit_transform(X)

#------------------Dzielimy zbiór na testowy i treningowy-------------------------#
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 123)
