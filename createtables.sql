-- phpMyAdmin SQL Dump
-- version 3.1.2deb1ubuntu0.2
-- http://www.phpmyadmin.net
--
-- Serveur: localhost
-- Généré le : Jeu 23 Avril 2015 à 13:41
-- Version du serveur: 5.0.75
-- Version de PHP: 5.2.6-3ubuntu4.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de données: `alnieto`
--

-- --------------------------------------------------------

--
-- Structure de la table `BONUSSTATS`
--

CREATE TABLE IF NOT EXISTS `BONUSSTATS` (
  `id` tinyint(3) unsigned NOT NULL,
  `description` varchar(50) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `BONUSSTATS`
--

INSERT INTO `BONUSSTATS` (`id`, `description`) VALUES
(0, '?????????'),
(1, 'Health'),
(2, 'Mana'),
(3, 'Agility'),
(4, 'Strength'),
(5, 'Intellect'),
(6, 'Spirit'),
(7, 'Stamina'),
(8, '?????????'),
(9, '?????????'),
(10, '?????????'),
(11, '?????????'),
(12, 'Defense'),
(13, 'Dodge'),
(14, 'Parry'),
(15, 'Block rating'),
(16, 'Melee hit'),
(17, 'Ranged hit'),
(18, 'Spell hit'),
(19, 'Melee crit'),
(20, 'Range Crit'),
(21, 'Spell crit'),
(22, 'Melee avoid'),
(23, 'Ranged avoid'),
(24, 'Spell avoid'),
(25, 'M crit avoid'),
(26, 'R crit avoid'),
(27, 'S crit avoid'),
(28, 'Melee haste'),
(29, 'Ranged haste'),
(30, 'Spell haste'),
(31, 'Hit'),
(32, 'Crit'),
(33, 'Hit avoid'),
(34, 'Crit avoid'),
(35, 'Resil'),
(36, 'Haste'),
(37, 'Expertise'),
(38, 'Attack Power'),
(39, 'Ranged AP'),
(40, 'Feral AP'),
(41, 'Increase dmg'),
(42, 'Increase heal'),
(43, 'Mp5'),
(44, 'ArP'),
(45, 'Spell Power'),
(46, 'Health Regen'),
(47, 'Spell pen'),
(48, 'Block Value'),
(49, 'Mastery'),
(50, 'Armor'),
(51, 'Fire Resist'),
(52, 'Frost Resist'),
(54, 'Shadow Resist'),
(55, 'Nature Resist'),
(56, 'Arcane Resist'),
(57, 'Pvp Power');

-- --------------------------------------------------------

--
-- Structure de la table `CLASSES`
--

CREATE TABLE IF NOT EXISTS `CLASSES` (
  `id` tinyint(3) unsigned NOT NULL,
  `powerType` tinyint(3) unsigned NOT NULL,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `powerType` (`powerType`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `CLASSES`
--

INSERT INTO `CLASSES` (`id`, `powerType`, `name`) VALUES
(1, 1, 'Guerrier'),
(2, 0, 'Paladin'),
(3, 2, 'Chasseur'),
(4, 3, 'Voleur'),
(5, 0, 'Prêtre'),
(6, 6, 'Chevalier de la mort'),
(7, 0, 'Chaman'),
(8, 0, 'Mage'),
(9, 0, 'Démoniste'),
(10, 3, 'Moine'),
(11, 0, 'Druide');

-- --------------------------------------------------------

--
-- Structure de la table `FACTION`
--

CREATE TABLE IF NOT EXISTS `FACTION` (
  `id` tinyint(3) unsigned NOT NULL,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `FACTION`
--

INSERT INTO `FACTION` (`id`, `name`) VALUES
(0, 'alliance'),
(1, 'horde'),
(2, 'neutral');

-- --------------------------------------------------------

--
-- Structure de la table `FRIENDS`
--

CREATE TABLE IF NOT EXISTS `FRIENDS` (
  `idPlayer` int(10) unsigned NOT NULL,
  `idFriend` int(10) unsigned NOT NULL,
  PRIMARY KEY  (`idPlayer`,`idFriend`),
  KEY `idFriend` (`idFriend`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `FRIENDS`
--


-- --------------------------------------------------------

--
-- Structure de la table `ITEMCLASS`
--

CREATE TABLE IF NOT EXISTS `ITEMCLASS` (
  `id` tinyint(3) unsigned NOT NULL,
  `name` varchar(30) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `ITEMCLASS`
--

INSERT INTO `ITEMCLASS` (`id`, `name`) VALUES
(0, 'Consumable'),
(1, 'Container'),
(2, 'Weapon'),
(3, 'Gem'),
(4, 'Armor'),
(5, 'Reagent'),
(6, 'Projectile'),
(7, 'Trade Goods'),
(8, 'Generic'),
(9, 'Book'),
(10, 'Money'),
(11, 'Quiver'),
(12, 'Quest'),
(13, 'Key'),
(14, 'Permanent'),
(15, 'Junk'),
(16, 'Glyph');

-- --------------------------------------------------------

--
-- Structure de la table `ITEMS`
--

CREATE TABLE IF NOT EXISTS `ITEMS` (
  `id` mediumint(8) unsigned NOT NULL,
  `classid` tinyint(3) unsigned NOT NULL,
  `subclassid` tinyint(3) unsigned NOT NULL,
  `name` varchar(100) default NULL,
  `description` mediumint(8) unsigned NOT NULL default '0',
  `level` mediumint(8) unsigned NOT NULL,
  `picture` mediumint(8) unsigned default NULL,
  `quality` tinyint(3) unsigned NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `classid` (`classid`),
  KEY `subclassid` (`subclassid`),
  KEY `picture` (`picture`),
  KEY `description` (`description`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `ITEMS`
--


-- --------------------------------------------------------

--
-- Structure de la table `ITEMSDESCRIPTIONS`
--

CREATE TABLE IF NOT EXISTS `ITEMSDESCRIPTIONS` (
  `id` mediumint(8) unsigned NOT NULL auto_increment,
  `description` varchar(200) NOT NULL default '',
  PRIMARY KEY  (`id`,`description`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Contenu de la table `ITEMSDESCRIPTIONS`
--


-- --------------------------------------------------------

--
-- Structure de la table `ITEMSPICTURES`
--

CREATE TABLE IF NOT EXISTS `ITEMSPICTURES` (
  `id` mediumint(8) unsigned NOT NULL auto_increment,
  `name` varchar(100) NOT NULL default '',
  PRIMARY KEY  (`id`,`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Contenu de la table `ITEMSPICTURES`
--


-- --------------------------------------------------------

--
-- Structure de la table `ITEMSTAT`
--

CREATE TABLE IF NOT EXISTS `ITEMSTAT` (
  `id` mediumint(8) unsigned NOT NULL,
  `stat` tinyint(3) unsigned NOT NULL,
  `amount` mediumint(8) unsigned NOT NULL,
  PRIMARY KEY  (`id`,`stat`,`amount`),
  KEY `stat` (`stat`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `ITEMSTAT`
--


-- --------------------------------------------------------

--
-- Structure de la table `ITEMSUBCLASS`
--

CREATE TABLE IF NOT EXISTS `ITEMSUBCLASS` (
  `idClass` tinyint(3) unsigned NOT NULL,
  `idSubClass` tinyint(3) unsigned NOT NULL,
  `name` varchar(30) default NULL,
  `completeName` varchar(30) default NULL,
  PRIMARY KEY  (`idClass`,`idSubClass`),
  KEY `idSubClass` (`idSubClass`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `ITEMSUBCLASS`
--

INSERT INTO `ITEMSUBCLASS` (`idClass`, `idSubClass`, `name`, `completeName`) VALUES
(0, 0, 'Consumable', 'NULL'),
(0, 1, 'Potion', 'NULL'),
(0, 2, 'Elixir', 'NULL'),
(0, 3, 'Flask', 'NULL'),
(0, 4, 'Scroll', 'NULL'),
(0, 5, 'Food & Drink', 'NULL'),
(0, 6, 'Item Enhancement', 'NULL'),
(0, 7, 'Bandage', 'NULL'),
(0, 8, 'Other', 'NULL'),
(1, 0, 'Bag', 'NULL'),
(1, 1, 'Soul Bag', 'NULL'),
(1, 2, 'Herb Bag', 'NULL'),
(1, 3, 'Enchanting Bag', 'NULL'),
(1, 4, 'Engineering Bag', 'NULL'),
(1, 5, 'Gem Bag', 'NULL'),
(1, 6, 'Mining Bag', 'NULL'),
(1, 7, 'Leatherworking Bag', 'NULL'),
(1, 8, 'Inscription Bag', 'NULL'),
(1, 9, 'Tackle Box', 'NULL'),
(2, 0, 'Axe', 'One-Handed Axes'),
(2, 1, 'Axe', 'Two-Handed Axes'),
(2, 2, 'Bow', 'Bows'),
(2, 3, 'Gun', 'Guns'),
(2, 4, 'Mace', 'One-Handed Maces'),
(2, 5, 'Mace', 'Two-Handed Maces'),
(2, 6, 'Polearm', 'Polearms'),
(2, 7, 'Sword', 'One-Handed Swords'),
(2, 8, 'Sword', 'Two-Handed Swords'),
(2, 9, 'Obsolete', 'NULL'),
(2, 10, 'Staff', 'Staves'),
(2, 11, 'Exotic', 'One-Handed Exotics'),
(2, 12, 'Exotic', 'Two-Handed Exotics'),
(2, 13, 'Fist Weapon', 'Fist Weapons'),
(2, 14, 'Miscellaneous', 'NULL'),
(2, 15, 'Dagger', 'Daggers'),
(2, 16, 'Thrown', 'Thrown'),
(2, 17, 'Spear', 'Spears'),
(2, 18, 'Crossbow', 'Crossbows'),
(2, 19, 'Wand', 'Wands'),
(2, 20, 'Fishing Pole', 'Fishing Poles'),
(3, 0, 'Red', 'NULL'),
(3, 1, 'Blue', 'NULL'),
(3, 2, 'Yellow', 'NULL'),
(3, 3, 'Purple', 'NULL'),
(3, 4, 'Green', 'NULL'),
(3, 5, 'Orange', 'NULL'),
(3, 6, 'Meta', 'NULL'),
(3, 7, 'Simple', 'NULL'),
(3, 8, 'Prismatic', 'NULL'),
(3, 9, 'Hydraulic', 'NULL'),
(3, 10, 'Cogwheel', 'NULL'),
(4, 0, 'Miscellaneous', 'NULL'),
(4, 1, 'Cloth', 'Cloth'),
(4, 2, 'Leather', 'Leather'),
(4, 3, 'Mail', 'Mail'),
(4, 4, 'Plate', 'Plate'),
(4, 5, 'Buckler(OBSOLETE)', 'Bucklers'),
(4, 6, 'Shield', 'Shields'),
(4, 7, 'Libram', 'Librams'),
(4, 8, 'Idol', 'Idols'),
(4, 9, 'Totem', 'Totems'),
(4, 10, 'Sigil', 'Sigils'),
(4, 11, 'Relic', 'NULL'),
(5, 0, 'Reagent', 'NULL'),
(6, 0, 'Wand(OBSOLETE)', 'NULL'),
(6, 1, 'Bolt(OBSOLETE)', 'NULL'),
(6, 2, 'Arrow', 'NULL'),
(6, 3, 'Bullet', 'NULL'),
(6, 4, 'Thrown(OBSOLETE)', 'NULL'),
(7, 0, 'Trade Goods', 'NULL'),
(7, 1, 'Parts', 'NULL'),
(7, 2, 'Explosives', 'NULL'),
(7, 3, 'Devices', 'NULL'),
(7, 4, 'Jewelcrafting', 'NULL'),
(7, 5, 'Cloth', 'NULL'),
(7, 6, 'Leather', 'NULL'),
(7, 7, 'Metal & Stone', 'NULL'),
(7, 8, 'Meat', 'NULL'),
(7, 9, 'Herb', 'NULL'),
(7, 10, 'Elemental', 'NULL'),
(7, 11, 'Other', 'NULL'),
(7, 12, 'Enchanting', 'NULL'),
(7, 13, 'Materials', 'NULL'),
(7, 14, 'Item Enchantment', 'Item Enchantment'),
(7, 15, 'Weapon Enchantment - Obsolete', 'Weapon Enchantment - Obsolete'),
(8, 0, 'Generic(OBSOLETE)', 'NULL'),
(9, 0, 'Book', 'NULL'),
(9, 1, 'Leatherworking', 'NULL'),
(9, 2, 'Tailoring', 'NULL'),
(9, 3, 'Engineering', 'NULL'),
(9, 4, 'Blacksmithing', 'NULL'),
(9, 5, 'Cooking', 'NULL'),
(9, 6, 'Alchemy', 'NULL'),
(9, 7, 'First Aid', 'NULL'),
(9, 8, 'Enchanting', 'NULL'),
(9, 9, 'Fishing', 'NULL'),
(9, 10, 'Jewelcrafting', 'NULL'),
(9, 11, 'Inscription', 'Inscription'),
(10, 0, 'Money(OBSOLETE)', 'NULL'),
(11, 0, 'Quiver(OBSOLETE)', 'NULL'),
(11, 1, 'Quiver(OBSOLETE)', 'NULL'),
(11, 2, 'Quiver', 'NULL'),
(11, 3, 'Ammo Pouch', 'NULL'),
(12, 0, 'Quest', 'NULL'),
(13, 0, 'Key', 'NULL'),
(13, 1, 'Lockpick', 'NULL'),
(14, 0, 'Permanent', 'NULL'),
(15, 0, 'Junk', 'NULL'),
(15, 1, 'Reagent', 'NULL'),
(15, 2, 'Pet', 'NULL'),
(15, 3, 'Holiday', 'NULL'),
(15, 4, 'Other', 'NULL'),
(15, 5, 'Mount', 'Mount'),
(16, 1, 'Warrior', 'Warrior'),
(16, 2, 'Paladin', 'Paladin'),
(16, 3, 'Hunter', 'Hunter'),
(16, 4, 'Rogue', 'Rogue'),
(16, 5, 'Priest', 'Priest'),
(16, 6, 'Death Knight', 'Death Knight'),
(16, 7, 'Shaman', 'Shaman'),
(16, 8, 'Mage', 'Mage'),
(16, 9, 'Warlock', 'Warlock'),
(16, 11, 'Druid', 'Druid');

-- --------------------------------------------------------

--
-- Structure de la table `LANGUES`
--

CREATE TABLE IF NOT EXISTS `LANGUES` (
  `id` tinyint(3) unsigned NOT NULL,
  `langue` varchar(30) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `LANGUES`
--

INSERT INTO `LANGUES` (`id`, `langue`) VALUES
(1, 'de_DE'),
(2, 'en_GB'),
(3, 'es_ES'),
(4, 'fr_FR'),
(5, 'it_IT'),
(6, 'ru_RU'),
(7, 'pt_PT');

-- --------------------------------------------------------

--
-- Structure de la table `PLAYERS`
--

CREATE TABLE IF NOT EXISTS `PLAYERS` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `name` varchar(50) NOT NULL default '',
  `serverId` tinyint(3) unsigned NOT NULL,
  `genderId` tinyint(3) unsigned default NULL,
  `factionId` tinyint(3) unsigned default NULL,
  `raceId` tinyint(3) unsigned default NULL,
  `classId` tinyint(3) unsigned default NULL,
  `level` tinyint(3) unsigned default NULL,
  `thumbnail` varchar(100) default NULL,
  `backId` mediumint(9) default NULL,
  `chestId` mediumint(8) unsigned default NULL,
  `feetId` mediumint(8) unsigned default NULL,
  `finger1Id` mediumint(8) unsigned default NULL,
  `finger2Id` mediumint(8) unsigned default NULL,
  `handsId` mediumint(8) unsigned default NULL,
  `legsId` mediumint(8) unsigned default NULL,
  `mainHandId` mediumint(8) unsigned default NULL,
  `neckId` mediumint(8) unsigned default NULL,
  `shoulderId` mediumint(8) unsigned default NULL,
  `trinket1Id` mediumint(8) unsigned default NULL,
  `trinket2Id` mediumint(8) unsigned default NULL,
  `waistId` mediumint(8) unsigned default NULL,
  `wristId` mediumint(8) unsigned default NULL,
  PRIMARY KEY  (`id`,`name`,`serverId`),
  KEY `wristId` (`wristId`),
  KEY `waistId` (`waistId`),
  KEY `trinket2Id` (`trinket2Id`),
  KEY `trinket1Id` (`trinket1Id`),
  KEY `shoulderId` (`shoulderId`),
  KEY `neckId` (`neckId`),
  KEY `mainHandId` (`mainHandId`),
  KEY `handsId` (`handsId`),
  KEY `finger2Id` (`finger2Id`),
  KEY `finger1Id` (`finger1Id`),
  KEY `feetId` (`feetId`),
  KEY `chestId_3` (`chestId`),
  KEY `legsId` (`legsId`),
  KEY `serverId` (`serverId`),
  KEY `raceId` (`raceId`),
  KEY `genderId` (`genderId`),
  KEY `PLAYERS_ibfk_18` (`classId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Contenu de la table `PLAYERS`
--


-- --------------------------------------------------------

--
-- Structure de la table `POWERTYPE`
--

CREATE TABLE IF NOT EXISTS `POWERTYPE` (
  `id` tinyint(3) unsigned NOT NULL,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `POWERTYPE`
--

INSERT INTO `POWERTYPE` (`id`, `name`) VALUES
(0, 'mana'),
(1, 'rage'),
(2, 'focus'),
(3, 'energy'),
(4, 'hapiness'),
(5, 'runes'),
(6, 'runic power'),
(7, 'soul shards'),
(8, 'eclipse'),
(9, 'holy power'),
(10, 'alternate power'),
(11, 'dark power'),
(12, 'light force'),
(13, 'shadow orbs'),
(14, 'burnings embers'),
(15, 'fury');

-- --------------------------------------------------------

--
-- Structure de la table `RACES`
--

CREATE TABLE IF NOT EXISTS `RACES` (
  `id` tinyint(3) unsigned NOT NULL,
  `idFaction` tinyint(3) unsigned NOT NULL,
  `NAME` varchar(30) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `idFaction` (`idFaction`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `RACES`
--

INSERT INTO `RACES` (`id`, `idFaction`, `NAME`) VALUES
(1, 1, 'Humain'),
(2, 2, 'Orc'),
(3, 1, 'Nain'),
(4, 1, 'Elfe de la nuit'),
(5, 2, 'Mort-vivant'),
(6, 2, 'Tauren'),
(7, 1, 'Gnome'),
(8, 2, 'Troll'),
(9, 2, 'Gobelin'),
(10, 2, 'Elfe de sang'),
(11, 0, 'Draeneï'),
(22, 1, 'Worgen'),
(24, 0, 'Pandaren'),
(25, 1, 'Pandaren'),
(26, 2, 'Pandaren');

-- --------------------------------------------------------

--
-- Structure de la table `SERVEURS`
--

CREATE TABLE IF NOT EXISTS `SERVEURS` (
  `id` tinyint(3) unsigned NOT NULL auto_increment,
  `name` varchar(30) NOT NULL,
  `idLangue` tinyint(3) unsigned NOT NULL,
  `idType` tinyint(3) unsigned NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `idLangue` (`idLangue`),
  KEY `idType` (`idType`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Contenu de la table `SERVEURS`
--


-- --------------------------------------------------------

--
-- Structure de la table `SERVEURTYPE`
--

CREATE TABLE IF NOT EXISTS `SERVEURTYPE` (
  `id` tinyint(3) unsigned NOT NULL,
  `type` varchar(30) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `SERVEURTYPE`
--

INSERT INTO `SERVEURTYPE` (`id`, `type`) VALUES
(0, 'pve'),
(1, 'pvp'),
(2, 'rp'),
(3, 'rppvp');

-- --------------------------------------------------------

--
-- Structure de la table `TALENTS`
--

CREATE TABLE IF NOT EXISTS `TALENTS` (
  `id` smallint(5) unsigned NOT NULL,
  `idItem` mediumint(8) unsigned NOT NULL,
  `idIcon` mediumint(8) unsigned NOT NULL,
  `idType` tinyint(3) unsigned NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `idItem` (`idItem`),
  KEY `idIcon` (`idIcon`),
  KEY `idType` (`idType`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `TALENTS`
--


-- --------------------------------------------------------

--
-- Structure de la table `WEAPON`
--

CREATE TABLE IF NOT EXISTS `WEAPON` (
  `id` mediumint(8) unsigned NOT NULL,
  `damageMax` smallint(5) unsigned default NULL,
  `damageMin` smallint(5) unsigned default NULL,
  `dps` decimal(8,3) default NULL,
  `weaponSpeed` decimal(5,3) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `WEAPON`
--


--
-- Contraintes pour les tables exportées
--

--
-- Contraintes pour la table `CLASSES`
--
ALTER TABLE `CLASSES`
  ADD CONSTRAINT `CLASSES_ibfk_1` FOREIGN KEY (`powerType`) REFERENCES `POWERTYPE` (`id`);

--
-- Contraintes pour la table `FRIENDS`
--
ALTER TABLE `FRIENDS`
  ADD CONSTRAINT `FRIENDS_ibfk_2` FOREIGN KEY (`idPlayer`) REFERENCES `PLAYERS` (`id`),
  ADD CONSTRAINT `FRIENDS_ibfk_1` FOREIGN KEY (`idFriend`) REFERENCES `PLAYERS` (`id`);

--
-- Contraintes pour la table `ITEMS`
--
ALTER TABLE `ITEMS`
  ADD CONSTRAINT `ITEMS_ibfk_5` FOREIGN KEY (`subclassid`) REFERENCES `ITEMSUBCLASS` (`idSubClass`),
  ADD CONSTRAINT `ITEMS_ibfk_1` FOREIGN KEY (`classid`) REFERENCES `ITEMCLASS` (`id`),
  ADD CONSTRAINT `ITEMS_ibfk_3` FOREIGN KEY (`picture`) REFERENCES `ITEMSPICTURES` (`id`),
  ADD CONSTRAINT `ITEMS_ibfk_4` FOREIGN KEY (`description`) REFERENCES `ITEMSDESCRIPTIONS` (`id`);

--
-- Contraintes pour la table `ITEMSTAT`
--
ALTER TABLE `ITEMSTAT`
  ADD CONSTRAINT `ITEMSTAT_ibfk_1` FOREIGN KEY (`stat`) REFERENCES `BONUSSTATS` (`id`),
  ADD CONSTRAINT `ITEMSTAT_ibfk_2` FOREIGN KEY (`id`) REFERENCES `ITEMS` (`id`);

--
-- Contraintes pour la table `PLAYERS`
--
ALTER TABLE `PLAYERS`
  ADD CONSTRAINT `PLAYERS_ibfk_1` FOREIGN KEY (`chestId`) REFERENCES `ITEMS` (`id`),
  ADD CONSTRAINT `PLAYERS_ibfk_10` FOREIGN KEY (`trinket1Id`) REFERENCES `ITEMS` (`id`),
  ADD CONSTRAINT `PLAYERS_ibfk_11` FOREIGN KEY (`trinket2Id`) REFERENCES `ITEMS` (`id`),
  ADD CONSTRAINT `PLAYERS_ibfk_12` FOREIGN KEY (`waistId`) REFERENCES `ITEMS` (`id`),
  ADD CONSTRAINT `PLAYERS_ibfk_13` FOREIGN KEY (`wristId`) REFERENCES `ITEMS` (`id`),
  ADD CONSTRAINT `PLAYERS_ibfk_14` FOREIGN KEY (`serverId`) REFERENCES `SERVEURS` (`id`),
  ADD CONSTRAINT `PLAYERS_ibfk_17` FOREIGN KEY (`raceId`) REFERENCES `RACES` (`id`),
  ADD CONSTRAINT `PLAYERS_ibfk_18` FOREIGN KEY (`classId`) REFERENCES `CLASSES` (`id`),
  ADD CONSTRAINT `PLAYERS_ibfk_2` FOREIGN KEY (`feetId`) REFERENCES `ITEMS` (`id`),
  ADD CONSTRAINT `PLAYERS_ibfk_3` FOREIGN KEY (`finger1Id`) REFERENCES `ITEMS` (`id`),
  ADD CONSTRAINT `PLAYERS_ibfk_4` FOREIGN KEY (`finger2Id`) REFERENCES `ITEMS` (`id`),
  ADD CONSTRAINT `PLAYERS_ibfk_5` FOREIGN KEY (`handsId`) REFERENCES `ITEMS` (`id`),
  ADD CONSTRAINT `PLAYERS_ibfk_6` FOREIGN KEY (`legsId`) REFERENCES `ITEMS` (`id`),
  ADD CONSTRAINT `PLAYERS_ibfk_7` FOREIGN KEY (`mainHandId`) REFERENCES `ITEMS` (`id`),
  ADD CONSTRAINT `PLAYERS_ibfk_8` FOREIGN KEY (`neckId`) REFERENCES `ITEMS` (`id`),
  ADD CONSTRAINT `PLAYERS_ibfk_9` FOREIGN KEY (`shoulderId`) REFERENCES `ITEMS` (`id`);

--
-- Contraintes pour la table `RACES`
--
ALTER TABLE `RACES`
  ADD CONSTRAINT `RACES_ibfk_1` FOREIGN KEY (`idFaction`) REFERENCES `FACTION` (`id`);

--
-- Contraintes pour la table `SERVEURS`
--
ALTER TABLE `SERVEURS`
  ADD CONSTRAINT `SERVEURS_ibfk_2` FOREIGN KEY (`idType`) REFERENCES `SERVEURTYPE` (`id`),
  ADD CONSTRAINT `SERVEURS_ibfk_1` FOREIGN KEY (`idLangue`) REFERENCES `LANGUES` (`id`);

--
-- Contraintes pour la table `TALENTS`
--
ALTER TABLE `TALENTS`
  ADD CONSTRAINT `TALENTS_ibfk_2` FOREIGN KEY (`idIcon`) REFERENCES `ITEMSPICTURES` (`id`),
  ADD CONSTRAINT `TALENTS_ibfk_1` FOREIGN KEY (`idItem`) REFERENCES `ITEMS` (`id`);

--
-- Contraintes pour la table `WEAPON`
--
ALTER TABLE `WEAPON`
  ADD CONSTRAINT `WEAPON_ibfk_1` FOREIGN KEY (`id`) REFERENCES `ITEMS` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
