from connection import execute_query

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