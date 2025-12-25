import random

name = input("What is your name?: ")
age = int(input("How old are you?: "))

total_points = 0

def check_treasure():
    total = 0
    for site in range(1, 4):
        print(f"\nYou are now in site: {site}")
        choice = input("Would you like to search in this place? (yes/no): ").lower()
        
        if choice == "yes":
            found = random.randint(10, 100)
            total += found
            print(f"You earned: {found} coins :D")
            
            if found >= 100:
                print("You have found the great treasure 🏆")
            elif 50 <= found <= 99:
                print("You got a medium-sized treasure 💰")
            else:
                print("You didn't find anything, try again 🔍")
        else:
            print("You did not search this site")
    
    return total

total_points = check_treasure()

print(f"""
=======================================================
              **Explorer name: {name}**
                **Age: {age}**
                Total points: {total_points}
=======================================================
""")
