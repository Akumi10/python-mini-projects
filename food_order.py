def main():
    friends = ["Yuki", "Rina", "Haru", "Sora", "Aiko"]
    foods = ["Sushi", "Pasta", "Ramen", "Pizza", "Ice cream"]
    for i in range(len(friends)):
        print(create_invitation(friends[i], foods[i]))

def create_invitation(name, food):
    return f"""
    -------------Hello {name} !---------------------
****You are invited to Akumi's special dinner tonight 🍽️
We'll be serving your favorite meal: {food} 😋
Hope to see you there!**** """



main()
