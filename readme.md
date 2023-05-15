# Overview

This program was delevoped to test and demonstrate a basic database. Using this project I have learned about databases, sqlite and how to integrate it with python and get peculiarities to function properly.

This software is a basic scheduling program and database. It provides you function using the console to interact with a program that sends sql commands to a database holding scheduling events depending on what the user inputs as a command. When the user starts the program they are prompted on whether to create a new schedule or not. After this check, they are entered into the core of the program which is a looping command that gives them the ability to use 6 preregistered commands to interact with the database. The user has the ability to search the database, edit entries, add entries, remove entries, list all entries, and get a day by day event overview. parameters of these commands is further changed by user input giving the user the ability to edit the database's information as they wish. When the program ends, it will input all events that are registered for the current day and the following day. The database and the information in it can be recalled in future sessions for further interaction. 

[Software Demo Video](https://youtu.be/000bUKYt6lo)

# Relational Database

This program uses the sqlite relational database.

The database contained within has a single table containing 3 columns: Date, Time and event, and is interacted with using python code and sqlite3 commands.


# Development Environment

This program was developed using visual studio code.

It is developed in the python programming language and utilizes the sqlite3 and datetime libraries.

# Useful Websites

- [sqlite3 — DB-API 2.0 interface for SQLite databases](https://docs.python.org/3.8/library/sqlite3.html)
- [SQLite - Python](https://www.tutorialspoint.com/sqlite/sqlite_python.htm)
- [datetime — Basic date and time types](https://docs.python.org/3/library/datetime.html)
- [SQLite BETWEEN](https://www.sqlitetutorial.net/sqlite-between/)

# Future Work

- improve implementation and entry of date and time to be more precise and uniform
- include between time search