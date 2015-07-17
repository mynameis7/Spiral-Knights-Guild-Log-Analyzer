# -*- mode: python -*-
data_files = [('Items.json', 'C:\\Users\\Andrew\\Dropbox\\Spiral Knights Software Dev\\League of Gunners App\\Items.json', 'DATA')]
a = Analysis(['qtLog_Analyzer_GUI_V5.py'],
             pathex=['C:\\Users\\Andrew\\Dropbox\\Spiral Knights Software Dev\\League of Gunners App'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas + data_files,
          name='qtLog_Analyzer_GUI_V5.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False )
