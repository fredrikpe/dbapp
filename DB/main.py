
import gdata.spreadsheet.text_db as gst


def CreateTable(db, name, fields):
    db.CreateTable(name, fields)



db = client2.CreateDatabase("tmpdb")
table = db.CreateTable('Kong', ['navn', 'alder'])
row1 = table.AddRecord({'navn':'Pelle', 'alder':'10'})
