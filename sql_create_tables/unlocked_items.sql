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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='解禁个股'
