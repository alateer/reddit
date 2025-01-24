CREATE TABLE `sequence_id_generator` (
  `id` int(10) NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `current_max_id` bigint(20) NOT NULL COMMENT '当前最大ID',
  `step` int(10) NOT NULL COMMENT '号段长度',
  `biz_type`    varchar(125) NOT NULL COMMENT '业务类型',
   PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
