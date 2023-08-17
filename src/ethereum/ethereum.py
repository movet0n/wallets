import json
from tqdm import tqdm
from web3 import Web3, HTTPProvider

from src.utils.constants import *


w3 = Web3(HTTPProvider("https://eth.llamarpc.com"))


def generate_wallet(alias=None, check_function=None):
    acc = w3.eth.account.create()
    wallet_info = {
        "alias": alias or acc.address,
        "address": acc.address,
        "private_key": acc._private_key.hex(),
        "proxy": "",
    }

    if not check_function or check_function(acc.address):
        return wallet_info
    return None


def create_wallets():
    total_wallets = int(input("\n>>> Enter the number of wallets you want to create: "))

    wallets = [generate_wallet(alias=f"Set-1-{i+1}") for i in range(total_wallets)]

    with open("wallets.json", "w") as f:
        json.dump(wallets, f, indent=4)

    print(f"\n>>> Created {total_wallets} wallets and saved to wallets.json")


def create_wallet_with_specific_ending():
    alias = input("\n>>> Enter the wallet ending you want to create: ")

    for _ in tqdm(range(MAX_ATTEMPTS), desc="> Searching for specific wallet ending"):
        wallet_info = generate_wallet(alias, check_function=lambda address: address.endswith(alias))

        if wallet_info:
            with open("wallets.json", "w") as f:
                json.dump(wallet_info, f, indent=4)

            print(f"\n>>> Created a wallet with [{alias}] and saved to wallets.json after {_ + 1} attempts.")
            break
    else:
        print(f"\n>>> After {MAX_ATTEMPTS} attempts, couldn't find a wallet ending with [{alias}].")


def create_wallet_that_contains():
    alias = input("\n>>> Enter a text you want your wallet to contain: ")

    for _ in tqdm(range(MAX_ATTEMPTS), desc="> Searching for specific wallet content"):
        wallet_info = generate_wallet(alias, check_function=lambda address: alias.lower() in address.lower())

        if wallet_info:
            with open("wallets.json", "w") as f:
                json.dump(wallet_info, f, indent=4)

            print(f"\n>>> Created a wallet with [{alias}] and saved to wallets.json after {_ + 1} attempts.")
            break
    else:
        print(f"\n>>> After {MAX_ATTEMPTS} attempts, couldn't find a wallet that contains [{alias}].")
