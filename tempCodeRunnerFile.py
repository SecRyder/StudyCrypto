cipher = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
cipherByte = bytes.fromhex(cipher)
knowPlain = b"crypto{"
key = bytes([c ^ p for c, p in zip(cipherByte,knowPlain)])
print(key)

from itertools import cycle # Lap vo han cac phan tu cua chuoi key neu can
fullKey = key
plaintext = bytes([c ^ k for c, k in zip(cipherByte,cycle(fullKey))])
print(plaintext.decode())