CREATE TABLE `users` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `login` varchar(100) NOT NULL,
  `password` longtext NOT NULL,
  `user_type` INT UNSIGNED NOT NULL,
  `active` tinyint(1) NOT NULL DEFAULT 1,
  UNIQUE KEY `users_unique` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=106 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='Tabela dos usuarios utilizadores da API';