import os
from blockchain import Blockchain

def git_commit(block_index):
    """
    Auto-commit the current blockchain state to GitHub.
    """
    os.system("git add .")
    os.system(f'git commit -m "Auto Commit: Block {block_index}"')
    os.system("git push origin main")

def main():
    blockchain = Blockchain()
    print("Mini Blockchain Initialized!")

    while True:
        print("\nOptions:")
        print("1. Add Block")
        print("2. Show Blockchain")
        print("3. Validate Chain")
        print("4. Exit")
        choice = input("Choose: ")

        if choice == "1":
            data = input("Enter block data: ")
            block = blockchain.add_block(data)
            print(f"Block added! Index: {block.index}, Hash: {block.hash}")
            git_commit(block.index)  # Auto-commit & push
        elif choice == "2":
            for block in blockchain.chain:
                print(f"Index: {block.index}, Data: {block.data}, Hash: {block.hash}")
        elif choice == "3":
            valid = blockchain.is_chain_valid()
            print("Blockchain is valid!" if valid else "Blockchain is invalid!")
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()

