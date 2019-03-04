# -*- coding: utf-8 -*-

import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


class signature():
    pub_key = b"""
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxS1LsXrEWEEMPooLHa4r
osCAnmkO3HaBAk0YcsDMR6hQeuQNLqRWP65TpbfTbKWmZ22Hzep3Ekhs1qvSZgI+
iq/bnVeDhkcD+LqVQGP+7fyE0E0bO96FOzMmtbRet4wAiiE9+uw5GmZfg+fRG3yI
y2N5u5p7VHJ1RwNugrIUQjhrLvZc+lhqR/aKTxQCQ5CGAgLZIcr3FIWCWrSBMK3d
Wy3KI+qe3ZX0STrCCNxl2UFnuuAa2RZZ2j4QtWHlNkyK+UEup+cGkvpc1XrT7anL
HlbTP6jE7MqB5sJ9r2EEzrJzJZjD13UqlzvI61tTC8SKpuk5AEaSsUV7RKlKUCjB
8wIDAQAB
-----END PUBLIC KEY-----
"""

    def __init__(self):
        self.public_key = serialization.load_pem_public_key(self.pub_key, backend=default_backend())

    def verify(self, signature, message):
        try:
            self.public_key.verify(
                base64.b64decode(signature),
                message,
                padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())
        except:
            return False
        return True