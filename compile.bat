cd src
gui-compile.py
cd ..\
pyinstaller -F LogAnalyzerApp.spec > app_installation.log.txt
pyinstaller -F LogAnalyzer.spec > cli_installation.log.txt