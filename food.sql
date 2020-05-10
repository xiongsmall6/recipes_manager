
-- ----------------------------
-- Table structure for `food`
-- ----------------------------
DROP TABLE IF EXISTS `food`;
CREATE TABLE `food` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `FOOD_NAME` varchar(128)  DEFAULT NULL,
  `FOOD_INFO` varchar(512)  DEFAULT NULL,
  `FOOD_IMAGE` varchar(512)  DEFAULT NULL,
  `FOOD_TYPE` int(2) DEFAULT NULL,
  `PRAISE` int(11) DEFAULT NULL,
  `COLLECTIONS` int(11) DEFAULT NULL,
  `CREATE_TIME` timestamp NULL DEFAULT NULL,
  `CREATE_USER` varchar(128)  DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='食物表';

-- ----------------------------
-- Table structure for `food_material`
-- ----------------------------
DROP TABLE IF EXISTS `food_material`;
CREATE TABLE `food_material` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `FOOD_ID` int(11) DEFAULT NULL,
  `MATERIAL_NAME` varchar(512)  DEFAULT NULL,
  `MATERIAL_UNIT` varchar(64)  DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='食物材料表';

-- ----------------------------
-- Table structure for `food_step`
-- ----------------------------
DROP TABLE IF EXISTS `food_step`;
CREATE TABLE `food_step` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `FOOD_ID` int(11) DEFAULT NULL,
  `STEP_NUM` int(2) DEFAULT NULL,
  `STEP_INFO` varchar(1024)  DEFAULT NULL,
  `STEP_IMAGE` varchar(256)  DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='食物制作步骤表';

-- ----------------------------
-- Table structure for `user`
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `USER_NAME` varchar(128)  DEFAULT NULL,
  `NIKE_NAME` varchar(128) DEFAULT NULL,
  `PASSWORD` varchar(512)  DEFAULT NULL,
  `USER_IMAGE` varchar(512)  DEFAULT NULL,
  `GENDER` int(11) DEFAULT NULL,
  `AGE` int(11) DEFAULT NULL,
  `CREATE_TIME` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='用户表';
