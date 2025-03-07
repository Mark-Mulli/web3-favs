import getpass
import os
from eth_account import Account
from vyper import compile_code
from web3 import Web3

from dotenv import load_dotenv

from encrypt_key import KEYSTORE_PATH

load_dotenv()
RPC_URL = os.getenv("RPC_URL")
MY_ADDRESS = os.getenv("MY_ADDRESS")

def main():
    print("Read from the vyper code and deploy it")
    with open("favorites.vy", 'r') as f:
        favs_code = f.read()
        compilation_details = compile_code(favs_code, output_formats=['bytecode', 'abi'])
        # print(compilation_details)
    
    w3 = Web3(Web3.HTTPProvider())
    favs_contract = w3.eth.contract(bytecode=compilation_details["bytecode"], abi=compilation_details["abi"])
    # print(favs_contract)
    
    print("Building the transaction.....")
    
    nonce = w3.eth.get_transaction_count(MY_ADDRESS)
    transaction = favs_contract.constructor().build_transaction({
        "nonce": nonce,
        "from": MY_ADDRESS,
        "gasPrice": w3.eth.gas_price
    })
    
    private_key = decrypt_key()
    signed_transaction = w3.eth.account.sign_transaction(transaction, private_key=private_key)
    
    tx_hash = w3.eth.send_raw_transaction(signed_transaction.raw_transaction)
    print(f"my TX Hash is {tx_hash}")
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"Done! Contract deployed to {tx_receipt.contractAddress}")
    

def decrypt_key() -> str:
    with KEYSTORE_PATH.open("r") as f:
        encrypted_account = f.read()
        password = getpass.getpass("Enter the password:\n")
        key = Account.decrypt(encrypted_account, password)
        print("Decrypted Key")
        return key
    


if __name__ == "__main__":
    main()