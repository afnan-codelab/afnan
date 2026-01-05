def main():
  correct_password = "12345"
  attempts = 5

  while attempts > 0:
    password = input("Enter the password: ")

    if password == correct_password:
        print("Access granted. Welcome!")
        break
    else:
        attempts -= 1
        if attempts > 0:
             print("Wrong password. Attempts left:", attempts)
        else:
            print("Too many incorrect attmpts. Authorities have been alerted!")
if __name__ == "__main__":
    main()
