import pyotp

key: str = pyotp.random_base32()
totp: pyotp.TOTP = pyotp.TOTP(key)
now_totp: str = totp.now()
print(now_totp)

input_code: str = input("Enter your OTP:")
print(totp.verify(input_code))