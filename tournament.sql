
-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


-- INITIALIZATION OF AND CONNECTION TO DATABASE

DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament


-- THE TABLE PLAYERS CONTAINS ALL PLAYERS NAME AND IDs
CREATE TABLE players (
    ID serial PRIMARY KEY,
    name text);


-- The table TOURNAMENTS can be used to create many tournaments at the same time
-- In order to use the file tournament_test.py, the table is initialized by adding
--  the following index and name: 1, "one".
-- I also added a function deleteTournaments() in tournament.py to delete the table 

CREATE TABLE tournaments (
	ID serial PRIMARY KEY,
	name text);


-- THE TABLE MATCHES CONTAINS THE TOURNAMENT NUMBER, THE MATCH ID, \
-- AND THE RESULT OF THE MATCH (EITHER ONE WINS AND ONE LOSES OR \
-- THERE IS A TIE (CAPTURED BY VARIABLE draw).

CREATE TABLE matches (
	tournament integer,
	ID serial,
	loser integer,
	winner integer,
	draw boolean,
	CHECK (winner != loser),
	FOREIGN KEY (tournament) REFERENCES tournaments(ID),
	FOREIGN KEY (loser) REFERENCES players(ID) ON DELETE CASCADE,
	FOREIGN KEY (winner) REFERENCES players(ID) ON DELETE CASCADE,
	PRIMARY KEY (tournament, ID)
	);

-- INITIALIZATION OF THE TOURNAMENTS TABLES FOR THIS EXERCISE

INSERT INTO TOURNAMENTS(ID, name) VALUES(1, 'One');


-- VIEW TO DETERMINE WINS

CREATE VIEW nb_wins AS
    SELECT players.id, count(matches.winner) AS wins
    FROM players LEFT JOIN matches 
    ON players.ID = matches.winner
    GROUP by players.id
    ORDER by players.id;


-- VIEW TO DETERMINE THE NUMBER OF MATCHES

CREATE VIEW nb_matches AS
	SELECT players.id, count(matches.winner) AS matches
	FROM players LEFT JOIN matches
	ON players.ID = matches.winner
	OR players.ID = matches.loser
	GROUP BY players.id
	ORDER by players.id;


-- VIEW THAT ADDS THE NUMBER OF WINS AND THE NUMBER OF MATCHES 
-- IN ONE TABLE

CREATE VIEW wins_matches AS
	SELECT nb_matches.ID, nb_wins.wins, nb_matches.matches
	FROM nb_wins LEFT JOIN nb_matches
	ON nb_wins.ID = nb_matches.ID;


-- VIEW USED TO DETERMINE PLAYERS' STANDINGS

CREATE VIEW players_standings AS 
	SELECT players.id, players.name, wins_matches.wins, wins_matches.matches
	FROM players LEFT JOIN wins_matches
	on players.ID = wins_matches.ID;




