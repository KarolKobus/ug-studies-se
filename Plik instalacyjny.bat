@echo on
setlocal

:: Ustalanie ścieżki bazowej (ug-studies-se)
echo --- Ustalanie ścieżki bazowej (ug-studies-se) ---
set "SCRIPT_DIR=%~dp0"
cd /d "%SCRIPT_DIR%"
for %%i in (.) do set "BASE_DIR=%%~fi"

echo Sprawdzanie czy folder %BASE_DIR% istnieje...
if not exist "%BASE_DIR%" (
    echo Błąd: Folder %BASE_DIR% nie istnieje!
    pause
    exit /b
)

echo Bieżący katalog roboczy: %BASE_DIR%

:: Sprawdzenie i ustawienie Pythona
echo --- Sprawdzanie wersji Pythona ---
where python
set "PYTHON_EXEC=python"
if exist "C:\Program Files\Python311\python.exe" set "PYTHON_EXEC=C:\Program Files\Python311\python.exe"

echo Używany Python: %PYTHON_EXEC%
%PYTHON_EXEC% --version 2>nul
if %errorlevel% neq 0 (
    echo Błąd: Python nie działa poprawnie lub nie jest zainstalowany! Sprawdź instalację.
    pause
    exit /b
)

echo --- Ustawienie zmiennej PATH ---
set "PATH=%PATH%;C:\Program Files\Python311;C:\Program Files\Python311\Scripts"

echo --- Usuwanie starego środowiska wirtualnego (jeśli istnieje) ---
if exist venv (
    echo Usuwanie istniejącego środowiska wirtualnego...
    rmdir /s /q venv
)

echo --- Tworzenie nowego wirtualnego środowiska ---
%PYTHON_EXEC% -m venv venv 2>venv_error.log
if %errorlevel% neq 0 (
    echo Błąd: Nie można utworzyć środowiska wirtualnego! Sprawdź plik venv_error.log
    echo Próba instalacji virtualenv...
    %PYTHON_EXEC% -m pip install virtualenv
    %PYTHON_EXEC% -m virtualenv venv 2>venv_error.log
    if %errorlevel% neq 0 (
        echo Błąd: Nie można utworzyć środowiska wirtualnego nawet z virtualenv! Sprawdź instalację Pythona.
        pause
        exit /b
    )
)

echo --- Aktywacja środowiska wirtualnego ---
call venv\Scripts\activate 2>venv_activate.log
if %errorlevel% neq 0 (
    echo Błąd: Nie można aktywować środowiska wirtualnego! Sprawdź plik venv_activate.log
    pause
    exit /b
)
echo Wirtualne środowisko aktywowane.

echo --- Instalacja wymaganych bibliotek, tkinter i PyInstaller ---
if exist "%BASE_DIR%\requirements.tzt" (
    pip install -r "%BASE_DIR%\requirements.tzt"
    pip install tk
    pip install pyinstaller
    if %errorlevel% neq 0 (
        echo Błąd: Nie udało się zainstalować wymaganych bibliotek!
        pause
        exit /b
    )
    echo Biblioteki zostały pomyślnie zainstalowane.
) else (
    echo Błąd: Plik requirements.tzt nie został znaleziony w %BASE_DIR%!
    pause
    exit /b
)

echo --- Sprawdzanie pliku main.py ---
set "MAIN_SCRIPT=%BASE_DIR%\main.py"
if not exist "%MAIN_SCRIPT%" (
    echo Błąd: Plik main.py nie istnieje w %BASE_DIR%!
    pause
    exit /b
)

echo --- Sprawdzanie, czy tkinter działa poprawnie ---
%PYTHON_EXEC% -c "import tkinter; print('Tkinter działa!')" 2>tkinter_check.log
if %errorlevel% neq 0 (
    echo Błąd: Tkinter nie działa w tym środowisku! Sprawdź plik tkinter_check.log
    pause
    exit /b
)

echo --- Generowanie pliku .exe ---
venv\Scripts\pyinstaller --onefile --windowed --hidden-import=tkinter --hidden-import=_tkinter --collect-submodules=tkinter --hidden-import=joblib --hidden-import=scipy --hidden-import=scipy.special --hidden-import=xgboost --hidden-import=numpy --hidden-import=numpy._core --hidden-import=numpy._core.multiarray --hidden-import=numpy._core._methods --hidden-import=numpy.linalg --hidden-import=numpy.fft --hidden-import=numpy.random --hidden-import=tkinter --hidden-import=sklearn --hidden-import=importlib.resources --collect-all xgboost --collect-submodules numpy --exclude-module xgboost.testing --exclude-module hypothesis --icon="%BASE_DIR%\assets\icon.ico" --add-data "%BASE_DIR%\assets;assets/" --add-data "%BASE_DIR%\gui;gui/" --add-data "%BASE_DIR%\model;model/" "%MAIN_SCRIPT%"

if %errorlevel% neq 0 (
    echo Błąd: Nie udało się wygenerować pliku .exe!
    pause
    exit /b
)
echo Plik .exe został wygenerowany pomyślnie.

echo --- Przeniesienie pliku exe do głównego katalogu ---
move dist\main.exe "%BASE_DIR%"
if %errorlevel% neq 0 (
    echo Błąd: Nie udało się przenieść pliku .exe!
    pause
    exit /b
)
echo Plik .exe przeniesiony do: %BASE_DIR%

echo --- Uruchomienie pliku .exe ---
if exist "%BASE_DIR%\main.exe" (
    call "%BASE_DIR%\main.exe"
    echo Plik .exe został uruchomiony.
) else (
    echo Błąd: Plik .exe nie został wygenerowany poprawnie!
    pause
    exit /b
)

pause
endlocal
