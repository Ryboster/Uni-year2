# LO 1

## 10th October 2025

### Abstract

----------------------------------------------

Quality assurance (QA) is a process that helps developers maintain the quality of their software. It defines a set of rules used to ensure that the application meets the expected specifications and requirements.

There is a myriad of different QA processes, and developers should consider which ones to incorporate to fit their specific application's needs. Some of those processes can also be automated. Those processes usually involve writing different "tests" that are then ran periodically. This article focuses on those particular processes.

### Body Section

----------------------------------------------

### Unit Testing

Unit testing involves writing scripts called Unit Tests. Those scripts target specific parts (or "units") of the application, and use assertions to ensure that the unit functions as expected.

Each unit test follows a standardized workflow - It defines input data, sends it to the unit, and asserts that the output of that unit is correct. Consider the following example:

```python
def add_two(x:int):
    return x + 2
```

An example unit test for this particular function could look something like this:

```python
import unittest
def test_add_two():
    input_data = 1
    output_data = add_two(input_data)
    assertEqual(output_data, input_data + 2)
```

here, the unit test defines a simple input (`input_data`), sends that input to the unit (`add_two()`), and ensures that the unit produced expected output (3). 

This could then be expanded further. For example, we may want to ensure that the output data is of expected type (`integer`), or that input data of incorrect type is rejected.

#### Conclusion

Unit testing is the most versatile of QA methods. It helps developers ensure that the smallest parts of their applications aren't mutating in unexpected ways over time. They are perhaps the most common given that every application has units it relies on.

It is best applied when the application is still small, and other QA methods aren't yet appropriate. 

### Integration Testing

Integration testing, similarly to unit testing, also focuses on units. The difference however, is that integration tests, instead of just testing a single unit, verify that multiple units work together as expected; In other words they verify the **integration** of multiple units.

Consider the following example:

```python
class Employee
    def __init__(self, name):
        self.name = name

class Company
    def __init__(self):
        self.employees = []
    def hire_employee(self, employee):
        self.employees.append(employee.name)
```

```python
def test_hire_empoyee_integration():
    jeff = Employee("jeff")
    bosch = Company()

    bosch.hire_employee(jeff)
    assert "jeff" in bosch.employees
```

In this example, a `Company` class has the ability to hire an `Employee`. To do that however, it expects that the `Employee` has a `name`. If the `Employee` class was to mutate in a way where the `name` field disappears, it would result in an error.

To ensure that the two classes can work together, we write an integration test that asserts that the `Company` class adds an instance of `Employee` in the expected way.

#### Conclusion

Integration testing is more advanced than unit testing and requires that the application has multiple units. It is best applied when multiple units of an application need to be able to work together.

### Performance Testing

Performance tests - as the name suggests, focus on testing the performance of a given unit or system. This could mean execution time, number of successful outcomes, or any other change over time. This QA method helps ensure that a given unit of the application finishes in a time effective manner.

Consider the following example:

```python
def generate_random_map():
    map = [][]
    for x in range(0, 10):
        for y in range(0,10):
            map[x][y].append(random.randint(0,10))

def test_performance_of_map_generation():
    start_time = time.time()
    generate_random_map()
    end_time = time.time()
    duration = end_time - start_time
    assert duration < 2
```

In this example we define a process that generates a completely random map, registering the time at the beginning and end of it. We then derive the duration that the process took to complete, and assert that it is below some predefined amount that we deem reasonable.

While crude, this example demonstrates the importance of performance testing. Sometimes processes can evolve over time leading to different time efficiencies.

#### Conclusion

Performance testing helps developers ensure that their applications stay efficient over time, which helps them develop for a wider range of devices. By knowing the tested hardware and the execution time, developers can better deduce hardware requirements on the consumer end, which can also aid any efforts in lowering them.

While not all applications can benefit from performance testing, for those that can, it can be an instrumental QA process that can even make the difference between releasing the application or binning it. Applications are made for consumers, but if their hardware can't handle them, they are as good as a beached whale (not very).

### References

----------------------------------------------

Sandman, Adam. (2025), Full Guide To Software Quality Assurance. Available at: https://www.inflectra.com/Ideas/Topic/Software-Quality-Assurance.aspx (10th Oct 2025)

[What is Integration Testing? | IBM](https://www.ibm.com/think/topics/integration-testing)
