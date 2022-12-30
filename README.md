[![Actions Status](https://github.com/zluuba/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/zluuba/python-project-50/actions) 
[![Python CI](https://github.com/zluuba/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/zluuba/python-project-50/actions/workflows/pyci.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/83963175416f052072a8/maintainability)](https://codeclimate.com/github/zluuba/python-project-50/maintainability) 
[![Test Coverage](https://api.codeclimate.com/v1/badges/83963175416f052072a8/test_coverage)](https://codeclimate.com/github/zluuba/python-project-50/test_coverage)


## Difference generator
Difference generator compares two files and outputs the result of the comparison. The **.json** and **.yaml** formats are supported.
You can also output the comparison result in three different views: **stylish**, **plain** and **json**. </br>
Started and used with the terminal. </br>


### Requirements
- [python](https://www.python.org/), version 3.9 or higher
- [poetry](https://python-poetry.org/), version 1.0.0 or higher
- [pyyaml](https://pyyaml.org/), version 6.0 or higher


### Installation 

You can clone this repo or download it with pip:
```ch
pip install --user git+https://github.com/zluuba/python-project-50.git
```

Go to the installed folder in the terminal and using these commands to install package:
```ch
make install
make build
make package-install
```

### Commands
#### Options

```ch
gendiff -h                # print help text and exit
gendiff --help

gendiff -f                # set the generator display format
gendiff --format
```

### Sample commands
*You can compare .json or .yaml (.yml) files.* </br>
*Specify the path to the files* </br>

Show the differences between the two files with default style **'stylish'**.
[Demo](https://github.com/zluuba/python-project-50#generate-diff---nested-files)
```ch
gendiff file1.json file2.json
```

Show the differences between the two files with style **'plain'**.
[Demo](https://github.com/zluuba/python-project-50#generate-diff---plain-format)
```ch
gendiff --format plain file1.json file2.json
```

Show the differences between the two files with style **'json'**.
[Demo](https://github.com/zluuba/python-project-50#generate-diff---json-format)
```ch
gendiff --format json file1.json file2.json
```


### Package examples

#### Flat files (stylish format):
[![asciicast](https://asciinema.org/a/NhNSYNMJvnWCl2lOep6MM3mJ9.svg)](https://asciinema.org/a/NhNSYNMJvnWCl2lOep6MM3mJ9)


#### Nested files (stylish format):
[![asciicast](https://asciinema.org/a/tHGzpIpe4u93imAMITANqZ3fW.svg)](https://asciinema.org/a/tHGzpIpe4u93imAMITANqZ3fW)


#### Plain format:
[![asciicast](https://asciinema.org/a/WUOBYxL3JIfWbidEeasDnOwfB.svg)](https://asciinema.org/a/WUOBYxL3JIfWbidEeasDnOwfB)


#### Json format:
[![asciicast](https://asciinema.org/a/ENsHFwq1ET33gH1JZX3x4zavZ.svg)](https://asciinema.org/a/ENsHFwq1ET33gH1JZX3x4zavZ)
