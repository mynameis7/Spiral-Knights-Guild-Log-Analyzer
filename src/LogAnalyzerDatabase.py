import sqlite3

def find_member(db, name):
    cur = db.execute('SELECT * FROM Members WHERE Name=?', (name,))
    vals = cur.fetchone()
    return vals
    
def find_member_id(db, name):
    cur = db.execute('SELECT ID FROM Members WHERE Name=?', (name,))
    return cur.fetchone()    
def get_member_crown_deposits(db, name):
    member = find_member(db, name)["id"]
    cur = db.execute('SELECT * FROM Crown_Deposits WHERE ID=?', (member,))
    return cur.fetchall()
def get_member_energy_deposits(db, name):
    member = find_member(db, name)["id"]
    cur = db.execute('SELECT * FROM Energy_Deposits WHERE ID=?', (member,))
    return cur.fetchall()
def add_member_crown_deposit(db, name, deposit):
    member = find_member(db, name)["id"]
    cur = db.execute('INSERT INTO Crown_Deposits VALUES(?, ?, ?)', )
def add_member_energy_deposit(db, name, deposit):
    member = find_member(db, name)["id"]
    cur = db.execute('INSERT INTO Crown_Deposits VALUES(?, ?, ?)', )
def add_member(db, name, join_date):
    mem_pack = (name, join_date, True, 0)
    cur = db.execute('INSERT INTO Members (Name, JoinDate, InGuild, RankVal) VALUES(?,?,?,?)',mem_pack)
def remove_member(db, name):
    member = find_member(db, name)["id"]
    cur = db.execute('UPDATE Members SET InGuild=0 WHERE ID=?', (member,))
def update_member_name(db, old_name, new_name):
    member = find_member(db, old_name)["id"]
    cur = db.execute('UPDATE Members SET Name=? WHERE ID=?', (new_name,member,))


con = sqlite3.connect("guild.sqlite3")
con.row_factory = sqlite3.Row
for dep in get_member_crown_deposits(con, "Mynameis-Seven"):
    print dep["DepositDate"], dep["Amount"]
