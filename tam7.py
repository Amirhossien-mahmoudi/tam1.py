class Contact:
    def __init__(self, name, phone):
        if not phone.isdigit() or len(phone) != 11:
            raise ValueError
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"{self.name} - {self.phone}"


contacts = []

while True:
    print("\nMenu Asli")
    print("1. Ezafe kardan mokhatab")
    print("2. Namayesh hame mokhataban")
    print("3. Zakhire va khorooj")

    try:
        choice = int(input("Gozine mored nazar ra vared konid: "))
    except ValueError:
        print("Lotfan faghat adad vared konid")
        continue

    if choice == 1:
        name = input("Nam mokhatab: ")
        phone = input("Shomare telefon: ")

        try:
            contact = Contact(name, phone)
            contacts.append(contact)
            print("Mokhatab ba movafaghiat ezafe shod")
        except ValueError:
            print("Format shomare eshtebah ast, dobare talash konid")

    elif choice == 2:
        if not contacts:
            print("Hich mokhatabi vojood nadarad")
        else:
            for c in contacts:
                print(c)

    elif choice == 3:
        print("Ettela'at zakhire shod, barname baste shod")
        break

    else:
        print("Gozine eshtebah ast")
