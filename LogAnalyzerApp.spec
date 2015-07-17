# -*- mode: python -*-
data_files = [('Items.json', '.\\src\\Items.json', 'DATA')]

a = Analysis(['src/LogAnalyzerApp.py'],
             pathex=['.\\'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas + data_files,
          name='LogAnalyzerApp.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False )
