import boa

def main():
    print("Reading the vyper code and deploying it")
    favorites_contract = boa.load('favorites.vy')
    
    starting_favorite_number = favorites_contract.retrieve()
    
    print(f"The starting favorite number is {starting_favorite_number}")
    
    favorites_contract.store(7)
    ending_favorite_number = favorites_contract.retrieve()
    print(f"The ending favorite number is {ending_favorite_number}")

if __name__ == "__main__":
    main()