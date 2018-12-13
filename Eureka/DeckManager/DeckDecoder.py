import base64
from functools import reduce


class CArtifactDeckDecoder(object):
    """
    本地 DeckDecoder 解码
    """

    def __init__(self):
        self.current_version = 2
        self.encode_prefix = "ADC"

    def parse_deck(self, deck_code=""):
        if not deck_code.startswith(self.encode_prefix):
            raise ValueError("invalid deck code prefix")
        deck_code = deck_code[len(self.encode_prefix):].replace("-", "/").replace("_", "=")
        deck_code_bytes = base64.b64decode(deck_code)
        byte_index = 0
        version_and_heroes = deck_code_bytes[byte_index]
        byte_index += 1
        version = version_and_heroes >> 4
        checksum = deck_code_bytes[byte_index]
        byte_index += 1
        string_length = deck_code_bytes[byte_index] if version > 1 else 0
        byte_index += 1
        if version > self.current_version:
            raise ValueError("deck code version " + version + " is not supported")
        name_start_index = len(deck_code_bytes) - string_length
        deck_bytes = deck_code_bytes[byte_index:name_start_index]
        computed_checksum = self.compute_checksum(deck_bytes)
        if checksum != computed_checksum:
            raise ValueError("invalid deck code checksum")
        decoder = CardDecoder(deck_bytes)
        heroes_length = decoder.read_var(version_and_heroes, 3)
        heroes = []
        for i in range(heroes_length):
            heroes.append(decoder.read_card("turn"))
        decoder.reset_previous_id()
        cards = []
        while decoder.has_next():
            cards.append(decoder.read_card("count"))
        name = deck_code_bytes[name_start_index:].decode("UTF-8")
        return {"name": name, "heroes": heroes, "cards": cards}

    def compute_checksum(self, deck_bytes):
        return 0xFF & reduce(lambda x, y: x + y, deck_bytes)


class CardDecoder(object):
    def __init__(self, deck_bytes):
        self.bytes = deck_bytes
        self.bytes_length = len(self.bytes)
        self.i = 0
        self.previous_id = 0

    def read_var(self, base_value, base_bits):
        result = 0
        if base_bits != 0:
            continu_bit = 1 << base_bits
            result = base_value & (continu_bit - 1)
            if (base_value & continu_bit) == 0:
                return result
        current_shift = base_bits
        current_byte = 0
        while True:
            if self.i >= self.bytes_length:
                raise ValueError("invalid deck code")
            current_byte = self.bytes[self.i]
            self.i += 1
            result |= ((current_byte & 127) << current_shift)
            current_shift += 7
            if (current_byte & 128) <= 0:
                break
        return result

    def read_card(self, n_name="n"):
        if self.i > self.bytes_length:
            raise ValueError("invalid deck code")
        header = self.bytes[self.i]
        self.i += 1
        id = self.previous_id + self.read_var(header, 5)

        self.previous_id = id
        n = (header >> 6)
        if n == 3:
            n = self.read_var(0, 0)
        else:
            n += 1
        return {"id": id, n_name: n}

    def has_next(self):
        return self.i < self.bytes_length

    def reset_previous_id(self):
        self.previous_id = 0


CADD = CArtifactDeckDecoder()
if __name__ == "__main__":
    list = [
        "ADCJYsSJLkCgxhLC7hdQmTdAU6CipuiAWkBdgENsQGGYQPpu5HnuqLmiZPpkrEgLSBEb2c_",
        "ADCJWoWJLkCChFLi766Ak5CiliDQXIBFYKBBB+3AjkCSOe6oum7keS4remAnyAtIE1yWWFndXQ_",
        "ADCJSoYJLkCQwcRljpdpN0BiIEHiptqAoGBIwOWGn8BSOe6oum7keW-q+aUuyAtIFN0YW5DaWZrYQ__"
    ]
    for code in list:
        ans = CADD.parse_deck(code)
        print(ans)
