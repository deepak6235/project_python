/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 8.0.39 : Database - health
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`health` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `health`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add doctor_table',7,'add_doctor_table'),
(26,'Can change doctor_table',7,'change_doctor_table'),
(27,'Can delete doctor_table',7,'delete_doctor_table'),
(28,'Can view doctor_table',7,'view_doctor_table'),
(29,'Can add hospital_table',8,'add_hospital_table'),
(30,'Can change hospital_table',8,'change_hospital_table'),
(31,'Can delete hospital_table',8,'delete_hospital_table'),
(32,'Can view hospital_table',8,'view_hospital_table'),
(33,'Can add login_table',9,'add_login_table'),
(34,'Can change login_table',9,'change_login_table'),
(35,'Can delete login_table',9,'delete_login_table'),
(36,'Can view login_table',9,'view_login_table'),
(37,'Can add user_table',10,'add_user_table'),
(38,'Can change user_table',10,'change_user_table'),
(39,'Can delete user_table',10,'delete_user_table'),
(40,'Can view user_table',10,'view_user_table'),
(41,'Can add test_table',11,'add_test_table'),
(42,'Can change test_table',11,'change_test_table'),
(43,'Can delete test_table',11,'delete_test_table'),
(44,'Can view test_table',11,'view_test_table'),
(45,'Can add schedule_table',12,'add_schedule_table'),
(46,'Can change schedule_table',12,'change_schedule_table'),
(47,'Can delete schedule_table',12,'delete_schedule_table'),
(48,'Can view schedule_table',12,'view_schedule_table'),
(49,'Can add review_table',13,'add_review_table'),
(50,'Can change review_table',13,'change_review_table'),
(51,'Can delete review_table',13,'delete_review_table'),
(52,'Can view review_table',13,'view_review_table'),
(53,'Can add prescription_table',14,'add_prescription_table'),
(54,'Can change prescription_table',14,'change_prescription_table'),
(55,'Can delete prescription_table',14,'delete_prescription_table'),
(56,'Can view prescription_table',14,'view_prescription_table'),
(57,'Can add diet_plan_table',15,'add_diet_plan_table'),
(58,'Can change diet_plan_table',15,'change_diet_plan_table'),
(59,'Can delete diet_plan_table',15,'delete_diet_plan_table'),
(60,'Can view diet_plan_table',15,'view_diet_plan_table'),
(61,'Can add complaint_table',16,'add_complaint_table'),
(62,'Can change complaint_table',16,'change_complaint_table'),
(63,'Can delete complaint_table',16,'delete_complaint_table'),
(64,'Can view complaint_table',16,'view_complaint_table'),
(65,'Can add booking_table',17,'add_booking_table'),
(66,'Can change booking_table',17,'change_booking_table'),
(67,'Can delete booking_table',17,'delete_booking_table'),
(68,'Can view booking_table',17,'view_booking_table');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(17,'Healthify','booking_table'),
(16,'Healthify','complaint_table'),
(15,'Healthify','diet_plan_table'),
(7,'Healthify','doctor_table'),
(8,'Healthify','hospital_table'),
(9,'Healthify','login_table'),
(14,'Healthify','prescription_table'),
(13,'Healthify','review_table'),
(12,'Healthify','schedule_table'),
(11,'Healthify','test_table'),
(10,'Healthify','user_table'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'Healthify','0001_initial','2024-09-28 10:19:20.293032'),
(2,'contenttypes','0001_initial','2024-09-28 10:19:20.354355'),
(3,'auth','0001_initial','2024-09-28 10:19:21.118764'),
(4,'admin','0001_initial','2024-09-28 10:19:21.304063'),
(5,'admin','0002_logentry_remove_auto_add','2024-09-28 10:19:21.314854'),
(6,'admin','0003_logentry_add_action_flag_choices','2024-09-28 10:19:21.323927'),
(7,'contenttypes','0002_remove_content_type_name','2024-09-28 10:19:21.422401'),
(8,'auth','0002_alter_permission_name_max_length','2024-09-28 10:19:21.501934'),
(9,'auth','0003_alter_user_email_max_length','2024-09-28 10:19:21.526687'),
(10,'auth','0004_alter_user_username_opts','2024-09-28 10:19:21.537358'),
(11,'auth','0005_alter_user_last_login_null','2024-09-28 10:19:21.609020'),
(12,'auth','0006_require_contenttypes_0002','2024-09-28 10:19:21.614732'),
(13,'auth','0007_alter_validators_add_error_messages','2024-09-28 10:19:21.625307'),
(14,'auth','0008_alter_user_username_max_length','2024-09-28 10:19:21.712563'),
(15,'auth','0009_alter_user_last_name_max_length','2024-09-28 10:19:21.796149'),
(16,'auth','0010_alter_group_name_max_length','2024-09-28 10:19:21.819806'),
(17,'auth','0011_update_proxy_permissions','2024-09-28 10:19:21.833232'),
(18,'auth','0012_alter_user_first_name_max_length','2024-09-28 10:19:21.917878'),
(19,'sessions','0001_initial','2024-09-28 10:19:21.968015'),
(20,'Healthify','0002_alter_doctor_table_hospital','2024-09-30 10:26:39.605583'),
(21,'Healthify','0003_alter_doctor_table_hospital','2024-09-30 10:27:21.304581'),
(22,'Healthify','0004_alter_prescription_table_booking','2024-10-26 10:57:44.990840'),
(23,'Healthify','0005_auto_20241026_1627','2024-10-26 10:57:45.124815'),
(24,'Healthify','0006_diet_plan_table_prescription_table','2024-10-26 10:57:57.190245');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('9wr0o25jjp9icvybozb40tz350n9k31m','eyJsaWQiOjQyLCJkaWQiOjh9:1svKj4:P4c-YG5_d6XNENFXQauxeolyL-nOvs7Q1UszjTWLpg4','2024-10-14 18:02:26.589423'),
('frl1kkkc46slt7dc0wwvwnug0af1yv4i','eyJsaWQiOjMsImRpZCI6Mn0:1sunmL:9gFf-s9hlCqjAY6lSfzia2OWAtSyvutkgy5Ae_uOoVQ','2024-10-13 06:51:37.905781'),
('vmz0j0jaw7zajjc9pxgpn5zrsifscftt','eyJsaWQiOjQyLCJkaWQiOjd9:1svJQI:iG9W8rhk0T52V5UYX3CqiK6P9juD2rjCxD1WcG5Yqkw','2024-10-14 16:38:58.153506'),
('y2vkvgok60i01kfb1irx1fumb5l47x66','.eJyrVsrJTFGyMjHSUUoBMZTMlYAsKJ0EFjFRqgUAvKwJRg:1t4ebr:DcUn8cyyrNaRhLWWjWbQ6RNNMVJ7wLplmwzkSkXfYpM','2024-11-09 11:05:31.724299');

/*Table structure for table `healthify_booking_table` */

DROP TABLE IF EXISTS `healthify_booking_table`;

CREATE TABLE `healthify_booking_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `status` varchar(90) NOT NULL,
  `date` date NOT NULL,
  `SCHEDULE_id` bigint NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Healthify_booking_ta_SCHEDULE_id_4755b80d_fk_Healthify` (`SCHEDULE_id`),
  KEY `Healthify_booking_ta_USER_id_20539d36_fk_Healthify` (`USER_id`),
  CONSTRAINT `Healthify_booking_ta_SCHEDULE_id_4755b80d_fk_Healthify` FOREIGN KEY (`SCHEDULE_id`) REFERENCES `healthify_schedule_table` (`id`),
  CONSTRAINT `Healthify_booking_ta_USER_id_20539d36_fk_Healthify` FOREIGN KEY (`USER_id`) REFERENCES `healthify_user_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `healthify_booking_table` */

insert  into `healthify_booking_table`(`id`,`status`,`date`,`SCHEDULE_id`,`USER_id`) values 
(4,'availbale','2024-09-02',7,2),
(5,'available','2024-10-26',6,1),
(7,'available','2024-09-09',8,1);

/*Table structure for table `healthify_complaint_table` */

DROP TABLE IF EXISTS `healthify_complaint_table`;

CREATE TABLE `healthify_complaint_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `complaint` varchar(90) NOT NULL,
  `reply` varchar(90) NOT NULL,
  `date` date NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Healthify_complaint__USER_id_212c3cda_fk_Healthify` (`USER_id`),
  CONSTRAINT `Healthify_complaint__USER_id_212c3cda_fk_Healthify` FOREIGN KEY (`USER_id`) REFERENCES `healthify_user_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `healthify_complaint_table` */

insert  into `healthify_complaint_table`(`id`,`complaint`,`reply`,`date`,`USER_id`) values 
(2,'DEMO','Ok sett akkitt ind','2024-09-10',1);

/*Table structure for table `healthify_diet_plan_table` */

DROP TABLE IF EXISTS `healthify_diet_plan_table`;

CREATE TABLE `healthify_diet_plan_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `test_name` varchar(90) NOT NULL,
  `date` date NOT NULL,
  `BOOKING_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Healthify_diet_plan__BOOKING_id_d66b14ea_fk_Healthify` (`BOOKING_id`),
  CONSTRAINT `Healthify_diet_plan__BOOKING_id_d66b14ea_fk_Healthify` FOREIGN KEY (`BOOKING_id`) REFERENCES `healthify_booking_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `healthify_diet_plan_table` */

/*Table structure for table `healthify_doctor_table` */

DROP TABLE IF EXISTS `healthify_doctor_table`;

CREATE TABLE `healthify_doctor_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(90) NOT NULL,
  `email` varchar(80) NOT NULL,
  `phone` bigint NOT NULL,
  `image` varchar(100) NOT NULL,
  `department` varchar(90) NOT NULL,
  `qualification` varchar(80) NOT NULL,
  `experience` int NOT NULL,
  `HOSPITAL_id` bigint NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Healthify_doctor_tab_HOSPITAL_id_ddc2b943_fk_Healthify` (`HOSPITAL_id`),
  KEY `Healthify_doctor_tab_LOGIN_id_8054365b_fk_Healthify` (`LOGIN_id`),
  CONSTRAINT `Healthify_doctor_tab_HOSPITAL_id_ddc2b943_fk_Healthify` FOREIGN KEY (`HOSPITAL_id`) REFERENCES `healthify_hospital_table` (`id`),
  CONSTRAINT `Healthify_doctor_tab_LOGIN_id_8054365b_fk_Healthify` FOREIGN KEY (`LOGIN_id`) REFERENCES `healthify_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `healthify_doctor_table` */

insert  into `healthify_doctor_table`(`id`,`name`,`email`,`phone`,`image`,`department`,`qualification`,`experience`,`HOSPITAL_id`,`LOGIN_id`) values 
(3,'sheha','sheha@gmail.com',9656542932,'WIN_20240928_17_00_14_Pro_nuzWhss.jpg','dermatology','mbbs,mba',4,4,23),
(7,'ajmal','ajmal1@gmail.com',702581556555,'WIN_20240930_11_49_35_Pro.jpg','ENT','mbbs',2,1,42),
(8,'rajappvbvb','rajappan@gmail.com',98765462791,'WIN_20240930_11_49_52_Pro.jpg','Lungs','+2',1,4,43);

/*Table structure for table `healthify_hospital_table` */

DROP TABLE IF EXISTS `healthify_hospital_table`;

CREATE TABLE `healthify_hospital_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(90) NOT NULL,
  `email` varchar(90) NOT NULL,
  `website` varchar(90) NOT NULL,
  `contactno` bigint NOT NULL,
  `place` varchar(90) NOT NULL,
  `pin` int NOT NULL,
  `post` varchar(90) NOT NULL,
  `latitude` double NOT NULL,
  `longitude` double NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Healthify_hospital_t_LOGIN_id_b8332852_fk_Healthify` (`LOGIN_id`),
  CONSTRAINT `Healthify_hospital_t_LOGIN_id_b8332852_fk_Healthify` FOREIGN KEY (`LOGIN_id`) REFERENCES `healthify_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `healthify_hospital_table` */

insert  into `healthify_hospital_table`(`id`,`name`,`email`,`website`,`contactno`,`place`,`pin`,`post`,`latitude`,`longitude`,`LOGIN_id`) values 
(1,'sanil','discosheha@gmail.com','www.discosheha.com',9656542932,'mukkal kinar',673028,'arakkimar',106,102,2),
(4,'ajmal memorial','aju@gmail.com','www.aju.com',3456789098,'koduvally',3456,'peruvayi',567,783,22);

/*Table structure for table `healthify_login_table` */

DROP TABLE IF EXISTS `healthify_login_table`;

CREATE TABLE `healthify_login_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(90) NOT NULL,
  `password` varchar(80) NOT NULL,
  `type` varchar(80) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `healthify_login_table` */

insert  into `healthify_login_table`(`id`,`username`,`password`,`type`) values 
(1,'admin','admin','admin'),
(2,'hospital','123','hospital'),
(20,'hs','123','hospital'),
(22,'aju memorial','aju','hospital'),
(23,'disco','disco','doctor'),
(24,'user','user','user'),
(39,'sheha','123','doctor'),
(42,'aju','123','doctor'),
(43,'rajappan','123','doctor');

/*Table structure for table `healthify_prescription_table` */

DROP TABLE IF EXISTS `healthify_prescription_table`;

CREATE TABLE `healthify_prescription_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `prescription` varchar(90) NOT NULL,
  `date` date NOT NULL,
  `BOOKING_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Healthify_prescripti_BOOKING_id_fa3df0d3_fk_Healthify` (`BOOKING_id`),
  CONSTRAINT `Healthify_prescripti_BOOKING_id_fa3df0d3_fk_Healthify` FOREIGN KEY (`BOOKING_id`) REFERENCES `healthify_booking_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `healthify_prescription_table` */

insert  into `healthify_prescription_table`(`id`,`prescription`,`date`,`BOOKING_id`) values 
(1,'hh','2024-10-26',4);

/*Table structure for table `healthify_review_table` */

DROP TABLE IF EXISTS `healthify_review_table`;

CREATE TABLE `healthify_review_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `review` varchar(90) NOT NULL,
  `rating` varchar(90) NOT NULL,
  `date` date NOT NULL,
  `HOSPITAL_id` bigint NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Healthify_review_tab_HOSPITAL_id_0059654c_fk_Healthify` (`HOSPITAL_id`),
  KEY `Healthify_review_tab_USER_id_80deff97_fk_Healthify` (`USER_id`),
  CONSTRAINT `Healthify_review_tab_HOSPITAL_id_0059654c_fk_Healthify` FOREIGN KEY (`HOSPITAL_id`) REFERENCES `healthify_hospital_table` (`id`),
  CONSTRAINT `Healthify_review_tab_USER_id_80deff97_fk_Healthify` FOREIGN KEY (`USER_id`) REFERENCES `healthify_user_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `healthify_review_table` */

insert  into `healthify_review_table`(`id`,`review`,`rating`,`date`,`HOSPITAL_id`,`USER_id`) values 
(1,'good','4','2024-09-04',4,1),
(2,'bad','8','2024-09-25',1,2);

/*Table structure for table `healthify_schedule_table` */

DROP TABLE IF EXISTS `healthify_schedule_table`;

CREATE TABLE `healthify_schedule_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `fromtime` time(6) NOT NULL,
  `totime` time(6) NOT NULL,
  `DOCTOR_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Healthify_schedule_t_DOCTOR_id_23909def_fk_Healthify` (`DOCTOR_id`),
  CONSTRAINT `Healthify_schedule_t_DOCTOR_id_23909def_fk_Healthify` FOREIGN KEY (`DOCTOR_id`) REFERENCES `healthify_doctor_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `healthify_schedule_table` */

insert  into `healthify_schedule_table`(`id`,`date`,`fromtime`,`totime`,`DOCTOR_id`) values 
(5,'2024-09-02','03:24:00.000000','18:24:00.000000',3),
(6,'2024-09-03','03:24:00.000000','18:24:00.000000',3),
(7,'2024-09-02','01:53:00.000000','06:53:00.000000',7),
(8,'2024-09-09','01:53:00.000000','06:53:00.000000',7);

/*Table structure for table `healthify_test_table` */

DROP TABLE IF EXISTS `healthify_test_table`;

CREATE TABLE `healthify_test_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `test_name` varchar(90) NOT NULL,
  `result` varchar(90) NOT NULL,
  `date` date NOT NULL,
  `BOOKING_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Healthify_test_table_BOOKING_id_213c2ca6_fk_Healthify` (`BOOKING_id`),
  CONSTRAINT `Healthify_test_table_BOOKING_id_213c2ca6_fk_Healthify` FOREIGN KEY (`BOOKING_id`) REFERENCES `healthify_user_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `healthify_test_table` */

/*Table structure for table `healthify_user_table` */

DROP TABLE IF EXISTS `healthify_user_table`;

CREATE TABLE `healthify_user_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(90) NOT NULL,
  `email` varchar(80) NOT NULL,
  `place` varchar(90) NOT NULL,
  `dob` date NOT NULL,
  `phone` bigint NOT NULL,
  `pin` int NOT NULL,
  `post` varchar(90) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Healthify_user_table_LOGIN_id_1ba8e069_fk_Healthify` (`LOGIN_id`),
  CONSTRAINT `Healthify_user_table_LOGIN_id_1ba8e069_fk_Healthify` FOREIGN KEY (`LOGIN_id`) REFERENCES `healthify_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `healthify_user_table` */

insert  into `healthify_user_table`(`id`,`name`,`email`,`place`,`dob`,`phone`,`pin`,`post`,`LOGIN_id`) values 
(1,'shafi','shafi@gmail.com','kuttikattoor','2004-06-26',987654321,5678,'kozhikode',24),
(2,'rafiya','rafi@gmail.com','adivaram','2004-06-15',345678987,8797,'calicut',2);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
