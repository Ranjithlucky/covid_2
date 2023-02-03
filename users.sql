-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 02, 2023 at 12:26 PM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `covid`
--

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `continent` varchar(25) NOT NULL,
  `country` varchar(80) NOT NULL,
  `population` text NOT NULL,
  `new` text NOT NULL,
  `active` text NOT NULL,
  `critical` text NOT NULL,
  `recovered` text NOT NULL,
  `IM_pop` text NOT NULL,
  `total` text NOT NULL,
  `New_deaths` varchar(4) DEFAULT NULL,
  `Im_pop_deaths` text NOT NULL,
  `total_deaths` text NOT NULL,
  `IM_pop_tests` text NOT NULL,
  `total_tests` text NOT NULL,
  `Date` date NOT NULL DEFAULT current_timestamp(),
  `DateTime` datetime(6) NOT NULL DEFAULT current_timestamp(6)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `continent`, `country`, `population`, `new`, `active`, `critical`, `recovered`, `IM_pop`, `total`, `New_deaths`, `Im_pop_deaths`, `total_deaths`, `IM_pop_tests`, `total_tests`, `Date`, `DateTime`) VALUES
(1, 'Asia', 'Afghanistan', '40754388', '+3', '316723', '2162178', '26726', '2782872', '57216721', '34', '2672', '2277', '25267', '2526', '2023-01-18', '2023-01-18 21:12:46.159611'),
(2, 'Europe', 'Albania', '28663714', '+99', '23672378', '367378', '262728', '369', '32783', '45', '2278', '267278', '2627', '267287', '2023-01-18', '2023-01-18 21:12:46.159611'),
(3, 'africa', 'Algeria', '453524575', '+34', '378278', '2637', '2627', '2637', '262738', '65', '2672378', '5237', '267278', '27267', '2023-01-18', '2023-01-18 21:12:46.159611'),
(4, 'Oceania', 'American Samoa', '6721672378', '+34', '2627', '26727', '25347', '367', '26288', '12', '267278', '252', '2623', '267278', '2023-01-18', '2023-01-18 21:12:46.159611'),
(5, 'africa', 'Andorra', '67253873278', '+56', '262782', '86277', '2626', '26372', '2637388', '31', '436378', '36378', '2672782', '25167', '2023-01-18', '2023-01-18 21:12:46.159611'),
(6, 'Asia', 'Angola', '672672792', '+34', '2426', '265278', '256267', '26278', '21521727', '45', '2561267', '2526', '27811298', '2782192089', '2023-01-18', '2023-01-18 21:12:46.159611'),
(7, 'North-America', 'Anguilla', '89367628', '+67', '25262', '2527', '26289', '2627', '26272', '32', '23628', '26827', '27239', '292783', '2023-01-18', '2023-01-18 21:12:46.159611'),
(8, 'africa', 'Antarctica', '2672892892', '+23', '2526', '24266', '47834', '3562', '2623327', '78', '278289', '267378', '353872', '267987', '2023-01-18', '2023-01-18 21:12:46.159611'),
(9, 'Oceania', 'Antigua and Barbuda', '5624262', '+54', '256278', '25272526', '2526', '2526', '252724', '32', '3737', '7858', '378328932', '378363', '2023-01-18', '2023-01-18 21:12:46.159611'),
(10, 'africa', 'Argentina', '2672787', '+62', '25267', '56687', '12527', '28299', '28378498', '32', '367278', '236727', '3637', '37923198', '2023-01-18', '2023-01-18 21:12:46.159611');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
