##Joining heroes to ability numbers

# SELECT abilities.id AS ability_number, hero_id AS ability_num, heroes.name, heroes.id AS hero_id
# FROM abilities
# INNER JOIN heroes ON heroes.id=abilities.hero_id;

##expanding and joinging heroes to ability names
# SELECT heroes.name, heroes.id, abilities.hero_id, abilities.ability_type_id, ability_types.name, ability_types.id
# FROM heroes
# FULL OUTER JOIN abilities
# ON heroes.id = abilities.hero_id
# FULL OUTER JOIN ability_types
# ON abilities.ability_type_id = ability_types.id

##cleaning up the result table and formatting it nicely
# SELECT heroes.name AS Hero, ability_types.name AS Ability
# FROM heroes
# JOIN abilities
# ON heroes.id = abilities.hero_id
# JOIN ability_types
# ON abilities.ability_type_id = ability_types.id