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

/*Table structure for table `s_cashflows` */

DROP TABLE IF EXISTS `s_cashflows`;

CREATE TABLE `s_cashflows` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `report_date` int(10) unsigned NOT NULL DEFAULT '0',
  `item_code` char(6) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `item_name` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `notice_date` int(10) unsigned NOT NULL DEFAULT '0',
  `cce_add` double NOT NULL DEFAULT '0' COMMENT '净现金流（元）:CCE_ADD',
  `cce_add_ratio` double NOT NULL DEFAULT '0' COMMENT '净现金流同比（%）:CCE_ADD_RATIO',
  `netcash_operate` double NOT NULL DEFAULT '0' COMMENT '经营性现金流-现金流量净额（元）:NETCASH_OPERATE',
  `netcash_operate_ratio` double NOT NULL DEFAULT '0' COMMENT '经营性现金流-现金流量净额占比（%）:NETCASH_OPERATE_RATIO',
  `netcash_invest` double NOT NULL DEFAULT '0' COMMENT '投资性现金流-现金流量净额（元）: NETCASH_INVEST',
  `netcash_invest_ratio` double NOT NULL DEFAULT '0' COMMENT '投资性现金流-现金流量净额占比（%） NETCASH_INVEST_RATIO',
  `netcash_finance` double NOT NULL DEFAULT '0' COMMENT '融资性性现金流-现金流量净额（元） NETCASH_FINANCE',
  `netcash_finance_ratio` double NOT NULL DEFAULT '0' COMMENT '融资性现金流-现金流量净额占比（元） NETCASH_FINANCE_RATIO',
  `sales_services` double NOT NULL DEFAULT '0' COMMENT '依据字面意思是售后服务（元） SALES_SERVICES',
  `sales_services_ratio` double NOT NULL DEFAULT '0' COMMENT '依据字面意思是售后服务同比（%） SALES_SERVICES_RATIO',
  `pay_staff_cash` double NOT NULL DEFAULT '0' COMMENT '依据字面意思是员工支付现金-薪水（元） PAY_STAFF_CASH',
  `psc_ratio` double NOT NULL DEFAULT '0' COMMENT '依据字面意思是员工支付现金-薪水同比（%）  PSC_RATIO',
  `receive_invest_income` double NOT NULL DEFAULT '0' COMMENT '依据字面意思是投资收益（元） RECEIVE_INVEST_INCOME',
  `rii_ratio` double NOT NULL DEFAULT '0' COMMENT '依据字面意思是投资收益同比（%） RII_RATIO',
  `construct_long_asset` double NOT NULL DEFAULT '0' COMMENT '依据字面意思是长期建设资产？（元） CONSTRUCT_LONG_ASSET',
  `cla_ratio` double NOT NULL DEFAULT '0' COMMENT '依据字面意思是长期建设资产？（元） CLA_RATIO',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36506 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='现金流量表';

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
