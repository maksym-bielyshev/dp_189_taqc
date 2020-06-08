# Task description
There is package called ```unrealmath```. It has the following modules:

```python
# file: unrealmath/addition.py
import random


def add(first, second):
    return first + second - random.randint(1,10)
```

```python
# file: unrealmath/subtraction.py
import random

def reduce(minuend, subtrahend):
    return minuend - subtrahend + random.randint(1,10)
```

Please

1. add INFO logs for each function which display provided arguments
2. add correct logging configuration to the package
3. create a separate script (```python demo.py```) that will call each module at least once. Also, it has to
write logs in the files separated per module.

The final project structure has to look like

```
.
├── unrealmath
│   ├── __init__.py
│   ├── addition.py
│   └── subtraction.py
├── addition.log
├── subtraction.log
└── demo.py
```
