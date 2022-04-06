from connection import execute_query

#####################
## Deleting a Hero ##
#####################

def delete_hero(hero):
    name = hero
    delete_a_hero="""
    DELETE FROM heroes
    WHERE name='{}'
    """.format(hero)
    confirm = input('Are you sure you want to delete this hero? y/n\n ')
    if confirm == 'y':
        delete=execute_query(delete_a_hero)
        print('Gone forever!')
    else:
        print('They\'ll live...\n ...for now...')

# delete_hero(hero1)