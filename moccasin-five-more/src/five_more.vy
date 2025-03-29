#pragma version 0.4.0
# @licence MIT

import favorites

initializes: favorites
exports: (
    favorites.add_number,
    favorites.retrieve
)

@deploy
def __init__():
    favorites.__init__()


@external
def store(new_num: uint256):
    favorites.my_fav_num = new_num + 5
    
    
