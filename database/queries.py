# -- counting wins/losses
# select p.player_id, p.first_name, p.last_name, COUNT(pm.match_id) as games_played, 
# 	case when sum(pm.winner) is NULL THEN 0
#     ELSE sum(pm.winner) end as wins
# from Players p
# LEFT JOIN Player_Matches pm on p.player_id = pm.player_id
# GROUP BY p.player_id, p.first_name, p.last_name
# order by wins
# ;


# Modifying players table
def players_insert(user_name: str, first_name: str, last_name: str, email: str, subscribe: bool):
    """Adds players to database"""
    query = f"""
    INSERT INTO Players (`user_name`, `first_name`, `last_name`, `email`, `subscribe`)
    VALUES ('{user_name}', '{first_name}', '{last_name}', '{email}', {subscribe})
    """
    return query


def players_delete(player_id: int):
    """Deletes player player database"""
    query = f"""
    DELETE FROM Players 
    WHERE player_id = {player_id}'
    """
    return query


###############################################################################################
###############################################################################################


# Modifying proprietors table
def proprietors_insert(name: str, phone_number: str, address_street: str, city: str, state: str, zip_code: str,
                       country: str, email: str):
    """Adds players to database"""
    query = f"""
    INSERT INTO proprietors (`name`, `first_name`, `last_name`, `email`, `subscribe`)
    VALUES ('{name}', '{phone_number}', '{last_name}', '{email}', {subscribe})
    """
    return query


def proprietors_delete(proprietor_id: int):
    """Deletes player player database"""
    query = f"""
    DELETE FROM Players 
    WHERE player_id = {player_id}'
    """
    return query


print(players_insert('philip', 'hunter', 'richards', 'test@gmail', False))
