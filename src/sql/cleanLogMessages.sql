UPDATE Logs
SET  New_Message=NULL
WHERE New_Message = True_Message;

UPDATE Logs
SET New_Message=NULL
WHERE New_Message = "None";

UPDATE Logs
SET New_Message=NULL
WHERE New_Message = "";