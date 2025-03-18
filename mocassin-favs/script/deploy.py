from src import favorites
from moccasin.boa_tools import VyperContract


def deployed() -> VyperContract:
    favs_contract: VyperContract = favorites.deploy()
    starting_number: int = favs_contract.retrieve()
    print(f"Starting number: {starting_number}")
    
    favs_contract.store(7)
    end: int  = favs_contract.retrieve()
    print(f"Ending number: {end}")
    return favs_contract
    

def moccasin_main() -> VyperContract:
    return deployed()