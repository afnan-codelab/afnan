def main():
    names = ["Afnan", "Arwa", "Hadeel", "Lian", "Haifa", "Ayat", "Floh"]

    search_name = input("Enter a name to search for: ")

    if search_name in names:
        print(search_name, "was found in the list.")
    else:
        print(search_name, "was not found in the list.")

if __name__ == "__main__":
    main()
