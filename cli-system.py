#!/usr/bin/python3

#######################################################################################
#              GROUP MEMBERS : JAYSON, ARSENIUS, MAYNARD, JASPER, NICO                #
#######################################################################################
                
#######################################################################################
#######################################################################################

# LIBRARIES
import sqlite3, os
from time import sleep

#######################################################################################
#######################################################################################

# COLOR LIST
class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
#######################################################################################
#######################################################################################

# BANNER
banner = """
          ·▄▄▄▪   ▐ ▄  ▄▄▄· ▄▄▌       
          ▐▄▄·██ •█▌▐█▐█ ▀█ ██•       
          ██▪ ▐█·▐█▐▐▌▄█▀▀█ ██▪       
          ██▌.▐█▌██▐█▌▐█ ▪▐▌▐█▌▐▌     
          ▀▀▀ ▀▀▀▀▀ █▪ ▀  ▀ .▀▀▀      
   ▄▄▄·▄▄▄         ▐▄▄▄▄▄▄ . ▄▄· ▄▄▄▄▄
  ▐█ ▄█▀▄ █·▪       ·██▀▄.▀·▐█ ▌▪•██  
   ██▀·▐▀▀▄  ▄█▀▄ ▪▄ ██▐▀▀▪▄██ ▄▄ ▐█.▪
  ▐█▪·•▐█•█▌▐█▌.▐▌▐▌▐█▌▐█▄▄▌▐███▌ ▐█▌·
  .▀   .▀  ▀ ▀█▄▀▪ ▀▀▀• ▀▀▀ ·▀▀▀  ▀▀▀ 
"""

#######################################################################################
#######################################################################################

# GROUP MEMBERS
def group_members():
    os.system("clear")
    print(bcolors.CYAN + banner + bcolors.ENDC)
    sleep(.1)
    print(bcolors.WARNING + "┌──────────────────────────────────────┐" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.WARNING + "│      [+] OUR GROUP MEMBERS [+]       │" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.WARNING + "│──────────────────────────────────────│" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.WARNING + "│ * JAYSON SAN BUENAVENTURA            │" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.WARNING + "│ * JOHN MAYNARD ELEC                  │" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.WARNING + "│ * MARK ARSENIUS GAMBOA               │" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.WARNING + "│ * JASPER CEDRICK ABELLA              │" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.WARNING + "│ * NICO YBAÑEZ MANDAPAT               │" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.WARNING + "└──────────────────────────────────────┘" + bcolors.ENDC)
    sleep(.1)
    print("\n")
    input(" Press any key to continue...")
    
#######################################################################################
#######################################################################################

# CREATE DATABASE TABLE
def create_table():
        conn = sqlite3.connect('Item.db')
        cur = conn.cursor()
        cur.executescript("""
                    CREATE TABLE IF NOT EXISTS NAMES(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL);

                    CREATE TABLE IF NOT EXISTS FISH(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL);

                    CREATE TABLE IF NOT EXISTS NUMBER(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL);

                    CREATE TABLE IF NOT EXISTS COUNTRY(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL);

                    CREATE TABLE IF NOT EXISTS POSTAL(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name INTEGER);
    """)
        conn.commit()
        cur.close()
        conn.close()

#######################################################################################
#######################################################################################

# MAIN MENU
def menu():
    print(bcolors.CYAN + banner + bcolors.ENDC)
    sleep(.1)
    print(bcolors.HEADER + " ───────────────────────────────────────" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.WARNING + "   Welcome to our Final Project in DSA" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.HEADER + " ───────────────────────────────────────" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.CYAN + " [1]. ADD ITEM" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.CYAN + " [2]. SEARCH ITEM" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.CYAN + " [3]. DELETE ITEM" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.CYAN + " [4]. UPDATE ITEM" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.CYAN + " [5]. VIEW ALL ITEM" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.CYAN + " [6]. GROUP MEMBERS" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.CYAN + " [0]. CLOSE PROGRAM\n")

#######################################################################################
#######################################################################################

# INSERT QUERY

def insert_name():
    ID = int(input(" Enter ID: "))
    NAME = input(" Enter name: ")
    conn = sqlite3.connect('Item.db')
    cur = conn.cursor()
    sql = f"""INSERT INTO NAME(id,name)VALUES ('{ID}','{NAME}');"""
    cur.execute(sql)
    conn.commit()
    conn.close()
    print(' Item Information Add Complete')
    input(" Press any key to continue...")
    os.system("clear")
    add_item()

def insert_fish():
    ID = int(input(" Enter ID: "))
    NAME = input(" Enter name: ")
    conn = sqlite3.connect('Item.db')
    cur = conn.cursor()
    sql = f"""INSERT INTO FISH(id,name)VALUES ('{ID}','{NAME}');"""
    cur.execute(sql)
    conn.commit()
    conn.close()
    print(' Item Information Add Complete')
    input(" Press any key to continue...")
    os.system("clear")
    add_item()

def insert_number():
    ID = int(input(" Enter ID: "))
    NAME = input(" Enter name: ")
    conn = sqlite3.connect('Item.db')
    cur = conn.cursor()
    sql = f"""INSERT INTO NUMBER(id,name)VALUES ('{ID}','{NAME}');"""
    cur.execute(sql)
    conn.commit()
    conn.close()
    print(' Item Information Add Complete')
    input(" Press any key to continue...")
    os.system("clear")
    add_item()

def insert_country():
    ID = int(input(" Enter ID: "))
    NAME = input(" Enter name: ")
    conn = sqlite3.connect('Item.db')
    cur = conn.cursor()
    sql = f"""INSERT INTO COUNTRY(id,name)VALUES ('{ID}','{NAME}');"""
    cur.execute(sql)
    conn.commit()
    conn.close()
    print(' Item Information Add Complete')
    input(" Press any key to continue...")
    os.system("clear")
    add_item()

def insert_postal():
    ID = int(input(" Enter ID: "))
    NAME = input(" Enter name: ")
    conn = sqlite3.connect('Item.db')
    cur = conn.cursor()
    sql = f"""INSERT INTO POSTAL(id,name)VALUES ('{ID}','{NAME}');"""
    cur.execute(sql)
    conn.commit()
    conn.close()
    print(' Item Information Add Complete')
    input(" Press any key to continue...")
    os.system("clear")
    add_item()

#######################################################################################
#######################################################################################

# DELETE QUERY
def delete_name():
    ID = int(input(" Enter ID: "))
    conn = sqlite3.connect('Item.db')
    cur = conn.cursor()
    sql=f"""DELETE FROM NAME WHERE id='{ID}'; """
    cur.execute(sql)
    conn.commit()
    conn.close()
    print(' Item Deletion Complete')
    input(" Press any key to continue...")
    os.system("clear")
    delete_item()

def delete_fish():
    ID = int(input(" Enter ID: "))
    conn = sqlite3.connect('Item.db')
    cur = conn.cursor()
    sql=f"""DELETE FROM NAME WHERE id='{ID}'; """
    cur.execute(sql)
    conn.commit()
    conn.close()
    print(' Item Deletion Complete')
    input(" Press any key to continue...")
    os.system("clear")
    delete_item()

def delete_number():
    ID = int(input(" Enter ID: "))
    conn = sqlite3.connect('Item.db')
    cur = conn.cursor()
    sql=f"""DELETE FROM NAME WHERE id='{ID}'; """
    cur.execute(sql)
    conn.commit()
    conn.close()
    print(' Item Deletion Complete')
    input(" Press any key to continue...")
    os.system("clear")
    delete_item()

def delete_country():
    ID = int(input(" Enter ID: "))
    conn = sqlite3.connect('Item.db')
    cur = conn.cursor()
    sql=f"""DELETE FROM NAME WHERE id='{ID}'; """
    cur.execute(sql)
    conn.commit()
    conn.close()
    print(' Item Deletion Complete')
    input(" Press any key to continue...")
    os.system("clear")
    delete_item()

def delete_postal():
    ID = int(input(" Enter ID: "))
    conn = sqlite3.connect('Item.db')
    cur = conn.cursor()
    sql=f"""DELETE FROM NAME WHERE id='{ID}'; """
    cur.execute(sql)
    conn.commit()
    conn.close()
    print(' Item Deletion Complete')
    input(" Press any key to continue...")
    os.system("clear")
    delete_item()

#######################################################################################
#######################################################################################

# UPDATE QUERY
def update_name():
    try:
        sqliteConnection = sqlite3.connect('Item.db')
        cursor = sqliteConnection.cursor()
        print(" Connected to SQLite")
        ID = int(input(" Enter ID: "))
        NAME = input(" Enter name: ")
        sql_update_query = f"""UPDATE NAME SET name = '{NAME}' WHERE id = '{ID}'"""
        cursor.execute(sql_update_query)
        sqliteConnection.commit()
        print(" Record Updated successfully ")
        cursor.close()
        input(" Press any key to continue...")
        os.system("clear")
        update_item()

    except sqlite3.Error as error:
        print(" Failed to update sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print(" The SQLite connection is closed")

def update_fish():
    try:
        sqliteConnection = sqlite3.connect('Item.db')
        cursor = sqliteConnection.cursor()
        print(" Connected to SQLite")
        ID = int(input(" Enter ID: "))
        NAME = input(" Enter name: ")
        sql_update_query = f"""UPDATE FISH SET name = '{NAME}' WHERE id = '{ID}'"""
        cursor.execute(sql_update_query)
        sqliteConnection.commit()
        print(" Record Updated successfully ")
        cursor.close()
        input(" Press any key to continue...")
        os.system("clear")
        update_item()

    except sqlite3.Error as error:
        print(" Failed to update sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print(" The SQLite connection is closed")

def update_number():
    try:
        sqliteConnection = sqlite3.connect('Item.db')
        cursor = sqliteConnection.cursor()
        print(" Connected to SQLite")
        ID = int(input(" Enter ID: "))
        NAME = input(" Enter name: ")
        sql_update_query = f"""UPDATE NUMBER SET name = '{NAME}' WHERE id = '{ID}'"""
        cursor.execute(sql_update_query)
        sqliteConnection.commit()
        print(" Record Updated successfully ")
        cursor.close()
        input(" Press any key to continue...")
        os.system("clear")
        update_item()

    except sqlite3.Error as error:
        print(" Failed to update sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print(" The SQLite connection is closed")

def update_country():
    try:
        sqliteConnection = sqlite3.connect('Item.db')
        cursor = sqliteConnection.cursor()
        print(" Connected to SQLite")
        ID = int(input(" Enter ID: "))
        NAME = input(" Enter name: ")
        sql_update_query = f"""UPDATE COUNTRY SET name = '{NAME}' WHERE id = '{ID}'"""
        cursor.execute(sql_update_query)
        sqliteConnection.commit()
        print(" Record Updated successfully ")
        cursor.close()
        input(" Press any key to continue...")
        os.system("clear")
        update_item()        

    except sqlite3.Error as error:
        print(" Failed to update sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print(" The SQLite connection is closed")

def update_postal():
    try:
        sqliteConnection = sqlite3.connect('Item.db')
        cursor = sqliteConnection.cursor()
        print(" Connected to SQLite")
        ID = int(input(" Enter ID: "))
        NAME = input(" Enter name: ")
        sql_update_query = f"""UPDATE NAME SET name = '{NAME}' WHERE id = '{ID}'"""
        cursor.execute(sql_update_query)
        sqliteConnection.commit()
        print(" Record Updated successfully ")
        cursor.close()
        input(" Press any key to continue...")
        os.system("clear")
        update_item()
        
    except sqlite3.Error as error:
        print(" Failed to update sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print(" The SQLite connection is closed")

#######################################################################################
#######################################################################################

# ADD ITEM
def add_item():
    print(bcolors.CYAN + banner + bcolors.ENDC)
    sleep(.1)
    print(bcolors.HEADER + " ───────────────────────────────────────" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.WARNING + "   Please select item category" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.HEADER + " ───────────────────────────────────────" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.CYAN + " [1]. NAME" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.CYAN + " [2]. FISH" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.CYAN + " [3]. NUMBER" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.CYAN + " [4]. COUNTRY" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.CYAN + " [5]. POSTAL" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.CYAN + " [0]. MAIN MENU\n")

    cat = input(" Choose category: ")

    if cat == '1':
        insert_name()
    elif cat == '2':
        insert_fish()
    elif cat == '3':
        insert_number()
    elif cat == '4':
        insert_country()
    elif cat == '5':
        insert_postal()
    elif cat == '0':
        main()
    else:
        print(" Invalid input, try again...")

#######################################################################################
#######################################################################################

# DELETE ITEM
def delete_item():
    print(bcolors.CYAN + banner + bcolors.ENDC)
    sleep(.1)
    print(bcolors.HEADER + " ───────────────────────────────────────" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.WARNING + "   Please select item category" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.HEADER + " ───────────────────────────────────────" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.CYAN + " [1]. NAME" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.CYAN + " [2]. FISH" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.CYAN + " [3]. NUMBER" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.CYAN + " [4]. COUNTRY" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.CYAN + " [5]. POSTAL" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.CYAN + " [0]. MAIN MENU\n")

    cat = input(" Choose category: ")

    if cat == '1':
        delete_name()
    elif cat == '2':
        delete_fish()
    elif cat == '3':
        delete_number()
    elif cat == '4':
        delete_country()
    elif cat == '5':
        delete_postal()
    elif cat == '0':
        main()
    else:
        print(" Invalid input, try again...")

#######################################################################################
#######################################################################################

# UPDATE ITEM
def update_item():
    print(bcolors.CYAN + banner + bcolors.ENDC)
    sleep(.1)
    print(bcolors.HEADER + " ───────────────────────────────────────" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.WARNING + "   Please select item category" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.HEADER + " ───────────────────────────────────────" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.CYAN + " [1]. NAME" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.CYAN + " [2]. FISH" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.CYAN + " [3]. NUMBER" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.CYAN + " [4]. COUNTRY" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.CYAN + " [5]. POSTAL" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.CYAN + " [0]. MAIN MENU\n")

    cat = input(" Choose category: ")

    if cat == '1':
        update_name()
    elif cat == '2':
        update_fish()
    elif cat == '3':
        update_number()
    elif cat == '4':
        update_country()
    elif cat == '5':
        update_postal()
    elif cat == '0':
        main()
    else:
        print(" Invalid input, try again...")

#######################################################################################
#######################################################################################

# SEARCH ITEM
def search_item():
    print(bcolors.CYAN + banner + bcolors.ENDC)
    sleep(.1)
    print(bcolors.HEADER + " ───────────────────────────────────────" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.WARNING + "   Please select item category" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.HEADER + " ───────────────────────────────────────" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.CYAN + " [1]. NAME" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.CYAN + " [2]. FISH" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.CYAN + " [3]. NUMBER" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.CYAN + " [4]. COUNTRY" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.CYAN + " [5]. POSTAL" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.CYAN + " [0]. MAIN MENU\n")

    cat = input(" Choose category: ")

    if cat == '1':
        sqliteConnection = sqlite3.connect('Item.db')
        cursor = sqliteConnection.cursor()
        print(" Connected to SQLite\n")
        ID = int(input(" Enter ID: "))
        sqlite_select_query1=f"""SELECT * FROM NAME WHERE id='{ID}'; """
        cursor.execute(sqlite_select_query1)
        records = cursor.fetchall()
        print(" Search Result: " + str(records))
        input(" Press any key to continue...")
        os.system("clear")
        search_item()
        
    elif cat == '2':
        sqliteConnection = sqlite3.connect('Item.db')
        cursor = sqliteConnection.cursor()
        print(" Connected to SQLite\n")
        ID = int(input(" Enter ID: "))
        sqlite_select_query1=f"""SELECT * FROM FISH WHERE id='{ID}'; """
        cursor.execute(sqlite_select_query1)
        records = cursor.fetchall()
        print(" Search Result: " + str(records))
        input(" Press any key to continue...")
        os.system("clear")
        search_item()
        
    elif cat == '3':
        sqliteConnection = sqlite3.connect('Item.db')
        cursor = sqliteConnection.cursor()
        print(" Connected to SQLite\n")
        ID = int(input(" Enter ID: "))
        sqlite_select_query1=f"""SELECT * FROM NUMBER WHERE id='{ID}'; """
        cursor.execute(sqlite_select_query1)
        records = cursor.fetchall()
        print(" Search Result: " + str(records))
        input(" Press any key to continue...")
        os.system("clear")
        search_item()
        
    elif cat == '4':
        sqliteConnection = sqlite3.connect('Item.db')
        cursor = sqliteConnection.cursor()
        print(" Connected to SQLite\n")
        ID = int(input(" Enter ID: "))
        sqlite_select_query1=f"""SELECT * FROM COUNTRY WHERE id='{ID}'; """
        cursor.execute(sqlite_select_query1)
        records = cursor.fetchall()
        print(" Search Result: " + str(records))
        input(" Press any key to continue...")
        os.system("clear")
        search_item()
        
    elif cat == '5':
        sqliteConnection = sqlite3.connect('Item.db')
        cursor = sqliteConnection.cursor()
        print(" Connected to SQLite\n")
        ID = int(input(" Enter ID: "))
        sqlite_select_query1=f"""SELECT * FROM POSTAL WHERE id='{ID}'; """
        cursor.execute(sqlite_select_query1)
        records = cursor.fetchall()
        print(" Search Result: " + str(records))
        input(" Press any key to continue...")
        os.system("clear")
        search_item()
            
    elif cat == '0':
        main()
    else:
        print(" Invalid input, try again...")

#######################################################################################
#######################################################################################

# VIEW ITEM
def view_item():
    print(bcolors.CYAN + banner + bcolors.ENDC)
    sleep(.1)
    print(bcolors.HEADER + " ───────────────────────────────────────" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.WARNING + "   Please select item category" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.HEADER + " ───────────────────────────────────────" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.CYAN + " [1]. NAME" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.CYAN + " [2]. FISH" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.CYAN + " [3]. NUMBER" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.CYAN + " [4]. COUNTRY" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.CYAN + " [5]. POSTAL" + bcolors.ENDC)
    sleep(.1)
    print(bcolors.CYAN + " [0]. MAIN MENU\n")

    cat = input(" Choose category: ")

    if cat == '1':
        try:
            sqliteConnection = sqlite3.connect('Item.db')
            cursor = sqliteConnection.cursor()
            print(" Connected to SQLite")

            sqlite_select_query1 = """SELECT * from NAME"""
            cursor.execute(sqlite_select_query1)
            records = cursor.fetchall()
            print(" Total rows are:  ", len(records))
            print(" Printing each row")
            for row in records:
                print(" Id: ", row[0])
                print(" Name: ", row[1]) 
                print("\n")
            input(" Press any key to continue...")
            os.system("clear")
            cursor.close()
            view_item()

        except sqlite3.Error as error:
            print(" Failed to read data from sqlite table", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print(" The SQLite connection is closed")

    elif cat == '2':
        try:
            sqliteConnection = sqlite3.connect('Item.db')
            cursor = sqliteConnection.cursor()
            print(" Connected to SQLite")

            sqlite_select_query1 = """SELECT * from FISH"""
            cursor.execute(sqlite_select_query1)
            records = cursor.fetchall()
            print(" Total rows are:  ", len(records))
            print(" Printing each row")
            for row in records:
                print(" Id: ", row[0])
                print(" Name: ", row[1]) 
                print("\n")
            input(" Press any key to continue...")
            os.system("clear")
            cursor.close()
            view_item()

        except sqlite3.Error as error:
            print(" Failed to read data from sqlite table", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print(" The SQLite connection is closed")
            
    elif cat == '3':
        try:
            sqliteConnection = sqlite3.connect('Item.db')
            cursor = sqliteConnection.cursor()
            print(" Connected to SQLite")

            sqlite_select_query1 = """SELECT * from NUMBER"""
            cursor.execute(sqlite_select_query1)
            records = cursor.fetchall()
            print(" Total rows are:  ", len(records))
            print(" Printing each row")
            for row in records:
                print(" Id: ", row[0])
                print(" Name: ", row[1]) 
                print("\n")
            input(" Press any key to continue...")
            os.system("clear")
            cursor.close()
            view_item()

        except sqlite3.Error as error:
            print(" Failed to read data from sqlite table", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print(" The SQLite connection is closed")

    elif cat == '4':
        try:
            sqliteConnection = sqlite3.connect('Item.db')
            cursor = sqliteConnection.cursor()
            print(" Connected to SQLite")

            sqlite_select_query1 = """SELECT * from COUNTRY"""
            cursor.execute(sqlite_select_query1)
            records = cursor.fetchall()
            print(" Total rows are:  ", len(records))
            print(" Printing each row")
            for row in records:
                print(" Id: ", row[0])
                print(" Name: ", row[1]) 
                print("\n")
            input(" Press any key to continue...")
            os.system("clear")
            cursor.close()
            view_item()

        except sqlite3.Error as error:
            print(" Failed to read data from sqlite table", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print(" The SQLite connection is closed")

    elif cat == '5':
        try:
            sqliteConnection = sqlite3.connect('Item.db')
            cursor = sqliteConnection.cursor()
            print(" Connected to SQLite")

            sqlite_select_query1 = """SELECT * from POSTAL"""
            cursor.execute(sqlite_select_query1)
            records = cursor.fetchall()
            print(" Total rows are:  ", len(records))
            print(" Printing each row")
            for row in records:
                print(" Id: ", row[0])
                print(" Name: ", row[1]) 
                print("\n")
            input(" Press any key to continue...")
            os.system("clear")
            cursor.close()
            view_item()

        except sqlite3.Error as error:
            print(" Failed to read data from sqlite table", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print(" The SQLite connection is closed")
            
    elif cat == '0':
        main()
    else:
        print(" Invalid input, try again...")

#######################################################################################
#######################################################################################

# MAIN FUNCTION
def main():
    while True:
        os.system("clear")
        menu()
        choice = input(" Enter your choice: ")
        
        if choice == '1':
            add_item()
        elif choice == '2':
            search_item()
        elif choice == '3':
            delete_item()
        elif choice == '4':
            update_item()
        elif choice == '5':
            view_item()
        elif choice == '6':
            group_members()
        else:
            os.system("clear")
            quit()
            os.system("clear")

#######################################################################################
#######################################################################################

# EXECUTE MAIN FUNCTION
if __name__=='__main__':
    main()

#######################################################################################
#              GROUP MEMBERS : JAYSON, ARSENIUS, MAYNARD, JASPER, NICO                #
#######################################################################################
