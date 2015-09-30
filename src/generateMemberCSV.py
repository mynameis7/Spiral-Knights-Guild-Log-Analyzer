import LogAnalyzer as LA
import sqlite3

if __name__ == "__main__":
    g = LA.Guild()
    g.load_from_file("./League_of_Gunners.guild")
    con = sqlite3.connect("./League_of_Gunners.sqlite3")
    
    
    
