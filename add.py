from connection import execute_query

#leaving this so I can go back over the process of solving this

#this is working if I hard code the values, but when I try to add them as variables, I am getting the error:
#name 'Error' is not defined
#maybe this has to do with the formatting of the variables?
#also this error seems to occur whenever the hero name is not unique
#this is confirmed 
#that seems to have been the cause of the error

#get the 3 fields to dynamically fill :done:

#get the fields filled by input that is passed in via a few questions.

#######################
## Adding a New Hero ##
#######################

def add_hero(hero, about, bio):
    add_a_hero="""
    INSERT INTO heroes (name, about_me, biography)
    VALUES ('{}', '{}', '{}')
    """.format(hero, about, bio)
    add=execute_query(add_a_hero)
    print('Hero added')

# add_hero('hero2', 'about', 'bio')