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

/*Table structure for table `s_balance_sheets` */

DROP TABLE IF EXISTS `s_balance_sheets`;

CREATE TABLE `s_balance_sheets` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `report_date` int(10) unsigned NOT NULL DEFAULT '0',
  `item_code` char(6) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `item_name` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `monetaryfunds` double NOT NULL DEFAULT '0' COMMENT '货币资产（元）：MONETARYFUNDS',
  `monetaryfunds_ratio` double NOT NULL DEFAULT '0' COMMENT '货币资产（元）：MONETARYFUNDS_RATIO',
  `accounts_rece` double NOT NULL DEFAULT '0' COMMENT '应收账款（元）：ACCOUNTS_RECE',
  `accounts_rece_ratio` double NOT NULL DEFAULT '0' COMMENT '应收账款同比（%）：ACCOUNTS_RECE_RATIO',
  `inventory` double NOT NULL DEFAULT '0' COMMENT '存货（元）:INVENTORY',
  `inventory_ratio` double NOT NULL DEFAULT '0' COMMENT '存货同比（%）:INVENTORY_RATIO',
  `total_assets` double NOT NULL DEFAULT '0' COMMENT '总资产（元）:TOTAL_ASSETS',
  `total_assets_ratio` double NOT NULL DEFAULT '0' COMMENT '总资产同比（%）:TOTAL_ASSETS_RATIO',
  `accounts_payable` double NOT NULL DEFAULT '0' COMMENT '应付账款（元）:ACCOUNTS_PAYABLE',
  `accounts_payable_ratio` double NOT NULL DEFAULT '0' COMMENT '应付账款同比（%）:ACCOUNTS_PAYABLE_RATIO',
  `advance_receivables` double NOT NULL DEFAULT '0' COMMENT '预收账款（元）:ADVANCE_RECEIVABLES',
  `advance_receivables_ratio` double NOT NULL DEFAULT '0' COMMENT '预收账款同比（%）:ADVANCE_RECEIVABLES_RATIO',
  `total_liabilities` double NOT NULL DEFAULT '0' COMMENT '总负债（元）:TOTAL_LIABILITIES',
  `total_liab_ratio` double NOT NULL DEFAULT '0' COMMENT '总负债同比（%）:TOTAL_LIAB_RATIO',
  `debt_asset_ratio` double NOT NULL DEFAULT '0' COMMENT '总资产负债率（%）:DEBT_ASSET_RATIO',
  `total_equity` double NOT NULL DEFAULT '0' COMMENT '股东权益合计（元）:TOTAL_EQUITY',
  `total_equity_ratio` double NOT NULL DEFAULT '0' COMMENT '股东权益合计同比（%）:TOTAL_EQUITY_RATIO',
  `fixed_asset` double NOT NULL DEFAULT '0' COMMENT '固定资产（元）:FIXED_ASSET',
  `industry_code` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '' COMMENT '行业代码',
  PRIMARY KEY (`id`),
  KEY `report_date` (`report_date`),
  KEY `item_code` (`item_code`)
) ENGINE=InnoDB AUTO_INCREMENT=20382 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='资产负债表';

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
