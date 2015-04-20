-- phpMyAdmin SQL Dump
-- version 3.1.2deb1ubuntu0.2
-- http://www.phpmyadmin.net
--
-- Serveur: localhost
-- Généré le : Lun 20 Avril 2015 à 15:51
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
(0, 'neutral'),
(1, 'alliance'),
(2, 'horde');

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
  `description` varchar(100) NOT NULL default '',
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
  `amount` tinyint(3) unsigned NOT NULL,
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
  PRIMARY KEY  (`idClass`,`idSubClass`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `ITEMSUBCLASS`
--


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
(1, 'Allemand'),
(2, 'Anglais'),
(3, 'Espagnol'),
(4, 'Français'),
(5, 'Italien'),
(6, 'Russe');

-- --------------------------------------------------------

--
-- Structure de la table `PLAYERS`
--

CREATE TABLE IF NOT EXISTS `PLAYERS` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `name` varchar(50) NOT NULL default '',
  `server` tinyint(3) unsigned NOT NULL,
  `genderId` tinyint(3) unsigned default NULL,
  `raceId` tinyint(3) unsigned default NULL,
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
  PRIMARY KEY  (`id`),
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
  KEY `server` (`server`),
  KEY `raceId` (`raceId`),
  KEY `genderId` (`genderId`)
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
(0, 'Normal'),
(1, 'JcJ'),
(2, 'JdR'),
(3, 'JcJ et JdR');

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
  `requiredLevel` tinyint(3) unsigned NOT NULL,
  `damageMax` smallint(5) unsigned default NULL,
  `damageMin` smallint(5) unsigned default NULL,
  `dps` decimal(8,3) default NULL,
  `weaponSpeed` decimal(5,3) default NULL,
  `maxDurability` tinyint(3) unsigned default NULL,
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
  ADD CONSTRAINT `ITEMS_ibfk_1` FOREIGN KEY (`classid`) REFERENCES `ITEMCLASS` (`id`),
  ADD CONSTRAINT `ITEMS_ibfk_2` FOREIGN KEY (`subclassid`) REFERENCES `ITEMSUBCLASS` (`idClass`),
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
  ADD CONSTRAINT `PLAYERS_ibfk_14` FOREIGN KEY (`server`) REFERENCES `SERVEURS` (`id`),
  ADD CONSTRAINT `PLAYERS_ibfk_17` FOREIGN KEY (`raceId`) REFERENCES `RACES` (`id`),
  ADD CONSTRAINT `PLAYERS_ibfk_18` FOREIGN KEY (`genderId`) REFERENCES `CLASSES` (`id`),
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
