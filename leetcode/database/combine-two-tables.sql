select FirstName, LastName, City, State
from Person as p left join Address as a on p.PersonId = a.PersonId;