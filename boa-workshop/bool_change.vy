# pragma version ^0.4.0

"""
@author Mark
@title Bool State Change
@license MIT

"""

my_bool: bool

@external
def set_bool(prev_bool: bool) -> bool:
    if (prev_bool == True):
        self.my_bool = True
    else:
        self.my_bool = False
    return self.my_bool

@external
@view
def get_bool() -> bool:
    return self.my_bool
