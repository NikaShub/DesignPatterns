

def integer_to_binary(integer: int) -> str:
    base = 2
    word_size = 16

    binary = ""
    for i in range(word_size):
        binary = str((integer // base**i) % base) + binary

    return binary


def test() -> None:
    assert integer_to_binary(0) == "0000000000000000"
    assert integer_to_binary(1) == "0000000000000001"
    assert integer_to_binary(2) == "0000000000000010"
    assert integer_to_binary(3) == "0000000000000011"
    assert integer_to_binary(4) == "0000000000000100"
    assert integer_to_binary(5) == "0000000000000101"
    assert integer_to_binary(6) == "0000000000000110"
    assert integer_to_binary(7) == "0000000000000111"
    assert integer_to_binary(8) == "0000000000001000"
    assert integer_to_binary(17) == "0000000000010001"
    assert integer_to_binary(65535) == "1111111111111111"