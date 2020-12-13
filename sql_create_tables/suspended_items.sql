/*
SQLyog Ultimate v11.27 (32 bit)
MySQL - 5.7.26 : Database - stock
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`stock` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;

USE `stock`;

/*Table structure for table `s_suspended_items` */

DROP TABLE IF EXISTS `s_suspended_items`;

CREATE TABLE `s_suspended_items` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `item_code` char(6) NOT NULL,
  `item_name` varchar(32) DEFAULT '',
  `begin_datetime` datetime NOT NULL COMMENT '停牌开始时间',
  `end_datetime` varchar(32) NOT NULL DEFAULT '' COMMENT '停牌截止时间',
  `suspended_type` varchar(255) NOT NULL DEFAULT '' COMMENT '停牌类型',
  `suspended_reasons` varchar(255) NOT NULL DEFAULT '' COMMENT '停牌原因',
  `mark_type` varchar(32) NOT NULL DEFAULT '' COMMENT '所属市场',
  `begin_date` date DEFAULT NULL COMMENT '停牌开始日期',
  `resumption_date` varchar(16) NOT NULL DEFAULT '' COMMENT '复牌时间',
  PRIMARY KEY (`id`),
  KEY `begin_datetime` (`begin_datetime`,`item_code`)
) ENGINE=InnoDB AUTO_INCREMENT=1381 DEFAULT CHARSET=utf8mb4 COMMENT='停复牌个股';

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
