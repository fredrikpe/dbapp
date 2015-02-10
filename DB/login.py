
import gdata.spreadsheet.text_db as gst

def login(username, password):
    " Returns a google client. "
    return gst.DatabaseClient(username,password)
