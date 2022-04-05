# This is why you'll execute a series of SQL statements during demo day.
from connection import execute_query

select_heroes = """
    SELECT * FROM heroes
    ORDER BY id DESC 
"""

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
def find_hero(name):
            select_a_hero = """
            SELECT name, about_me FROM heroes
            WHERE name = '{}'
            """.format(name)
            hero = execute_query(select_a_hero).fetchall()
            print(hero)



#this should add a hero.  It is working when things are hard-coded into the add_a_hero string, but not when they are placed in as variables
def add_hero(name, about_string, biography):
    about = about_string
    add_a_hero="""
    INSERT INTO heroes (name, about_me, biography)
    VALUES ({0}, {1}, {2})
    """.format(name, about_string, biography)
    add=execute_query(add_a_hero)
    print(add)

# add_hero('Quincy', 'no idea', 'He forgot his keys')


############################################################################################################
## The whole program should run inside of this function, and allow users to type in what they want to do" ##
############################################################################################################

def initialize(instruction):
    if instruction == 'find' or 'Find':
        print('What Hero are you looking for? ')
        x=input()
        find_hero(str(x))
    elif instruction == 'Create' or 'create':
        print('Tell me about your hero! \n What\'s their name? ')
        name=input()
        print('That\'s a great name!  What would they say about themselves?')
        about_string=input()
        print('I bet they would say that.  What\'s their bio?')
        bio=input()
        add_hero(name, about_string, biography)
        
print(
    'Instructions\n What do you want to do?\n Find: Type a Hero\'s name to learn more about them \n Create: Make up your own hero.'
)
instruction = input()
initialize(instruction)