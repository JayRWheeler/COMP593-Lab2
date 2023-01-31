def main():
    about_me = {
        'full_name': 'James Wheeler',
        'student_id': 10279432,
        'pizza_toppings': ['CHICKEN', 'SAUSAGE', 'PEPPERONI'],
        'movies': [
            {'title': 'Knives Out: Glass Onion', 'genre': 'mystery'},
            {'title': 'Last Night In Soho', 'genre': 'thriller'},
            {'title': 'The Lord Of The Rings', 'genre': 'fantasy'}
        ]
    }

    about_me['movies'].insert(0, {'title': 'Batman: Assault on Arkham', 'genre': 'Action'})
    about_me['pizza_toppings'].extend(('bacon', 'hot peppers', 'jalapeno'))
    about_me['pizza_toppings'].sort()

    print_student_name_and_id(about_me)
    print_pizza_toppings(about_me)
    print_movie_genres(about_me)
    print_movie_titles(about_me['movies'])
    
def print_student_name_and_id(about_me):
    first_name = about_me['full_name'].split()[0]
    print(f"My name is {about_me['full_name']}, but you can call me Supreme Galactic Emperor {first_name}.")
    print(f"My student ID is {about_me['student_id']}.")
    print()
    
def print_pizza_toppings(about_me):
    print("My favourite pizza toppings are:")
    for topping in about_me['pizza_toppings'][:3]:
        print(f"- {topping}")
    print("\nMy favourite pizza toppings are:")
    for topping in about_me['pizza_toppings'][3:]:
        print(f"- {topping}")

def print_movie_genres(about_me):
    genres = [movie['genre'].lower() for movie in about_me['movies']]
    genre_str = ', '.join(genres)
    if len(genres) > 1:
        genre_str = genre_str.rsplit(',', 1)[0] + ", and" + genre_str.rsplit(',', 1)[1]
    print(f"\nI like to watch {genre_str} movies.")
    print()

def print_movie_titles(movie_list):
    titles = [movie['title'].title() for movie in movie_list]
    title_str = ', '.join(titles)
    if len(titles) > 1:
        title_str = title_str.rsplit(',', 1)[0] + ", and" + title_str.rsplit(',', 1)[1]
    print(f"Some of my favourite movies are {title_str}!")
    
if __name__ == '__main__':
    main()