def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
    'Full Name': 'James Wheeler',
    'Student_ID': 10279432,
    'Pizza_Toppings': [
        'Pepperoni', 
        'Sausage', 
        'Olives'
    ],
    'Movies': [
        'The Menu',
        'Knives Out: Glass Onion',
        'Last Night In Soho'
    ]
}

    # TODO: Step 3 - Add another movie to the data structure
    about_me['Movies'].insert(1, 'Batman: Assault on Arkham')
    print (about_me)
# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    Full_Name = about_me['Full Name'].split()
    First_Name = Full_Name[0]
    print(f"My name is {about_me['Full_Name'].title()} but you can call me High Supreme Omega Galactic Emperor{about_me[First_Name].title}")
    print(f"My student ID is {about_me['Student_ID']}")
    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    about_me['Pizza_Toppings'].extend(toppings)

    for i,p in enumerate(about_me['Pizza_Toppings']):
        about_me['Pizza_Toppings'][i] = p.lower()

    about_me['Pizza_Toppings'].sort()
    
    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print('\nMy favorite pizza toppings are:')
    for topping in about_me['Pizza_Toppings']:
        print(f"\t- {topping.title()}")
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    print("My favorite movies are:")
    print(', '.join(movie_list))
    return
    
if __name__ == '__main__':
    main()