#Task description

Write tests for all functions located in ```calculation.py``` module.

```python
# file: calculation.py
def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2
```
Please use one test class for each function. Also, you need to write 3 tests for each function:
- all arguments are greater than 0
- all arguments are less than 0
- at least one argument is 0

After, please create two suites:
- a suite which runs tests where at least one argument is 0
- a suite which runs tests where all arguments are greater than 0
