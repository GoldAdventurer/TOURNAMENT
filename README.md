## Tournament Results

This Python module uses a PostgreSQL database to keep track of players and matches in a game tournament.

The game tournament uses the Swiss system for pairing up players in each round: players are not eliminated, and each player is paired with another player with the same number of wins, or as close as possible.

This Udacity project has two parts: defining the database schema (SQL table definitions), and writing the code that will use it.

The number of players in a tournament is an even number. This means that no player will be left out of a round.

### Prerequisite 

#### Use of Vitual Machines
You need to install Vagrant and VirtualBox and then launch the Vagrant VM.

#### Creating the Database

Before you can run your code or create your tables, you'll need to use the `create database tournament` command in psql to create the database. Use the name tournament for your database.

Then you can connect psql to your new database by typing the command psql and create your tables from the statements you've written in tournament.sql. You can do this in either of two ways:

- Paste each statement in to psql.
- Use the command `\i tournament.sql;` to import the whole file into psql at once.

### Description

#### Python Module
The files for this project are in the tournament subdirectory of your VM’s /vagrant directory. There are three files : tournament.sql, tournament.py, and tournament_test.py.

The file tournament.sql contains the database schema, mostly in the form of SQL `create table`, and `create view` commands. The database accommodates multiple tournaments. In order to use the file tournament_test.py, the fiel tournament.sql contains an insert command to create a tournament named 'One' with the the index 1.

The template file tournament.py contains the functions used to query the database. Those functions are in turn used by tournament_test.py.

Finally, the file tournament_test.py was provided by Udacity and contains unit tests that test the functions written in tournament.py. You can run the tests from the command line, using the following command.
```
python tournament_test.py
```

#### Database 

The database contains three tables.

- tournaments : each entry contains an ID (serial) and a name (text). The ID is the primary key.
- players: this table contains all the players names (text) and ID (serial). The ID is the primary key. 
- matches: this table contains five columns.

--Tournaments which references the tournaments ID (foreign key).

--ID which identifies unequivocally the match within a tournament (serial).

--loser which references the ID of the player who loses the games (foreign key).

--winner which references the ID of the player who wins the games (foreign key). 

--draw which could be used if there is a tie. It is a boolean which takes the value "true" if there is a tie.

An additional check is used to ensure that the winner and the loser are different players.

The primary key is the couple (tournament ID, match ID).

The references for the winner and loser columns contain the command `DELETE ON CASCADE` to ensure that if the match is deleted then the player's ID is also deleted. 

There are three views which are used to determine the players' standings:
- nb_wins to determine each player's wins,
- nb_matches to determine each player's total number of matches,
- wins_matches which joins the previous two views, and
- players_standings which gathers each player's ID, name, wins and total number of matches.

### How to run the code

#### Create the Database

You need to install Vagrant and VirtualBox and then launch the Vagrant VM.

Then you can use the following commands to create the database

- Create the database
```
CREATE DATABASE Tournament;
```

- Connect to the database
```
\c Tournament;
```

- Create the tables, and views
```
\i tournament.sql;
```

- Check that all three tables were created. This step is optional.
```
\d;
```

You can view the details of each table by using the command /d following by the table name. For example, you should type \d players; to check the table players.

#### Run the code

You can use the following command to test the database and the python functions written in the file tournament.py
```
python tournament_test.py
```

**Author**

C. D. wrote the code for the functions in tournament.py.

**License**

The files are private domain works.

