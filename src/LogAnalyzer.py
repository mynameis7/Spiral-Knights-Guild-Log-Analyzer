import os
import re
import cPickle
from datetime import datetime
import datetime as dt
import csv
import json
try:
    import jsonpickle
except Exception:
    jsonpickle = None
    
TAGS = ("Membership", "Treasury", "Storage", "Energy", "Upkeep", "Guild Hall")
class Event(object):
    def __init__(self, (d, c, n, m)):
        #4 sections that the guild log has.
        self.date = d
        self.category = c
        self.true_name = n
        self.true_message = m
        self.new_message = None
        self.new_name = None

    def get_name(self):
        return self.new_name if self.new_name else self.true_name
    name = property(get_name)

    def get_message(self):
        return self.new_message if self.new_message else self.true_message
    message = property(get_message)
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return str(self.date) == str(other.date)
        else:
            return False

    def __str__(self):
        return self.get_csv_string()

    def get_csv_string(self):
        return '"%s","%s","%s","%s"' % (self.date, self.category, self.true_name, self.true_message)
    
def get_datetime_from_stamp(timestamp):
    formatstr = '%m/%d/%y %I:%M:%S %p'
    date = datetime.strptime(timestamp, formatstr)
    return date


class Guildmate(object):
    def __init__(self, nam=None, rnk=None, join_stamp=None):
        self.join_date = None
        if not join_stamp:
            self.join_date = datetime(2011, 1, 1, 0, 0, 0)
        else:
            self.join_date = get_datetime_from_stamp(join_stamp)
        self.name = nam
        self.rank_val = rnk
        self.in_guild = True
        self.deposits = []
        self.energy = []
    def get_rank_name(self):
        rank_dict = {0: "Recruit",
                     1: "Member",
                     2: "Veteran",
                     3: "Officer",
                     4: "Guild Master"}
        return rank_dict[self.rank_val]

    def set_rank_name(self, name):
        rank_dict = {"Recruit": 0,
                     "Member": 1,
                     "Veteran": 2,
                     "Officer": 3,
                     "Guild Master": 4}
        self.rank_val = rank_dict[name]
    rank = property(get_rank_name, set_rank_name)

    def get_total_deposits(self):
        total = 0
        for i in self.deposits:
            total += i[1]
        return total
    total_deposits = property(get_total_deposits)

    def get_days_in_guild(self):
        tdelta = dt.datetime.now() - self.join_date
        seconds = tdelta.total_seconds()
        minutes = seconds/60
        hours = minutes/60
        days = hours/24
        return int(round(days))
    days = property(get_days_in_guild)

    def __str__(self):
        string = "{:<20}|{:<12}|{:<10}| {:<5}"
        return string.format(self.name, self.rank, str(self.join_date), self.days)

    def get_deposits_in_dates(self, start, end):
        d = []
        for i in self.deposits:
            if start <= i[0] < end:
                d.append(i)
        return d

    def get_deposits_this_week(self):
        s, e = get_week()
        total = 0
        for i in self.get_deposits_in_dates(s, e):
            total += i[1]
        return total
    weekly_deposits = property(get_deposits_this_week)

    def add_deposit(self, dep):
        for i in self.deposits:
            if i[0] == dep[0] and i[1] == dep[1]:
                return None
        self.deposits.append(dep)

    def add_energy_transaction(self, trans):
        for i in self.energy:
            if i[0] == trans[0] and i[1] == trans[1]:
                return None
        self.energy.append(trans)


class Guild(object):
    def __init__(self, name="blank", log=None):
        #new structure should be implemented
        #keep a total record of all people in the guild who ever were in the guild
        #then move names around and use the search feature.
        #try a dictionary?
        self.data = dict()
        self.name = name
        self.log = log
        if not self.log:
            self.log = EventList()
        self.refresh()
        self.filepath = self.name.replace(' ', '_')+".guild"
        self.inventory = {}
        self.inventory_buffer = {}

    def reset(self):
        self.data = dict()
        self.name = ""
        self.log = EventList()
        self.filepath = ""

    def search(self, name):
        for mate in self.data:
            if mate.name == name:
                return mate
        return None

    def member_name_change(self, old, new):
        member = self.data[old]
        if new in self.members:
            for m in self.data[new].deposits:
                member.deposits.append(m)
            self.data[new] = member
            self.data.pop(old)
        else:
            member.name = new
            self.data[new] = member
            self.data.pop(old)
        for ev in self.log.data:
            ev.new_name = ev.name.replace(old, new)
            ev.new_message = ev.message.replace(old, new)
        self.refresh()

    def get_weekly_total(self):
        total = 0
        for mem in self.data:
            total += self.data[mem].weekly_deposits
        return total
    weekly_total = property(get_weekly_total)

    def get_guild_total(self):
        total = 0
        for i in self.data.values():
            total += i.total_deposits
        return total
    total_dep = property(get_guild_total)

    def get_total_in_week(self, s, e):
        total = 0
        for mem in self.data:
            dep = self.data[mem].get_deposits_in_dates(s, e)
            for i in dep:
                total += i[1]
        return total

    def get_date_range(self):
        if self.log.data:
            self.log.order()
            end = get_datetime_from_stamp(self.log.data[0].date).date()
            start = get_datetime_from_stamp(self.log.data[-1].date).date()
            curr = start
            date_list = []
            while curr <= end:
                date_list.append(curr)
                curr += dt.timedelta(days=1)
            return date_list
        else:
            return []

    def get_date_range_str(self):
        if self.log.data:
            self.log.order()
            end = get_datetime_from_stamp(self.log.data[0]).date()
            start = get_datetime_from_stamp(self.log.data[-1]).date()
            curr = start
            date_list = []
            while curr <= end:
                date_list.append(str(curr))
                curr += dt.timedelta(days=1)
            return date_list
        else:
            return []
    def filter_by_rank(self, rankstr):
        temp = []
        for mem in self.data.values():
            if mem.rank == rankstr and mem.in_guild:
                temp.append(mem)
        return temp

    def filter_by_name(self, pre):
        newlist = []
        for i in self.data.values():
            if i.name.lower().startswith(pre.lower()):
                newlist.append(self.data[i.name])
        return newlist

    def get_members_in_guild(self):
        temp = {}
        for mem in self.data.values():
            if mem.in_guild:
                temp[mem.name] = mem
        return temp

    def get_members_out_guild(self):
        temp = {}
        for mem in self.data. values():
            if not mem.in_guild:
                temp[mem.name] = mem
        return temp

    def save_to_file(self, filepath):
        if not filepath.endswith('.guild'):
            filepath += '.guild'
            self.filepath = filepath
        with open(filepath, 'wb') as f:
            cPickle.dump(self.data, f, cPickle.HIGHEST_PROTOCOL)
            cPickle.dump(self.log, f, cPickle.HIGHEST_PROTOCOL)
            cPickle.dump(self.name, f, cPickle.HIGHEST_PROTOCOL)
            cPickle.dump(self.filepath, f, cPickle.HIGHEST_PROTOCOL)
        if jsonpickle:
            with open("guild.json","w") as f:
                string = jsonpickle.encode(self, unpicklable=False)
                #string = string.replace("\"", r"\"")
                #string = string.replace("\'",r"\'")
                f.write(string)

            
    def set_state(self, dict_):
        self.reset()
        data = dict_['data']
        for i in data:
            g = Guildmate()
            g.__setstate__(i)
            self.add(g)
        log = dict_['log']
        for i in log['data']:
            vals = (i['date'],i['category'],i['name'],i['message'])
            self.log.add(Event(vals))
        self.log.headers = log['headers']
        self.filepath = dict_['filepath']
        self.name = dict_['name']
        
    def load_from_file(self, filepath):
        with open(filepath, 'rb') as f:
            self.data = cPickle.load(f)
            self.log = cPickle.load(f)
            self.name = cPickle.load(f)
            self.filepath = cPickle.load(f)

    def get(self):
        dict_ = dict(self.__dict__)
        dict_['data'] = [self.data[i].get() for i in self.data]
        dict_['log'] = self.log.get()
        return dict_
    def get_last_log_date(self):
        self.log.order()
        if self.log.data:
            dateStr = self.log.data[0].date
            dateObj = get_datetime_from_stamp(dateStr)
            return dateObj.strftime("%m/%d/%Y")
        return ""
    def save_to_json(self):        
        return None
    
    def save_to_xml(self):
        return None

    def refresh(self):
        self.data = dict()
        self.inventory = dict()
        self.log.order()
        self.update_members(self.log)
        self.update_treasury(self.log)
        self.update_energy(self.log)
        self.update_inventory(self.log)

    def add_log(self, log):
        for i in log.data:
            self.log.add(i)
        self.log.order()

    def update(self):
        self.log.order()
        self.update_members(self.log)
        self.update_treasury(self.log)
        self.update_energy(self.log)
        self.update_inventory(self.log)
    def update_members(self, eventlist):
        def rank_analyzer(mssg):
            rank_re = re.compile("(Promoted|Demoted) (.*) to (Recruit|Member|Veteran|Officer|Guild Master)")
            return rank_re.match(mssg).groups()

        def removed_analyzer(mssg):
            removed_re = re.compile("Removed (.*) from the guild.")
            return removed_re.match(mssg).groups()[0].strip()

        member_re = re.compile("(Accepted|Promoted|Demoted|Removed|Left)")
        events = eventlist.get_filtered("Membership")
        events.reverse()
        #depending on the topic of the message
        #change membership status of a member in
        #a member list of sorts.
        for evt in events:
            mssg = evt.new_message if evt.new_message else evt.message
            name = evt.new_name if evt.new_name else evt.name
            topic = member_re.match(evt.message).group()
            if topic == "Accepted":
                name = evt.name
                if name in self.data.keys():
                    self.data[name].in_guild = True
                    self.data[name].rank = "Recruit"
                    self.data[name].join_date = get_datetime_from_stamp(evt.date)
                else:
                    newmem = Guildmate(name, 0, evt.date)
                    self.add(newmem)
            elif topic == "Promoted":
                shift, name, rank = rank_analyzer(evt.message)
                if name in self.data.keys():
                    self.data[name].rank = rank
                else:
                    #if knight not found, add them with their current rank
                    #join_date will default to opening release of SK.
                    g = Guildmate(name, 0, evt.date)
                    g.rank = rank
                    self.add(g)
            elif topic == "Demoted":
                shift, name, rank = rank_analyzer(evt.message)
                if name in self.data.keys():
                    self.data[name].rank = rank
                else:
                    g = Guildmate(name, 0, evt.date)
                    g.rank = rank
                    self.add(g)
            elif topic == "Removed":
                name = removed_analyzer(evt.message)
                if name in self.data.keys():
                    self.remove(name)
                else:
                    newmem = Guildmate(name, 0, evt.date)
                    self.data[name] = newmem
                    self.data[name].in_guild = False
                    
            elif topic == "Left":
                name = evt.name
                if name in self.data.keys():
                    self.remove(name)
                else:
                    newmem = Guildmate(name, 0, evt.date)
                    self.data[name] = newmem
                    self.data[name].in_guild = False

    def update_treasury(self, eventlist):
        crown_re = re.compile("Added (.*) crowns to the guild treasury.")
        item_re = re.compile("Added (\w*) (.* copies) to the Treasury")
        
        events = eventlist.get_filtered("Treasury")
        events.reverse()
        for evt in events:
            crowns = crown_re.match(evt.message)
            items = item_re.match(evt.message)
            if crowns:
                value = int(crowns.groups()[0].replace(',', ''))
                dt = get_datetime_from_stamp(evt.date)
                #Find the knight in the guild
                if evt.name in self.data.keys():
                    #if knight found in guild add a deposit pair to their deposit list
                    self.data[evt.name].add_deposit((dt, value))
                else:
                    #if knight not found, add them with their current rank
                    #join_date will default to opening release of SK.
                    g = Guildmate(evt.name, 0, evt.date)
                    g.rank = "Recruit"
                    self.add(g)
                    self.data[evt.name].add_deposit((dt, value))

    def update_energy(self, eventlist):
        energy_re = re.compile("(Withdrew|Deposited) (.*) energy (to|from) the energy well \(new total: (.*)\).*")

        events = eventlist.get_filtered("Energy")
        events.reverse()
        for evt in events:
            energy = energy_re.match(evt.message)
            name = evt.name
            date = get_datetime_from_stamp(evt.date)
            if energy:
                trans, amt, dump, total = energy.groups()
                amt = int(amt.replace(',', ''))
                if trans == "Withdrew":
                    amt = -amt
                try:
                    self.data[name].add_energy_transaction((date, amt))
                except KeyError:
                    pass


    def get_energy_withdrawls(self, start, end):
        withdrawls = []
        for mem in self.data:
            member = self.data[mem]
            for trans in member.energy:
                if trans[1] < 0 and start <= trans[0] < end:
                    d = trans[0]
                    if type(d) == datetime:
                        d.date()
                    withdrawls.append((trans[0], mem, trans[1]))
        return withdrawls

    def get_energy_deposits(self, start, end):
        deposits = []
        for mem in self.data:
            member = self.data[mem]
            for trans in member.energy:
                if trans[1] > 0 and start <= trans[0] < end:
                    d = trans[0]
                    if type(d) == datetime:
                        d.date()
                    deposits.append((trans[0], mem, trans[1]))
        return deposits

    def update_inventory(self, eventlist):
        recipe_pattern1 = re.compile("(Added|Removed) (.*) Recipe (to|from) officer storage")
        recipe_pattern2 = re.compile("(Added|Removed) (.*) Recipe (\(\d+ copies\))* (to|from) officer storage")
        add_extract = re.compile("\((\d+) copies\)")
        eventlist = list(eventlist.data)
        eventlist.reverse()
        for event in eventlist:
            if event.category == "Storage":
                add = 1
                change = recipe_pattern1.match(event.message)
                if not change:
                    change = recipe_pattern2.match(event.message)
                    if change:
                        add = int(add_extract.match(change.group(3)).group(1))
                        change = change.groups()
                        if change[0] == "Added":
                            if change[1] in self.inventory:
                                self.inventory[change[1]] += add
                            else:
                                self.inventory[change[1]] = 1
                        elif change[0] == "Removed":
                            if change[1] in self.inventory:
                                self.inventory[change[1]] -= add
                            else:
                                self.inventory[change[1]] = 0
                elif change:
                    change = change.groups()
                    if change[0] == "Added":
                        if change[1] in self.inventory:
                            self.inventory[change[1]] += add
                        else:
                            self.inventory[change[1]] = 1
                    elif change[0] == "Removed":
                        if change[1] in self.inventory:
                            self.inventory[change[1]] -= add
                            if self.inventory[change[1]] < 0: self.inventory[change[1]] = 0
                        else:
                            self.inventory[change[1]] = 0
    def print_inventory(self):
        inventory = self.get_organized_inventory()
        for key in inventory:
            print "%s*:"%key
            for i in inventory[key]:
                print "\t%s - %s"%(i, self.inventory[i])
                
    def find_item_star(self, item):
        for r in recipesList:
            if r["name"] == item:
                return r["Star"]
        print "Item not found: %s"%item
        cat = raw_input("Item Category:").strip()
        star = input("Item Star:")
        recipesList.append({"name":item, "Category":cat, "Star":star})
        return star
    def export_inventory(self):
        output = ""
        inventory = self.get_organized_inventory()
        for key in inventory:
            output += "%s*:\n"%key
            for i in inventory[key]:
                output += "\t%s - %s\n"%(i, self.inventory[i])
                
        return output
    def export_stylized_inventory(self):
        h = '[color=#ffcc00][b]'
        h_close = '[/b][/color]'
        li = '[*]'
        _list = '[list]'
        _list_close = '[/list]'
        output = ""
        inventory = self.get_organized_inventory()
        for key in inventory:
            output += h + "%s*"%key + h_close + '\n'
            output += _list + '\n'
            for i in inventory[key]:
                output += li + "%s - %s\n"%(i, self.inventory[i])
            output += _list_close +'\n'
        return output
    def get_organized_inventory(self):
        inventory = {1:[],
                     2:[],
                     3:[],
                     4:[],
                     5:[]}
        for item in self.inventory:
            if self.inventory[item] > 0:
                star_level = self.find_item_star(item)
                inventory[star_level].append(item)
        return inventory
    recipes=property(get_organized_inventory)
    def get_last_log_date(self):
        self.log.order()
        if self.log.data:
            dateStr = self.log.data[0].date
            dateObj = get_datetime_from_stamp(dateStr)
            return dateObj.strftime("%m/%d/%Y")
        return ""

    def get_member_logs(self, name):
        logs = []
        for ev in self.log.data:
            if ev.name.lower() == name.lower():
                logs.append(ev)
        return logs
    
    def add(self, member):
        self.data[member.name] = member

    def remove(self, name):
        self.data[name].in_guild = False

    def get_member_list(self):
        return self.get_members_in_guild().keys() + self.get_members_out_guild().keys()
    members = property(get_member_list)


class EventList(object):
    #list of all the events retrieved from a guild log
    def __init__(self):
        self.data = []
        self.headers = ('Timestamp', 'Category', 'Name', 'Message')

    def add(self, evt):
        if not self.event_in_list(evt):
            self.data.append(evt)

    def get_filtered(self, string):
        return filter(lambda x: x.category == string, self.data)

    def event_in_list(self, ev):
        for event in self.data:
            if ev == event:
                return True
        return False

    def export_list(self, filepath):
        with open(filepath, 'w') as f:
            f.write('"%s","%s","%s","%s"' % self.headers + '\n')
            for event in self.data:
                f.write(event.get_csv_string() + "\n")

    def get(self):
        newdict = {'data': [i.__dict__ for i in self.data],
                   'headers': self.headers}
        return newdict

    def order(self):
        
        self.data.sort(key=lambda ev: get_datetime_from_stamp(ev.date), reverse=True)


def extract_data(data):
    #You send it the filepath to the Spiral Knights Log csv
    with open(data) as f:
        c = csv.reader(f)
        d = [i for i in c]

    datalist2 = EventList()
    for i in d[1:]:
        datalist2.add(Event(i))
    
    return datalist2


def export_wiki(g,filepath=None):
    output = "{{SKNewRow}}\n"
    output += "{{SKCell|'''Guild Masters'''\n"
    GMs = g.filter_by_rank("Guild Master")
    for i in GMs:
        if i.in_guild:
            output += "*%s\n" % i.name
    output += "|||2}}\n\n"
    
    output += "{{SKNewRow}}\n"
    output += "{{SKCell|'''Officers'''\n"
    Officers = g.filter_by_rank("Officer")
    for i in Officers:
        if i.in_guild:
            output += "*%s\n" % i.name
    output += "|||2}}\n\n"

    output += "{{SKNewRow}}\n"
    output += "{{SKCell|{{showhide|'''Veterans'''|width=20em|content=\n"
    Veterans = g.filter_by_rank("Veteran")
    for i in Veterans:
        if i.in_guild:
            output += "*%s\n" % i.name
    output += "}}|||2}}\n\n"

    output += "{{SKNewRow}}\n"
    output += "{{SKCell|{{showhide|'''Members'''|width=20em|content=\n"
    Members = g.filter_by_rank("Member")
    for i in Members:
        if i.in_guild:
            output += "*%s\n" % i.name
    output += "}}|||2}}\n\n"

    output += "{{SKNewRow}}\n"
    output += "{{SKCell|{{showhide|'''Recruits'''|width=20em|content=\n"
    Recruits = g.filter_by_rank("Recruit")
    for i in Recruits:
        if i.in_guild:
            output += "*%s\n" % i.name
    output += "}}|||2}}\n\n"

    output += "{{SKNewRow}}\n"
    output += "{{SKCell|'''Population'''|center|||50%}}\n"
    output += "{{SKCell|%s|center}}\n" % len(GMs+Officers+Veterans+Members+Recruits)
    output += "}}"
    if filepath:
        with open(filepath, 'w') as f:
            f.write(output)
    else:
        return output


def add_log_to_guild(guild, *filepaths):
    for i in filepaths:
        l = extract_data(i)
        guild.add_log(l)
    guild.refresh()


def get_week(day=dt.datetime.now()):
    tdelta = dt.timedelta(7)
    mon = day-dt.timedelta(day.weekday())
    sun = mon + tdelta
    return mon, sun


def save(g):
    g.save_to_file(g.filepath)


def interface(guild):
    def member_menu(g, m):
        mem_menu = "%s:\n"%m.name
        mem_menu += "1: deposits\n"
        mem_menu += "2: quit\n"
        mem_choice = ''
        while mem_choice != '2':
            mem_choice = raw_input(mem_menu)
            if mem_choice == '1':
                for date,value in m.deposits:
                    print date,value
    menu = "%s:\n"%guild.name
    menu += "1: List Members\n"
    menu += "2: Find Member by Name\n"
    menu += "3: Guild Data\n"
    menu += "4: Save\n"
    menu += "5: Load\n"
    menu += "6: Quit\n"
    choice = ''
    while choice != '6':
        choice = raw_input(menu)
        if choice == '1':
            for name in guild.members:
                print name
        if choice == '2':
            name = raw_input("Name begins with?")
            if name.lower() != 'quit':
                names = guild.filter_by_name(name)
                for i in xrange(len(names)):
                    print "%s: %s"%(i+1, names[i])
                print "%s: Back"%(len(names)+1)
                name_choice = raw_input("Select Member by Number:")
                try:
                    mem = names[int(name_choice)-1]
                    member_menu(guild,mem)
                except IndexError:
                    pass
        if choice == '4':
            guild.save_to_file(guild.filepath)
            print "SAVED!"
        if choice == '5':
            path = raw_input("path to guild file:")
            guild.load_from_file(path)
            return guild
        if choice == '6':
            break
    return
if jsonpickle:
    class DatetimeHandler(jsonpickle.handlers.BaseHandler):
        def flatten(self, obj, data):
            return obj.strftime('%Y-%m-%d %H:%M:%S.%f')
    jsonpickle.handlers.registry.register(datetime, DatetimeHandler)

if __name__ == "__main__":
    
    def resource_path(relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    recipesList = None
    itemPath = resource_path("Items.json")
    with open(itemPath) as f:
        recipesList = json.load(f)["Recipes"]
    if recipesList == None:
        raise Exception("File not Found: %s"%itemPath)


    import sys
    guild = Guild()
    print sys.argv
    if len(sys.argv) > 4 or len(sys.argv) == 1:
        print "Incorrect usage, type 'LogAnalyzer help' to see correct usage"
        sys.exit(-1)
    if sys.argv[1].lower() == "help":
        print "Usage Notes:"
        print "LogAnalyzer generate <log_folder>"
        print "LogAnalyzer merge <log_folder>"
        print "LogAnalyzer migrate <guild_name> <log_folder>"
        sys.exit()
    if sys.argv[1].lower() == "migrate":
        if len(sys.argv) != 4:
            print "Incorrect usage: LogAnalyzer migrate <guild_name> <log_folder>"
            sys.exit(-1)
        name = sys.argv[2]
        logpath1 = os.path.join(os.getcwd(), sys.argv[3])
        print "Migrating from: %s"%logpath1
        for path, dirnames, filenames in os.walk(logpath1):
            for i in filenames:
                add_log_to_guild(guild, os.path.join(path, i))
        print "Name Change Pair (Seperated by a space):<OLD_NAME> <NEW_NAME>"
        try:
            while True:
                pair = raw_input("Pair: ")
                pair = pair.strip()
                pair.split(" ")
                try:
                    guild.member_name_change(pair[0], pair[1])
                except Exception as e:
                    print "Name Change Error"
                    print e
                more = raw_input("More name changes? (y/n): ")
                more = more.strip()
                if more.lower() not in "yn":
                    more = raw_input("More name changes? (y/n): ")
                    more = more.strip()
                if more == "n":
                    break
##            guild.member_name_change('Trolololcreeper', 'Medium-Moose')
##            guild.member_name_change("Rhons","Akane-Akaza")
##            guild.member_name_change("Akane-Akaza","Rhons")
##            guild.member_name_change("Tannertt","Apocrisiary")
##            guild.member_name_change("Apocrisiary","Tannertt")
##            guild.member_name_change("Hazm", "Gun-Shots")
##            guild.member_name_change("Unominame", "Aeskau")
##            guild.member_name_change("Takeshipl", "Takeshi-Pl")
##            guild.member_name_change("Purple-Underdog", "Pink-Overkitty")
##            guild.save_to_file(guild.filepath)
        except Exception as e:
            print e
        guild.save_to_file(guild.filepath)
    if sys.argv[1].lower() == "generate":
        if len(sys.argv) != 3:
            print "Incorrect usage: LogAnalyzer generate <log_folder>"
            sys.exit(-1)
        logpath1 = os.path.join(os.getcwd(), sys.argv[2])
        print "Generating from: %s"%logpath1
        for path, dirnames, filenames in os.walk(logpath1):
            for i in filenames:
                add_log_to_guild(guild, os.path.join(path, i))
        name = raw_input("Guild Name:").strip()
        guild.name = name
        guild.save_to_file(guild.filepath)
    if sys.argv[1].lower() == "merge":
        if len(sys.argv) != 3:
            print "Incorrect usage: LogAnalyzer merge <log_folder>"
            sys.exit(-1)
        logpath1 = os.path.join(os.getcwd(), sys.argv[2])
        print "Merging from: %s"%logpath1
        for path, dirnames, filenames in os.walk(logpath1):
            for i in filenames:
                add_log_to_guild(guild, os.path.join(path, i))
        name = raw_input("Fileame:").strip()
        guild.log.export_list(name)
    if sys.argv[1].lower() == "interface":
        val = True
        while val:
            val = interface(guild)
            if val:
                guild = val
