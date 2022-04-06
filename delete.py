from connection import execute_query

#####################
## Deleting a Hero ##
#####################

def delete_hero():
    delete_a_hero="""
    DELETE FROM heroes
    WHERE name=banana
    """