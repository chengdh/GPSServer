-- MySQL dump 10.13  Distrib 5.5.31, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: unpnhis
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
) ENGINE=MyISAM AUTO_INCREMENT=18376454 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `gps_1212_0`
--

DROP TABLE IF EXISTS `gps_1212_0`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gps_1212_0` (
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
) ENGINE=MyISAM AUTO_INCREMENT=58739 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `gps_1212_1`
--

DROP TABLE IF EXISTS `gps_1212_1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gps_1212_1` (
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
) ENGINE=MyISAM AUTO_INCREMENT=598526 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `gps_1301_0`
--

DROP TABLE IF EXISTS `gps_1301_0`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gps_1301_0` (
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
) ENGINE=MyISAM AUTO_INCREMENT=16513 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `gps_1301_1`
--

DROP TABLE IF EXISTS `gps_1301_1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gps_1301_1` (
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
) ENGINE=MyISAM AUTO_INCREMENT=557303 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `gps_1303_0`
--

DROP TABLE IF EXISTS `gps_1303_0`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gps_1303_0` (
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
) ENGINE=MyISAM AUTO_INCREMENT=35375 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `gps_1303_1`
--

DROP TABLE IF EXISTS `gps_1303_1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gps_1303_1` (
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
) ENGINE=MyISAM AUTO_INCREMENT=627643 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `gps_1303_2`
--

DROP TABLE IF EXISTS `gps_1303_2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gps_1303_2` (
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
) ENGINE=MyISAM AUTO_INCREMENT=8000 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `gps_1304_0`
--

DROP TABLE IF EXISTS `gps_1304_0`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gps_1304_0` (
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
) ENGINE=MyISAM AUTO_INCREMENT=61837 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `gps_1304_1`
--

DROP TABLE IF EXISTS `gps_1304_1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gps_1304_1` (
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
) ENGINE=MyISAM AUTO_INCREMENT=836170 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `gps_1304_2`
--

DROP TABLE IF EXISTS `gps_1304_2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gps_1304_2` (
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
) ENGINE=MyISAM AUTO_INCREMENT=158272 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `gps_1305_0`
--

DROP TABLE IF EXISTS `gps_1305_0`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gps_1305_0` (
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
) ENGINE=MyISAM AUTO_INCREMENT=1179282 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `gps_1305_1`
--

DROP TABLE IF EXISTS `gps_1305_1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gps_1305_1` (
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
) ENGINE=MyISAM AUTO_INCREMENT=395973 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `gps_1305_2`
--

DROP TABLE IF EXISTS `gps_1305_2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gps_1305_2` (
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
) ENGINE=MyISAM AUTO_INCREMENT=963001 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `gps_1305_3`
--

DROP TABLE IF EXISTS `gps_1305_3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gps_1305_3` (
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
) ENGINE=MyISAM AUTO_INCREMENT=306729 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `gps_1305_None`
--

DROP TABLE IF EXISTS `gps_1305_None`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gps_1305_None` (
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
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `gps_1306_0`
--

DROP TABLE IF EXISTS `gps_1306_0`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gps_1306_0` (
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
) ENGINE=MyISAM AUTO_INCREMENT=267861 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `gps_1306_1`
--

DROP TABLE IF EXISTS `gps_1306_1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gps_1306_1` (
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
) ENGINE=MyISAM AUTO_INCREMENT=182751 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `gps_1306_2`
--

DROP TABLE IF EXISTS `gps_1306_2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gps_1306_2` (
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
) ENGINE=MyISAM AUTO_INCREMENT=470424 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `gps_1306_3`
--

DROP TABLE IF EXISTS `gps_1306_3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gps_1306_3` (
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
) ENGINE=MyISAM AUTO_INCREMENT=330724 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2013-06-04 15:08:08
