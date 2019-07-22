#!/usr/bin/env python

class Challenge:
    def __init__(self, _data):
        self._data = _data

        self.id = self._data["id"]
        self.category = self._data["category"]
        self.name = self._data["name"]
        self.script = self._data["script"]
        self.tags = self._data["tags"]
        self.template = self._data["template"]
        self.type = self._data["type"]
        self.value = self._data["value"]

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if not isinstance(category, str):
            raise Exception("Category must be string")
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be string")
        self._name = name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, idnum):
        if not isinstance(idnum, int):
            raise Exception("ID must be integer")
        self._id = idnum

    @property
    def script(self):
        return self._script

    @script.setter
    def script(self, script):
        if not isinstance(script, str):
            raise Exception("Script must be a string")
        self._script = script 

    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, tags):
        if not isinstance(tags, list):
            raise Exception("Tags must be a list")
        self._tags = tags

    @property
    def template(self):
        return self._template

    @template.setter
    def template(self, template):
        if not isinstance(template, str):
            raise Exception("Template must be a string")
        self._template = template

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        if not isinstance(type, str):
            raise Exception("Type must be a string")
        self._type = type 

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not isinstance(value, int):
            raise Exception("Value  must be a string")
        self._value = value
