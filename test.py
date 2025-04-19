from my_classes import Subject 

def main():
    # Subject anlegen und auf den Server laden
    subject = Subject("Anna", "Müller", "female", "1995-06-12")
    subject.put()  # legt die Person mit dem Vornamen auf dem Server an

    # Email aktualisieren
    subject.email = "anna.mueller@example.com"
    subject.update_email()

    # Ausgabe zur Kontrolle
    print(subject)

if __name__ == "__main__":
    main()