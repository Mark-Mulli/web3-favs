def test_starting_number(fixture_deploy):
    
    assert fixture_deploy.retrieve() == 7

def test_can_change_values(fixture_deploy):
   
    #act
    fixture_deploy.store(42)
    #assert
    assert fixture_deploy.retrieve() == 42
    
def test_add_person(fixture_deploy):
    #arrange
    name = "Alice"
    favs_number = 34
    #act
    fixture_deploy.add_number(name, favs_number)
    #assert
    assert fixture_deploy.person_list(0) == (name, favs_number)