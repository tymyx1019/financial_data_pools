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

/*Table structure for table `s_financial_profits` */

DROP TABLE IF EXISTS `s_financial_profits`;

CREATE TABLE `s_financial_profits` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `item_code` char(6) NOT NULL COMMENT 'SECURITY_CODE',
  `item_name` varchar(32) NOT NULL DEFAULT '' COMMENT 'SECURITY_NAME_ABBR',
  `parent_netprofit` double NOT NULL DEFAULT '0' COMMENT '净利润：PARENT_NETPROFIT',
  `total_operate_income` double NOT NULL DEFAULT '0' COMMENT '营业总收入（元）：TOTAL_OPERATE_INCOME',
  `operate_cost` double NOT NULL DEFAULT '0' COMMENT '营业支出：OPERATE_COST',
  `operate_expense` double NOT NULL DEFAULT '0' COMMENT '营业支出：OPERATE_EXPENSE',
  `operate_expense_ratio` double NOT NULL DEFAULT '0' COMMENT '营业支出同比：OPERATE_EXPENSE_RATIO',
  `sale_expense` double NOT NULL DEFAULT '0' COMMENT '销售支出：SALE_EXPENSE',
  `manage_expense` double NOT NULL DEFAULT '0' COMMENT '管理支出：MANAGE_EXPENSE',
  `finance_expense` double NOT NULL DEFAULT '0' COMMENT '财务支出：FINANCE_EXPENSE',
  `total_operate_cost` double NOT NULL DEFAULT '0' COMMENT '营业总支出：TOTAL_OPERATE_COST',
  `operate_profit` double NOT NULL DEFAULT '0' COMMENT '营业利润：OPERATE_PROFIT',
  `income_tax` double NOT NULL DEFAULT '0' COMMENT '退税收入：INCOME_TAX',
  `operate_tax_add` double NOT NULL DEFAULT '0' COMMENT '税收增加：OPERATE_TAX_ADD',
  `total_profit` double NOT NULL DEFAULT '0' COMMENT '利润总额：TOTAL_PROFIT',
  `notice_date` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '发公告日期，整型格式：NOTICE_DATE',
  `report_date` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '所属季度，格式为整型，一般为四个季度，20200331,20200631,20200930,20201231',
  `operate_profit_ratio` double NOT NULL DEFAULT '0' COMMENT 'OPERATE_PROFIT_RATIO',
  `deduct_parent_netprofit` double NOT NULL DEFAULT '0' COMMENT 'DE扣非净利润：DUCT_PARENT_NETPROFIT',
  `dpn_ratio` double NOT NULL DEFAULT '0' COMMENT '扣非净利润同比增长：DPN_RATIO',
  PRIMARY KEY (`id`),
  KEY `item_code` (`item_code`),
  KEY `report_date` (`report_date`)
) ENGINE=InnoDB AUTO_INCREMENT=8207 DEFAULT CHARSET=utf8mb4 COMMENT='利润表';

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
