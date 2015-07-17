cd src
./gui-compile.py
cd ..
pyinstaller -F LogAnalyzerApp.spec
pyinstaller -F LogAnalyzer.spec
