

/*Create players table*/

DROP TABLE IF EXISTS `Players`;

CREATE TABLE `Players` (
	`player_id` 	int(11) NOT NULL AUTO_INCREMENT,
	`user_name`     varchar(20) NOT NULL,
	`first_name`	varchar(255) NOT NULL,
	`last_name`		varchar(255),
	`email`			varchar(255),
	`subscribe`		boolean DEFAULT 0,
	PRIMARY KEY (`player_id`),
	UNIQUE KEY (`user_name`)
) ENGINE=InnoDB;

INSERT INTO `Players` VALUES 
	(1, 'jsmith283', 'John','Smith','JSmith@google.com',1),
	(2, 'slyPatcher239', 'Christina','Jones','sly-patch239@protonmail.com',0),
	(3, 'pipster', 'Steven','Hill','shill@google.com',0),
	(4, 'camaro4923', 'Brett','Johnston','camaro4923@msn.com',1),
	(5, 'prankster', 'Amanda','Hugandkiss','prankster@yahoo.com',1)
;

/*Drop and create Proprietors table*/

DROP TABLE IF EXISTS `Proprietors`;

CREATE TABLE `Proprietors`(
	`proprietor_id`		int(11) NOT NULL AUTO_INCREMENT,
	`name` 				varchar(255) NOT NULL,
	`phone_number`	 	varchar(32) NOT NULL,
	`address_street` 	varchar(255) NOT NULL,
	`city` 				varchar(255) NOT NULL,
	`state` 			varchar(255) NOT NULL,
	`zip_code`			varchar(255) NOT NULL,
	`country`			varchar(255) NOT NULL,
	`email`				varchar(255) NOT NULL,
	PRIMARY KEY (`proprietor_id`),
	UNIQUE KEY (`name`)
) ENGINE=InnoDB;

INSERT INTO `Proprietors` VALUES 
	(1, 'Fantasy Flight','1 (855) 382-8880','1975 County Road B2 W','Roseville','MN','55113','USA','help@ffg.com'),
	(2, 'iello','33 3 83 40 63 34','9 Avenue des Erables','Heillecourt','France','54180','France','help@iello.fr')
;

/**/
DROP TABLE IF EXISTS `Games`;

CREATE TABLE `Games` (
	`game_id`	 	int(11) NOT NULL AUTO_INCREMENT,
	`game_title`	varchar(255) NOT NULL,
	`proprietor_id`	int(11) NOT NULL,
	`player_min`	int NOT NULL,
	`player_max`	int NOT NULL,
	`complexity`	decimal(3,2),
	`age_min`		int NOT NULL,
	`duration_min`	int, 
	`duration_max`	int, 
	`style`			varchar(255),
	PRIMARY KEY (`game_id`),
	FOREIGN KEY (`proprietor_id`) REFERENCES `Proprietors`(`proprietor_id`)
) ENGINE=InnoDB;

INSERT INTO `Games` VALUES 
	(1, 'Star Wars: Rebellion', 1, 2, 4, 3.71, 14, 180, 240, 'Thematic'),
	(2, 'A Game of Thrones: Hand of the King', 1, 2, 4, 1.16, 14, 15, 30, 'Family'),
	(3, 'Happy Pigs', 2, 2, 6, 2.32, 8, 30, 45, 'Economic'),
	(4, 'King of New York', 2, 2, 6, 1.87, 10, 40, 40, 'Dice Rolling')
;

/*Create Matches table*/
DROP TABLE IF EXISTS `Matches`;

CREATE TABLE `Matches` (
	`match_id` 		int(11) NOT NULL AUTO_INCREMENT,
	`start_time`	DATETIME NOT NULL,
	`end_time`		DATETIME,
	`game_id`		int NOT NULL,
	PRIMARY KEY (`match_id`),
	FOREIGN KEY (`game_id`) REFERENCES `Games`(`game_id`)
) ENGINE=InnoDB;


/*Create Player_Matches table*/
DROP TABLE IF EXISTS `Player_Matches`;

CREATE TABLE `Player_Matches` (
	`player_id`		int(11) NOT NULL,
	`match_id` 		int(11) NOT NULL,
	`winner`		boolean,
	PRIMARY KEY (`player_id`,`match_id`),
	FOREIGN KEY (`player_id`) REFERENCES `Players`(`player_id`),
	FOREIGN KEY (`match_id`) REFERENCES `Matches`(`match_id`)
) ENGINE=InnoDB;


/*Create Matches table*/
DROP TABLE IF EXISTS `Sessions`;

CREATE TABLE `Sessions` (
	`session_id` 	int(11) NOT NULL AUTO_INCREMENT,
	`player_id`		int NOT NULL,
	`entry_date`	DATETIME NOT NULL,
	`amount`		decimal(7,2) NOT NULL,
	PRIMARY KEY (`session_id`),
	FOREIGN KEY (`player_id`) REFERENCES `Players`(`player_id`)
) ENGINE=InnoDB;