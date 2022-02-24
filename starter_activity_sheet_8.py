# program with errors for week 8

def example():
    more_pets = "y"
    print("Tell me about the pets do you have at home?")
    print()
    while more_pets == "y":      
          next_pet = input("Enter your dog's name  ")
          print("Thanks for adding "+ next_pet)
          more_pets = input("Do you have any more pets? (y/n)")
         
    print("End of program")
