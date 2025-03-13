
import getpass
import json
from pathlib import Path

from eth_account import Account


KEYSTORE_PATH = Path(".keystore.json")

def main():
    private_key = getpass.getpass("Enter your private key: ")
    account = Account.from_key(private_key)
    passcode = getpass.getpass("Enter a passcode to encrypt your private key: ")
    encrypted_key = account.encrypt(passcode)
    
    with open(KEYSTORE_PATH, 'w') as f:
        json.dump(encrypted_key, f)
        print(f"Encrypted private key saved to {KEYSTORE_PATH}")

if __name__ == '__main__':
    main()