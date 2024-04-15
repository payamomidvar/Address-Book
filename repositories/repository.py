import db


def init(book_name):
    db.db_init(book_name)


def add_contact(contact):
    db.insert_entry(contact)


def get_by_id(entry):
    return db.get_id(entry)


def get_contact(contact):
    entry = []

    try:
        if contact.split()[1]:
            entry.append(contact.split()[0])
            entry.append(contact.split()[1])
    except(Exception,):
        entry.append('')
        entry.append(contact.split()[0])

    for row in db.get_entry(db.get_id(entry)):
        return row


def remove_contact(contact):
    entry = []
    try:
        entry.append(contact.split()[0])
    except(Exception,):
        entry.append('')

    try:
        entry.append(contact.split()[1])
    except(Exception,):
        entry.append('')

    db.delete_entry(db.get_id(entry))


def edit_contact(entry_id, contact):
    db.edit_entry(entry_id, contact)


def commit():
    db.db_commit()


def search(search_string, sort):
    return db.search_entry(search_string, sort)



