import sqlite3

def connect():
    con = sqlite3.connect('Portfolio.db')
    cur = con.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS Portfolio(x INTEGER PRIMARY KEY, Mtype text, refno integer, fname text, \
                     surname text, address text, post integer, mobno integer, ID text, title text, Company text, \
                     borrow integer, due integer, loan integer)')

    con.commit()
    con.close()

def insert(Mtype=' ', refno=' ', fname=' ', surname=' ', address=' ', post=' ', mobno=' ', ID=' ',
           title=' ', Company=' ', borrow=' ', due=' ', loan=' '):
    con = sqlite3.connect('Portfolio.db')
    cur = con.cursor()

    cur.execute('INSERT INTO Portfolio VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?)', (Mtype, refno, fname, surname, address, post,
                                                                                  mobno, ID, title, Company, borrow, due, loan))

    con.commit()
    con.close()


def view():
    con = sqlite3.connect('Portfolio.db')
    cur = con.cursor()

    cur.execute('SELECT * FROM Portfolio')
    row = cur.fetchall()
    con.close()
    return row

def delete(x):
    con = sqlite3.connect('Portfolio.db')
    cur = con.cursor()

    cur.execute('DELETE FROM Portfolio WHERE x = ?', (x,))

    con.commit()
    con.close()


def update(x, Mtype=' ', refno=' ', fname=' ', surname=' ', address=' ', post=' ', mobno=' ', ID=' ',
           title=' ', Company=' ', borrow=' ', due=' ', loan=' '):
    con = sqlite3.connect('Portfolio.db')
    cur = con.cursor()

    cur.execute('UPDATE Portfolio SET Mtype = ? OR refno = ? OR fname = ? OR surname = ? OR address = ? OR post = ? OR \
       mobno = ? OR ID = ? OR title = ? OR Company = ? OR borrow = ? OR due = ? OR loan = ?', (Mtype, refno, fname, surname, address,
                                                                                               post, mobno, ID, title, Company, borrow, due, loan))
    con.commit()
    con.close()


def search(Mtype=' ', refno=' ', fname=' ', surname=' ', address=' ', post=' ', mobno=' ', ID=' ',
           title=' ', Company=' ', borrow=' ', due=' ', loan=' '):
    con = sqlite3.connect('Portfolio.db')
    cur = con.cursor()

    cur.execute('SELECT * FROM Portfolio WHERE Mtype = ? OR refno = ? OR fname = ? OR surname = ? OR address = ? OR \
       post = ? OR mobno = ? OR ID = ? OR title = ? OR Company = ? OR borrow = ? OR due = ? OR loan = ?', (Mtype, refno,
                                                                                                           fname, surname,
                                                                                                           address, post, mobno,
                                                                                                           ID, title, Company,
                                                                                                           borrow, due, loan))
    row = cur.fetchall()
    con.close()
    return row

connect()