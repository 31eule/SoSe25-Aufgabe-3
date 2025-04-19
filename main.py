from my_classes import Person

def main():
    # Neue Person anlegen und zum Server posten
    person = Person( "Anna", "Müller", "female")
    person.post()

if __name__ == "__main__":
    main()
