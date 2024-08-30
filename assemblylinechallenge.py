import time

def print_title():
    title = """
    ===========================================
               THE ASSEMBLY LINE CHALLENGE
    ===========================================
    """
    print(title)

def print_worker_art():
    art = """
    ____________________
   |  _________________  |
   | |              0. | |
   | |              0. | |
   | |              0. | |
   | |_________________| |
   |   ________________   |
   |  |                |  |
   |__|________________|__|
    """
    print(art)

def print_owner_art():
    art = """
     __________
    |  ______  |
    | |      | |
    | |      | |
    | |______| |
    |  ______  |
    | |      | |
    | |______| |
    |__________|
    """
    print(art)

def print_consumer_art():
    art = """
    _______________
   /               \\
  /  __         __  \\
 |  |__|       |__|  |
 |               /   |
 |               \\   |
  \\               \\/
   \\______________/
    """
    print(art)

def slow_print(text, delay=0.009):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print("\n")

def start_game():
    print_title()
    slow_print("Welcome to 'The Assembly Line Challenge'!")
    slow_print("You will experience life during the Roaring Twenties from different perspectives.")
    slow_print("Choose your character: Factory Worker, Small Business Owner, or Consumer.")
    
    character = input("Enter your character (Worker/Owner/Consumer): ").lower()
    if character == "worker":
        factory_worker()
    elif character == "owner":
        small_business_owner()
    elif character == "consumer":
        consumer()
    else:
        print("Invalid choice. Please choose again.")
        start_game()

def factory_worker():
    print_worker_art()
    slow_print("\nYou are a Factory Worker in the 1920s.")
    slow_print("You need to manage your work hours and negotiate wages while maintaining your well-being.")

    happiness = 50
    money = 100

    while True:
        print("\nYour current happiness: ", happiness)
        print("Your current money: $", money)
        slow_print("\nIt's a new day at work. What do you want to do?")
        slow_print("1. Work extra hours for more pay")
        slow_print("2. Take a rest day to increase happiness")
        slow_print("3. Negotiate for higher wages")
        slow_print("4. Join a workers' union for better rights")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            money += 20
            happiness -= 10
            slow_print("You earned $20, but your happiness decreased.")
        elif choice == "2":
            happiness += 10
            slow_print("You took a rest day. Your happiness increased.")
        elif choice == "3":
            if happiness < 40:
                slow_print("Your boss didn't accept your negotiation. Try again when you're happier.")
            else:
                money += 30
                slow_print("You successfully negotiated for higher wages! You earned $30 more.")
        elif choice == "4":
            if money < 50:
                slow_print("Joining the union requires $50 for membership, which you don't have.")
            else:
                money -= 50
                happiness += 20
                slow_print("You joined the workers' union! Your happiness increased, but you spent $50.")
        else:
            slow_print("Invalid choice. Please select again.")

        # Game end conditions
        if happiness <= 0:
            slow_print("\nYour happiness has dropped to zero. You are burnt out. Game Over.")
            break
        elif money >= 200:
            slow_print("\nCongratulations! You've saved up enough money for a comfortable life. You win!")
            break

def small_business_owner():
    print_owner_art()
    slow_print("\nYou are a Small Business Owner in the 1920s.")
    slow_print("You need to decide whether to adopt mass production and manage your finances wisely.")

    reputation = 50
    profit = 100

    while True:
        print("\nYour current reputation: ", reputation)
        print("Your current profit: $", profit)
        slow_print("\nIt's a new business quarter. What do you want to do?")
        slow_print("1. Invest in mass production technology")
        slow_print("2. Maintain current production methods")
        slow_print("3. Cut costs to increase profit margins")
        slow_print("4. Expand into new markets")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            profit += 50
            reputation -= 20
            slow_print("You invested in mass production and profits increased, but reputation decreased.")
        elif choice == "2":
            profit -= 10
            reputation += 10
            slow_print("You maintained current methods. Profit decreased, but reputation improved.")
        elif choice == "3":
            profit += 20
            reputation -= 10
            slow_print("You cut costs and increased profits, but at the cost of reputation.")
        elif choice == "4":
            profit += 30
            reputation += 20
            slow_print("You expanded into new markets! Your profit and reputation both increased.")
        else:
            slow_print("Invalid choice. Please select again.")

        # Game end conditions
        if reputation <= 0:
            slow_print("\nYour reputation has dropped to zero. You went out of business. Game Over.")
            break
        elif profit >= 300:
            slow_print("\nCongratulations! Your business has thrived. You win!")
            break

def consumer():
    print_consumer_art()
    slow_print("\nYou are a Consumer in the 1920s.")
    slow_print("You need to balance your budget and decide on which new products to purchase.")

    satisfaction = 50
    savings = 100

    while True:
        print("\nYour current satisfaction: ", satisfaction)
        print("Your current savings: $", savings)
        slow_print("\nIt's a new shopping season. What do you want to do?")
        slow_print("1. Buy a new car")
        slow_print("2. Save money for the future")
        slow_print("3. Buy household appliances")
        slow_print("4. Invest in the stock market")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            savings -= 80
            satisfaction += 20
            slow_print("You bought a new car. Your satisfaction increased, but your savings decreased.")
        elif choice == "2":
            savings += 30
            satisfaction -= 10
            slow_print("You saved money for the future. Your savings increased, but satisfaction decreased.")
        elif choice == "3":
            savings -= 40
            satisfaction += 10
            slow_print("You bought new household appliances. Your satisfaction increased, but savings decreased.")
        elif choice == "4":
            if savings < 50:
                slow_print("Investing in the stock market requires at least $50, which you don't have.")
            else:
                savings += 50
                satisfaction += 10
                slow_print("You invested in the stock market! Your savings and satisfaction both increased.")
        else:
            slow_print("Invalid choice. Please select again.")

        # Game end conditions
        if satisfaction <= 0:
            slow_print("\nYour satisfaction has dropped to zero. You are unhappy with life. Game Over.")
            break
        elif savings >= 200:
            slow_print("\nCongratulations! You've saved enough for a stable future. You win!")
            break

# Start the game
start_game()
