class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print("\n--- Book Information ---")
        print(f"Book title is: {self.title}")
        print(f"Book author is: {self.author}")
        print(f"Book price is: {self.price}\n")

    def apply_discount(self, percent):
        discount_amount = self.price * (percent / 100)
        self.price -= discount_amount


book1 = Book("The Alchemist", "Paulo Coelho", 80000)
book2 = Book("1984", "George Orwell", 120000)

print("First book information:")
book1.display_details()

print("Second book information:")
book2.display_details()

book2.apply_discount(20)

print("Final information for first book:")
book1.display_details()

print("Final information for second book:")
book2.display_details()
