# 24. NamedTuples
from collections import namedtuple

Employee = namedtuple("Employee", ["name", "department", "salary"])

employees = (
    Employee("Alice", "Engineering", 95000),
    Employee("Bob", "Marketing", 72000),
    Employee("Charlie", "Engineering", 88000)
)

for employee in employees:
    print(f"{employee.name} works in {employee.department} and earns ${employee.salary:,}")

highest = max(employees, key=lambda x: x.salary)
print(f"Highest paid: {highest.name} (${highest.salary:,})")
