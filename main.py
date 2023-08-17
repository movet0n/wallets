from src.ethereum.ethereum import *


def select_option(option):
    if option == 1:
        create_wallets()
    elif option == 2:
        create_wallet_with_specific_ending()
    elif option == 3:
        create_wallet_that_contains()
    else:
        print(">>> Please select an option 1-3. Try again.")


if __name__ == "__main__":
    option = int(
        input(
            "\n>>> Options:\
                       \n> 1. Create wallets.\
                       \n> 2. Create a wallet with a specific ending.\
                       \n> 3. Create a wallet that contains a text.\
                       \n  ===== ===== ===== ===== =====\
                       \n> Please select an option: "
        )
    )
    select_option(option)
