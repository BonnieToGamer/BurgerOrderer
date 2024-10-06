"""
A Websocket packet.
It consists of a type (str)
and a message also (str)
"""

from typing import Literal

PacketType = Literal["NewOrder"]

class Packet:
    def __init__(self, packet_type: PacketType, msg: str) -> None:
        self.packet_type = packet_type
        self.msg = msg