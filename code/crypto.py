from os import urandom
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from base64 import b64encode, b64decode

class Crypto(object):
    def __init__(self):
        self.key = urandom(32)
        self.block_size = urandom(16)
        self.backend = default_backend()
        self.cipher = Cipher(algorithms.AES(self.key), modes.CFB(self.block_size), backend=self.backend)
        self.key_loc = "/home/hardkase/enigma/vault/keys"
        self.ptext = "/home/hardkase/enigma/vault/plaintext"
        self.crypted = "/home/hardkase/enigma/vault/crypted"
        self.readable = "/home/hardkase/enigma/vault/rcrypted"

    def roll_iv(self):
        block_size = urandom(16)
        return block_size
    
    def gen_key(self):
        key = urandom(32)
        return key

    def write_key(self, key):
        with open(self.key_loc, "a+") as b:
            b.write(key)
            b.close()

    def get_key(self):
        with open(self.key_loc, "rb") as c:
            lines = c.read().splitlines()
            key = b64encode(lines[-1])
            print("Key: {0}".format(key))
            return key

    def encrypt(self, key, data=''):
        # Need to try rolling IV in function and in object and from constant
        encryptor = self.cipher.encryptor()
        crypted = encryptor.update(data) + encryptor.finalize()
        print("Encrypted Data: {0}".format(crypted))
        return crypted

    def encrypt_from_doc():
        pass

    def decrypt_from_doc():
        pass

    def decrypt(self, key, data=''):
        # cipher = Cipher(algorithms.AES(key), modes.CFB(self.block_size), backend=self.backend)
        decryptor = self.cipher.decryptor()
        dcrypted = decryptor.update(data) + decryptor.finalize()
        print("Decrypted Data: {0}".format(dcrypted))
        return dcrypted

    def get_crypted():
        pass

    def write_crypted():
        pass

    def write_readable_crypted():
        pass

# Fire it up
kryptor = Crypto()
key = kryptor.gen_key()
kryptor.write_key(key)
enc = kryptor.encrypt(key, 'fuckleBerry Hound, D005h')
print(b64encode(enc))
dec = kryptor.decrypt(key, enc)
print("end result: {0}".format(dec))


