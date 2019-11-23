CREATE DATABASE IF NOT EXISTS studentup

CREATE TABLE `studentup`.`fileswithpath` ( 
	`id` INT NOT NULL AUTO_INCREMENT , 
	`name` VARCHAR(80) NOT NULL , 
	`pathToFile` VARCHAR(100) NOT NULL , 
	`descryption` VARCHAR(500) NOT NULL , 
	`login` VARCHAR(15) NOT NULL , 
	`status` VARCHAR(30) NOT NULL , 
	PRIMARY KEY (`id`)
) ENGINE = InnoDB;
