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
    WHERE hero_id={}
    LIMIT 1
    """.format(ability_id, hero_id)
    execute_query(add_ability)

# change_ability('Chill Woman', 'Frost Breath')

def add_ability(hero, new_ability):
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
    ability_id=execute_query(find_new_ability_id).fetchone()[0]
    add="""
    INSERT INTO abilities (hero_id, ability_type_id)
    VALUES ('{}', '{}')
    """.format(hero_id, ability_id)
    execute_query(add)

# add_ability('Chill Woman', 'Flying')


def define_relationship(hero_a, hero_b):
    find_ship="""
    SELECT  heroes.name AS hero1, relationship_types.name AS status, h2.name AS hero2
    FROM heroes
    JOIN relationships
    ON heroes.id = relationships.hero1_id
    JOIN heroes h2
    ON h2.id = relationships.hero2_id
    JOIN relationship_types
    ON relationship_types.id=relationships.relationship_type_id
    WHERE heroes.name='{}' AND h2.name='{}'
    """.format(hero_a, hero_b)
    status = execute_query(find_ship).fetchone()
    if status==None:
        print("""\
        ????????????J?????????????????J????????????????????????????????????????????????????????77?7?????7?77
        ???????????JY?????????????????JJ?????????????????????????????????????????????????????77???77?77?777?
        ?????????????????????JJ????????????????JJ?JJJJJJ??????????????????????????????????????????????7?7777
        7????????????????????J?????????????????JJJJJJJJJJJJJJJ???????????????????????????????????????????77?
        77777????????????????J?????????????????7!!!!777???????JJJJ??????????????????????????????????????????
        7777777?7???7?????????J???????JJ??JJ?!~~~~~~~~~!!!!7?????JJJ????????????????????????????????????????
        77777777777???????????????????J????!~~~~~~~~~~~~~~~~~!!7???JJJ??????????????????????????????????????
        77777??77???J?????????????????JJ?77!~~~~~~~~~~~~~~~~~~~~!????JJ?????????????????????????????????????
        777?????????J????????J????????JJ7!!77!~~~~~~~!!!!~~~~~~~~7????Y???????????????????????????????J?????
        77???????????????????JJ????????J7!J!7!~~~~!777!!7!~~~~~~~!????JJ??????????????????????????????J?????
        7????????????????????J????????J!~~!~77~~~~!!?7!7~~~~~~~~~7????JJ??????????????????????????????J?????
        ?????????????????????J??????J?!~~!~~!~~~~~!~7!^7~~~~~~~!7?????JJ????????????????????????????????????
        ????????????Y??????????????JJ~~~~77!!!!~~~~~~~!~~~~~~~~7??????YJ??????????????????????????????????77
        777?77??????J???????????????~~~~!~~!!!!~~~~~~~~~~~~~~~~!??7J??Y???????????????????????????????????7?
        777777777?????????????????J!~~~!J5J?7!!~~~~~~~~~~~~~~~~~7!!??YJ?????????????????????????????????????
        77777777??????????????????J~~~~75##BGPP7~~~~~~~~~~~~~~~!!7J?JJ??????????????????????????????????????
        77777?????????????????????J7~~~!777?YPPJ~~~~~~~~~~~~~~!7J?JJ????????????????????????????????????????
        777????????????????????????J7~~~~!~~~!7!~~~~~~~~~~~~~~~~?YJ?????????????????????????????????????????
        777????????????????????????JJ~~~~~~~~~~~~~~~~~~~~~~~~~~7JJ??????????????????????????????????????????
        7???????????????????????????JJ7!!!~~!!~~~~~~~~~~~~~~~~?J????????????????????????????????????????????
        7????????????????????????????JJ7!7777!!~~~~~~~~~~~~~~!PG5YYJ????????????????????????????????????????
        ???????????????????????????????5?~~~~~~~~~~~~~~~~~~7JGBPPPPPP555YYJJJ???????????????????????????????
        ????????????????????????????J55GBY7!!~~~~~~~~~!!7J5GGGPPPPPPPPPPPPPPPP5YJ???????????????????????????
        ??????????????????????????YPPPPPPGGGP5YYYYYYY5PGGGGPPPPPPPPPPPPPPPPPPPPPP5Y?????????J???????????????
        PPPPP555P555555555555555PPPPPPPPPPPPPPGGGGGGGPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP555555PP55555555555555
        BBBBBBBBBBBBBBBBBBBBBBBBBPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPGBBBGPGBBBBBBBBBBBBBBBB
        55555PPPPPPPPPPPPPPPPPPGPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPGGP55555555555P555555
        ??JJJJJJJJYYJYYJYYYYYYYPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP55YYYYYYYYYJJ?????
        ?Y5PPPPPPPPPPPPPPPPPP5PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPGGGGGGGGGP5YJ????
        Y5PPPPPPPPPPPPPPPPP555GPPPPPGPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPY7YPGPPPPPPPY????
        5PGPPPPPPPPPPPPPPPPPPPPPPPPPGPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPGGPPPPPPPPPPP5?~~~!YGGPPPPGJ????
        5GPPPPPPGGGGGGPPPPPPPGPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP5J!~~~~~~7YPPGGP?????
        GGPPPPPPPPPGGGPPPPPPPGPPPPPPPGPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPG5!~~~~~~~~~~75GGY?????
        GPPPPPPPPPPPPPPPPPPPPPPG5?YYY5PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPGPP5J!~~~~~~~~~~JGJ?????
        PPPPPPPPPPPPPPPPPPPGPPGG5~~~~~7PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPGPPGP57~~~~~~~~~?J?????
        
        That's my purse!  I don't know you!
        """)
    else:    
        if status[1] == 'Friend':
            print("""\
            
                                 .~!J?!::^^.                                                        
                                ^J5GGPPYYPG7                                                        
                               75J5YY555YYY!                                                        
                              ^JJJYJ!7?YPPPG!                                                       
                             :5YJGYJJ?JJ5P?7?                                                       
                             !P!JP5YYJ?7~75J^                                                       
                            .55?YYJ?5B#G5PB5Y^                                                  :~?J
~^::^~~!^:.                 :JJY??YJY&@@@@&#@@Y:                                          .:~!!JB@@@
~~~7JJ?????7:               :55PJ!?Y#@@@@@@@@@@B.                                ..:!7?5PP#&@@@@@@@@
75PP57^.~JJ?7!~             .BBBP?Y#@@@@@@&@@@@#.                             :!?GBB@B@@@@@@@@@@@@@@
GGY?!^:JY!^.~JY7^            Y@GPBB#@@@@@@@@@@@&^                          .:7G#@@@@@&@@@@@@@@@@@@@@
5J7!^:7Y^. .^77!!^.           7&B5YJG@&&@@@@@@@@J                       :^75BB@@@@@@@@@@@@@@@@@@@@@@
J?!^^:^~:::^7J??7!^:           :PG5JJP#&@@@@@@@@J                    .~YG#&#@@@@@@@@@@@@@@@@@@@@@@@@
Y?7~~~!~^.:!J^. .~. .           .P#5J?B@@@@@@@@#:                  ..?#&&&&@@@@@@@&@@@@@@@@@@@@@@@@@
YYYYJ?~^..~?~.:^7! .^^:          .PBJ?@@@@@@@@@G              .:!?7?J?YB@@@@@@@@@@@@@@@@@@@@@@@@@@@@
PPP5J~^^:~?????J7.  :7^           ^Y^.JP@@@@@@@G:.          ^?JY?7?!77??5&@@@@@@@@@@@@@@@@@@@@@@@@@@
P5Y?7!~:?P5YJ7!^. .^!~~. .         .~5#@@@@@@@@G7?!^:      !P5Y7^::^!7JYJY#@@@@@@@@@@@@@@@@@@@@@@@@@
Y?7777^?&P!^... .7?^::.     :     :P@@@@@@@@@@@Y777?Y?^   7BP5?!~7J5PPPGP5Y#@@@@@@@@@@@@@@@@@@@@@@@@
??77!!^GB~     ^P?:        .JG^  :P@@@@@@@@@@@&!~~77??Y7!JYGG55PPGGGBB##BBGG&@@@@@@@@@@@@@@@@@@@@@@@
5J7!~~~BY.   .?P!         ::P@&77&@@@@@@@@@@@@BJ?7?J!^?YPPP5#&&#####&#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
GY7!!~^5?.  ^PY.         .~P@@@@@@@&&&@@@@@@@&PBPYJY?!!J5J??JG#&@@@@@@@@&###@@@@@@@@@@@@@@@@@@@@@@@@
5??JY?7J7:^YB7    .     :J#@@@@@@&#&#&&@@@@@@BB#G55YJJJ?JJ5PYJYYYGBBGPGP55G&@@@@@@@@@@@@@@@@@@@@@@@@
555YJJJP#B&#7::.^~:   .?#@@@@@@@@&&&&@@@@@@@@B&##BGP55YJ5G#PYYPBBGGPJ7YPPB&@@@@#5J?&@@@@@@@@@@@@@@@@
PP5YJJ?P@@&577JYY!::!Y#@@@@@@@@@@@@&@@@@@@@@#GBBBG55PGGP5PG5J?JY5Y??JPB&@@@#PY!.   !@@@@@@@@@@@@@@@@
PP##GPB@@@#GG55Y??YG@@@@@@@@@@@@@@&&@@@@@@@&7G###BGGGPP5Y5YJ5B&&@@##&@@&GJ~.        P@@@@@@@@@@@@@@@
#&&&@@@@@@@#!7G&&@@@@@@@@@@@@@@@@&#&@@@@@@@5 ?&&&&##BGY??YPB@@@@@@@@#5!:            !@@@@@@@@@@@@@@@

They're friends!
            
            """)
        elif status[1] == 'Enemy':
            print("""\
                    :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~

            They don\'t like each other.
            """)
        else:
            print('I did not plan for this.')
    
define_relationship('Chill Woman', 'Mental Mary')