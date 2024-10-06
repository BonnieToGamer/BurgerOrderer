from packet_content import PacketContent
import json

class NewOrderPacketContent(PacketContent):
    def __init__(self, burger: str, specials: list[str]) -> None:
        self.burger = burger
        self.specials = specials
    
    def to_json(self) -> str:
        return json.dumps(self)