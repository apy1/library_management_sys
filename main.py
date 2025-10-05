def addBook():

    name = str(input("\nEnter name of the book: "))
    f = open("books.txt", "a")
    f.write(name)
    print("\n Your book has been added!!!")
    f.close()

def viewBook():

    f = open("books.txt", "r")
    print("\nBooks:")
    print("\n", f.read())
    f.close()

def searchBook():

    search = input("\nEnter the book to search: ").strip()
     
    with open("books.txt", "r") as f:
        for line in f:
            if search.lower() in line.lower():   # case-insensitive search
                print(f"\nBook found: {line.strip()}")
            else:
                print("\nBook not found")

def borrowBook():

    name = str(input("\nEnter your name: "))
    book = str(input("\nEnter the book to borrow: "))
    date = int(input("\nEnter start date: "))
    date1 = int(input("\nEnter end date: "))
    a = "\nName: " + name + "\tBook: " + book + "\tIssue Date: " + str(date) + "\tEnd Date: " + str(date1)
    with open("borrow.txt", "a") as f:
        f.write(a)

    print(a)

def returnBook():

    name = str(input("\nEnter your name: "))
    book = str(input("\nEnter the book to return: "))
    date = int(input("\nEnter start date: "))
    date1 = int(input("\nEnter end date: "))
    a = "\nName: " + name + "\tBook: " + book + "\tIssue Date: " + str(date) + "\tEnd Date: " + str(date1)
    with open("return.txt", "a") as f:
        f.write(a)

def users():

    name = str(input("\nEnter your name: "))
    date = int(input("\nEnter start date: "))
    date1 = int(input("\nEnter end date: "))
    a = "\nName: " + name + "\tStarting date: " + str(date) + "\tEnd date: " + str(date1)
    with open("users.txt", "a") as f:
        f.write(a)

    with open("users.txt", "r") as f:
        print("\nCurrent users:\n", f.read())

def options():

    select = 0

    while select != 6:

        print("\n\n 1. Add books \n 2. View books \n 3. Search books \n 4. Borrow book \n 5. Return book \n 6. Add Users \n 7. Exit")

        try:
            select = int(input("\nEnter your choice: "))

        except ValueError:
            print("\n\nPlease enter an integer value.")

        if select == 1:
            addBook()

        if select == 2:
            viewBook()

        if select == 3:
            searchBook()

        if select == 4:
            borrowBook()

        if select == 5:
            returnBook()

        if select == 6:
            users()


options()



