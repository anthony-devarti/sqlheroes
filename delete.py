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
        print(
"""\
              .ed''' ""'$$$$be.
             -"           ^""**$$$e.
           ."                   '$$$c
          /                      "4$$b
         d  3                      $$$$
         $  *                   .$$$$$$
        .$  ^c           $$$$$e$$$$$$$$.
        d$L  4.         4$$$$$$$$$$$$$$b
        $$$$b ^ceeeee.  4$$ECL.F*$$$$$$$
        $$$$P d$$$$F $ $$$$$$$$$- $$$$$$
        3$$$F "$$$$b   $"$$$$$$$  $$$$*"
         $$P"  "$$b   .$ $$$$$...e$$
         *c    ..    $$ 3$$$$$$$$$$eF
            /ce""    $$$  $$$$$$$$$$*
             *$e.    *** d$$$$$"L$$
              $$$      4J$$$$$% $$$
             $"'$=e....$*$$**$cz$$"
             $  *=%4.$ L L$ P3$$$F
             $   "/*ebJLzb$e$$$$$b
              %..      4$$$$$$$$$$
               $$$e   z$$$$$$$$$$
                "*$c  "$$$$$$$P"
                  ""'*$$$$$$$"

        They're gone forever.
"""
        )
    else:
        print('They\'ll live...\n ...for now...')

# delete_hero(hero1)