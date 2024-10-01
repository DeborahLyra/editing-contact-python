contact_list = []

def add_contact():
   name = input('What is the name?')
   phone = input('What is the phone?')
   email = input('What is the email?')
   favourite = input('This contact is a favourite (yes or no)?').lower()

   if favourite == 'yes':
       favourite_type = True
   else: 
        favourite_type = False
  
       
   contact = {'name': name, 'phone': phone, 'email': email, 'favourite': favourite_type}
   
   contact_list.append(contact)
   print('Added contact')
   
def list_all_contacts(contact_list):
    for index, contact in enumerate(contact_list):
        status = '♥' if contact['favourite'] else ' '
        print(f"{index + 1}. {status} {contact['name']} ")

def mark_favourite(contact_list):
    list_all_contacts(contact_list)
    contact_num = int(input('Which contact do you want to change the favourite status? '))
    contact_list[contact_num - 1]['favourite'] = not contact_list[contact_num - 1]['favourite']
    print('Favourite status updated!')
  
def see_favourites(contact_list):
     for index, contact in enumerate(contact_list):
         if contact['favourite'] == True:
             print(f"{index + 1}. {contact['name']}") 
    
def delete_contact(contact_list):
    list_all_contacts(contact_list)
    contact_to_delete = int(input('Which contact do you want to delete? '))

    if 1 <= contact_to_delete <= len(contact_list):
        contact_list.pop(contact_to_delete - 1)
        print("Deleted successfully!")
    else:
        print("Invalid number")

        
def menu():
    print("Starting Application")
    print("\n1. Add a contact")
    print("2. List all contacts")
    print("3. Mark contact as favourite")
    print("4. See favourites")
    print("5. Delete contact")
    print("6. Exit")
    return input("Choose an option: ")

while True:
    option = menu()
    
    if option == '1':
        add_contact()
    elif option == '2':
        list_all_contacts(contact_list)
    elif option == '3':
        mark_favourite(contact_list)
    elif option == '4':
        see_favourites(contact_list)
    elif option == '5':
        delete_contact(contact_list)
    elif option == '6':
        print("Exiting...")
        break
    else:
        print("Invalid option, please try again.")
    
    