-- setup part types
INSERT INTO `part_types` (`partName`, `price`, `startDate`, `endDate`, `deletedAt`) VALUES ('batteryHigh', 5.00, date('now'), NULL, NULL);
INSERT INTO `part_types` (`partName`, `price`, `startDate`, `endDate`, `deletedAt`) VALUES ('batteryMedium', 4.00, date('now'), NULL, NULL);
INSERT INTO `part_types` (`partName`, `price`, `startDate`, `endDate`, `deletedAt`) VALUES ('batteryLow', 3.00, date('now'), NULL, NULL);
INSERT INTO `part_types` (`partName`, `price`, `startDate`, `endDate`, `deletedAt`) VALUES ('screenHigh', 5.00, date('now'), NULL, NULL);
INSERT INTO `part_types` (`partName`, `price`, `startDate`, `endDate`, `deletedAt`) VALUES ('screenMedium', 4.00, date('now'), NULL, NULL);
INSERT INTO `part_types` (`partName`, `price`, `startDate`, `endDate`, `deletedAt`) VALUES ('screenLow', 3.00, date('now'), NULL, NULL);
INSERT INTO `part_types` (`partName`, `price`, `startDate`, `endDate`, `deletedAt`) VALUES ('screenFlip', 2.00, date('now'), NULL, NULL);
INSERT INTO `part_types` (`partName`, `price`, `startDate`, `endDate`, `deletedAt`) VALUES ('memory', 5.00, date('now'), NULL, NULL);

-- setup phone types
INSERT INTO `phone_types` (`phoneType`, `screenType`, `batteryType`, `memoryType`, `description`, `imagePath`, `price`, `deletedAt`) VALUES ('High', 4, 1, 8, 'High End Phone', 'junk/garbage.jpg', 600.00, NULL);
INSERT INTO `phone_types` (`phoneType`, `screenType`, `batteryType`, `memoryType`, `description`, `imagePath`, `price`, `deletedAt`) VALUES ('Medium', 5, 2, 8, 'Medium Tier Phone', 'moreJunk/garbage.tiff', 500.00, NULL);
INSERT INTO `phone_types` (`phoneType`, `screenType`, `batteryType`, `memoryType`, `description`, `imagePath`, `price`, `deletedAt`) VALUES ('Low', 6, 3, 8, 'Low Tier Phone', 'thisistrash/garbage.gif', 300.00, NULL);
INSERT INTO `phone_types` (`phoneType`, `screenType`, `batteryType`, `memoryType`, `description`, `imagePath`, `price`, `deletedAt`) VALUES ('Flip', 7, 3, 8, 'Flip Phone for the budget conscious buyer', 'whatsgoingon/guys.png', 40.00, NULL);
