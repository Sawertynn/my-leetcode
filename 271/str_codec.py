"""
Design an algorithm to encode a list of strings to a string.
The encoded string is then sent over the network and is decoded back to the original list of strings.
"""

def encode(strings: list[str]) -> str:
    builder = []
    for token in strings:
        builder.append(f'{len(token)}#{token}')
    return str.join('', builder)



def decode(encoded: str) -> list[str]:
    builder = []
    pos = 0
    while pos < len(encoded):
        num_end = encoded.find('#', pos)
        length = int(encoded[pos:num_end])
        token = encoded[num_end + 1: num_end + 1 + length]
        builder.append(token)
        pos = num_end + 1 + length
    return builder

