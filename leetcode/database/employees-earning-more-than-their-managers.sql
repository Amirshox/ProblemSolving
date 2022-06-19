select e.Name as Employee
from Employee as e inner join Employee as m on e.ManagerId = m.id
where e.Salary > m.Salary;