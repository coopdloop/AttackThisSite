CREATE TABLE `names` (
  `id` mediumint(8) unsigned NOT NULL auto_increment,
  `first` varchar(255) default NULL,
  `last` varchar(255) default NULL,
  PRIMARY KEY (`id`)
) AUTO_INCREMENT=1;



CREATE TABLE `secret` (
  `secret id` mediumint(8) unsigned NOT NULL auto_increment,
  `secret first` varchar(255) default NULL,
  `secret last` varchar(255) default NULL,
  PRIMARY KEY (`secret id`)
) AUTO_INCREMENT=1;


INSERT into `secret` (`secret first`,`secret last`) VALUES ("cooper","j");