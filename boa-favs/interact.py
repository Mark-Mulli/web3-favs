import os
from boa.network import NetworkEnv, EthereumRPC
import boa
from dotenv import load_dotenv
from eth_account import Account


MY_CONTRACT = "0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512"

load_dotenv()

def main():
    rpc = os.getenv('RPC_URL')
    env = NetworkEnv(EthereumRPC(rpc))
    boa.set_env(env)
    
    anvil_key = os.getenv("ANVIL_KEY")
    my_account = Account.from_key(anvil_key)
    boa.env.add_account(my_account, force_eoa = True)
    
    favs_deployer = boa.load_partial('favorites.vy')
    favs_contract = favs_deployer.at(MY_CONTRACT)
    
    favs_number = favs_contract.retrieve()
    print(f"The favorite number is {favs_number}")
    
    
    favs_contract.store(22)
    favs_number_updated = favs_contract.retrieve()
    print(f"The updated favorite number is {favs_number_updated}")

if __name__ == "__main__":
    main()