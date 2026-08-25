# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all

datas = [
    ('icon.ico', '.'),
    ('icon.png', '.'),
    ('ubuy.gif', '.'),
    ('service_accounts_data.json', '.'),
    ('service-account.json', '.'),
    ('credentials_gschigh.json', '.'),
    ('credentials_gsclow.json', '.')
]
binaries = []
hiddenimports = ['pkg_resources.py2_warn', 'pkg_resources.markers', 'win10toast', 'PIL', 'openpyxl', 'googleapiclient', 'pkg_resources', 'setuptools']

# Auto-collect selenium and webdriver_manager hooks to prevent runtime errors
tmp_ret = collect_all('selenium')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('webdriver_manager')
tmp_ret = collect_all('win10toast')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]

datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]

a = Analysis(
    ['main5.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
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
    name='UBUY_SEO_Automation_V9.1',
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
    icon=['icon.ico'],
)
