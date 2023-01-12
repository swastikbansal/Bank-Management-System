-- ----------------------------------------------------------------------------
-- MySQL Workbench Migration
-- Migrated Schemata: banking
-- Source Schemata: banking
-- Created: Tue Feb  1 16:46:06 2022
-- Workbench Version: 8.0.27
-- ----------------------------------------------------------------------------

SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------------------------------------------------------
-- Schema banking
-- ----------------------------------------------------------------------------
DROP SCHEMA IF EXISTS `banking` ;
CREATE SCHEMA IF NOT EXISTS `banking` ;

-- ----------------------------------------------------------------------------
-- Table banking.clients_data
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `banking`.`clients_data` (
  `Name` VARCHAR(40) NOT NULL,
  `PIN` INT NULL DEFAULT NULL,
  `Balance` INT NULL DEFAULT NULL,
  PRIMARY KEY (`Name`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;
SET FOREIGN_KEY_CHECKS = 1;
