import hashlib


text = 'test1234' + 'random-string'
text = text.encode()

h = hashlib.md5(text).hexdigest()
# print(h)

# c3a19db5df5ce8a62a079c5cc1e6921c
# fee6283f210f18c2eae8082c17bd5f5c
# 16d7a4fca7442dda3ad93c9a726597e4

h = hashlib.sha256(text).hexdigest()
print(h)