def main():
    friends = ["Ayla", "Noah", "Liam"]
    for friend in friends:
        print(send_message(friend,"Akumi"))

def send_message(receiver, sender):
    return f"""
    Hello {receiver}
   ***This is a message from Akumi:***
    ------------"Have a wonderful day!"-------

    Sincerely,
    ***{sender}***"""

main()    