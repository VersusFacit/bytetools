
from bytetools.exceptions import InvalidByteValue


UPPER_A = 0x41
UPPER_Z = 0x5A


def lower(byte_value: int, strict_ascii: bool = True) -> int:
    """
    Convert the byte value to lowercase, if it's an uppercase ASCII letter.
    Optionally enforce strict ASCII validation.
    """
    if strict_ascii and (byte_value < 0x00 or byte_value > 0x7F):
        raise InvalidByteValue(
            f"Byte value {byte_value} is out of the ASCII range."
        )
    elif byte_value < UPPER_A or byte_value > UPPER_Z:
        return byte_value
    else:
        return byte_value + 0x20
