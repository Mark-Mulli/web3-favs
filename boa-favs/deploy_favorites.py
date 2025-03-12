import os
import boa
from boa.network import NetworkEnv, EthereumRPC
from dotenv import load_dotenv
from eth_account import Account

load_dotenv()



def main():
    rpc = os.getenv('RPC_URL')
    env = NetworkEnv(EthereumRPC(rpc))
    boa.set_env(env)
    
    anvil_key = os.getenv("ANVIL_KEY")
    my_account = Account.from_key(anvil_key)
    boa.env.add_account(my_account, force_eoa = True)
    
    favorites_contract = boa.load('favorites.vy')
    
    favorites_contract.add_number("Alice", 7)
    
    print(f"Person Data: {favorites_contract.person_list(0)}") 
    

if __name__ == "__main__":
    main()