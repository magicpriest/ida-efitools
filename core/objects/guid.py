from uuid import UUID

from .pointer import Pointer
from .structure import Structure


class GUID:

    def __init__(self, addr=None, name=None, ptr=None):
        if addr is not None and name is not None:
            self.__ptr = Pointer(addr, name)
        elif ptr is not None:
            self.__ptr = ptr
        else:
            raise ValueError()
        self.__ptr.type = Structure("GUID").name

    @property
    def name(self):
        return self.__ptr.name

    @property
    def data(self):
        return self.__ptr.get_bytes(16)

    @property
    def ptr(self):
        return self.__ptr

    def as_uuid(self):
        return UUID(bytes_le=self.data)

    def __str__(self):
        return "%s {%s}" % (self.name, self.as_uuid())

    def __hash__(self):
        return hash(self.data)

    def __cmp__(self, other):
        if isinstance(other, GUID):
            return cmp(self.data, other.data)
        raise NotImplementedError

    def __eq__(self, other):
        if isinstance(other, GUID):
            return self.data == other.data