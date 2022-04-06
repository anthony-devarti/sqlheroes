from connection import execute_query
from find import find_hero

##########################################
## Change specific aspects about heroes ##
##########################################

#########################
## Add Ability to hero ##
#########################

def change_ability(hero, new_ability):
    # find the id of the hero we are trying to change
    find_id="""
    SELECT id
    FROM heroes
    WHERE name='{}'
    """.format(hero)
    hero_id=execute_query(find_id).fetchone()[0]
    # print(hero_id)
    #then, find the ability id of the ability you want to add
    find_new_ability_id="""
    SELECT *
    FROM ability_types
    WHERE name='{}'
    """.format(new_ability)
    #something funky is going on here.  it doesn't want to spit out a number for this
    #it seems like my change has affected the abilities table and replaced frost breath with flying.
    #I simplified this chunk down to only finding the id of the incoming ability
    ability_id=execute_query(find_new_ability_id).fetchone()[0]
    # print(ability_id)
    #now, to add the ability id to the right cell to make it so the hero has it in their repertoire
    add_ability="""
    UPDATE abilities
    SET ability_type_id ={} 
    WHERE hero_id={};
    """.format(ability_id, hero_id)
    execute_query(add_ability)

change_ability('Chill Woman', 'Frost Breath')