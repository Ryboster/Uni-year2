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
    def __init__(self, role):
        self.role = role

class Company
    def __init__(self):
        self.employees = []
    def HireEmployee(self, employee):
        self.employees.append(employee)
```



### Performance Testing

Performance tests - as the name suggests, focus on testing the performance of a given unit or system. This could mean execution time, or number of successful outcomes, or any other change over time. 



### Personal Experience

----------------------------------------------

In my experience with QA, I had made use of unit testing

### References

----------------------------------------------

Sandman, Adam. (2025), Full Guide To Software Quality Assurance. Available at: https://www.inflectra.com/Ideas/Topic/Software-Quality-Assurance.aspx (10th Oct 2025)



[What is Integration Testing? | IBM](https://www.ibm.com/think/topics/integration-testing)
