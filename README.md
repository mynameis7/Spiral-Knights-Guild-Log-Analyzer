# Spiral-Knights-Guild-Log-Analyzer
Analyzer program for Spiral Knights guild logs
.spec files are used in compiling windows executables with pyinstaller (other platforms in the future)
Uses PyQt4 for the gui.

This is one of my older projects.  I will be going through and re-formatting and re-documenting the code in the near future since it's at a stable point.

The cli program has several commands for working with a folder that contains logs.

LogAnalyzer generate \<log_folder\> <br>
LogAnalyzer migrate \<guild_name\> \<log_folder\><br>
LogAnalyzer merge \<log_folder\> <br>

\<log_folder\> is the path to the folder containing the logs. <br>
\<guild_name\> is the name of the guild with a file that currently exists.<br>

generate: generates a guild file containing all the logs. "*.guild" file to be used with the gui program
migrate: generates a guild file containing all the logs, prompts for name change revisions after the generation.  Primarily for moving to a new version of the data.
merge: merges all the logs in the folder into 1 file. Prompts for a save name after it has completed the merging.
