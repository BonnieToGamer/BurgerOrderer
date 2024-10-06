"""
The content of a packet has a certain structure.
This is the interface for a packet structure.
"""

from abc import ABC, abstractmethod

class PacketContent(ABC):
    @abstractmethod
    def to_json(self) -> str:
        """
        Converts the class into a packet string
        """
        pass