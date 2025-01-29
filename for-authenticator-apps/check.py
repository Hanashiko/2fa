import pyotp

def simulate_authentication(key):
    totp: pyotp.TOTP = pyotp.TOTP(key)
    print("Enter the code from your Google Authenticator App")
    user_input: str = input("Enter code:")
    if totp.verify(user_input):
        print("Authentication Successful")
    else:
        print("Authentication Failed")
        
if __name__ == "__main__":
    user_key: str = open('2fa.txt').read()
    simulate_authentication(user_key)