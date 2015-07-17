import sys, os
from PyQt4.QtGui import QApplication, QFileDialog, QMainWindow, QInputDialog, QDialog, QTextEdit, QSizePolicy, QTableWidgetItem
from PyQt4.QtCore import QString, QTime, QDateTime, QDate
import LogAnalyzer as SK
from LogAnalyzer import * #for working with cPickle
import qtLog_GUI as gui
from PyQt4 import uic
import re

def get_datetime_from_stamp(timestamp):
    formatstr = '%m/%d/%y %I:%M:%S %p'
    date = datetime.strptime(timestamp, formatstr)
    return date

class Compiled_UI(QMainWindow, gui.Ui_MainWindow):
    def __init__(self, parent=None):
        def autoload():
            count = 0
            string = ""
            for i in os.listdir(os.getcwd()):
                if i.endswith(".guild"):
                    string = i
                    count += 1
            if count == 1:
                return string
            else:
                return False
        QMainWindow.__init__(self, parent)
      
        self.setupUi(self)

        self.guild = SK.Guild()
        self.curr_mem_count = 0
        self.timeStart = QTime(0, 0)
        self.timeEnd = QTime(23, 59)

        self.nameEntry.textChanged.connect(self.update_list)
        self.rankBox.currentIndexChanged.connect(self.update_list)
        self.statusBox.currentIndexChanged.connect(self.update_list)
        self.statusBox.currentIndexChanged.connect(self.update_guild_data)
        self.actionNew.triggered.connect(self.new_guild)
        self.actionOpen.triggered.connect(self.load_guild)
        self.actionSave.triggered.connect(self.save_guild)
        self.actionSave_As.triggered.connect(self.save_as_guild)
        self.actionQuit.triggered.connect(self._quit)
        self.memberList.itemSelectionChanged.connect(self.update_member_data)
        self.addLogBtn.clicked.connect(self.add_logs)
        self.guildTitle.returnPressed.connect(self.update_guild_name)
        self.guildTitle.editingFinished.connect(self.guild_name_finished)
        self.startDate.dateChanged.connect(self.update_treasury_data)
        self.endDate.dateChanged.connect(self.update_treasury_data)
        self.treasuryMemberList.itemSelectionChanged.connect(self.update_member_deposits)
        self.treasuryRankBox.currentIndexChanged.connect(self.update_treasury_data)
        self.treasuryNameEntry.textChanged.connect(self.update_treasury_data)
        self.renameBtn.clicked.connect(self.rename)
        self.dataTabs.currentChanged.connect(self.updateCurrent)
        self.startDate_2.dateChanged.connect(self.update_energy)
        self.endDate_2.dateChanged.connect(self.update_energy)
        self.startDate_3.dateChanged.connect(self.update_log)
        self.endDate_3.dateChanged.connect(self.update_log)
        self.memberNameFilter.textChanged.connect(self.update_log)
        self.messageFilter.textChanged.connect(self.update_log)
        self.categoryFilterBox.currentIndexChanged.connect(self.update_log)
        
        #guild menu bar actions
        self.actionExport_Log.triggered.connect(self.exportLog)
        self.actionExport_Wiki_Block.triggered.connect(self.showWikiBlockText)
        begin = QDate(2011, 4, 4)
        self.startDate.setMinimumDate(begin)
        self.endDate.setMinimumDate(begin)
        self.startDate_2.setMinimumDate(begin)
        self.endDate_2.setMinimumDate(begin)
        self.startDate_3.setMinimumDate(begin)
        self.endDate_3.setMinimumDate(begin)
        today = QDate.currentDate()
        self.startDate.setMaximumDate(today)
        self.endDate.setMaximumDate(today)
        self.startDate_2.setMaximumDate(today)
        self.endDate_2.setMaximumDate(today)
        self.startDate.setDate(begin)
        self.endDate.setDate(today)
        self.startDate_2.setDate(begin)
        self.endDate_2.setDate(today)
        self.startDate_3.setDate(begin)
        self.endDate_3.setDate(today)
        self.refresh_ui()

        load = autoload()
        if load:
            self.guild.load_from_file(load)
            self.refresh_ui()
        
        self.show()

    def refresh_ui(self):
        self.guild.refresh()
        self.memberList.setCurrentRow(0)
        self.rankBox.setCurrentIndex(0)
        self.update_list()
        self.update_member_data()
        self.update_treasury_data()
        self.update_guild_data()
        self.update_member_deposits()
        self.update_log()
        self.nameEntry.setText("")
        begin = QDate(2011, 4, 4)
        today = QDate.currentDate()
        self.startDate.setDate(begin)
        self.endDate.setDate(today)
        self.logDateLbl.setText(self.guild.get_last_log_date())

    def showWikiBlockText(self):
        string = export_wiki(self.guild)
        win = QDialog(self)
        win.setFixedSize(255, 190)
        textBlock = QTextEdit(win)
        textBlock.setReadOnly(True)
        textBlock.setPlainText(string)
        textBlock.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        win.setWindowTitle("Member Wiki Block Text")
        win.show()
    
    def updateCurrent(self):
        current = self.dataTabs
        if current.isTabEnabled(0):
            self.update_list()
            self.update_member_data()
            self.update_guild_data()
        if current.isTabEnabled(1):
            self.update_treasury_data()
            self.update_member_deposits()
        if current.isTabEnabled(2):
            self.update_energy()
        if current.isTabEnabled(3):
            self.update_log()

    def _quit(self):
        self.close()

    def exportLog(self):
        filepath = QFileDialog.getSaveFileName()
        if filepath:
            self.guild.log.export_list(filepath)

    def rename(self):
        old = self.memberList.currentItem().text()
        name = QInputDialog.getText(self, "Name", "%s's Name" % old)[0]
        if name:
            self.guild.member_name_change(str(old), str(name))
        self.refresh_ui()

    def new_guild(self):
        name = QInputDialog.getText(self, "Guild Name", "New Guild Name")[0]
        self.guild.reset()
        self.guild.name = name
        self.guild.filepath = name + ".guild"
        self.update_guild_data()
        self.update_treasury_data()
        self.update_member_deposits()

    def load_guild(self):
        filepath = QFileDialog.getOpenFileName()
        if filepath:
            self.guild.reset()
            self.guild.load_from_file(filepath)
            self.guild.filepath = filepath;
            self.refresh_ui()

    def save_guild(self):
        self.guild.filepath = str(self.guild.filepath)
        self.guild.save_to_file(self.guild.filepath)

    def save_as_guild(self):
        filepath = QFileDialog.getSaveFileName()
        if filepath:
            filepath = str(filepath)
            self.guild.save_to_file(filepath)
            self.guild.filepath = filepath

    def update_list(self):
        self.memberList.clear()
        status = self.statusBox.currentText().toLower()
        memlist = []#list(self.guild.members)
        if status == 'active':
            memlist = list(self.guild.get_members_in_guild().keys())
        elif status == 'inactive':
            memlist = list(self.guild.get_members_out_guild().keys())
        else:
            memlist = list(self.guild.members)
        self.curr_mem_count = len(memlist)
        memlist.sort()
        memlist = sorted(memlist, key=lambda x: self.guild.data[x].rank_val, reverse=True)
        text = self.nameEntry.text().toLower()
        rank = self.rankBox.currentText()
        for i in memlist:
            compare = i.lower()
            compare = QString(compare)
            if compare.startsWith(text) and (self.guild.data[i].rank == rank or rank == "All"):
                self.memberList.addItem(i)
                
    def update_member_data(self):
        try:
            name = str(self.memberList.currentItem().text())
            member = self.guild.data[name]
            title = name + "'s Data"
            self.name_txt.setText(name)
            self.rank_txt.setText(member.rank)
            self.join_txt.setText(str(member.join_date.date()))
            self.days_txt.setText(str(member.days))
            self.deposit_txt.setText(str(member.total_deposits))

            self.memberLog.setRowCount(0)
            logs = self.guild.get_member_logs(name)
            row = 0
            for ev in logs:
                self.memberLog.insertRow(row);
                dt = QTableWidgetItem(str(ev.date))
                cat = QTableWidgetItem(str(ev.category))
                nam = QTableWidgetItem(str(ev.name))
                mess = QTableWidgetItem(str(ev.message))
                self.memberLog.setItem(row, 0, dt)
                self.memberLog.setItem(row, 1, cat)
                self.memberLog.setItem(row, 2, nam)
                self.memberLog.setItem(row, 3, mess)
                row += 1
                #self.memberLog.addItem(str(ev))
                
        except AttributeError, message:
            #print message
            self.name_txt.setText("name_text")
            self.rank_txt.setText("rank_text")
            self.join_txt.setText("join_text")
            self.days_txt.setText("days_text")
            self.deposit_txt.setText("deposit_text")

    def update_log(self):
        def search_func(ev):
            date = get_datetime_from_stamp(ev.date)
            d_pass = start <= date and end >= date
            n_pass = ev.true_name.lower().startswith(name) or name == ""
            c_pass = category == "Category" or category == ev.category
            m_pass = False
            re_pass = False
            if regex:
                re_pass = regex.match(ev.true_message)
            else:
                m_pass = ev.true_message.lower().startswith(message) or message == ""
            
            return d_pass and n_pass and c_pass and (m_pass or re_pass)
                
        try:
            name = str(self.memberNameFilter.text()).lower()
            message = str(self.messageFilter.text())
            category = self.categoryFilterBox.currentText()
            start = self.startDate_3.date()
            start = QDateTime(start, self.timeStart).toPyDateTime()
            end = self.endDate_3.date()
            end = QDateTime(end, self.timeEnd).toPyDateTime()
            self.logTable.setRowCount(0);
            logs = self.guild.log.data


            temp = "";
            regex = False
            if message.startswith("re:"):
                temp = message[3:]
                temp = temp.strip()
                regex = re.compile(temp, re.I)
            row = 0
            logs_filtered = filter(search_func, logs)
            for ev in logs_filtered:
                self.logTable.insertRow(row)
                dt = QTableWidgetItem(str(ev.date))
                cat = QTableWidgetItem(str(ev.category))
                nam = QTableWidgetItem(str(ev.true_name))
                mess = QTableWidgetItem(str(ev.true_message))
                self.logTable.setItem(row, 0, dt)
                self.logTable.setItem(row, 1, cat)
                self.logTable.setItem(row, 2, nam)
                self.logTable.setItem(row, 3, mess)
                row += 1
        except Exception as e:
            pass
    
    def add_logs(self):
        filepaths = QFileDialog.getOpenFileNames()
        filepaths = [str(i) for i in filepaths]
        if filepaths:
            for f in filepaths:
                add_log_to_guild(self.guild, f)
        self.refresh_ui()

    def update_guild_name(self):
        self.guild.name = self.guildTitle.text()

    def guild_name_finished(self):
        self.guildTitle.clear()
        self.guildTitle.insert(self.guild.name)

    def update_guild_data(self):
        self.memCount_txt.setText(str(self.curr_mem_count))
        self.totalDeposit_txt.setText(str(self.guild.total_dep))
        self.weekDeposit_txt.setText(str(self.guild.weekly_total))

    def update_treasury_data(self):
        start = self.startDate.date()
        start = QDateTime(start, self.timeStart).toPyDateTime()
        end = self.endDate.date()
        end = QDateTime(end, self.timeEnd).toPyDateTime()
        total = self.guild.get_total_in_week(start, end)
        self.depositDate_txt.setText(str(total))

        rank = self.treasuryRankBox.currentText()
        text = self.treasuryNameEntry.text().toLower()
        memlist = []
        self.treasuryMemberList.clear()
        for i in self.guild.data:
            compare = i.lower()
            compare = QString(compare)
            mem_total = 0
            for j in self.guild.data[i].get_deposits_in_dates(start, end):
                mem_total += j[1]
            if mem_total and compare.startsWith(text) and (self.guild.data[i].rank == rank or rank == "All"):
                memlist.append(i)
        memlist = sorted(memlist, key=lambda x: self.guild.data[x].rank_val, reverse=True)
        for i in memlist:
            if not i in self.guild.get_members_in_guild().keys():
                i += ' (left)'
            self.treasuryMemberList.addItem(i)
        self.update_member_deposits()

    def update_member_deposits(self):
        start = self.startDate.date()
        start = QDateTime(start, self.timeStart).toPyDateTime()
        end = self.endDate.date()
        end = QDateTime(end, self.timeEnd).toPyDateTime()
        self.memberDepositList.setRowCount(0)#clear()
        try:
            name = str(self.treasuryMemberList.currentItem().text())
            name = name.replace(' (left)', '')
            
            deposits = self.guild.data[name].get_deposits_in_dates(start, end)
            total = 0
            row = 0
            self.memberDepositList.setSortingEnabled(False)
            for i in deposits:
                #outstr = "%s|%s" % (i[0].date(), i[1])
                self.memberDepositList.insertRow(row)#(outstr)
                d = QTableWidgetItem(str(i[0].date()))
                amt = QTableWidgetItem(str(i[1]))
                self.memberDepositList.setItem(row, 0, d)
                self.memberDepositList.setItem(row, 1, amt)
                total += i[1]
            self.memberDateTotal_txt.setText("Total: %s" % total)
            self.memberDepositList.setSortingEnabled(True)
        except AttributeError, message:
            #print message
            self.memberDateTotal_txt.setText("Total:")

    def update_energy(self):
        s = QDateTime(self.startDate_2.date(), self.timeStart).toPyDateTime()
        e = QDateTime(self.endDate_2.date(), self.timeEnd).toPyDateTime()
        withdrawls = self.guild.get_energy_withdrawls(s, e)
        withdrawls = sorted(withdrawls, key=lambda w: w[0])
        deposits = self.guild.get_energy_deposits(s, e)
        deposits = sorted(deposits, key=lambda d: d[0])
        self.energyWithdrawlList.clear()
        self.energyDepositList.clear()
        total_w = 0
        for i in withdrawls:
            string = "{:}| {:} |{:}".format(i[0].date(),  -i[2], i[1])
            total_w += -i[2]
            self.energyWithdrawlList.addItem(string)
        total_d = 0
        for i in deposits:
            string = "{:}| {:} |{:}".format(i[0].date(), i[2], i[1])
            total_d += i[2]
            self.energyDepositList.addItem(string)
        net_energy = total_d - total_w
        self.netEnergy_txt.setText(str(net_energy))

##    def update_graph(self):
##        x = np.random.normal(1000)
##        y = np.random.normal(1000)
##        #plot = pg.PlotWidget(self.graphicsView)
##        self.graphicsView = pg.plot(x,y)

    
if __name__ == '__main__':
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


    try:
        if len(sys.argv) > 1:
            app = QApplication(sys.argv)
            window = Compiled_UI()
            filepath = sys.argv[1]
            window.guild.load_from_file(filepath)
            window.refresh_ui()
        else:
            app = QApplication(sys.argv)
            window = Compiled_UI()
        #window.guild.load_from_file("League_of_Gunners.guild")
        #window.refresh_ui()
        sys.exit(app.exec_())
    except Exception as E:
        #raise E
        with open("LOG.txt", "w") as f:
            f.write(str(E))
