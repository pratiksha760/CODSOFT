import random
choice_emoji ={"r":"🪨","p":"📃","s":"✂️"}
choices =('s','p','r')
def get_choice():
    while True:
        choice_input =input("Enter your choice (r,p,s) : ").lower()
        computer_choice = random.choice(choices)
        if choice_input not in choices:
            print("Invalid input")
            continue
            return choice_input
        
        elif choice_input == computer_choice:
            print(f"You choose {choice_emoji[choice_input]}")
            print(f"AI choose {choice_emoji[computer_choice]}")
            print("Its a Draw ")
        elif ( 
        (choice_input=='r' and computer_choice=='s') or
        (choice_input=='p' and computer_choice=='r') or
        (choice_input =='s'and computer_choice =='p')):
            print(f"You choose {choice_emoji[choice_input]}")
            print(f"AI choose {choice_emoji[computer_choice]}")
            print("You won 😊")
        else:
            print(f"You choose {choice_emoji[choice_input]}")
            print(f"AI choose {choice_emoji[computer_choice]}")
            print("You Loose")
            choose =input("want to continue(y/n)").lower()
            if choose =='n':
                break
            else:
                continue
                 
get_choice()