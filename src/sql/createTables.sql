CREATE TABLE `Logs` (
	Timestamp datetime,
	Category,
	True_Name varchar(18),
	True_Message,
	New_Name varchar(18),
	New_Message
);

CREATE TABLE 'Members' (
	ID integer PRIMARY KEY AUTOINCREMENT,
	Name varchar(18),
	JoinDate datetime,
	InGuild boolean,
	RankVal integer
);

CREATE TABLE 'Crown_Deposits' (
	DepositDate datetime,
	ID integer,
	amount integer,
	FOREIGN KEY(ID) REFERENCES Members(ID)
);

CREATE TABLE 'Energy_Deposits' (
	DepositDate datetime,
	ID integer,
	amount integer,
	FOREIGN KEY(ID) REFERENCES Members(ID)
);