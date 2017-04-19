-- setup part types
INSERT INTO `part_types` (`partName`, `price`, `startDate`, `endDate`, `deletedAt`) VALUES ('screenHigh', 5.00, datetime('now'), NULL, NULL);
INSERT INTO `part_types` (`partName`, `price`, `startDate`, `endDate`, `deletedAt`) VALUES ('screenMedium', 4.00, datetime('now'), NULL, NULL);
INSERT INTO `part_types` (`partName`, `price`, `startDate`, `endDate`, `deletedAt`) VALUES ('screenLow', 3.00, datetime('now'), NULL, NULL);
INSERT INTO `part_types` (`partName`, `price`, `startDate`, `endDate`, `deletedAt`) VALUES ('screenFlip', 2.00, datetime('now'), NULL, NULL);
INSERT INTO `part_types` (`partName`, `price`, `startDate`, `endDate`, `deletedAt`) VALUES ('screenRadiation', 100.00, datetime('now'), NULL, NULL);
INSERT INTO `part_types` (`partName`, `price`, `startDate`, `endDate`, `deletedAt`) VALUES ('batteryHigh', 5.00, datetime('now'), NULL, NULL);
INSERT INTO `part_types` (`partName`, `price`, `startDate`, `endDate`, `deletedAt`) VALUES ('batteryMedium', 4.00, datetime('now'), NULL, NULL);
INSERT INTO `part_types` (`partName`, `price`, `startDate`, `endDate`, `deletedAt`) VALUES ('batteryLow', 3.00, datetime('now'), NULL, NULL);
INSERT INTO `part_types` (`partName`, `price`, `startDate`, `endDate`, `deletedAt`) VALUES ('batteryRadiation', 120.00, datetime('now'), NULL, NULL);
INSERT INTO `part_types` (`partName`, `price`, `startDate`, `endDate`, `deletedAt`) VALUES ('memory', 5.00, datetime('now'), NULL, NULL);
INSERT INTO `part_types` (`partName`, `price`, `startDate`, `endDate`, `deletedAt`) VALUES ('memoryRadiation', 150.00, datetime('now'), NULL, NULL);

-- setup phone types
INSERT INTO `phone_types` (`phoneType`, `screenTypeId`, `batteryTypeId`, `memoryTypeId`, `description`, `imagePath`, `price`, `deletedAt`) VALUES ('High', 1, 6, 10, 'Top Tier Phone', 'static/images/high.png', 600.00, NULL);
INSERT INTO `phone_types` (`phoneType`, `screenTypeId`, `batteryTypeId`, `memoryTypeId`, `description`, `imagePath`, `price`, `deletedAt`) VALUES ('Medium', 2, 7, 10, 'Medium Tier Phone', 'static/images/medium.png', 500.00, NULL);
INSERT INTO `phone_types` (`phoneType`, `screenTypeId`, `batteryTypeId`, `memoryTypeId`, `description`, `imagePath`, `price`, `deletedAt`) VALUES ('Low', 3, 8, 10, 'Low Tier Phone', 'static/images/low.png', 300.00, NULL);
INSERT INTO `phone_types` (`phoneType`, `screenTypeId`, `batteryTypeId`, `memoryTypeId`, `description`, `imagePath`, `price`, `deletedAt`) VALUES ('Retro', 4, 8, 10, 'Retro Flip Phone for those balling on a budget.', 'static/images/retro.png', 40.00, NULL);
INSERT INTO `phone_types` (`phoneType`, `screenTypeId`, `batteryTypeId`, `memoryTypeId`, `description`, `imagePath`, `price`, `deletedAt`) VALUES ('Radiation King', 5, 9, 11, 'Radiation King: The Holographic Car Phone Model, now including a geiger counter.', 'static/images/radiation.png', 1000.00, NULL);

-- setup parts
--Phone id 1 parts high end
INSERT INTO `parts` (`modelType`, `defective`, `used`, `partTypeId`, `phoneId`, `bogo`) VALUES (1, 0, 1, 1, 1, 0);
INSERT INTO `parts` (`modelType`, `defective`, `used`, `partTypeId`, `phoneId`, `bogo`) VALUES (1, 0, 1, 4, 1, 0);
INSERT INTO `parts` (`modelType`, `defective`, `used`, `partTypeId`, `phoneId`, `bogo`) VALUES (1, 0, 1, 7, 1, 0);

--Phone id 2 parts with defective part middle end
INSERT INTO `parts` (`modelType`, `defective`, `used`, `partTypeId`, `phoneId`, `bogo`) VALUES (2, 0, 1, 5, 3, 0);
INSERT INTO `parts` (`modelType`, `defective`, `used`, `partTypeId`, `phoneId`, `bogo`) VALUES (2, 1, 1, 2, 3, 0);
INSERT INTO `parts` (`modelType`, `defective`, `used`, `partTypeId`, `phoneId`, `bogo`) VALUES (2, 0, 1, 7, 3, 0);

--Phone id 3 refurbished with broken part in db
INSERT INTO `parts` (`modelType`, `defective`, `used`, `partTypeId`, `phoneId`, `bogo`) VALUES (2, 0, 1, 5, 2, 0);
INSERT INTO `parts` (`modelType`, `defective`, `used`, `partTypeId`, `phoneId`, `bogo`) VALUES (2, 0, 1, 2, 2, 0);
INSERT INTO `parts` (`modelType`, `defective`, `used`, `partTypeId`, `phoneId`, `bogo`) VALUES (2, 0, 1, 7, 2, 0);

INSERT INTO `parts` (`modelType`, `defective`, `used`, `partTypeId`, `phoneId`, `bogo`) VALUES (2, 1, 0, 2, 2, 0);

-- setup phones
INSERT INTO `phones` (`status`,`modelId`,`saleDate`,`returnDate`,`refurbishedDate`, `bogo`) VALUES ('New', 1, datetime('now'), datetime('now'), datetime('now'),0);
INSERT INTO `phones` (`status`,`modelId`,`saleDate`,`returnDate`,`refurbishedDate`, `bogo`) VALUES ('Broken', 2, datetime('now'), datetime('now'), datetime('now'), 0);
INSERT INTO `phones` (`status`,`modelId`,`saleDate`,`returnDate`,`refurbishedDate`, `bogo`) VALUES ('Refurbished', 2, datetime('now'), datetime('now'), datetime('now'), 0);
