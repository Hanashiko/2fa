import pyotp
import qrcode

def generate_otp_key() -> str:
    return pyotp.random_base32()

def generate_qr_code(key: str, account_name: str, issuer_name: str) -> None:
    uri: str = pyotp.totp.TOTP(key).provisioning_uri(name=account_name, issuer_name=issuer_name)
    img = qrcode.make(uri)
    image_name: str = 'totp_qr'
    image_format: str = 'png'
    img.save(f'{image_name}.{image_format}')
    print(f"QR Code saved as {image_name}.{image_format}")
    
if __name__ == "__main__":
    user_key: str = generate_otp_key()
    print("Your Two-Factor Authentication Key:", user_key)
    
    with open('2fa.txt','w') as file:
        file.write(user_key)
        
    generate_qr_code(user_key, 'Hanashiko', 'Test')