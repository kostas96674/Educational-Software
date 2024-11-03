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
-- Table structure for table `answer`
--

DROP TABLE IF EXISTS `answer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `answer` (
  `id` int NOT NULL AUTO_INCREMENT,
  `correct` tinyint(1) NOT NULL,
  `text` text NOT NULL,
  `question_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `question_id` (`question_id`),
  CONSTRAINT `answer_ibfk_1` FOREIGN KEY (`question_id`) REFERENCES `question` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=81 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `answer`
--

LOCK TABLES `answer` WRITE;
/*!40000 ALTER TABLE `answer` DISABLE KEYS */;
INSERT INTO `answer` VALUES (1,1,'age = 25',1),(2,0,'int age = 25',1),(3,0,'age := 25',1),(4,0,'declare age = 25',1),(5,1,'x = 10',2),(6,0,'x := 10',2),(7,0,'int x = 10',2),(8,0,'change x to 10',2),(9,1,'if x > 0: print(\"x is positive\")',3),(10,0,'if (x > 0) print(\"x is positive\")',3),(11,0,'if x > 0 then print(\"x is positive\")',3),(12,0,'if x > 0 { print(\"x is positive\") }',3),(13,1,'elif checks another condition, else does not',4),(14,0,'elif and else are identical',4),(15,0,'elif is used to end the program, else is not',4),(16,0,'elif runs only if else is True',4),(17,1,'for fruit in fruits: print(fruit)',5),(18,0,'for (fruit: fruits) { print(fruit) }',5),(19,0,'for fruit of fruits { print(fruit) }',5),(20,0,'foreach fruit in fruits: print(fruit)',5),(21,1,'for loops iterate over a sequence, while loops run until a condition is met',6),(22,0,'for loops run indefinitely, while loops do not',6),(23,0,'for loops can only iterate over numbers, while loops can iterate over anything',6),(24,0,'for loops are used for infinite loops, while loops are not',6),(25,1,'s[0]',7),(26,0,'s(0)',7),(27,0,'s.first()',7),(28,0,'s[1]',7),(29,1,'s[7:12]',8),(30,0,'s[6:11]',8),(31,0,'s(7, 12)',8),(32,0,'s.slice(7, 12)',8),(33,1,'my_dict[\"age\"] = 25',9),(34,0,'my_dict.add(\"age\", 25)',9),(35,0,'my_dict[\"age\"] := 25',9),(36,0,'my_dict.insert(\"age\", 25)',9),(37,1,'my_dict.get(\"name\", \"Unknown\")',10),(38,0,'my_dict.get(\"name\")',10),(39,0,'my_dict[\"name\"].get(\"Unknown\")',10),(40,0,'my_dict.fetch(\"name\", \"Unknown\")',10),(41,1,'Pto rgamn',11),(42,0,'Pyto rgamn',11),(43,0,'Pto rgan',11),(44,0,'Python Programming',11),(45,1,'s[::-1]',12),(46,0,'reverse(s)',12),(47,0,'s.reverse()',12),(48,0,'reversed(s)',12),(49,1,'def function_name():',13),(50,0,'function function_name():',13),(51,0,'define function_name():',13),(52,0,'func function_name():',13),(53,1,'Hello, World! and Hello, Alice!',14),(54,0,'Hello, ! and Hello, Alice!',14),(55,0,'Hello, World! and Hello, World!',14),(56,0,'Hello, Alice! and Hello, Alice!',14),(57,1,'120',15),(58,0,'24',15),(59,0,'5',15),(60,0,'None',15),(61,1,'5',16),(62,0,'8',16),(63,0,'13',16),(64,0,'21',16),(65,1,'\'key\' in my_dict',17),(66,0,'my_dict.has_key(\'key\')',17),(67,0,'exists(\'key\', my_dict)',17),(68,0,'my_dict.contains(\'key\')',17),(69,1,'3',18),(70,0,'2',18),(71,0,'1',18),(72,0,'0',18),(73,1,'(2, 3)',19),(74,0,'(1, 2)',19),(75,0,'(3, 4)',19),(76,0,'(2, 3, 4)',19),(77,1,'No, tuples are immutable.',20),(78,0,'Yes, tuples are mutable.',20),(79,0,'Only if the element is an integer.',20),(80,0,'Only if the element is a string.',20);
/*!40000 ALTER TABLE `answer` ENABLE KEYS */;
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
