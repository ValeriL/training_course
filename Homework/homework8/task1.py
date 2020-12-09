"""
We have a file that works as key-value storage.

Each like is represented as key and value separated by = symbol, example:
name=kek
last_name=top
song_name=shadilay
power=9001

Values can be strings or integer numbers.
If a value can be treated both as a number and a string, it is treated as number.

Write a wrapper class for this key value storage that works like this:
storage = KeyValueStorage('path_to_file.txt') that has its keys and values
accessible as collection items and as attributes.
Example:
storage['name'] # will be string 'kek'
storage.song_name # will be 'shadilay'
storage.power # will be integer 9001

In case of attribute clash existing built-in attributes take precedence.
In case when value cannot be assigned to an attribute
(for example when there's a line 1=something) ValueError should be raised.
File size is expected to be small, you are permitted to read it entirely into memory.
"""


class KeyValueStorage:
    def __init__(self, path):  # noqa : CCR001
        with open(path) as file:
            for line in file:
                attr, value = line.strip().split("=")
                if attr.isdigit():
                    raise ValueError("Int cant be an attribute")
                if attr in self.__dict__:
                    continue
                if value.isdigit():
                    self.__dict__[attr] = int(value)
                else:
                    self.__dict__[attr] = value

    def __getitem__(self, key):
        return self.__dict__[key]
