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

/*Table structure for table `s_unlocked_items` */

DROP TABLE IF EXISTS `s_unlocked_items`;

CREATE TABLE `s_unlocked_items` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `item_code` char(6) NOT NULL,
  `item_name` varchar(32) NOT NULL DEFAULT '',
  `unlocked_time` int(10) unsigned NOT NULL COMMENT '解禁时间',
  `unlocked_type` varchar(32) NOT NULL DEFAULT '' COMMENT '解禁类型，如：首发原股东限售股份',
  `circulation_percent` decimal(10,2) unsigned NOT NULL DEFAULT '0.00' COMMENT '占解禁前流通市值比例(%)',
  `mark_type` varchar(32) NOT NULL DEFAULT '' COMMENT '所属市场',
  `total_percent` decimal(10,2) unsigned NOT NULL DEFAULT '0.00' COMMENT '总占比',
  `shareholders_num` smallint(5) unsigned NOT NULL DEFAULT '1' COMMENT '解禁股东数',
  `unlocked_total` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '解禁数量',
  `true_unlocked_total` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '实际解禁数量',
  `circulation_total` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '该次解禁后流通数量',
  `locked_total` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '剩余待解禁数量',
  PRIMARY KEY (`id`),
  KEY `unlocked_time` (`unlocked_time`,`item_code`)
) ENGINE=InnoDB AUTO_INCREMENT=5332 DEFAULT CHARSET=utf8mb4 COMMENT='解禁个股';

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
