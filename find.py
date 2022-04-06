from connection import execute_query

#####################################
##searching for a precise hero name##
#####################################
def find_hero(name):
    select_a_hero = """
    SELECT name, about_me FROM heroes
    WHERE name LIKE '%{}%'
    """.format(name)
    hero = execute_query(select_a_hero).fetchall()
    print(hero)

def find_hero_by_ability(ability):
    select="""
    SELECT heroes.name AS Hero, ability_types.name AS Ability
    FROM heroes
    JOIN abilities
    ON heroes.id = abilities.hero_id
    JOIN ability_types
    ON abilities.ability_type_id = ability_types.id
    WHERE ability_types.name= '{}'
    """.format(ability)
    hero=execute_query(select).fetchall()
    print(hero)