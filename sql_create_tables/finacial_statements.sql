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

/*Table structure for table `s_financial_statements` */

DROP TABLE IF EXISTS `s_financial_statements`;

CREATE TABLE `s_financial_statements` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `report_date` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '所属季度，如20200930',
  `item_code` char(6) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `item_name` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `notice_date` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '公告时间',
  `update_date` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '更新时间，有的股喜欢更换报表',
  `basic_eps` double NOT NULL DEFAULT '0' COMMENT '每股收益（元）：BASIC_EPS',
  `bps` double NOT NULL DEFAULT '0' COMMENT '每股净资产（元）：BPS',
  `bps_roe` double NOT NULL DEFAULT '0' COMMENT '净资产收益率：WEIGHTAVG_ROE',
  `operating_cash_flow` double NOT NULL DEFAULT '0' COMMENT '每股营业现金流（元）：MGJYXJJE',
  `sales_margins` double NOT NULL DEFAULT '0' COMMENT '销售毛利率（%）：XSMLL',
  `toi_ratio` double NOT NULL DEFAULT '0' COMMENT '营业收入同比增长（%）：YSTZ',
  `toi_chair_ratio` double NOT NULL DEFAULT '0' COMMENT '营业收入环比增长（%）：YSHZ',
  `parent_netprofit_ratio` double NOT NULL DEFAULT '0' COMMENT '净利润同比增长（%）：SJLTZ',
  `netprofit_chair_ratio` double NOT NULL DEFAULT '0' COMMENT '净利润环比增长（%）：YSHZ',
  `industry_name` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '' COMMENT '所属行业：INDUSTRY_NAME',
  PRIMARY KEY (`id`),
  KEY `item_code` (`item_code`),
  KEY `report_date` (`report_date`)
) ENGINE=InnoDB AUTO_INCREMENT=8076 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='业绩报表';

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
