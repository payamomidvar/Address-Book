import sqlite3 as sql
import os.path as path
import config as cfg


def db_init(db_name):
    if db_exists(db_name):
        cfg.DB = sql.connect(db_name + '.ab')
        cfg.C = cfg.DB.cursor()
        print('Database already exists')

    else:
        cfg.DB = sql.connect(db_name + '.ab')
        cfg.C = cfg.DB.cursor()
        create_table = '''CREATE TABLE Contacts(First TEXT, 
					Last TEXT, Street1 TEXT, Street2 TEXT, City TEXT, State TEXT,
					Zip TEXT, Home TEXT, Mobile TEXT, Email TEXT, Birthday TEXT, 
					Notes TEXT) '''
        cfg.C.execute(create_table)
        cfg.DB.commit()
        print('New table created')


def db_exists(db_name):
    if (path.isfile(db_name + '.ab')):
        return True
    else:
        return False


def get_id(entry):
    entry_id = "SELECT rowid, * FROM Contacts WHERE First = ? AND Last = ?"
    cfg.C.execute(entry_id, [entry[0], entry[1]])

    for row in cfg.C:
        return row[0]


def insert_entry(entry):
    cfg.C.execute('INSERT INTO Contacts VALUES (?,?,?,?,?,?,?,?,?,?,?,?)',
                  entry)

    cfg.DB.commit()


def delete_entry(entry_id):
    cfg.C.execute("DELETE FROM Contacts WHERE rowid = ?", [entry_id])


def get_entry(entry_id):
    cfg.C.execute("SELECT * FROM Contacts WHERE rowid = ?", [entry_id])
    return cfg.C


def db_commit():
    cfg.DB.commit()


def edit_entry(entry_id, entry):
    entry_update = '''UPDATE Contacts SET First = ?, Last = ?, Street1 = ?,
			Street2 = ?, City = ?, State = ?, Zip = ?, Home = ?, Mobile = ?, 
			Email = ?, Birthday = ?, Notes = ? WHERE rowid = ? '''

    cfg.C.execute(entry_update, [entry[0], entry[1], entry[2], entry[3],
                                 entry[4], entry[5], entry[6], entry[7],
                                 entry[8], entry[9], entry[10],
                                 entry[11], entry_id])


def search_entry(value, sort):
    if sort == 'Last Name':
        search_last = '''SELECT * FROM Contacts WHERE (First || Last || Street1 || 
				Street2 || City || State || Zip || Home || Mobile || Email || 
				Birthday || Notes) LIKE '%' || ? || '%' ORDER BY Last ASC, First ASC'''
        cfg.C.execute(search_last, [value])

    elif sort == 'Zip':
        search_zip = '''SELECT * FROM Contacts WHERE (First || Last || Street1 || 
				Street2 || City || State || Zip || Home || Mobile || Email || 
				Birthday || Notes) LIKE '%' || ? || '%' ORDER BY Zip ASC, Last ASC'''
        cfg.C.execute(search_zip, [value])

    return cfg.C
