CREATE TABLE ITEMS (`id` MEDIUMINT UNSIGNED NOT NULL,
		    `classid` TINYINT UNSIGNED NOT NULL,
		    `subclassid` TINYINT UNSIGNED NOT NULL,
		    `name` varchar(100),
		    `description` bool,
		    `level` MEDIUMINT UNSIGNED NOT NULL,
		    `picture` MEDIUMINT UNSIGNED,
		    `quality` TINYINT UNSIGNED NOT NULL,
		    PRIMARY KEY (id));

CREATE TABLE ITEMCLASS (`id` TINYINT UNSIGNED NOT NULL,
			`name` varchar(30),
			PRIMARY KEY(id));

CREATE TABLE ITEMSUBCLASS (`idClass` TINYINT UNSIGNED NOT NULL,
			   `idSubClass` TINYINT UNSIGNED NOT NULL,
			   `name` varchar(30),
			   `completeName` varchar(30),
			   PRIMARY KEY(idClass,idSubClass));

CREATE TABLE ITEMSPICTURES (`id` MEDIUMINT UNSIGNED NOT NULL,
			    `name` varchar(100) ,
			    PRIMARY KEY(id,name));

CREATE TABLE ITEMSDESCRIPTIONS (`id` MEDIUMINT UNSIGNED NOT NULL,
				`description` varchar(100) ,
				PRIMARY KEY(id,description));

CREATE TABLE BONUSSTATS (`id` TINYINT UNSIGNED NOT NULL,
			 `description` varchar(50),
			 PRIMARY KEY(id));

CREATE TABLE ITEMSTAT (`id` MEDIUMINT UNSIGNED NOT NULL,
		       `stat` TINYINT UNSIGNED NOT NULL,
		       `amount` TINYINT UNSIGNED NOT NULL,
		       PRIMARY KEY(id,stat,amount));

CREATE TABLE PLAYERS (`name` varchar(50),
		      `server` varchar(50),
		      `genderId` TINYINT UNSIGNED,
		      `factionId` TINYINT UNSIGNED,
		      `raceId` TINYINT,
		      `level` TINYINT UNSIGNED,
		      `thumbnail` varchar(100),
		      `backId` MEDIUMINT,
		      `chestId` MEDIUMINT UNSIGNED,
		      `feetId` MEDIUMINT UNSIGNED,
		      `finger1Id` MEDIUMINT UNSIGNED,
		      `finger2Id` MEDIUMINT UNSIGNED,
		      `handsId` MEDIUMINT UNSIGNED,
		      `legsId` MEDIUMINT UNSIGNED,
		      `mainHandId` MEDIUMINT UNSIGNED,
		      `neckId` MEDIUMINT UNSIGNED,
		      `shoulderId` MEDIUMINT UNSIGNED,
		      `trinket1Id` MEDIUMINT UNSIGNED,
		      `trinket2Id` MEDIUMINT UNSIGNED,
		      `waistId` MEDIUMINT UNSIGNED,
		      `wristId` MEDIUMINT UNSIGNED,
		      PRIMARY KEY(name, server));

CREATE TABLE WEAPON (`id` MEDIUMINT UNSIGNED NOT NULL,
		     `requiredLevel` TINYINT UNSIGNED NOT NULL,
		     `damageMax` SMALLINT UNSIGNED,
		     `damageMin` SMALLINT UNSIGNED,
		     `dps` DECIMAL(8,3),
		     `weaponSpeed` DECIMAL(5,3),
		     `maxDurability` TINYINT UNSIGNED,
		     PRIMARY KEY(id));

