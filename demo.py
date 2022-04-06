# This is why you'll execute a series of SQL statements during demo day.
from connection import execute_query
from find import find_hero
from add import add_hero

# select_heroes = """
#     SELECT * FROM heroes
#     ORDER BY id DESC 
# """

# heroes = execute_query(select_heroes).fetchall()
# for hero in heroes:
#     print(hero[1])

# select_a_hero = """
#     SELECT name, about_me FROM heroes
#     WHERE name = 'The Seer'
# """

# hero = execute_query(select_a_hero).fetchall()
# print(hero)


#####################################
##searching for a precise hero name##
#####################################
# def find_hero(name):
#             select_a_hero = """
#             SELECT name, about_me FROM heroes
#             WHERE name = '{}'
#             """.format(name)
#             hero = execute_query(select_a_hero).fetchall()
#             print(hero)



#this should add a hero.  It is working when things are hard-coded into the add_a_hero string, but not when they are placed in as variables
# def add_hero(name, about_string, biography):
#     about = about_string
#     add_a_hero="""
#     INSERT INTO heroes (name, about_me, biography)
#     VALUES ({0}, {1}, {2})
#     """.format(name, about_string, biography)
#     add=execute_query(add_a_hero)
#     print(add)

# add_hero('Quincy', 'no idea', 'He forgot his keys')


############################################################################################################
## The whole program should run inside of this function, and allow users to type in what they want to do" ##
############################################################################################################

def initialize():
    instruction = input('Instructions:\n What do you want to do?\n Find: Type a Hero\'s name to learn more about them \n Create: Make up your own hero.\n')
    command = instruction
    if command == 'Find':
        print('What Hero are you looking for? ')
        x=input()
        find_hero(x)
    elif command == 'Create' or 'create':
        print('Tell me about your hero!\n What\'s their name?\n')
        user_name=input()
        print('That\'s a great name!  What would they say about themselves?\n')
        user_about=input()
        print('I bet they would say that.  What\'s their bio?\n')
        user_bio=input()
        add_hero(user_name, user_about, user_bio)
    elif command == 'Destroy':
        user_delete=input('What hero do you want to wipe out of existence?\n')
        delete_hero(user_delete)
    else:
        print('Huh?  I don\'t understand.  Try saying something else')
        initialize()
        
initialize()