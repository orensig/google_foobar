# -*- coding: utf-8 -*-
from base64 import b64decode

encrypted_message = "FFUWGxAKAhwBQk5JSUAIAAAPB05LT1UGAR8FAg4VEAtUSV1PVQAdBwwCAhcBSV9JQAoUAwEBHRRI Ul9OVAAJDAAAChoLCwpVSU5UCAQHGwAYFgQCAQZCTklJQBocCQEQAgILVUlOVBsGDRAMGgBOR1VS Qh0SDwJIXkVJFQYISFJfTlQeDgFTQhM="
key = "orensig"

message = []
len = len(key)
for i, c in enumerate(b64decode(encrypted_message)):
    message.append(chr(ord(c) ^ ord(key[i % len])))
message = ''.join(message)

print(message)
