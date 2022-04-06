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
    confirm_message=print('Are you sure you want to delete {}? y/n\n').format(name)
    confirm = input(confirm_message)
    if confirm == 'y':
        delete=execute_query(delete_a_hero)
        print('Gone forever!')
    else:
        print('They\'ll live...\n ...for now...')

# delete_hero(hero1)