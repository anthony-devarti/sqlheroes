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

# Aggregate multiple values into one
# SELECT  heroes.name AS heroes, STRING_AGG(ability_types.name, ', ') AS Ability
# FROM heroes
# JOIN abilities
# ON heroes.id = abilities.hero_id
# JOIN ability_types
# ON abilities.ability_type_id = ability_types.id
# GROUP BY heroes.name


# SELECT  heroes.name AS hero1, relationships.hero2_id, relationship_types.name AS status
# FROM heroes
# JOIN relationships
# ON heroes.id = relationships.hero1_id
# JOIN relationship_types
# ON relationship_types.id=relationships.relationship_type_id
# WHERE heroes.name = 'The Hummingbird' AND relationships.hero2_id = 1

# SELECT  heroes.name AS hero1, relationship_types.name AS status, h2.name AS hero2
# FROM heroes
# JOIN relationships
# ON heroes.id = relationships.hero1_id
# JOIN heroes h2
# ON h2.id = relationships.hero2_id
# JOIN relationship_types
# ON relationship_types.id=relationships.relationship_type_id

##here is where you can join this new table to another table
# JOIN (SELECT * FROM table_name) aliased_as *this is needed so you have a unique instance name
# ON primary key to foreign key