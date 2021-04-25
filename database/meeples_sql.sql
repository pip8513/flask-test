

------- Modifying players table

-- Adding new players
INSERT INTO Players 
	(`user_name`, `first_name`, `last_name`, `email`, `subscribe`)
VALUES 
	(:uname, :fname, :lname, :email, :subscribe)
;

UPDATE


-- counting wins/losses
select p.player_id, p.first_name, p.last_name, COUNT(pm.match_id) as games_played, 
	case when sum(pm.winner) is NULL THEN 0
    ELSE sum(pm.winner) end as wins
from Players p
LEFT JOIN Player_Matches pm on p.player_id = pm.player_id
GROUP BY p.player_id, p.first_name, p.last_name
order by wins
;

