-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 11, 2024 at 07:13 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bmi`
--

-- --------------------------------------------------------

--
-- Table structure for table `food`
--

CREATE TABLE `food` (
  `id` int(100) NOT NULL,
  `nama` varchar(200) NOT NULL,
  `kalori` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `food`
--

INSERT INTO `food` (`id`, `nama`, `kalori`) VALUES
(100, 'Nasi Putih', 200),
(101, 'Ayam Goreng', 246),
(102, 'Tempe Goreng', 193),
(103, 'Sate Ayam', 310),
(104, 'Gado-Gado', 330),
(105, 'Bakso', 225),
(106, 'Rendang Daging', 312),
(107, 'Mie Goreng', 400),
(108, 'Tahu Isi Goreng', 120),
(109, 'Pisang Goreng', 140);

-- --------------------------------------------------------

--
-- Table structure for table `intake`
--

CREATE TABLE `intake` (
  `id` int(30) NOT NULL,
  `id_user` int(100) UNSIGNED NOT NULL,
  `time` datetime NOT NULL DEFAULT current_timestamp(),
  `food` varchar(100) NOT NULL,
  `serving` int(30) NOT NULL,
  `calories` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `intake`
--

INSERT INTO `intake` (`id`, `id_user`, `time`, `food`, `serving`, `calories`) VALUES
(1, 2, '2024-06-11 09:00:05', 'Ayam Goreng', 3, 738),
(2, 2, '2024-06-11 09:47:45', 'Tempe Goreng', 2, 386),
(3, 2, '2024-06-11 09:55:09', 'Sate Ayam', 3, 930),
(4, 2, '2024-06-11 10:09:49', 'Gado-Gado', 1, 330),
(5, 2, '2024-06-11 10:11:28', 'Sate Ayam', 2, 620),
(6, 2, '2024-06-11 10:37:01', 'Bakso', 2, 450);

-- --------------------------------------------------------

--
-- Table structure for table `user_data`
--

CREATE TABLE `user_data` (
  `id` int(100) UNSIGNED NOT NULL,
  `nama` varchar(200) NOT NULL,
  `height` int(20) NOT NULL,
  `weight` int(30) NOT NULL,
  `age` datetime NOT NULL,
  `gender` varchar(30) NOT NULL,
  `activity` varchar(40) NOT NULL,
  `bmr` float NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user_data`
--

INSERT INTO `user_data` (`id`, `nama`, `height`, `weight`, `age`, `gender`, `activity`, `bmr`, `password`) VALUES
(1, 'alfiatul@gmail.com', 140, 30, '0000-00-00 00:00:00', 'Wanita', 'Jarang', 1072.12, ''),
(2, 'alfi', 150, 50, '0000-00-00 00:00:00', 'Wanita', 'Jarang', 1288.04, '1234567'),
(3, 'alg', 130, 50, '0000-00-00 00:00:00', 'Pria', 'Jarang', 1155, '123456'),
(4, 'alfi@email.com', 140, 50, '0000-00-00 00:00:00', 'Wanita', 'Keaktifan', 1283.04, '1234567'),
(5, 'alfi', 160, 40, '0000-00-00 00:00:00', 'Wanita', 'Jarang', 1222.22, '12345'),
(6, 'gia', 150, 50, '2003-12-02 00:00:00', 'Wanita', 'Jarang', 1712.4, '12345'),
(7, 'wais', 150, 40, '2003-12-02 00:00:00', 'Wanita', 'Tidak Pernah Olahraga', 1465.92, '12345'),
(8, 'aji', 160, 40, '2003-12-02 00:00:00', 'Wanita', 'Sering', 1736.14, '123456');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `food`
--
ALTER TABLE `food`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `intake`
--
ALTER TABLE `intake`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_user` (`id_user`);

--
-- Indexes for table `user_data`
--
ALTER TABLE `user_data`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `food`
--
ALTER TABLE `food`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=110;

--
-- AUTO_INCREMENT for table `intake`
--
ALTER TABLE `intake`
  MODIFY `id` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `user_data`
--
ALTER TABLE `user_data`
  MODIFY `id` int(100) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `intake`
--
ALTER TABLE `intake`
  ADD CONSTRAINT `fk_user` FOREIGN KEY (`id_user`) REFERENCES `user_data` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
