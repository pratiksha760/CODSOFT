def book():
    contacts = {}
    while True:
        print("\n Contact Book")
        print(" 1. Create Contact")
        print(" 2. View Contacts")
        print(" 3. Update Contact")
        print(" 4. Delete Contact")
        print(" 5. Search Contact")
        print(" 6. Count Contact")
        print(" 7. Exit")
        try:
            choice= int(input("Enter your choice  = "))
        except ValueError:
            print("Enter number !!")
            continue
        if choice==1:
            name = input("Enter name = ")
            if name in contacts:
                print("contact already exists")
            else:
                age= input("Enter Age = ")
                email = input("Enter Email =")
                mobile = input("Enter Mobile Number = ")
                contacts[name]={'age':int(age),'email':email,'mobile':mobile}
                print(f"Contact name {name} has been saved succefully! ")
        elif choice==2:
            name =input("Enter name of contact you want to View = ")
            if name in contacts:
                contact =contacts[name]
                print(f"Name : {name} , Age : {age} , Mobile : {mobile} , Email : {email}  ")
            else:
                print("Contact not found")
        elif choice==3:
            name = input("Enter name to update contact  ")
            if name in contacts:
                age= input("  Enter updated Age = ")
                email = input("Enter updated Email =")
                mobile = input("Enter updated Mobile Number = ")
                contacts[name]={'age':int(age),'email':email,'mobile':mobile}
            else:
                print("Contact not found !!")
        elif choice==4:
            name  = input("Enter name to delete contact  ")
            if name in contacts:
                del contacts[name]
                print("Contact deleted !!")
            else :
                print("Contact not found")
        elif choice==5:
            search_name  = input("Enter name to search contact  ")
            found =False
            for name,contact in contacts.items():
                if search_name.lower() in name.lower():
                    print(f"Found - Name : {name} , Age : {age} , Mobile : {mobile} , Email : {email} ")
                    print("Contact Found ")
                    found=True
            if not found:
                    print("Contact not found with that name")
        elif choice ==6:
            print(f"Total contacts are {len(contacts)} ")
        elif choice==7:
            print("Thank you for using Contact book ......")
            print("Closing the program ")
            break
        else:
            print("Invalid input ")
            
book()