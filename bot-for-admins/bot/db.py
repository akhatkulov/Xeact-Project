from helper_db import Database
import os

db = Database(path_to_db="move.sql")
try:
    db.create_table()
except:
    pass
try:
    os.mkdir("../data")
except:
    pass

def return_cnt():
    return db.cnt_vd()

def get_data(page):
    page*=10
    x = []
    for i in range((page-11),page):
        x.append({"id":i+1,"name":db.get_vd()[i][0],"description":db.get_vd()[i][1],"down_link":db.get_vd()[i][3],"photo_link":db.get_vd()[i][2]})
        print(x)
    
    return x