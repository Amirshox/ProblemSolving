SELECT Employees.employee_id
FROM Employees
         LEFT JOIN Salaries S on Employees.employee_id = S.employee_id WHERE S.employee_id IS NULL
UNION
SELECT S.employee_id
FROM Employees
         RIGHT JOIN Salaries S on Employees.employee_id = S.employee_id WHERE Employees.employee_id IS NULL ORDER BY employee_id ASC;