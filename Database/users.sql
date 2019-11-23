CREATE DATABASE IF NOT EXISTS studentup

CREATE TABLE `studentup`.`users` ( 
	`id` INT NOT NULL AUTO_INCREMENT , 
	`login` VARCHAR(15) NOT NULL , 
	`email` VARCHAR(45) NOT NULL , 
	`password` VARCHAR(256) NOT NULL , 
	`user_type` VARCHAR(10) NOT NULL , 
	PRIMARY KEY (`id`)
) ENGINE = InnoDB;
