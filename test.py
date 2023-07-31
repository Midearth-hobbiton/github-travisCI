import os

# test file
print("hello world")
secret = os.environ["SECRET"]
print(secret)
print(f"This is not a secret {secret}, 123456789, 1|23456789")
