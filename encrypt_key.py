
import getpass
import json
from pathlib import Path
from eth_account import Account


KEYSTORE_PATH = Path(".keystore.json")
def main():
    private_key = getpass.getpass("Enter your private key: ")
    
    account = Account.from_key(private_key)
    
    password = getpass.getpass("Enter a password:\n")
    
    encrypted_account = account.encrypt(password)
    
    print(f"Saving to {KEYSTORE_PATH}")
    
    with KEYSTORE_PATH.open("w") as f:
        json.dump(encrypted_account,f)
        print("Done!")
    

if __name__ == "__main__":
    main()
    



