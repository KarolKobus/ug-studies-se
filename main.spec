# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_submodules
from PyInstaller.utils.hooks import collect_all

datas = [('C:\\Users\\wrons\\ug-studies-se\\assets\\logo.png', 'assets/')]
binaries = []
hiddenimports = ['joblib', 'scipy', 'scipy.special', 'xgboost', 'numpy', 'numpy._core', 'numpy._core.multiarray', 'numpy._core._methods', 'numpy.linalg', 'numpy.fft', 'numpy.random', 'tkinter', 'sklearn', 'importlib.resources']
hiddenimports += collect_submodules('numpy')
tmp_ret = collect_all('xgboost')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['xgboost.testing', 'hypothesis'],
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
    icon=['C:\\Users\\wrons\\ug-studies-se\\assets\\icon.ico'],
)
