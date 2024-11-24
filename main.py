import random

def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("*****************")
    print("  |  ".join(row))
    print("*****************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 2
        elif row[0] == "🍉":
            return bet * 3
        elif row[0] == "🍋":
            return bet * 4
        elif row[0] == "🔔":
            return bet * 5
        elif row[0] == "⭐":
            return bet * 10
    return 0

def deposit():
    while True:
        amount = input("Enter the amount you would like to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
            else:
                print("Deposit must be greater than 0.")
        else:
            print("Please enter a valid number.")

def main():
    print("***************************")
    print("Welcome to the Slot-Machine")
    print("Symbols: 🍒  🍉  🍋  🔔  ⭐")
    print("Match any 3 in a row to win 💰")
    print("***************************")

    balance = deposit()  # User sets the initial balance

    while True:
        print(f"Current balance is ${balance}")
        bet = input("Enter the bet amount: ")
        if not bet.isdigit():
            print('Please enter a valid number.')
            continue
        bet = int(bet)

        if bet > balance:
            print(f"Bet amount cannot exceed your current balance of ${balance}.")
            continue
        if bet <= 0:
            print("Bet must be greater than 0.")
            continue
        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)
        if payout > 0:
            print(f"You won ${payout}!")
        else:
            print("Sorry! You lost this round.")

        balance += payout
        print(f"Your current balance is ${balance}")

        if balance == 0:
            print("Your balance is $0. Please make a deposit to continue playing.")
            new_deposit = deposit()
            balance += new_deposit
            print(f"Your updated balance is ${balance}.")  # Notify only after a zero-balance deposit

        play_again = input("Do you want to play again? (Y/N): ").upper()
        if play_again != "Y":
            break

    print("*************************************************")
    print(f"Game is over! Your final balance is ${balance}")
    print("*************************************************")

if __name__ == "__main__":
    main()
