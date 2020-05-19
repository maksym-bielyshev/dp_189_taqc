# Task description
Write a program which provides the statistic about given file. It has to print the following statistic about an
arbitrary file:

- a number of lines
- a number of empty lines
- a number of lines with letter "z"
- a number of "z" letters in the file
- a number of lines with "and" group (for instance, "andromeda" has "and" as well as "you and me").

Sample file (./storage/run2019.txt):
```
zzzzzzzzz
zzz
zzzzzzzzzzzzzzzzzz

andromeda

and

z and a and z
```

Sample statistic:
```
>>>>
File: ./storage/run2019.txt
  total lines:      10
  empty lines:      4
  lines with "z":   4
  "z" count":       34
  lines with "and": 3
>>>>
```

Please take into account, that the program
- has to ask a user about a path to a file
- has to ask a user if one more file needs to be analyzed
- has to stop only if a user wants to stop
