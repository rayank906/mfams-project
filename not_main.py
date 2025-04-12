from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from pathlib import Path


def load_private_key_from_file(file_path):
    with open(file_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,  # or provide a password if your key is encrypted
            backend=default_backend()
        )
    return private_key


import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.exceptions import InvalidSignature

def sign_pss_text(private_key: rsa.RSAPrivateKey, text: str) -> str:
    # Before signing, we need to hash our message.
    # The hash is what we actually sign.
    # Convert the text to bytes
    message = text.encode('utf-8')



    try:
        signature = private_key.sign(
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.DIGEST_LENGTH
            ),
            hashes.SHA256()
        )
        return base64.b64encode(signature).decode('utf-8')
    except InvalidSignature as e:
        raise ValueError("RSA sign PSS failed") from e
    
import requests
import datetime

# Get the current time
current_time = datetime.datetime.now()

# Convert the time to a timestamp (seconds since the epoch)
timestamp = current_time.timestamp()

# Convert the timestamp to milliseconds
current_time_milliseconds = int(timestamp * 1000)
timestampt_str = str(current_time_milliseconds)

# Load the RSA private key
path = Path.home() / "MFAMS.txt"
private_key = load_private_key_from_file(path)

method = "GET"
base_url = 'https://demo-api.kalshi.co'
path='/trade-api/v2/portfolio/balance'


msg_string = timestampt_str + method + path

sig = sign_pss_text(private_key, msg_string)

headers = {
        'KALSHI-ACCESS-KEY': 'a952bafb-12dd-4955-9e7c-3895265e812d',
        'KALSHI-ACCESS-SIGNATURE': sig,
        'KALSHI-ACCESS-TIMESTAMP': timestampt_str
    }
response = requests.get(base_url + path, headers=headers)
print("Status Code:", response.status_code)
print("Response Body:", response.text)