#pragma version 0.4.0
# @licence MIT

prev_bool: public(bool)

@deploy
def __init__():
    self.prev_bool = False
   
@external
def setBool(var: bool):
    self.prev_bool = var

@external
@view
def getBool() -> bool:
    return self.prev_bool
    




    



    

    
    
    

    



    
