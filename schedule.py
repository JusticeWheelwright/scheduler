import sqlite3
from datetime import datetime, timedelta, date
#class which edits a database file holding time and event entries
class scheduler:
    #initializes with a connection to the database file and a cursor object to execute commands
    def __init__(self):
        self.con = sqlite3.connect('calendar.db')
        self.cur = self.con.cursor()

    #creates a new table
    def new(self):
        self.cur.execute('''CREATE TABLE schedule
               (date text, time text, event text)''')
    
    #deletes the table if it exists
    def delete_table(self):
        self.cur.execute("DROP TABLE IF EXISTS schedule")

    #adds an event to the database using date, time and event values which are passed in, dates should be in the format yyyy-mm-dd
    def add_event(self, date, time, event):
        self.cur.execute("INSERT INTO schedule VALUES (?,?,?)", (date, time, event))

    #removes an event specified by the row id passed in
    def remove_event(self, id):
        self.cur.execute("DELETE FROM schedule WHERE rowid =?", (id,))

    #prints all entries
    def get_all(self):
        for row in self.cur.execute("SELECT rowid, * FROM schedule"):
                print(row)

    #edits a single data point of a single entry that is passed in
    def edit(self, item, value, id):
        self.cur.execute("UPDATE schedule SET "+item+"=? WHERE rowid =?", (value, id,))

    #prints the prints the searched entries according to the values passed into the function
    def get_event(self, item, value, item2 = "", value2 = ""):
        if item2 == "" and value2 == "":
            for row in self.cur.execute("SELECT rowid, * FROM schedule WHERE "+item+"=?", (value,)):
                print(row)
        else:
            for row in self.cur.execute("SELECT rowid, * FROM schedule WHERE "+item+"=? AND "+item2+"=?", (value, value2,)):
                print(row)

    #prints the total number of entries for each day
    def count_days(self):
        for row in self.cur.execute("SELECT date, COUNT(rowid) FROM schedule GROUP BY date"):
                print(row)

    #saves changes to the database file
    def save(self):
        self.con.commit()

    #prints all events for the current day and the next one
    def today(self):
        today = datetime.now()
        tomorrow = today + timedelta(1)
        print("In the next two days you still have to do: ")
        for row in self.cur.execute("SELECT rowid, * FROM schedule WHERE date BETWEEN ? AND ?", (today.strftime("%Y-%m-%d"),tomorrow.strftime("%Y-%m-%d"))):
            print(row)

    #closes the file access
    def finish(self):
        self.con.close()

#constructs an instance of the scheduler class which interacts with the database
calendar = scheduler()
cont = True

#constructs new table and deletes old one
new = input("delete old table and create fresh table (y/n)?")
if new == "y":
    calendar.delete_table()
    calendar.new()

#loop to keep interacting with the database
while cont == True:
    #gets a command from the user (add, remove, edit, search, list, days)
    action = input("Would you like to add an entry(add)?\nWould you like to remove an entry(remove)?\nWould you like to edit an entry(edit)?\nWould you like to search entries(search)?\nWould you like to list all entries(list)?\nWould you like to see how many events you have scheduled for each day(days)?")
    
    #adds an entry to the database
    if action == "add":
        date = input("what date will this event take place? (yyyy-mm-dd)") #date should be in the format yyyy-mm-dd to properly interact with the program
        time = input("what time will it happen?")
        event = input("what is the event?")
        calendar.add_event(date,time,event)

    #removes an entry from the calendar
    elif action == "remove":
        calendar.get_all()
        id = int(input("What row would you like to remove?"))
        calendar.remove_event(id)

    #edits an entry in the calendar
    elif action == "edit":
        calendar.get_all()
        id = int(input("What row would you like to edit?"))
        item = input("What item would you like to change (date, time, event)?")
        value = input("What would you like to replace it with?")
        calendar.edit(item, value, id)

    #searches the database for the user's specified conditions
    elif action == "search":
        search = input("what would you like to search by (date, time, event)?")
        while search != "date" or search != "time" or search != "event":
            search = input("that is not a proper input. What would you like to search by (date, time, event)?")
        value = input("What value would you like to search for?")
        search2 = input("Would you like to search by (date, time, event) or not (n)?")
        while search != "date" or search != "time" or search != "event" or search != "n":
            search = input("that is not a proper input. Would you like to search by (date, time, event) or not (n)?")
        value2 = ""
        if search2 != "n":
            value2 = input("What value would you like to search for?")
        else:
            search2 = ""
            value2 = ""
        calendar.get_event(search, value, search2, value2)

    #lists all the events
    elif action == "list":
        calendar.get_all()

    #counts the number of events for each day
    elif action == "days":
        calendar.count_days()

    #informs the user that they did not use a proper input
    else: 
        print("That is not one of the commands.")

    #save to the database
    calendar.save()

    #input to continue loop or not
    action = input("Would you like to do anything else (y/n)?")
    if action == "n":
        cont = False

calendar.today()
calendar.finish()
