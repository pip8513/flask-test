# -- counting wins/losses
# select p.player_id, p.first_name, p.last_name, COUNT(pm.match_id) as games_played,
# 	case when sum(pm.winner) is NULL THEN 0
#     ELSE sum(pm.winner) end as wins
# from Players p
# LEFT JOIN Player_Matches pm on p.player_id = pm.player_id
# GROUP BY p.player_id, p.first_name, p.last_name
# order by wins
# ;

from datetime import datetime


def format_mysql_time(tm_stamp: datetime):
    """used to convert datetime form to MySQL formatted datetime without surrounding '' marks. """
    return tm_stamp.strftime("'%Y-%m-%d %H:%M:%S'")


# Modifying players table
def players_insert(user_name: str, first_name: str, last_name: str, email: str, subscribe: bool):
    """Adds players to database"""
    # convert boolean to tinyint (0 or 1)
    if subscribe:
        subscribe = 1
    else:
        subscribe = 0

    query = f"""
    INSERT INTO Players 
        (`user_name`, `first_name`, `last_name`, `email`, `subscribe`)
    VALUES 
        ('{user_name}', '{first_name}', '{last_name}', '{email}', {subscribe});
    """
    return query


def players_update(user_name_current, user_name_new, first_name, last_name, email, subscribe: bool):
    """update a player entity data"""

    # convert boolean to tinyint (0 or 1)
    if subscribe:
        subscribe = 1
    else:
        subscribe = 0

    query = f"""
    UPDATE Players
    SET
        user_name = '{user_name_new}',
        first_name = '{first_name}',
        last_name = '{last_name}',
        email = '{email}',
        subscribe = {subscribe}
    WHERE
        player_id = (SELECT player_id from Players WHERE user_name = '{user_name_current}');
    """
    return query


def players_delete(user_name: str):
    """Deletes player player database"""
    query = f"""
    DELETE FROM Players 
    WHERE player_id = (SELECT player_id from Players WHERE user_name = '{user_name}');
    """
    return query


###############################################################################################
###############################################################################################
# Modifying proprietors table


def proprietors_insert(name: str, phone_number: str, address_street: str, city: str, state: str, zip_code: str,
                       country: str, email: str):
    """Adds players to database"""
    query = f"""
    INSERT INTO Proprietors 
        (`name`, `phone_number`, `address_street`, `city`, `state`, `zip_code`, `country`, `email`)
    VALUES 
        ('{name}', '{phone_number}', '{address_street}', '{city}', '{state}', '{zip_code}', '{country}', '{email}');
    """
    return query


def proprietors_update(name_current, name_new, phone_number, address_street, city, state, zip_code, country, email):
    """update a player entity data"""
    query = f"""
    UPDATE Proprietors
    SET
        name = '{name_new}',
        phone_number = '{phone_number}',
        address_street = '{address_street}',
        city = '{city}',
        state = '{state}',
        zip_code = '{zip_code}',
        country = '{country}',
        email = '{email}'
    WHERE
        proprietor_id = (SELECT proprietor_id from Proprietors WHERE name = '{name_current}');
    """
    return query


def proprietors_delete(name: str):
    """Deletes player from database"""
    query = f"""
    DELETE FROM Proprietors 
    WHERE proprietor_id = (SELECT proprietor_id from Proprietors WHERE name = '{name}');
    """
    return query


###############################################################################################
###############################################################################################
# Modifying Games table

def games_insert(game_title, proprietor_name, player_min, player_max, complexity, age_min, duration_min, duration_max,
                 style):
    """Adds game to database"""
    query = f"""
    INSERT INTO Games 
        (`game_title`, `proprietor_id`, `player_min`, `player_max`, `complexity`, `age_min`, 
        `duration_min`, `duration_max`, `style`)
    VALUES 
        ('{game_title}', (SELECT proprietor_id FROM Proprietors WHERE name = '{proprietor_name}'), {player_min}, 
        {player_max}, {complexity}, {age_min}, {duration_min}, {duration_max}, '{style}');
    """
    return query


def games_update(game_id, game_title, proprietor_name, player_min, player_max, complexity, age_min, duration_min,
                 duration_max, style):
    """update a games entity data"""
    query = f"""
    UPDATE Games
    SET
        game_title = '{game_title}',
        proprietor_id = (SELECT proprietor_id FROM Proprietors WHERE name = '{proprietor_name}'), 
        player_min = {player_min}, 
        player_max = {player_max}, 
        complexity = {complexity}, 
        age_min = {age_min}, 
        duration_min = {duration_min}, 
        duration_max = {duration_max}, 
        style = '{style}'
    WHERE
        game_id = {game_id};
    """
    return query


def games_delete(game_id: int):
    """Deletes game database"""
    query = f"""
    DELETE FROM Games 
    WHERE game_id = {game_id};
    """
    return query


###############################################################################################
###############################################################################################
# Modifying Sessions table

def sessions_insert(user_name: str, entry_date: datetime, amount: float):
    """Adds session to database"""
    entry_date = format_mysql_time(entry_date)
    query = f"""
    INSERT INTO Sessions
        (`player_id`, `entry_date`, `amount`)
    VALUES 
        ((SELECT player_id FROM Players WHERE user_name = '{user_name}'), {entry_date}, {amount});
    """
    return query


def sessions_update(session_id: int, user_name: str, entry_date: datetime, amount: float):
    """update a session entity data"""
    entry_date = format_mysql_time(entry_date)
    query = f"""
    UPDATE Sessions
    SET
        player_id = (SELECT player_id FROM Players WHERE user_name = '{user_name}'),
        entry_date = {entry_date}, 
        amount = {amount}
    WHERE
        session_id = {session_id};
    """
    return query


def sessions_delete(session_id: int):
    """Deletes session from database"""
    query = f"""
    DELETE FROM Sessions 
    WHERE session_id = {session_id};
    """
    return query


###############################################################################################
###############################################################################################
# Modifying Matches table

def matches_insert(start_time: datetime, game_id, end_time: datetime = None):
    """Adds session to database"""

    # format start/end time
    start_time = format_mysql_time(start_time)
    if end_time:
        end_time = format_mysql_time(end_time)
    else:
        end_time = 'NULL'

    query = f"""
    INSERT INTO Matches
        (`start_time`, `end_time`, `game_id`)
    VALUES 
        ({start_time}, {end_time}, {game_id});
    """
    return query


def matches_update(match_id, start_time: datetime, game_id, end_time: datetime = None):
    """update a session entity data"""

    # format start/end time
    start_time = format_mysql_time(start_time)
    if end_time:
        end_time = format_mysql_time(end_time)
    else:
        end_time = 'NULL'

    query = f"""
    UPDATE Matches
    SET
        start_time = {start_time},
        end_time = {end_time}, 
        game_id = {game_id}
    WHERE
        match_id = {match_id};
    """
    return query


def matches_delete(match_id: int):
    """Deletes session from database"""
    query = f"""
    DELETE FROM Matches 
    WHERE match_id = {match_id};
    """
    return query


###############################################################################################
###############################################################################################
# Modifying Player_Matches table

def player_matches_insert(user_name, match_id, winner: bool = None):
    """Adds session to database"""
    if winner is None:
        winner = "NULL"
    elif winner:
        winner = 1
    else:
        winner = 0

    query = f"""
    INSERT INTO Player_Matches
        (`player_id`, `match_id`, `winner`)
    VALUES 
        ((SELECT player_id FROM Players WHERE user_name = '{user_name}'), {match_id}, {winner});
    """
    return query


def player_matches_update(user_name, match_id, winner: bool = None):
    """update a session entity data"""

    if winner is None:
        winner = "NULL"
    elif winner:
        winner = 1
    else:
        winner = 0

    query = f"""
    UPDATE Player_Matches
    SET
        player_id = (SELECT player_id FROM Players WHERE user_name = '{user_name}'),
        match_id = {match_id}, 
        winner = {winner}
    WHERE
        match_id = {match_id}
        AND player_id = (SELECT player_id FROM Players WHERE user_name = '{user_name}');
    """
    return query


def player_matches_delete(user_name: str, match_id: int):
    """Deletes session from database"""
    query = f"""
    DELETE FROM Player_Matches 
    WHERE match_id = {match_id}
    AND player_id = (SELECT player_id FROM Players WHERE user_name = '{user_name}');
    """
    return query


if __name__ == "__main__":

    test_list = [
        ['players_insert',
         players_insert('pip8513', 'Phil', 'Hunter', 'test@gmail', False)],
        ['players_update',
         players_update('pip8513', 'pip1234', 'Phils', 'Huntes', 'test2@gail.com', True)],
        ['players_delete',
         players_delete('pip1234')],

        ['proprietors_insert',
         proprietors_insert('ZMAN Games', '123-555-1985', '123 Main Street', 'Portland', 'OR', '98681', 'USA',
                            'ZMAN@zman.com')],
        ['proprietors_update',
         proprietors_update('ZMAN Games', 'ZMAN', '123-555-1985', '123 Main Street', 'Portland', 'OR', '98681', 'USA',
                            'ZMAN@zman.com')],
        ['proprietors_delete',
         proprietors_delete('ZMAN')],

        ['games_insert',
         games_insert('King of Tokyo', 'iello', 2, 6, 1.56, 10, 30, 45, 'Dice Rolling')],
        ['games_update',
         games_update(5, 'King of Tokyo', 'iello', 2, 6, 1.56, 10, 30, 45, 'Dice Rolling')],
        ['games_delete',
         games_delete(5)],

        ['sessions_insert',
         sessions_insert('jsmith283', datetime.now(), 4.99)],
        ['sessions_update',
         sessions_update(1, 'slyPatcher239', datetime.now(), 2.99)],
        ['sessions_delete',
         sessions_delete(1)],

        ['matches_insert',
        matches_insert(datetime.now(), 1)],
        ['matches_update',
         matches_update(1, datetime.now(), 2, datetime.now())],
        ['player_matches_insert',
         player_matches_insert('jsmith283', 1)],
        ['player_matches_insert',
         player_matches_insert('slyPatcher239', 1)],
        ['player_matches_update',
         player_matches_update('jsmith283', 1, True)],
        ['player_matches_update',
         player_matches_update('slyPatcher239', 1, False)],
        ['player_matches_delete',
         player_matches_delete('jsmith283', 1)],
        ['player_matches_delete',
         player_matches_delete('slyPatcher239', 1)],
        ['matches_delete',
         matches_delete(1)]

    ]

    for test in test_list:
        print(f"""-- ##### Test {test[0]} query. #####{test[1]}\n""")

    # print(players_insert('philip', 'hunter', 'richards', 'test@gmail', False))

