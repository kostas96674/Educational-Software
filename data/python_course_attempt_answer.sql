-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: python_course
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `attempt_answer`
--

DROP TABLE IF EXISTS `attempt_answer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `attempt_answer` (
  `id` int NOT NULL AUTO_INCREMENT,
  `attempt_id` int NOT NULL,
  `question_id` int NOT NULL,
  `answer_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `attempt_id` (`attempt_id`),
  KEY `question_id` (`question_id`),
  KEY `answer_id` (`answer_id`),
  CONSTRAINT `attempt_answer_ibfk_1` FOREIGN KEY (`attempt_id`) REFERENCES `attempt` (`ID`),
  CONSTRAINT `attempt_answer_ibfk_2` FOREIGN KEY (`question_id`) REFERENCES `question` (`id`),
  CONSTRAINT `attempt_answer_ibfk_3` FOREIGN KEY (`answer_id`) REFERENCES `answer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=117 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attempt_answer`
--

LOCK TABLES `attempt_answer` WRITE;
/*!40000 ALTER TABLE `attempt_answer` DISABLE KEYS */;
INSERT INTO `attempt_answer` VALUES (1,1,1,1),(2,1,2,5),(3,1,4,14),(4,1,5,17),(5,2,13,49),(6,2,14,53),(7,2,15,60),(8,2,16,64),(9,3,1,1),(10,3,2,5),(11,3,4,13),(12,3,5,17),(13,4,13,49),(14,4,14,53),(15,4,15,57),(16,4,16,61),(17,5,7,25),(18,5,8,29),(19,5,11,41),(20,5,12,45),(21,6,1,1),(22,6,2,5),(23,6,4,13),(24,6,5,17),(25,7,1,1),(26,7,2,7),(27,7,4,13),(28,7,5,17),(29,8,13,49),(30,8,14,53),(31,8,15,59),(32,8,16,63),(33,9,1,1),(34,9,2,5),(35,9,4,13),(36,9,5,17),(37,10,13,51),(38,10,14,55),(39,10,15,57),(40,10,16,61),(41,11,9,33),(42,11,10,37),(43,11,18,69),(44,11,17,65),(77,19,1,2),(78,19,2,8),(79,19,4,16),(80,19,5,17),(81,20,1,2),(82,20,2,5),(83,20,4,13),(84,20,5,17),(85,21,13,49),(86,21,14,53),(87,21,15,57),(88,21,16,61),(89,22,9,36),(90,22,10,40),(91,22,18,70),(92,22,17,67),(93,23,6,21),(94,23,19,73),(95,23,12,47),(96,23,9,34),(97,23,18,69),(98,23,16,61),(99,23,7,25),(100,23,13,49),(101,24,7,26),(102,24,8,31),(103,24,11,42),(104,24,12,48),(105,25,9,36),(106,25,10,38),(107,25,18,70),(108,25,17,67),(109,26,10,38),(110,26,8,32),(111,26,12,46),(112,26,7,27),(113,26,5,18),(114,26,16,62),(115,26,3,11),(116,26,20,77);
/*!40000 ALTER TABLE `attempt_answer` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-22 18:47:27
