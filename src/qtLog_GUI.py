# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Log_Analyzer.ui'
#
# Created: Thu Jul 16 23:59:07 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(878, 797)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.guildTitle = QtGui.QLineEdit(self.centralwidget)
        self.guildTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.guildTitle.setObjectName(_fromUtf8("guildTitle"))
        self.verticalLayout_5.addWidget(self.guildTitle)
        self.dataTabs = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.dataTabs.sizePolicy().hasHeightForWidth())
        self.dataTabs.setSizePolicy(sizePolicy)
        self.dataTabs.setElideMode(QtCore.Qt.ElideLeft)
        self.dataTabs.setObjectName(_fromUtf8("dataTabs"))
        self.memberTab = QtGui.QWidget()
        self.memberTab.setObjectName(_fromUtf8("memberTab"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.memberTab)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.frame = QtGui.QFrame(self.memberTab)
        self.frame.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.formLayout_7 = QtGui.QFormLayout()
        self.formLayout_7.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_7.setObjectName(_fromUtf8("formLayout_7"))
        self.rankLbl = QtGui.QLabel(self.frame)
        self.rankLbl.setObjectName(_fromUtf8("rankLbl"))
        self.formLayout_7.setWidget(1, QtGui.QFormLayout.LabelRole, self.rankLbl)
        self.rankBox = QtGui.QComboBox(self.frame)
        self.rankBox.setObjectName(_fromUtf8("rankBox"))
        self.rankBox.addItem(_fromUtf8(""))
        self.rankBox.addItem(_fromUtf8(""))
        self.rankBox.addItem(_fromUtf8(""))
        self.rankBox.addItem(_fromUtf8(""))
        self.rankBox.addItem(_fromUtf8(""))
        self.rankBox.addItem(_fromUtf8(""))
        self.formLayout_7.setWidget(1, QtGui.QFormLayout.FieldRole, self.rankBox)
        self.nameLbl = QtGui.QLabel(self.frame)
        self.nameLbl.setObjectName(_fromUtf8("nameLbl"))
        self.formLayout_7.setWidget(2, QtGui.QFormLayout.LabelRole, self.nameLbl)
        self.nameEntry = QtGui.QLineEdit(self.frame)
        self.nameEntry.setObjectName(_fromUtf8("nameEntry"))
        self.formLayout_7.setWidget(2, QtGui.QFormLayout.FieldRole, self.nameEntry)
        self.statusLbl = QtGui.QLabel(self.frame)
        self.statusLbl.setObjectName(_fromUtf8("statusLbl"))
        self.formLayout_7.setWidget(0, QtGui.QFormLayout.LabelRole, self.statusLbl)
        self.statusBox = QtGui.QComboBox(self.frame)
        self.statusBox.setObjectName(_fromUtf8("statusBox"))
        self.statusBox.addItem(_fromUtf8(""))
        self.statusBox.addItem(_fromUtf8(""))
        self.statusBox.addItem(_fromUtf8(""))
        self.formLayout_7.setWidget(0, QtGui.QFormLayout.FieldRole, self.statusBox)
        self.verticalLayout_3.addLayout(self.formLayout_7)
        self.memberList = QtGui.QListWidget(self.frame)
        self.memberList.setMinimumSize(QtCore.QSize(208, 0))
        self.memberList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.memberList.setObjectName(_fromUtf8("memberList"))
        self.verticalLayout_3.addWidget(self.memberList)
        self.renameBtn = QtGui.QPushButton(self.frame)
        self.renameBtn.setObjectName(_fromUtf8("renameBtn"))
        self.verticalLayout_3.addWidget(self.renameBtn)
        self.horizontalLayout_2.addWidget(self.frame)
        spacerItem = QtGui.QSpacerItem(20, 298, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.memCount = QtGui.QLabel(self.memberTab)
        self.memCount.setObjectName(_fromUtf8("memCount"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.memCount)
        self.memCount_txt = QtGui.QLabel(self.memberTab)
        self.memCount_txt.setObjectName(_fromUtf8("memCount_txt"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.memCount_txt)
        self.weekDeposit = QtGui.QLabel(self.memberTab)
        self.weekDeposit.setObjectName(_fromUtf8("weekDeposit"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.weekDeposit)
        self.weekDeposit_txt = QtGui.QLabel(self.memberTab)
        self.weekDeposit_txt.setObjectName(_fromUtf8("weekDeposit_txt"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.weekDeposit_txt)
        self.totalDeposit = QtGui.QLabel(self.memberTab)
        self.totalDeposit.setObjectName(_fromUtf8("totalDeposit"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.totalDeposit)
        self.totalDeposit_txt = QtGui.QLabel(self.memberTab)
        self.totalDeposit_txt.setObjectName(_fromUtf8("totalDeposit_txt"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.totalDeposit_txt)
        self.gridLayout_5.addLayout(self.formLayout_3, 1, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem1, 2, 0, 1, 2)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.nameLbl_2 = QtGui.QLabel(self.memberTab)
        self.nameLbl_2.setObjectName(_fromUtf8("nameLbl_2"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.nameLbl_2)
        self.name_txt = QtGui.QLabel(self.memberTab)
        self.name_txt.setObjectName(_fromUtf8("name_txt"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.name_txt)
        self.rankLbl_2 = QtGui.QLabel(self.memberTab)
        self.rankLbl_2.setObjectName(_fromUtf8("rankLbl_2"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.rankLbl_2)
        self.rank_txt = QtGui.QLabel(self.memberTab)
        self.rank_txt.setObjectName(_fromUtf8("rank_txt"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.rank_txt)
        self.joinLbl = QtGui.QLabel(self.memberTab)
        self.joinLbl.setObjectName(_fromUtf8("joinLbl"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.joinLbl)
        self.join_txt = QtGui.QLabel(self.memberTab)
        self.join_txt.setObjectName(_fromUtf8("join_txt"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.join_txt)
        self.daysLbl = QtGui.QLabel(self.memberTab)
        self.daysLbl.setObjectName(_fromUtf8("daysLbl"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.daysLbl)
        self.days_txt = QtGui.QLabel(self.memberTab)
        self.days_txt.setObjectName(_fromUtf8("days_txt"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.days_txt)
        self.depositLbl = QtGui.QLabel(self.memberTab)
        self.depositLbl.setObjectName(_fromUtf8("depositLbl"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.depositLbl)
        self.deposit_txt = QtGui.QLabel(self.memberTab)
        self.deposit_txt.setObjectName(_fromUtf8("deposit_txt"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.deposit_txt)
        self.gridLayout_5.addLayout(self.formLayout_2, 4, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.memberTab)
        self.label_3.setMaximumSize(QtCore.QSize(128, 16777215))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_5.addWidget(self.label_3, 4, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.memberTab)
        self.label_2.setMaximumSize(QtCore.QSize(128, 16777215))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_5.addWidget(self.label_2, 1, 0, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout_5)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_7.addItem(spacerItem2)
        self.memberLog = QtGui.QTableWidget(self.memberTab)
        self.memberLog.setObjectName(_fromUtf8("memberLog"))
        self.memberLog.setColumnCount(4)
        self.memberLog.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.memberLog.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.memberLog.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.memberLog.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.memberLog.setHorizontalHeaderItem(3, item)
        self.verticalLayout_7.addWidget(self.memberLog)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_7.addItem(spacerItem3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.dataTabs.addTab(self.memberTab, _fromUtf8(""))
        self.treasuryTab = QtGui.QWidget()
        self.treasuryTab.setObjectName(_fromUtf8("treasuryTab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.treasuryTab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.treasuryMemberListLbl = QtGui.QLabel(self.treasuryTab)
        self.treasuryMemberListLbl.setObjectName(_fromUtf8("treasuryMemberListLbl"))
        self.gridLayout.addWidget(self.treasuryMemberListLbl, 0, 0, 1, 1)
        self.memberDepositListLbl = QtGui.QLabel(self.treasuryTab)
        self.memberDepositListLbl.setObjectName(_fromUtf8("memberDepositListLbl"))
        self.gridLayout.addWidget(self.memberDepositListLbl, 0, 2, 1, 1)
        self.memberDepositList = QtGui.QTableWidget(self.treasuryTab)
        self.memberDepositList.setObjectName(_fromUtf8("memberDepositList"))
        self.memberDepositList.setColumnCount(2)
        self.memberDepositList.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.memberDepositList.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.memberDepositList.setHorizontalHeaderItem(1, item)
        self.gridLayout.addWidget(self.memberDepositList, 1, 2, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 0, 1, 2, 1)
        self.frame1 = QtGui.QFrame(self.treasuryTab)
        self.frame1.setMinimumSize(QtCore.QSize(211, 0))
        self.frame1.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame1.setObjectName(_fromUtf8("frame1"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.frame1)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.formLayout_6 = QtGui.QFormLayout()
        self.formLayout_6.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_6.setObjectName(_fromUtf8("formLayout_6"))
        self.treasuryRankLbl = QtGui.QLabel(self.frame1)
        self.treasuryRankLbl.setObjectName(_fromUtf8("treasuryRankLbl"))
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.LabelRole, self.treasuryRankLbl)
        self.treasuryNamelbl = QtGui.QLabel(self.frame1)
        self.treasuryNamelbl.setObjectName(_fromUtf8("treasuryNamelbl"))
        self.formLayout_6.setWidget(1, QtGui.QFormLayout.LabelRole, self.treasuryNamelbl)
        self.treasuryNameEntry = QtGui.QLineEdit(self.frame1)
        self.treasuryNameEntry.setObjectName(_fromUtf8("treasuryNameEntry"))
        self.formLayout_6.setWidget(1, QtGui.QFormLayout.FieldRole, self.treasuryNameEntry)
        self.treasuryRankBox = QtGui.QComboBox(self.frame1)
        self.treasuryRankBox.setObjectName(_fromUtf8("treasuryRankBox"))
        self.treasuryRankBox.addItem(_fromUtf8(""))
        self.treasuryRankBox.addItem(_fromUtf8(""))
        self.treasuryRankBox.addItem(_fromUtf8(""))
        self.treasuryRankBox.addItem(_fromUtf8(""))
        self.treasuryRankBox.addItem(_fromUtf8(""))
        self.treasuryRankBox.addItem(_fromUtf8(""))
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.FieldRole, self.treasuryRankBox)
        self.verticalLayout_4.addLayout(self.formLayout_6)
        self.treasuryMemberList = QtGui.QListWidget(self.frame1)
        self.treasuryMemberList.setObjectName(_fromUtf8("treasuryMemberList"))
        self.verticalLayout_4.addWidget(self.treasuryMemberList)
        self.gridLayout.addWidget(self.frame1, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 1, 0, 1, 2)
        self.memberDateTotal_txt = QtGui.QLabel(self.treasuryTab)
        self.memberDateTotal_txt.setObjectName(_fromUtf8("memberDateTotal_txt"))
        self.gridLayout_3.addWidget(self.memberDateTotal_txt, 2, 1, 1, 1)
        self.formLayout_4 = QtGui.QFormLayout()
        self.formLayout_4.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        self.startDateLbl = QtGui.QLabel(self.treasuryTab)
        self.startDateLbl.setObjectName(_fromUtf8("startDateLbl"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.startDateLbl)
        self.endDateLbl = QtGui.QLabel(self.treasuryTab)
        self.endDateLbl.setObjectName(_fromUtf8("endDateLbl"))
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.LabelRole, self.endDateLbl)
        self.endDate = QtGui.QDateEdit(self.treasuryTab)
        self.endDate.setObjectName(_fromUtf8("endDate"))
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.FieldRole, self.endDate)
        self.startDate = QtGui.QDateEdit(self.treasuryTab)
        self.startDate.setObjectName(_fromUtf8("startDate"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.startDate)
        self.gridLayout_3.addLayout(self.formLayout_4, 0, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.depositDateLbl = QtGui.QLabel(self.treasuryTab)
        self.depositDateLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.depositDateLbl.setObjectName(_fromUtf8("depositDateLbl"))
        self.verticalLayout.addWidget(self.depositDateLbl)
        self.depositDate_txt = QtGui.QLabel(self.treasuryTab)
        self.depositDate_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.depositDate_txt.setObjectName(_fromUtf8("depositDate_txt"))
        self.verticalLayout.addWidget(self.depositDate_txt)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.dataTabs.addTab(self.treasuryTab, _fromUtf8(""))
        self.energyTab = QtGui.QWidget()
        self.energyTab.setObjectName(_fromUtf8("energyTab"))
        self.gridLayout_4 = QtGui.QGridLayout(self.energyTab)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.formLayout_5 = QtGui.QFormLayout()
        self.formLayout_5.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_5.setObjectName(_fromUtf8("formLayout_5"))
        self.startDate_2 = QtGui.QDateEdit(self.energyTab)
        self.startDate_2.setObjectName(_fromUtf8("startDate_2"))
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.FieldRole, self.startDate_2)
        self.endDateLbl_2 = QtGui.QLabel(self.energyTab)
        self.endDateLbl_2.setObjectName(_fromUtf8("endDateLbl_2"))
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.LabelRole, self.endDateLbl_2)
        self.endDate_2 = QtGui.QDateEdit(self.energyTab)
        self.endDate_2.setObjectName(_fromUtf8("endDate_2"))
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.FieldRole, self.endDate_2)
        self.startDateLbl_2 = QtGui.QLabel(self.energyTab)
        self.startDateLbl_2.setObjectName(_fromUtf8("startDateLbl_2"))
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.LabelRole, self.startDateLbl_2)
        self.gridLayout_4.addLayout(self.formLayout_5, 0, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.netEnergyLbl = QtGui.QLabel(self.energyTab)
        self.netEnergyLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.netEnergyLbl.setWordWrap(True)
        self.netEnergyLbl.setObjectName(_fromUtf8("netEnergyLbl"))
        self.verticalLayout_2.addWidget(self.netEnergyLbl)
        self.netEnergy_txt = QtGui.QLabel(self.energyTab)
        self.netEnergy_txt.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.netEnergy_txt.setObjectName(_fromUtf8("netEnergy_txt"))
        self.verticalLayout_2.addWidget(self.netEnergy_txt)
        self.gridLayout_4.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.energyDepositList = QtGui.QListWidget(self.energyTab)
        self.energyDepositList.setObjectName(_fromUtf8("energyDepositList"))
        self.gridLayout_2.addWidget(self.energyDepositList, 1, 0, 1, 1)
        self.energyDepositLbl = QtGui.QLabel(self.energyTab)
        self.energyDepositLbl.setObjectName(_fromUtf8("energyDepositLbl"))
        self.gridLayout_2.addWidget(self.energyDepositLbl, 0, 0, 1, 1)
        self.energyWithdrawlLbl = QtGui.QLabel(self.energyTab)
        self.energyWithdrawlLbl.setObjectName(_fromUtf8("energyWithdrawlLbl"))
        self.gridLayout_2.addWidget(self.energyWithdrawlLbl, 0, 2, 1, 1)
        self.energyWithdrawlList = QtGui.QListWidget(self.energyTab)
        self.energyWithdrawlList.setObjectName(_fromUtf8("energyWithdrawlList"))
        self.gridLayout_2.addWidget(self.energyWithdrawlList, 1, 2, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem5, 0, 1, 2, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 1, 0, 1, 2)
        self.dataTabs.addTab(self.energyTab, _fromUtf8(""))
        self.logTab = QtGui.QWidget()
        self.logTab.setObjectName(_fromUtf8("logTab"))
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.logTab)
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.formLayout_8 = QtGui.QFormLayout()
        self.formLayout_8.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_8.setObjectName(_fromUtf8("formLayout_8"))
        self.startDateLbl_3 = QtGui.QLabel(self.logTab)
        self.startDateLbl_3.setObjectName(_fromUtf8("startDateLbl_3"))
        self.formLayout_8.setWidget(0, QtGui.QFormLayout.LabelRole, self.startDateLbl_3)
        self.startDate_3 = QtGui.QDateEdit(self.logTab)
        self.startDate_3.setObjectName(_fromUtf8("startDate_3"))
        self.formLayout_8.setWidget(0, QtGui.QFormLayout.FieldRole, self.startDate_3)
        self.endDateLbl_3 = QtGui.QLabel(self.logTab)
        self.endDateLbl_3.setObjectName(_fromUtf8("endDateLbl_3"))
        self.formLayout_8.setWidget(1, QtGui.QFormLayout.LabelRole, self.endDateLbl_3)
        self.endDate_3 = QtGui.QDateEdit(self.logTab)
        self.endDate_3.setObjectName(_fromUtf8("endDate_3"))
        self.formLayout_8.setWidget(1, QtGui.QFormLayout.FieldRole, self.endDate_3)
        self.horizontalLayout_4.addLayout(self.formLayout_8)
        self.categoryFilterBox = QtGui.QComboBox(self.logTab)
        self.categoryFilterBox.setObjectName(_fromUtf8("categoryFilterBox"))
        self.categoryFilterBox.addItem(_fromUtf8(""))
        self.categoryFilterBox.addItem(_fromUtf8(""))
        self.categoryFilterBox.addItem(_fromUtf8(""))
        self.categoryFilterBox.addItem(_fromUtf8(""))
        self.categoryFilterBox.addItem(_fromUtf8(""))
        self.categoryFilterBox.addItem(_fromUtf8(""))
        self.categoryFilterBox.addItem(_fromUtf8(""))
        self.horizontalLayout_4.addWidget(self.categoryFilterBox)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.label_4 = QtGui.QLabel(self.logTab)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_9.addWidget(self.label_4)
        self.memberNameFilter = QtGui.QLineEdit(self.logTab)
        self.memberNameFilter.setObjectName(_fromUtf8("memberNameFilter"))
        self.verticalLayout_9.addWidget(self.memberNameFilter)
        self.horizontalLayout_4.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.label_5 = QtGui.QLabel(self.logTab)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_10.addWidget(self.label_5)
        self.messageFilter = QtGui.QLineEdit(self.logTab)
        self.messageFilter.setObjectName(_fromUtf8("messageFilter"))
        self.verticalLayout_10.addWidget(self.messageFilter)
        self.horizontalLayout_4.addLayout(self.verticalLayout_10)
        self.verticalLayout_11.addLayout(self.horizontalLayout_4)
        self.logTable = QtGui.QTableWidget(self.logTab)
        self.logTable.setObjectName(_fromUtf8("logTable"))
        self.logTable.setColumnCount(4)
        self.logTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.logTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.logTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.logTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.logTable.setHorizontalHeaderItem(3, item)
        self.verticalLayout_11.addWidget(self.logTable)
        self.verticalLayout_12.addLayout(self.verticalLayout_11)
        self.dataTabs.addTab(self.logTab, _fromUtf8(""))
        self.verticalLayout_5.addWidget(self.dataTabs)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.addLogBtn = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addLogBtn.sizePolicy().hasHeightForWidth())
        self.addLogBtn.setSizePolicy(sizePolicy)
        self.addLogBtn.setMinimumSize(QtCore.QSize(171, 23))
        self.addLogBtn.setMaximumSize(QtCore.QSize(251, 23))
        self.addLogBtn.setObjectName(_fromUtf8("addLogBtn"))
        self.horizontalLayout.addWidget(self.addLogBtn)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.logDateLbl = QtGui.QLabel(self.centralwidget)
        self.logDateLbl.setObjectName(_fromUtf8("logDateLbl"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.logDateLbl)
        self.horizontalLayout.addLayout(self.formLayout)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 878, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuGuild = QtGui.QMenu(self.menubar)
        self.menuGuild.setObjectName(_fromUtf8("menuGuild"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSave_As = QtGui.QAction(MainWindow)
        self.actionSave_As.setObjectName(_fromUtf8("actionSave_As"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionExport_Log = QtGui.QAction(MainWindow)
        self.actionExport_Log.setObjectName(_fromUtf8("actionExport_Log"))
        self.actionExport_Wiki_Block = QtGui.QAction(MainWindow)
        self.actionExport_Wiki_Block.setObjectName(_fromUtf8("actionExport_Wiki_Block"))
        self.actionAdjust_Inventory = QtGui.QAction(MainWindow)
        self.actionAdjust_Inventory.setObjectName(_fromUtf8("actionAdjust_Inventory"))
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuGuild.addAction(self.actionExport_Log)
        self.menuGuild.addAction(self.actionExport_Wiki_Block)
        self.menuGuild.addAction(self.actionAdjust_Inventory)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuGuild.menuAction())

        self.retranslateUi(MainWindow)
        self.dataTabs.setCurrentIndex(0)
        self.statusBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.guildTitle, self.memberList)
        MainWindow.setTabOrder(self.memberList, self.renameBtn)
        MainWindow.setTabOrder(self.renameBtn, self.addLogBtn)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Spiral Knights Log Tracker", None))
        self.guildTitle.setText(_translate("MainWindow", "Guild Title", None))
        self.rankLbl.setText(_translate("MainWindow", "Rank", None))
        self.rankBox.setItemText(0, _translate("MainWindow", "All", None))
        self.rankBox.setItemText(1, _translate("MainWindow", "Guild Master", None))
        self.rankBox.setItemText(2, _translate("MainWindow", "Officer", None))
        self.rankBox.setItemText(3, _translate("MainWindow", "Veteran", None))
        self.rankBox.setItemText(4, _translate("MainWindow", "Member", None))
        self.rankBox.setItemText(5, _translate("MainWindow", "Recruit", None))
        self.nameLbl.setText(_translate("MainWindow", "Name", None))
        self.statusLbl.setText(_translate("MainWindow", "Status", None))
        self.statusBox.setItemText(0, _translate("MainWindow", "All", None))
        self.statusBox.setItemText(1, _translate("MainWindow", "Active", None))
        self.statusBox.setItemText(2, _translate("MainWindow", "Inactive", None))
        self.renameBtn.setText(_translate("MainWindow", "Rename", None))
        self.memCount.setText(_translate("MainWindow", "Member Count", None))
        self.memCount_txt.setText(_translate("MainWindow", "count", None))
        self.weekDeposit.setText(_translate("MainWindow", "Weekly Deposits", None))
        self.weekDeposit_txt.setText(_translate("MainWindow", "deposit", None))
        self.totalDeposit.setText(_translate("MainWindow", "Total Deposits", None))
        self.totalDeposit_txt.setText(_translate("MainWindow", "total", None))
        self.nameLbl_2.setText(_translate("MainWindow", "Name", None))
        self.name_txt.setText(_translate("MainWindow", "name_text", None))
        self.rankLbl_2.setText(_translate("MainWindow", "Rank", None))
        self.rank_txt.setText(_translate("MainWindow", "rank_text", None))
        self.joinLbl.setText(_translate("MainWindow", "Join Date", None))
        self.join_txt.setText(_translate("MainWindow", "join_text", None))
        self.daysLbl.setText(_translate("MainWindow", "Days in Guild", None))
        self.days_txt.setText(_translate("MainWindow", "days_text", None))
        self.depositLbl.setText(_translate("MainWindow", "Total Deposits", None))
        self.deposit_txt.setText(_translate("MainWindow", "deposit_text", None))
        self.label_3.setText(_translate("MainWindow", "Member Data", None))
        self.label_2.setText(_translate("MainWindow", "Guild Data", None))
        item = self.memberLog.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Timestamp", None))
        item = self.memberLog.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Category", None))
        item = self.memberLog.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Member", None))
        item = self.memberLog.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Message", None))
        self.dataTabs.setTabText(self.dataTabs.indexOf(self.memberTab), _translate("MainWindow", "Membership", None))
        self.treasuryMemberListLbl.setText(_translate("MainWindow", "Member Names", None))
        self.memberDepositListLbl.setText(_translate("MainWindow", "Member Deposits", None))
        item = self.memberDepositList.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date", None))
        item = self.memberDepositList.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Amount", None))
        self.treasuryRankLbl.setText(_translate("MainWindow", "Rank", None))
        self.treasuryNamelbl.setText(_translate("MainWindow", "Name", None))
        self.treasuryRankBox.setItemText(0, _translate("MainWindow", "All", None))
        self.treasuryRankBox.setItemText(1, _translate("MainWindow", "Guild Master", None))
        self.treasuryRankBox.setItemText(2, _translate("MainWindow", "Officer", None))
        self.treasuryRankBox.setItemText(3, _translate("MainWindow", "Veteran", None))
        self.treasuryRankBox.setItemText(4, _translate("MainWindow", "Member", None))
        self.treasuryRankBox.setItemText(5, _translate("MainWindow", "Recruit", None))
        self.memberDateTotal_txt.setText(_translate("MainWindow", "Total:", None))
        self.startDateLbl.setText(_translate("MainWindow", "Start Date", None))
        self.endDateLbl.setText(_translate("MainWindow", "End Date", None))
        self.depositDateLbl.setText(_translate("MainWindow", "Deposit Value in Dates", None))
        self.depositDate_txt.setText(_translate("MainWindow", "Date_Deposits", None))
        self.dataTabs.setTabText(self.dataTabs.indexOf(self.treasuryTab), _translate("MainWindow", "Treasury", None))
        self.endDateLbl_2.setText(_translate("MainWindow", "End Date", None))
        self.startDateLbl_2.setText(_translate("MainWindow", "Start Date", None))
        self.netEnergyLbl.setText(_translate("MainWindow", "Net Energy", None))
        self.netEnergy_txt.setText(_translate("MainWindow", "energy_text", None))
        self.energyDepositLbl.setText(_translate("MainWindow", "Energy Deposited", None))
        self.energyWithdrawlLbl.setText(_translate("MainWindow", "Energy Withdrawl", None))
        self.dataTabs.setTabText(self.dataTabs.indexOf(self.energyTab), _translate("MainWindow", "Energy", None))
        self.startDateLbl_3.setText(_translate("MainWindow", "Start Date", None))
        self.endDateLbl_3.setText(_translate("MainWindow", "End Date", None))
        self.categoryFilterBox.setItemText(0, _translate("MainWindow", "Category", None))
        self.categoryFilterBox.setItemText(1, _translate("MainWindow", "Membership", None))
        self.categoryFilterBox.setItemText(2, _translate("MainWindow", "Treasury", None))
        self.categoryFilterBox.setItemText(3, _translate("MainWindow", "Storage", None))
        self.categoryFilterBox.setItemText(4, _translate("MainWindow", "Energy", None))
        self.categoryFilterBox.setItemText(5, _translate("MainWindow", "Upkeep", None))
        self.categoryFilterBox.setItemText(6, _translate("MainWindow", "Guild Hall", None))
        self.label_4.setText(_translate("MainWindow", "Member Filter", None))
        self.label_5.setText(_translate("MainWindow", "Message Filter", None))
        item = self.logTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Timestamp", None))
        item = self.logTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Category", None))
        item = self.logTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Member", None))
        item = self.logTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Message", None))
        self.dataTabs.setTabText(self.dataTabs.indexOf(self.logTab), _translate("MainWindow", "Logs", None))
        self.addLogBtn.setText(_translate("MainWindow", "Add Guild Log(s)", None))
        self.label.setText(_translate("MainWindow", "Last Log Date", None))
        self.logDateLbl.setText(_translate("MainWindow", "date", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuGuild.setTitle(_translate("MainWindow", "Guild", None))
        self.actionNew.setText(_translate("MainWindow", "New", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionSave_As.setText(_translate("MainWindow", "Save As", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionExport_Log.setText(_translate("MainWindow", "Export Log", None))
        self.actionExport_Wiki_Block.setText(_translate("MainWindow", "Export Wiki Block", None))
        self.actionAdjust_Inventory.setText(_translate("MainWindow", "Adjust Inventory", None))

