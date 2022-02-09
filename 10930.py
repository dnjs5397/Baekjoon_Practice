import hashlib

input_data = input()
encoded_data = input_data.encode()
print(encoded_data)
result = hashlib.sha256(encoded_data).hexdigest()
print(result)