import os
import boa
from boa.network import NetworkEnv, EthereumRPC
from dotenv import load_dotenv
from eth_account import Account

load_dotenv()

MY_CONTRACT = "0xCf7Ed3AccA5a467e9e704C703E8D87F634fB0Fc9"

def main():
    rpc = os.getenv('RPC_URL')
    boa_env = NetworkEnv(EthereumRPC(rpc))
    boa.set_env(boa_env)

    private_key = os.getenv('PRIVATE_KEY')
    my_account = Account.from_key(private_key)
    boa.env.add_account(my_account, force_eoa = True)
    
    contract = boa.load_partial("bool_change.vy")
    prev_contract = contract.at(MY_CONTRACT)
    
    boolStatus = prev_contract.get_bool()
    print(f"Current bool status: {boolStatus}")
    
    stateChange = prev_contract.set_bool(True)
    print(f"Changed bool to {stateChange}")


if __name__ == '__main__':
    main()