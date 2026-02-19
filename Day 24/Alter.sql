-- Add column
ALTER TABLE employees
ADD email VARCHAR(50);

-- Modify column
ALTER TABLE employees
MODIFY salary FLOAT;

-- Drop column
ALTER TABLE employees
DROP COLUMN email;

