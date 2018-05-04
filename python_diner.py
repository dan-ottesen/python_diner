mainMenu = ['Cheeseburger', 'Steak', 'BLT']
user = input('Which Entree would you like? We have a Cheeseburger, Steak, and a BLT.')

total = 0


if user == "Cheeseburger":
  print("My kind of order! That'll be $5.00") 
  total = total + 5.00
  
elif user == "Steak": 
  print("We only cook ours Medium Rare, hope that's okay!")
  total = total + 8.00


elif user == "BLT":
  print("Our bacon is amazing! You'll love it")
  total = total + 4.00


else:
    print("Sorry, we don't have that")


sideMenu = ['Salad', 'Onion Rings', 'Fries']
user = input('What side would you like? We have Salad, Onion Rings, and Fries')

if user == "Salad": 
  print("Our lettuce is ecoli free!")
  total = total + 1.00
  
elif user == "Fries":
  print("It comes with a side of Fry Sauce")
  total = total + 2.00

elif user == "Onion Rings":
  print("Great choice, ours are world famous...I think?")
  total = total + 2.75
  print(f'Your current total is ${total}')

else: 
  print("Sorry, we don't have that.")
  
user = input('Please choose one additional side, we have Salad, Onion Rings and Fries')

if user == "Salad":
    print("Our lettuce is ecoli free!")
    total = total + 1.00
    print(f'Your final payment comes to ${total}')

elif user == "Fries":
    print("It comes with a side of Fry Sauce")
    total = total + 2.00
    print(f'Your final payment comes to ${total}')

elif user == "Onion Rings":
    print("Great choice, ours are world famous...I think?")
    total = total + 2.75
    print(f'Your final payment comes to ${total}')

else:
    print('Sorry, we don\'t have that here')