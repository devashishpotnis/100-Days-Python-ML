-- Start transaction (automatic in many DBs)

INSERT INTO students VALUES (101, 'Devashish', 24);

SAVEPOINT s1;

UPDATE students SET age = 24 WHERE id = 5;

ROLLBACK TO s1;   -- Undo update

COMMIT;           -- Save insert permanently