
INSERT INTO usuarios (id, username, role) VALUES
(1, 'admin_geral', 'admin'),
(2, 'analista_dados', 'analyst'),
(3, 'db_manutencao', 'db_maintainer'),
(4, 'dev_ops', 'dev_ops');

INSERT INTO acessos (id, usuario_id, evento, query_text, timestamp) VALUES
(1, 1, 'LOGIN', NULL, '2025-10-10 00:05:00'),
(2, 2, 'QUERY', 'SELECT * FROM relatorios;', '2025-10-10 00:10:00'),
(3, 3, 'LOGIN', NULL, '2025-10-10 01:30:00'),
(4, 3, 'DELETE', 'DELETE FROM logs WHERE old_data;', '2025-10-10 01:45:00'),
(5, 4, 'LOGIN', NULL, '2025-10-10 02:00:00'),
(6, 4, 'DROP', 'DROP TABLE temp_data;', '2025-10-10 02:15:00'),
(7, 1, 'QUERY', 'SELECT count(*) FROM usuarios;', '2025-10-10 03:00:00'),
(8, 3, 'DELETE', 'DELETE FROM cache;', '2025-10-10 03:30:00'),
(9, 4, 'DROP', 'DROP INDEX idx_old;', '2025-10-10 03:45:00');

INSERT INTO jobs (id, nome, usuario_id, tipo, horario_cron, ultima_execucao) VALUES
(1, 'Backup Diário', 1, 'Backup', '0 0 2 * * *', '2025-10-10 02:00:00'),
(2, 'Limpeza de Logs', 3, 'Maintenance', '0 30 1 * * *', '2025-10-10 01:30:00'),
(3, 'Otimização de Banco', 4, 'Maintenance', '0 15 2 * * *', '2025-10-10 02:15:00');

INSERT INTO alerts (id, nivel, mensagem, timestamp) VALUES
(1, 'INFO', 'Sistema inicializado.', '2025-10-10 00:00:00'),
(2, 'WARNING', 'Pico de acessos detectado.', '2025-10-10 01:00:00'),
(3, 'CRITICAL', 'Servidor corrompido. Erro de disco.', '2025-10-10 04:00:00');

