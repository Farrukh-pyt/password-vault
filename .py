from vault import PasswordVault

vault = PasswordVault()

while True:
    print("\n===== PASSWORD VAULT =====")
    print("1. Add Password")
    print("2. View Passwords")
    print("3. Search")
    print("4. Generate Password")
    print("5. Delete Password")
    print("6. Save")
    print("7. Exit")

    choice = input("Choose: ")

    if choice == "1":
        vault.add_password()

    elif choice == "2":
        vault.view_passwords()

    elif choice == "3":
        vault.search_password()

    elif choice == "4":
        vault.generate_password()

    elif choice == "5":
        vault.delete_password()

    elif choice == "6":
        vault.save()

    elif choice == "7":
        vault.save()
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
