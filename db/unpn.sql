-- MySQL dump 10.13  Distrib 5.5.31, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: unpn
-- ------------------------------------------------------
-- Server version	5.5.31-0ubuntu0.12.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alm`
--

DROP TABLE IF EXISTS `alm`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alm` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `epid` varchar(20) NOT NULL,
  `time` datetime NOT NULL,
  `reptime` datetime DEFAULT NULL,
  `type` smallint(6) DEFAULT NULL,
  `data` varchar(100) DEFAULT NULL,
  `gpstime` datetime DEFAULT NULL,
  `longitude` double DEFAULT NULL,
  `latitude` double DEFAULT NULL,
  `direction` smallint(5) unsigned DEFAULT NULL,
  `speed` smallint(5) unsigned DEFAULT NULL,
  `mileage` double DEFAULT NULL,
  `flags` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `epid` (`epid`),
  KEY `time` (`time`),
  KEY `type` (`type`)
) ENGINE=MyISAM AUTO_INCREMENT=287638 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ep`
--

DROP TABLE IF EXISTS `ep`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ep` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `epid` varchar(20) NOT NULL,
  `name` varchar(64) NOT NULL,
  `eptype` varchar(45) NOT NULL DEFAULT '',
  `dept_id` int(11) NOT NULL,
  `devid` varchar(20) NOT NULL DEFAULT '',
  `devtype` varchar(10) NOT NULL DEFAULT '',
  `phone` varchar(20) NOT NULL DEFAULT '',
  `bsl` int(11) NOT NULL DEFAULT '0',
  `bankno` int(13) unsigned NOT NULL DEFAULT '1',
  `creator_id` int(10) NOT NULL,
  `create_time` timestamp NULL DEFAULT NULL,
  `update_time` timestamp NULL DEFAULT NULL,
  `info` varchar(200) NOT NULL DEFAULT '',
  `change_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `capability` varchar(80) DEFAULT NULL,
  `note` varchar(200) DEFAULT NULL,
  `version` int(10) NOT NULL DEFAULT '0',
  `owner_unit` varchar(60) DEFAULT NULL,
  `owner_name` varchar(30) DEFAULT NULL,
  `owner_phone` varchar(200) DEFAULT NULL,
  `factory_name` varchar(60) DEFAULT NULL,
  `model` varchar(60) DEFAULT NULL,
  `power` varchar(20) DEFAULT NULL,
  `reap_width` double(15,2) DEFAULT '0.00',
  PRIMARY KEY (`id`),
  UNIQUE KEY `epid` (`epid`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=3988 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `epstat`
--

DROP TABLE IF EXISTS `epstat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `epstat` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `epid` varchar(20) NOT NULL,
  `time` datetime DEFAULT '2000-01-01 00:00:00',
  `state` smallint(5) unsigned DEFAULT '0' COMMENT '终端状态',
  `desc` varchar(30) DEFAULT '' COMMENT '状态描述',
  `gpstime` datetime DEFAULT '2000-01-01 00:00:00',
  `longitude` double DEFAULT '0',
  `latitude` double DEFAULT '0',
  `direction` smallint(5) unsigned DEFAULT '0',
  `speed` smallint(5) unsigned DEFAULT '0',
  `mileage` double DEFAULT '0',
  `flags` char(10) DEFAULT '',
  `altitude` int(11) DEFAULT NULL,
  `tire_press` int(11) DEFAULT NULL,
  `temp` int(11) DEFAULT NULL,
  `round` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `epid` (`epid`) USING BTREE,
  KEY `time` (`time`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=3980 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `gps`
--

DROP TABLE IF EXISTS `gps`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gps` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `epid` char(20) CHARACTER SET latin1 NOT NULL,
  `time` datetime DEFAULT NULL,
  `reptime` datetime DEFAULT NULL,
  `longitude` double DEFAULT NULL,
  `latitude` double DEFAULT NULL,
  `direction` smallint(5) unsigned DEFAULT NULL,
  `speed` smallint(5) unsigned DEFAULT NULL,
  `mileage` double DEFAULT NULL,
  `flags` char(20) CHARACTER SET latin1 DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `epid` (`epid`),
  KEY `time` (`time`)
) ENGINE=MyISAM AUTO_INCREMENT=72619 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2013-06-04 15:06:16
