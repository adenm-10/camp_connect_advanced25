i_am_hungry = input("Are you hungry? (yes/no): ").strip().lower() == "yes"

if (i_am_hungry):
    i_am_broke = input("Are you broke? (yes/no): ").strip().lower() == "yes"
    
    if (not i_am_broke):
        print("Order some wingstop")
    else:
        print("Starve")

else:
    print("You don't need to eat")

a = 1
if (a == 0):
    print(0)
elif (a == 2):
    print(2)
else:
    print()
