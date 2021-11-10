from secret import _encode_dict, _decode_dict


class KCODE:
    def encode(msg):
        return ''.join((str(_encode_dict[key]) if key in _encode_dict.keys() else str(key) for key in msg)).encode('utf-8').hex()
    def decode(msg):
        return ''.join((str(_decode_dict[key]) if key in _decode_dict.keys() else str(key) for key in bytes.fromhex(msg).decode('utf-8')))