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
-- Table structure for table `question`
--

DROP TABLE IF EXISTS `question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `question` (
  `id` int NOT NULL AUTO_INCREMENT,
  `text` text NOT NULL,
  `difficulty` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question`
--

LOCK TABLES `question` WRITE;
/*!40000 ALTER TABLE `question` DISABLE KEYS */;
INSERT INTO `question` VALUES (1,'What is the correct way to declare a variable named age with the value 25 in Python?','Easy'),(2,'In Python, how do you change the value of an existing variable x to 10?','Easy'),(3,'Write an if statement that prints \"x is positive\" if the variable x is greater than 0.','Easy'),(4,'How does the elif statement differ from the else statement in Python?','Medium'),(5,'Write a for loop that prints all the elements in the list fruits = [\"apple\", \"banana\", \"cherry\"].','Easy'),(6,'What is the difference between a for loop and a while loop in Python?','Medium'),(7,'How do you access the first character of a string s = \"Hello\"?','Easy'),(8,'Explain string slicing with an example to extract \"World\" from the string s = \"Hello, World!\".','Medium'),(9,'How do you add a new key-value pair to a dictionary my_dict = {\"name\": \"Alice\"}?','Easy'),(10,'Explain the use of the get() method in dictionaries with an example.','Medium'),(11,'What is the output of the following code snippet? s = \"Python Programming\" print(s[::2])','Medium'),(12,'How can you reverse the string s = \"Hello, World!\" in Python?','Easy'),(13,'How do you define a function in Python?','Easy'),(14,'What will be printed by the following function calls? def greet(name=\"World\"): print(f\"Hello, {name}!\") greet() greet(\"Alice\")','Medium'),(15,'What is the result of calling factorial(5) given the following function? def factorial(n): if n == 1: return 1 else: return n * factorial(n - 1)','Hard'),(16,'What is the value of fibonacci(6) using the following recursive function? def fibonacci(n): if n <= 0: return \"Input should be a positive integer\" elif n == 1: return 0 elif n == 2: return 1 else: return fibonacci(n-1) + fibonacci(n-2)','Hard'),(17,'How do you check if a key exists in a dictionary my_dict?','Easy'),(18,'What is the output of the following code snippet? my_dict = {\"a\": 1, \"b\": 2, \"c\": 3} my_dict[\"b\"] = my_dict.get(\"b\", 0) + 1 print(my_dict[\"b\"])','Medium'),(19,'What will be the output of the following code snippet? my_tuple = (1, 2, 3, 4) print(my_tuple[1:3])','Medium'),(20,'Can you change the value of an element in a tuple in Python?','Easy');
/*!40000 ALTER TABLE `question` ENABLE KEYS */;
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
