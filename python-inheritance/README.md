# Python - Inheritance

## Description
This project covers fundamental concepts of object-oriented programming (OOP) in Python, focusing on **inheritance**, **object introspection**, and **built-in functions** used to inspect objects and classes.

## Learning Objectives
By completing this project, you should be able to explain:
* What inheritance is and why it is used in OOP
* How to inspect attributes and methods of an object using `dir()`
* How to identify class origins and relationships using `type()`, `isinstance()`, and `issubclass()`
* How to inherit classes, override methods, and call parent constructors with `super()`
* The difference between class attributes and instance attributes

## Requirements
* **Environment:** Executed on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
* **Allowed Editors:** `vi`, `vim`, `emacs`
* **File Header:** The first line of all Python scripts must be `#!/usr/bin/python3`
* **Style Guide:** Conforms to `pycodestyle` (version 2.8.*)
* **File Endings:** All files must end with a new line
* **Permissions:** All Python scripts must be executable (`chmod +x`)

## File Summary

| File | Description |
| --- | --- |
| `0-lookup.py` | Function `lookup(obj)` that returns the list of available attributes and methods of an object using `dir()`. |

## Usage & Testing

To test the lookup function, run the test script:

```bash
chmod +x 0-main.py 0-lookup.py
./0-main.py
