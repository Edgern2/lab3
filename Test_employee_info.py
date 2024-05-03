import employee_info

def test_average_salary():

    test = (60166.666666666664)
    assert (test == employee_info.calculate_average_salary())




def test_get_employees_by_age_range():

    result = []
    test = [{'name': 'Jane', 'age': 25, 'department': 'Marketing', 'salary': 60000}]
    result = employee_info.get_employees_by_age_range(24,30)
    assert (result == test)


def test_employees_by_dept():

    result = []
    test = [{'name': 'John', 'age': 30, 'department': 'Sales', 'salary': 50000}, {'name': 'Peter', 'age': 40, 'department': 'Sales', 'salary': 60000}]
    result = employee_info.get_employees_by_dept("Sales")
    assert (result == test)