[![Actions Status](https://github.com/zluuba/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/zluuba/python-project-50/actions) 
[![Python CI](https://github.com/zluuba/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/zluuba/python-project-50/actions/workflows/pyci.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/83963175416f052072a8/maintainability)](https://codeclimate.com/github/zluuba/python-project-50/maintainability) 
[![Test Coverage](https://api.codeclimate.com/v1/badges/83963175416f052072a8/test_coverage)](https://codeclimate.com/github/zluuba/python-project-50/test_coverage)


## Difference generator
Compare two files and output the result in three different style: stylish, plain and json. </br>
**Json** and **yaml** formats are supported. </br>
Used with the terminal. </br>


### Requirements
- [python](https://www.python.org/), version 3.9 or higher
- [poetry](https://python-poetry.org/), version 1.0.0 or higher
- [pyyaml](https://pyyaml.org/), version 6.0 or higher


### Installation 

Clone this repo or download it with pip:
```ch
git clone https://github.com/zluuba/python-project-50.git
```
```ch
pip install --user git+https://github.com/zluuba/python-project-50.git
```

Use these commands to install package:
```ch
make install
make build
make package-install
```

### Commands
#### Options

```ch
gendiff -h                # print help text
gendiff --help

gendiff -f                # set output format
gendiff --format
```

#### Gendiff commands

Show the differences between two files with default formatter **stylish**
([demo](https://github.com/zluuba/python-project-50#nested-files-stylish-formatter)):
```ch
gendiff file1.json file2.json
```

**Plain** formatter
([demo](https://github.com/zluuba/python-project-50#plain-formatter)):
```ch
gendiff -f plain file1.json file2.json
```

**Json** formatter
([demo](https://github.com/zluuba/python-project-50#json-formatter)):
```ch
gendiff -f json file1.yml file2.yml
```


### Demos

#### Help option, flat files, stylish formatter:
[![asciicast](https://asciinema.org/a/V8EMBZ8dyIeVdGrgz5yOiY7tk.svg)](https://asciinema.org/a/V8EMBZ8dyIeVdGrgz5yOiY7tk)


#### Nested files, stylish formatter:
[![asciicast](https://asciinema.org/a/arUl8ZVGSi4hzsnaNf0nKwjZL.svg)](https://asciinema.org/a/arUl8ZVGSi4hzsnaNf0nKwjZL)


#### Plain formatter:
[![asciicast](https://asciinema.org/a/0V1KMW2AuUasLxNQ9ty6E11GO.svg)](https://asciinema.org/a/0V1KMW2AuUasLxNQ9ty6E11GO)


#### Json formatter:
[![asciicast](https://asciinema.org/a/zCfIoYSHW2KjjMHeJTkAHFnzC.svg)](https://asciinema.org/a/zCfIoYSHW2KjjMHeJTkAHFnzC)