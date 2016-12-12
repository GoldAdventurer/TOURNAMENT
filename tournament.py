#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#
# import forumdb
import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    c = connect()
    cursor = c.cursor()
    cursor.execute('DELETE FROM matches')
    c.commit()
    c.close()


def deletePlayers():
    """Remove all the player records from the database."""
    c = connect()
    cursor = c.cursor()
    cursor.execute('DELETE FROM players')
    c.commit()
    c.close()    


# added the function to deal with multiple tournaments
def deleteTournaments():
    c = connect()
    cursor = c.cursor()
    cursor.execute('DELETE FROM tournaments')
    c.commit()
    c.close()


def countPlayers():
    """Returns the number of players currently registered."""
    c = connect()
    cursor = c.cursor()
    cursor.execute('SELECT COUNT(*) AS num FROM players')
    row = cursor.fetchall()
    num = row[0][0]
    c.close()
    return num


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    c = connect()
    cursor = c.cursor()
    cursor.execute('INSERT INTO players(name) VALUES(%s)', (name,))
    c.commit()
    c.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a 
    player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    c = connect()
    cursor = c.cursor()
    cursor.execute('SELECT ID, name, wins, matches from players_standings\
        ORDER by wins, matches, name, ID')
    result = [(row[0], row[1], row[2], row[3]) for row in cursor.fetchall()]
    c.close()
    return result
       

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    c = connect()
    cursor = c.cursor()
    cursor.execute('INSERT INTO matches(tournament, Loser, Winner, draw)\
                   VALUES(%s, %s, %s, %s)', (1, loser, winner, 'false'))
    c.commit()
    c.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    players = playerStandings()
    result = []
    for i in range(0, len(players), 2):
        pair = []
        pair.extend(players[i][0:2])
        pair.extend(players[i+1][0:2])
        result.append(pair)
    return result