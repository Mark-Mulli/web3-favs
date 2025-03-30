from src import favorites, favorites_factory, five_more
from moccasin.boa_tools import VyperContract

def deploy_contract() -> VyperContract:
    contract: VyperContract = favorites.deploy()
    return contract

def deploy_factory(contract: VyperContract):
    contract_factory: VyperContract = favorites_factory.deploy(contract.address)
    contract_factory.create_favorites_contract()
    
    new_fav_address: str = contract_factory.list_of_favorite_contract(0)
    new_favorites_contract: VyperContract = favorites.at(new_fav_address)
    
    new_favorites_contract.store(77)
    print(f"Stored value: {new_favorites_contract.retrieve()}")
    
    contract_factory.store_from_factory(0, 88)
    print(f"Stored value: {new_favorites_contract.retrieve()}")
    print(f"original contract value: {contract.retrieve()}")

def deploy_five_more():
    five_more_contract: VyperContract = five_more.deploy()
    # print(five_more_contract.retrieve())
    # five_more_contract.store(90)
    # print(five_more_contract.retrieve())
    five_more_contract.setBool(True)
    print(five_more_contract.getBool())
def moccasin_main() -> VyperContract:
    favorites_contract = deploy_contract()
    deploy_factory(favorites_contract)
    deploy_five_more()
    
    
    