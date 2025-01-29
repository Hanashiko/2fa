import pyotp
import base64

key: str = base64.b32encode(b'Hanashiko').decode() 
hotp: pyotp.HOTP = pyotp.HOTP(key)

print(hotp.at(0))
print(hotp.at(1))
print(hotp.at(2))
print(hotp.at(3))

counter: int = 0
for otp in range(4):
   print(hotp.verify(input("Enter Code: "), counter))
   counter += 1