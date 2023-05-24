# Difference generator

[![Actions Status](https://github.com/zluuba/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/zluuba/python-project-50/actions) 
[![Python CI](https://github.com/zluuba/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/zluuba/python-project-50/actions/workflows/pyci.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/83963175416f052072a8/maintainability)](https://codeclimate.com/github/zluuba/python-project-50/maintainability) 
[![Test Coverage](https://api.codeclimate.com/v1/badges/83963175416f052072a8/test_coverage)](https://codeclimate.com/github/zluuba/python-project-50/test_coverage)


Difference generator compares two files and outputs the result in three different style: stylish, plain and json. </br>
Used with the terminal. </br>
**Json** and **yaml** formats are supported. </br>


## Requirements
- [python](https://www.python.org/), version 3.9 or higher
- [poetry](https://python-poetry.org/), version 1.2.0 or higher


## Installation 

Clone this repo or download it with pip:
```ch
git clone https://github.com/zluuba/difference-generator.git
```
```ch
pip install --user git+https://github.com/zluuba/difference-generator.git
```

Install package and dependencies:
```ch
cd difference-generator
make install
make build
make package-install
```

## Commands
### Options

```ch
gendiff [-h] [-f FORMAT] first_file second_file

-h, --help                # print help text
-f, --format              # set output format
```

### Gendiff commands

```python
# Outputs brief documentation for how to invoke the program
gendiff --help


# Show the differences between two files with stylish formatter
# P.S. stylish is the default formatter, but you can specify it:
# gendiff -f stylish file1.json file2.json
gendiff file1.json file2.json


# Show the differences between two files with plain formatter
gendiff -f plain file1.json file2.json


# Show the differences with json formatter
gendiff -f json file1.yml file2.yml
```

You can also compare json and yaml file formats in the same command, for example:
```ch
gendiff file1.yml file2.json
```


## Demos

### Help option, flat files, stylish formatter
[![asciicast](https://asciinema.org/a/V8EMBZ8dyIeVdGrgz5yOiY7tk.svg)](https://asciinema.org/a/V8EMBZ8dyIeVdGrgz5yOiY7tk)


### Nested files, stylish formatter
[![asciicast](https://asciinema.org/a/arUl8ZVGSi4hzsnaNf0nKwjZL.svg)](https://asciinema.org/a/arUl8ZVGSi4hzsnaNf0nKwjZL)


### Plain formatter
[![asciicast](https://asciinema.org/a/0V1KMW2AuUasLxNQ9ty6E11GO.svg)](https://asciinema.org/a/0V1KMW2AuUasLxNQ9ty6E11GO)


### Json formatter
[![asciicast](https://asciinema.org/a/6RRQ0OlgISxrA9vx9ueJFCqcJ.svg)](https://asciinema.org/a/6RRQ0OlgISxrA9vx9ueJFCqcJ)