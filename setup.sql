-- setup part types
INSERT INTO `part_types` (`partName`, `price`, `startDate`, `endDate`, `deletedAt`) VALUES ('batteryHigh', 5.00, datetime('now'), NULL, NULL);
INSERT INTO `part_types` (`partName`, `price`, `startDate`, `endDate`, `deletedAt`) VALUES ('batteryMedium', 4.00, datetime('now'), NULL, NULL);
INSERT INTO `part_types` (`partName`, `price`, `startDate`, `endDate`, `deletedAt`) VALUES ('batteryLow', 3.00, datetime('now'), NULL, NULL);
INSERT INTO `part_types` (`partName`, `price`, `startDate`, `endDate`, `deletedAt`) VALUES ('screenHigh', 5.00, datetime('now'), NULL, NULL);
INSERT INTO `part_types` (`partName`, `price`, `startDate`, `endDate`, `deletedAt`) VALUES ('screenMedium', 4.00, datetime('now'), NULL, NULL);
INSERT INTO `part_types` (`partName`, `price`, `startDate`, `endDate`, `deletedAt`) VALUES ('screenLow', 3.00, datetime('now'), NULL, NULL);
INSERT INTO `part_types` (`partName`, `price`, `startDate`, `endDate`, `deletedAt`) VALUES ('screenFlip', 2.00, datetime('now'), NULL, NULL);
INSERT INTO `part_types` (`partName`, `price`, `startDate`, `endDate`, `deletedAt`) VALUES ('memory', 5.00, datetime('now'), NULL, NULL);

-- setup phone types
INSERT INTO `phone_types` (`phoneType`, `screenTypeId`, `batteryTypeId`, `memoryTypeId`, `description`, `imagePath`, `price`, `deletedAt`) VALUES ('High', 4, 1, 8, 'High End Phone', 'junk/garbage.jpg', 600.00, NULL);
INSERT INTO `phone_types` (`phoneType`, `screenTypeId`, `batteryTypeId`, `memoryTypeId`, `description`, `imagePath`, `price`, `deletedAt`) VALUES ('Medium', 5, 2, 8, 'Medium Tier Phone', 'moreJunk/garbage.tiff', 500.00, NULL);
INSERT INTO `phone_types` (`phoneType`, `screenTypeId`, `batteryTypeId`, `memoryTypeId`, `description`, `imagePath`, `price`, `deletedAt`) VALUES ('Low', 6, 3, 8, 'Low Tier Phone', 'thisistrash/garbage.gif', 300.00, NULL);
INSERT INTO `phone_types` (`phoneType`, `screenTypeId`, `batteryTypeId`, `memoryTypeId`, `description`, `imagePath`, `price`, `deletedAt`) VALUES ('Flip', 7, 3, 8, 'Flip Phone for the budget conscious buyer', 'whatsgoingon/guys.png', 40.00, NULL);


-- setup parts
INSERT INTO `parts` (`modelType`, `defective`, `used`, `partTypeId`, `phoneId`) VALUES (1, 0, 0, 1, NULL);
INSERT INTO `parts` (`modelType`, `defective`, `used`, `partTypeId`, `phoneId`) VALUES (2, 1, 0, 5, 3);
INSERT INTO `parts` (`modelType`, `defective`, `used`, `partTypeId`, `phoneId`) VALUES (4, 0, 1, 7, 5);
INSERT INTO `parts` (`modelType`, `defective`, `used`, `partTypeId`, `phoneId`) VALUES (3, 1, 1, 3, 4);
INSERT INTO `parts` (`modelType`, `defective`, `used`, `partTypeId`, `phoneId`) VALUES (3, 1, 0, 6, 2);
INSERT INTO `parts` (`modelType`, `defective`, `used`, `partTypeId`, `phoneId`) VALUES (2, 0, 1, 5, 3);
INSERT INTO `parts` (`modelType`, `defective`, `used`, `partTypeId`, `phoneId`) VALUES (4, 0, 0, 8, 5);
INSERT INTO `parts` (`modelType`, `defective`, `used`, `partTypeId`, `phoneId`) VALUES (2, 1, 0, 2, 3);
INSERT INTO `parts` (`modelType`, `defective`, `used`, `partTypeId`, `phoneId`) VALUES (1, 0, 0, 4, 1);

-- setup phones
INSERT INTO `phones` (`status`,`modelId`,`saleDate`,`returnDate`,`refurbishedDate`) VALUES ('New', 1, datetime('now'), datetime('now'), datetime('now'));
INSERT INTO `phones` (`status`,`modelId`,`saleDate`,`returnDate`,`refurbishedDate`) VALUES ('Broken', 3, datetime('now'), datetime('now'), datetime('now'));
INSERT INTO `phones` (`status`,`modelId`,`saleDate`,`returnDate`,`refurbishedDate`) VALUES ('Refurbished', 2, datetime('now'), datetime('now'), datetime('now'));
INSERT INTO `phones` (`status`,`modelId`,`saleDate`,`returnDate`,`refurbishedDate`) VALUES ('Broken', 3, datetime('now'), datetime('now'), datetime('now'));
INSERT INTO `phones` (`status`,`modelId`,`saleDate`,`returnDate`,`refurbishedDate`) VALUES ('New', 4, datetime('now'), datetime('now'), datetime('now'));

