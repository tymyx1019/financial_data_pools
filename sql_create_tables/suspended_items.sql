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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='停复牌个股'
