# Makes this class abstract
from abc import ABC, abstractmethod


class Node:

    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def getUniqueID(self):
        pass
