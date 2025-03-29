#pragma version 0.4.0
#@licence MIT

from interfaces import i_favorites

list_of_favorite_contract: public(DynArray[i_favorites, 100])
original_favorite_contract:address



@deploy
def __init__(original_contract: address):
    self.original_favorite_contract = original_contract

@external
def create_favorites_contract():
    new_favorite_contract: address = create_copy_of(self.original_favorite_contract)
    self.list_of_favorite_contract.append(i_favorites(new_favorite_contract))
    
@external
def store_from_factory(favorite_index: uint256, new_num: uint256): 
    favorites_contract: i_favorites = self.list_of_favorite_contract[favorite_index]
    extcall favorites_contract.store(new_num)

@external
@view
def view_from_factory(index: uint256) -> uint256:
    return staticcall self.list_of_favorite_contract[index].retrieve()