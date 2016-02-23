import sqlite3
import sys
import LogAnalyzer as LA
from LogAnalyzer import *
from os.path import exists, join, abspath
from os import pathsep
from os import remove

def executeSQLFile(filepath, cursor):
    with open(filepath) as f:
        qry = f.read()
        cursor.executescript(qry)

def search_file(filename, search_path):
   """Given a search path, find file
   """
   file_found = 0
   paths = search_path.split(pathsep)
   for path in paths:
      if exists(join(path, filename)):
          file_found = 1
          break
   if file_found:
      return abspath(join(path, filename))
   else:
      return None

if __name__ == "__main__":
    sys.argv.append("League of Gunners.json-guild")
    print sys.argv
    con = sqlite3.Connection(":memory:")
    cur = con.cursor()
    executeSQLFile("./sql/createTables.sql", cur)

    g = LA.Guild()
    g.load_from_json(sys.argv[1])
    for member in g.data.values():
        mem_pack = (member.name, member.join_date, member.in_guild, member.rank_val)
        cur.execute("INSERT INTO Members (Name,JoinDate,InGuild,RankVal) VALUES(?,?,?,?)", mem_pack)
        _id = cur.execute("SELECT ID FROM Members WHERE Name=?",(member.name,)).fetchone()[0]
        for deposit in member.deposits:
            dep_pack = (deposit[0], _id, deposit[1])
            cur.execute("INSERT INTO Crown_Deposits VALUES(?,?,?)", dep_pack)
        for deposit in member.energy:
            dep_pack = (deposit[0], _id, deposit[1])
            cur.execute("INSERT INTO Energy_Deposits VALUES(?,?,?)", dep_pack)
    for ev in g.log.data:
        ev_pack = (ev.date, ev.category, ev.true_name, ev.true_message, ev.new_name, ev.new_message)
        cur.execute("INSERT INTO Logs VALUES(?,?,?,?,?,?)", ev_pack)
    for rename in g.renames:
        print rename
        cur.execute("INSERT INTO Renames VALUES(?, ?, ?)", rename)
    con.commit()
    with open("dump.sql", "w") as f:
        for line in con.iterdump():
            f.write("%s\n"%line)
    con.close()
    con = sqlite3.Connection("guild.sqlite3")
    cur = con.cursor();
    executeSQLFile("./dump.sql", cur)
    con.commit()
    con.close()
    remove("./dump.sql")
