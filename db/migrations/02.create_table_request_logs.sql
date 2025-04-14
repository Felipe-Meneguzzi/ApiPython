CREATE TABLE `request_logs` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(10) unsigned NOT NULL,
  `method` varchar(100) NOT NULL,
  `url` longtext NOT NULL,
  `url_params` longtext DEFAULT NULL,
  `request_body` longtext DEFAULT NULL,
  `time` datetime NOT NULL,
  `ip` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `request_logs_users_fk` (`user_id`),
  CONSTRAINT `request_logs_users_fk` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='Tabela dos logs de requisição para a API';