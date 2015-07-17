from PyQt4 import uic

f = open("qtLog_GUI.py", 'w')
uic.compileUi('Log_Analyzer.ui', f)
f.close()
print "Compiled"
