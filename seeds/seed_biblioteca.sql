
INSERT INTO leitores (id, nome, email) VALUES
(1, 'Alice Silva', 'alice.silva@email.com'),
(2, 'Bruno Costa', 'bruno.costa@email.com'),
(3, 'Carla Dias', 'carla.dias@email.com'),
(4, 'Daniel Rocha', 'daniel.rocha@email.com'),
(5, 'Eva Lima', 'eva.lima@email.com');

INSERT INTO livros (id, titulo, autor, edicao) VALUES
(101, 'A História dos Bancos de Dados', 'Dr. Data', 1),
(102, 'SQL para Iniciantes', 'Ana Query', 3),
(103, 'Python Avançado', 'Guido Van', 2),
(104, 'Mistérios da Programação', 'Alan Turing', 1),
(105, 'Redes e Servidores', 'Linus Torvalds', 4);

INSERT INTO emprestimos (id, livro_id, leitor_id, data_emprestimo, data_devolucao_plano, data_devolucao_real) VALUES
(1, 102, 1, '2025-09-01', '2025-09-15', '2025-09-14'),
(2, 103, 2, '2025-09-05', '2025-09-20', '2025-09-19'),
(3, 101, 3, '2025-09-10', '2025-09-25', NULL), -- Livro raro não devolvido
(4, 104, 4, '2025-09-12', '2025-09-27', '2025-09-26'),
(5, 105, 5, '2025-09-15', '2025-09-30', NULL);

INSERT INTO multas (id, emprestimo_id, valor, pago) VALUES
(1, 3, 15.50, FALSE);

