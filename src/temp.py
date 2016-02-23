from LogAnalyzer import *

g = Guild()
g.load_from_json("League of Gunners.json-guild")
renames = [
    ["Trolololcreeper","Medium-Moose",0],
    ["Rhons","Akane-Akaza",1],
    ["Akane-Akaza","Rhons",2],
    ["Tannertt","Apocrisiary",3],
    ["Apocrisiary","Tannertt",4],
    ["Hazm","Gun-Shots",5],
    ["Unominame","Aeskau",6],
    ["Takeshipl","Takeshi-Pl",7],
    ["Purple-Underdog","Pink-Overkitty",8]

    ]#g.renames
g.renames = renames#[0]
print renames
g.save_to_json(g.filepath)
