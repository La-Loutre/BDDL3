CREATE TABLE ITEMS (`id` MEDIUMINT UNSIGNED NOT NULL,
		    `classid` TINYINT UNSIGNED NOT NULL,
		    `subclassid` TINYINT UNSIGNED NOT NULL,
		    `name` varchar(100),
		    `description` bool,
		    `level` TINYINT UNSIGNED NOT NULL,
		    PRIMARY KEY (id),
		    `picture` MEDIUMINT UNSIGNED);
CREATE TABLE ITEMSPICTURES (`id` MEDIUMINT UNSIGNED NOT NULL,
			    `name` varchar(100) ,
			    PRIMARY KEY(id,name));
CREATE TABLE ITEMSDESCRIPTIONS (`id` MEDIUMINT UNSIGNED NOT NULL,
				`description` varchar(100) ,
				PRIMARY KEY(id,description));



