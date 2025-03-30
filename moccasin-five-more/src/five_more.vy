#pragma version 0.4.0
# @licence MIT

import favorites
import second_mod

initializes: favorites
initializes: second_mod

exports: (
    favorites.add_number,
    favorites.retrieve,
    second_mod.setBool,
    second_mod.getBool
)

@deploy
def __init__():
    favorites.__init__()
    second_mod.__init__()   

@external
def store(new_num: uint256):
    favorites.my_fav_num = new_num + 5


   
    
