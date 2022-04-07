# This is why you'll execute a series of SQL statements during demo day.
from connection import execute_query
from find import find_hero
from find import find_hero_by_ability
from add import add_hero
from delete import delete_hero
from change import change_ability

# select_heroes = """
#     SELECT * FROM heroes
#     ORDER BY id DESC 
# """

############################################################################################################
## The whole program should run inside of this function, and allow users to type in what they want to do" ##
############################################################################################################

def initialize():
    instruction = input(
    """\n\n\nWhat do you want to do?
    \nFind: Find a specific Hero. 
    \nCreate: Make up your own hero.
    \nDestroy: Delete a hero.
    \nAdd: Give a Hero a specific power\n""")
    command = instruction.lower()
    if command == 'find':
        print('How do you want to find them?')
        search_type=input('\nName: Search by name.\nAbility: Search by ability.\n')
        if search_type == 'name':
            user_search=input('What hero are you looking for?\n')
            find_hero(user_search)
        elif search_type == 'ability':
            ability_search = input('What ability do they have?\n')
            find_hero_by_ability(ability_search)
        else:
            print('I don\'t know what you mean.')
            initialize()
    elif command == 'create':
        user_name=input('Tell me about your hero!\nWhat\'s their name?\n')
        user_about=input('That\'s a great name!  What would they say about themselves?\n')
        user_bio=input('I bet they would say that.  What\'s their bio?\n')
        add_hero(user_name, user_about, user_bio)
    elif command == 'destroy':
        user_delete=input('What hero do you want to wipe out of existence?\n')
        delete_hero(user_delete)
    elif command == 'add':
        ##call the change element function
        target_hero=input('What hero do you want to change?\n')
        target_power=input('What new power should they have?\n')
        change_ability(target_hero, target_power)
    elif command == 'relationships':
        hero_1, hero_2=input('Type in 2 hero names. Make sure to separate them with ').split('+', maxsplit)
    else:
        print('\nHuh?  I don\'t understand.  Try saying something else\n')
    initialize()
        
initialize()