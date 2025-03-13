import getpass
import os
import boa
from boa.network import NetworkEnv, EthereumRPC
from dotenv import load_dotenv
from eth_account import Account
from encrypted import KEYSTORE_PATH

load_dotenv()


def main():
    rpc = os.getenv("RPC")
    boa_env = NetworkEnv(EthereumRPC(rpc))
    boa.set_env(boa_env)

    private_key = decrypt()
    my_account = Account.from_key(private_key)
    boa.env.add_account(my_account, force_eoa = True)
    
    contract = boa.load("bool_change.vy")
    prevBool = contract.get_bool()
    print(f"Initialized bool to {prevBool}")
    
    stateChange = contract.set_bool(True)
    print(f"Changed bool to {stateChange}")    
    
    
def decrypt() -> str:
    with KEYSTORE_PATH.open("r") as f:
        encrypted_account = f.read()
        passcode = getpass.getpass("Enter the passcode to decrypt your private key: ")
        key = Account.decrypt(encrypted_account, passcode)
        print("Decrypted private key")
        return key
    
    


if __name__ == '__main__':
    main()  