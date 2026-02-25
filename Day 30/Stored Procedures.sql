DELIMITER //

CREATE PROCEDURE GetEmployeesByDept(IN dept INT)
BEGIN
    SELECT * FROM Employee
    WHERE dept_id = dept;
END //

DELIMITER ;

CALL GetEmployeesByDept(2);