# -*- coding: utf-8 -*-

import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


class signature():

    def __init__(self):
        self.pub_key_file = open("public.key", "rb").read()
        self.public_key = serialization.load_pem_public_key(self.pub_key_file, backend=default_backend())
        self.padding = padding.PKCS1v15()
        self.hash = hashes.SHA256()

    def set_algorithm(self, padding, hash):
        self.padding = padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH)
        self.hash = hashes.SHA256()

    def verify(self, signature, message):
        try:
            self.public_key.verify(
                base64.b64decode(signature),
                message,
                self.padding,
                self.hash
            )
        except:
            return False
        return True