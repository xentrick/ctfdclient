#!/usr/bin/env python
from copy import deepcopy
from ..base import CTFBase


class InfoBase(CTFBase):
    @staticmethod
    def _safely_add_arguments(argument_dict, key, **new_arguments):
        """Replace argument_dict[key] with a deepcopy and update.
        This method is often called when new parameters need to be added to a
        request. By calling this method and adding the new or updated
        parameters we can insure we don't modify the dictionary passed in by
        the caller.
        """
        value = deepcopy(argument_dict[key]) if key in argument_dict else {}
        value.update(new_arguments)
        argument_dict[key] = value

    @classmethod
    def parse(cls, data, ctfd):
        """Return an instance of ``cls`` from ``data``.
        :param data: The structured data.
        :param ctfd: An instance of :class:`.CTFd`.
        """
        return cls(ctfd, _data=data)

    def __init__(self, ctfd, _data):
        """Initialize a CTFModel instance.
        :param ctfd: An instance of :class:`.CTFd`.
        """
        self._ctfd = ctfd
        if _data:
            for cls in _data:
                setattr(self, cls.name, cls)

    def __init__(self, ctfd, _data):
        """Initialize a InfoBase instance (or a subclass).
        :param ctfd: An instance of :class:`~.CTFd`.
        """
        super(InfoBase, self).__init__(ctfd, _data=_data)

    def __getitem__(self, attr):
        """Return the value of `attribute`."""
        log.debug("__getattr__: {}".format(attr))
        if not attr.startswith("_"):
            return getattr(self, attr)
        return None

    def _reset(self, *attrs):
        for a in attrs:
            if a in self.__dict__:
                del self.__dict__[a]
