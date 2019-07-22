"""Provide the `CTFBase` superclass."""
from copy import deepcopy

from ..const import API_ROUTES

import logging

log = logging.getLogger(__name__)


class CTFBase:
    """Superclass for all models in CTF."""

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
                setattr(self, str(cls.id), cls)

    def __getitem__(self, attr):
        """Return the value of `attribute`."""
        log.debug("__getattr__: {}".format(attr))
        if not attr.startswith("_"):
            return getattr(self, attr)
        return None

    def _reset(self, *attrs):
        for a in deepcopy(self.__dict__):
            if a != "_ctfd" and a not in API_ROUTES:
                del self.__dict__[a]

    # def _reset(self, *attrs):
    #     for a in attrs:
    #         if a in self.__dict__:
    #             del self.__dict__[a]
