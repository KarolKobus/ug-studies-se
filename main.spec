# -*- mode: python ; coding: utf-8 -*-
<<<<<<< HEAD
=======
from PyInstaller.utils.hooks import collect_submodules
from PyInstaller.utils.hooks import collect_all

datas = [('C:\\Users\\wrons\\ug-studies-se\\assets\\logo.png', 'assets/')]
binaries = []
hiddenimports = ['joblib', 'scipy', 'scipy.special', 'xgboost', 'numpy', 'numpy._core', 'numpy._core.multiarray', 'numpy._core._methods', 'numpy.linalg', 'numpy.fft', 'numpy.random', 'tkinter', 'sklearn', 'importlib.resources']
hiddenimports += collect_submodules('numpy')
tmp_ret = collect_all('xgboost')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
>>>>>>> gui


a = Analysis(
    ['main.py'],
    pathex=[],
<<<<<<< HEAD
    binaries=[],
    datas=[('assets/logo.png', 'assets'), ('model/best_model.pkl', 'model'), ('model/scalar.pkl', 'model')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
=======
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['xgboost.testing', 'hypothesis'],
>>>>>>> gui
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
<<<<<<< HEAD
    icon=['assets\\icon.ico'],
=======
    icon=['C:\\Users\\wrons\\ug-studies-se\\assets\\icon.ico'],
>>>>>>> gui
)
