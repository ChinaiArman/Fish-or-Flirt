from art import *
import sys
import time

print(r"""\
                                                                                                                                                      
                                             ``                                                                                                       
                                             i:                                                                                                       
                                            ,*.                                                                                                       
                                           `;:                                                                                                        
                                           ,:,                                                                                                        
                                          `::`                                                             ``                                         
                                          ,,:`                                                             .+`                                        
                                         .,,,                                                              `i:                                        
                                        ,+,,,                                                               ::`                                       
                                       .ii,,.                                                               ::.                                       
                                      `;;:,:`                                                               ::.                                       
                                     `:;:.,:`                                                               ,:.`                                      
                                     ,;::,,,                                                                ,:..                                      
                                    `;:::;:,                                                                ,:..                                      
                                    ,;,,:;;.                                                                ,;,,`                                     
                                   `;:,:,:i,                                                                ,i,,`                                     
                                   ii,,,,:i:                                                                ,**:.                                     
                                  ,+;,,:::i.                                                                ,ii;,                                     
                                  i+;,,;i;i`                                                                ,;;::.                                    
                                 `*+;,:***i`                                                                :i;:,;`                                   
                                 ,++;,;+++;                                                                `i*i:,:,                                   
                                 :++i;*+++:                                                                `**i:,.:`                                  
                                 ;+#**++#+,                                                                .*ii:,.,,                                  
                                 i+#+*++##.                 .,                                             .*ii:,..:                                  
                                 i#++++##+:..              ;@W*                                            ,***:,.,;`                                 
                                 ;##+++####z*             `WW#x`                :n+                        :+#+:,,;i.                                 
                                 :###++##*#zni            ,@#WW.               `xMW:                       ;##+;,:i*,                                 
                                 .###++#+i##zn.           .@#WW+;;;ii:,`  ``..`+WWW*                       iz#+;:;**,                                 
                                  i###++**#zzn*         `.:W#WWWn#nxMMx#i+znxxnM###*`                    .i+z#+i;***,                                 
                                  .####+*+##znn`     `:*zxM@@WWW@WWMMMMxxMWWWWMW@#@#i:,`                `#xzz#+*i*+*.                                 
                                   i#zz#+zz#znn:   ,#MWWM@@##@@W@@MxnnxMMMMMW@@@@#@Wx#*i,``             +xx#z#++*+**`                                 
                                   i+###zz##+#xi `+MWWWWMW@@###@@MnnnnznnnxxW@@W@@@@WMx#**i;:.         ,xxxzz##++++i                                  
                                   ,####z#i:;i#; :MWWWWWWMWW@##@@MxnxxxxnnnxM@#@@MM@@MxMxxxnnz*.       #xMxzzz#++++,                                  
                                    :####i:::;*zi*MWWW@WWWWWW@@WWWWWWWWWMxxWWMWW@xxMMMnnnznxMMMni`    .MxMxnn#####*`                                  
                                 ``,.inn+;;;;;*x*#MMWW@@WWWWW@@WWWWW@W@@WW@@WWWWWWWMMxnxnnnxMWWWWz.   :MxxMxnz####:                                   
                             `,i+++xnnnz#;i;:i#ninMxxMMMMxxxM@WMnWWWWMMW@@@@WW@@WMMxxxnzznnxMWWWWWM:  :znxxxnzz##*,                                   
                           `:+nxxxMMMMMz#i;;ii+nixMxxxxMMMxxMMxnxWW@@@W@@@@WMMx@Mxxnnn###zxMMMMWWWWx,#*++znnnzz#**`                                   
                          .*nxxxxMMMMMM#++**#+#x+xMxxxxxxxxxxnnMMxxxW@MWWMMWMxxxMxxn#++++#znxMMWWW@M#x***+znnz#++.                                    
                         .+xxxxxxMMMMMMx+#zzzznnzxMMnxxxxxxxxnxMxxxxnMWMxxMxxMxxxnnn###zzzznnxxMWW@@nn+**+++nnz#.                                     
                        .#xxxxxn;zxMMMMMnzzzzzznnxMMxxxxxxxxxxMMxMxxxnMxxxxxxnxxxxxxxnnnnnnnnxxxMW@@nn+*i*iizz*`                                      
                       `;nxxxxn*.,zMMMMMx#zzzzzxxMWMxxxxxxxxxMMMxMxxxnMxxxMMxxxxxxxnxnnnnnnnxxxxxMWWzn#*;;i*z,                                        
                      .iznnnnnz. `:xMMMMM#zznnnnxMWWxxxxxxxxMMMMMMxxxzMxMMMMMxxxxxxxnnnnnnnxxxxxxxMxzzz+*;;+#.       ``.`                             
                     .+xnxnnnn;` `:nMMMMMz#znnnnxMWWMxxxnxxxxMMMMMxxzxMnMMMxxxxnxxxxnnnnnxxxxxxxxMMz##zzz#++:      .i#zz#i:`                          
                    ,#nxxxnnn*.  `;nxMMMMx##nnnnnMWWMxxxxnnxnxxxMxxxzxMznxxxxxxnxxxnnnnnnnxxxxxxxMx##+##++#;     `;znnnnnzzzi`                        
                   ,#nnnnnnn#,`  .#nnMMMMMz#znnnnxWWMMxnnnnnnnnxxxxz#zxnznxxxxnnnxnnnnnnnnxxxxxxMM#######++`    .+nznnzzzz#zz*`                       
                  ,#nnnnnnnni`  `:zxnxMMMMM##nnnzzMWWMxxnnnxnnnnnzzn+*nzz#znzzznnnnnnnznnnxxxxxxMn*i#####+;`.,.:znnnnnnzzz#z#*i`                      
                 .+nnnnnnnzi.`  `;nxxxMMMMMx#znnzznWWMMxxnnxnnnz#znxnnMxzz#+zznnnnzzzznnxxxxxxxxM#iii*+#+#*znnznnnznnzzzz#+z#*i;`                     
                `*nnnnzzzzi.`   `inxxxxMMMMMn#znzzzMWWMxxnznnnnnnz#zxxMxz##znnnznnzzznnxxxxxxxxMx*;i*ii++nxxxnnnnnnnnzzz+*.*z+ii,                     
                ,znnzzzz+;.`    `inxxxznMMMMMn##+###zMWMxnzznnnnnz#+nxxx##znnnznznzzznnxxxxxxMMM#*iiiii*nxxxnnnnnnzzzzz#zn:*z#*ii`                    
               `;nnzzzz*,.`   ```innnn+:nMMMMMz#+##z**xWWMxnnnnnzz#++nnn++znnzzzzn##znnnxxxxxMMn+*+*iiizxxxnnnnnnzzzzz#zxxnnz##i+;                    
               `inzzz+;..``.:;;;;inxnn;`;xMMMMMnz+##+i*#nMMMMnzzz#++#nnn#++zzzzz#zz#zznnxxMMMMn#*##+**zxxxnnnnnzzzzzz##xxxxnz##*++;`                  
               `*zz+i,..``:#nxxxxxxxxz;..ixMMMMMx++++i;;i*+zxnzzz#+#++#z##+#zzzzz#znxxxxxxMMxz##++**+zxxxnnnnnzzzzzz##xxxnnzz#+*++##i.                
               .*++:.....,*nnxxxxxxxxxxz+*#xMMMMWn##**iii;i+#zz####++**+++#+#z###+#nnnnxnnnnz#*++++#nxxxnnnnnzzzzzzzzxxxnn#:;#+**+#zz#,               
               .*+*,..:*#znxnxxxxxxxxxxxxMxMMMMMMWWxz+*i;i**;+nnzz##+*####+++++#+#+z+++##+*###**++#nxxxxnnnzzzzzz#zzznxnzz#;`#z##+#z#zz+,             
               .*+*::+nnzzznzznxxxxxxxxxxxxxxMMMMMMWxx#**+#*;+nzz##++##**+#++##+##++*+***ii*++**zzxxxxxxnnzzz####znzzznzzzz*`:z####zzzzzzi.           
              `.**i*nnn#zz#+zznnnnnnnxnnxxxxxxMMMWMMMx####*;*#nnzz###z#+*i+++++###*+i#+*iii*++*+nxxxxxxnz####znnxxxznz##zzz; `*z#####znzzz+,          
              `,*++znn##z+++###zzznzzznnnnxxxxxMMMxxxxx#+ii+#zzzz##+###++**+++####*+i*#+ii+#znnxxxxxxxzznnxxxxxxxxxnzn#.#z#.  .+z#####zzzzzz;`        
              `,+nzzz+*#*;i**##zz##++++##zznnnnxxnnznxxxxn+++++###+++####+*+**++++*i+**++++nxxnxnnnnnxxxxxxxxxxxxxnnznx*+#;` ``.+#####zzzzzz#i`       
             `.,+zzz#i*#:::::i#zzzzz#+***+++##zxnz###zzzn#****++++++####+****ii*****i+*ii*#nnnnnznnnxxxxxxxxxxxxnnnnnnn#+;` ````,+######zzzzz#;`      
             `.:+zz#++#;,,,,,,,:i#zzzzz##+##z#nn##i;;*#zz+**+++++++#+++#z#*i***iiiiiii+#znnzzzzzznnnxxxxxxxxxxxnnnzznnn+;` ```` `,#######zzz###.      
            `.,#znnz#+*,,,,,..,,,,:;*######++*i;;::::;i*++**+++++**+*++++**i;;i+++****iiinnzzzz#znnxxxxxxxxxxnnnnznnnzz:````` ````,+####+#####z;      
            `.+nnnnz#+:.............,,,::;:,,,,,,,,::::::::;;;;;iiiiii******ii;i+++++++***###zzz#znxxxxxnnnnnnnnnnnzzz+,.``````````.+#+++,;+#z#i`     
           ``izznznz#*....````.`````.....,........,,,,,,,,,,,,,,,,,,:::;;iiiiiiii*ii*****+#zznnnz+*##zzzzzznnnnnn#z#zz;...``````````,+##+,.,:*+*,     
           `:znzzzzz+,...```````````````.........................,,,,,,,,,,,,,,,,,:::::::::;;;;;:::,,:;*+++*i;inn####+,...``````````.,*#*,...:*i:`    
           .+zzzz###,.```````````````````````````````.............................,,,,,,,,,,,,,,,,,,..,,,,,,,:znnz#++:,...``````````..i*i,....ii;`    
           :zzzzz#+,``````````````````````````````````````````````````````.................................,,*nnnzz#*,...```````````..**i,....;**`    
          `+zzzz#+:```````````                  ```````````````````````````````````..........................#nnnzz+,...````````````..**i,,...:#+.    
          .#zzz#+:.``````                                         `````````````````````````````````````````.,nznnzz;.````````````````.**:....,:##.    
         `.+nz#+:..``````                                                ```````````````````````````````````*nzzzzz,`````````````````:**....`.,;;`    
          `+zz#;.`````                                                              `   ```````````````````.#zzzzz+``  ````` ````````;+i.````````     
          `i#+*i:````                                                                             `````````:zzzzzz;             `````+#,````          
           `;*iii:.                                                                                ````````*zzzz#+`              ```.#z.``            
           `.:iii;;.`                                                                               ``````.#zzz##,                ``:#;`              
            `.,:ii;;,`                                                                              ``````,zzz##*`                  ,:`               
             `..,;i*i;.                                                                              `````:###+*.                                     
              ``..,:;iii.                                                                            `````;+##*,                                      
                 ````..,:.                                                                           ```.:+*+i:`                                      
                                                                                                   `````;**ii.`                                       
                                                                                                   `` `;iiii.`                                        
                                                                                                    ``;ii*;``                                         
                                                                                                    .;*ii,`                                           
                                                                                                  `.+**i.`                                            
                                                                                                 `:*++,`                                              
                                                                                               `:*+*:.                                                
                                                                                              `ii:,`                                                  
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      

""")
tprint("True Final Boss")

get_name = "Hello. We all know why you're here. \n" \
           "You wish to fish. \n" \
           "You want to warp a carp, \n" \
           "getta a betta, net a flounder ten-pounder, snag a daring red haring– \n" \
           "OK. \n" \
           "I'll stop embarrassing you. \n" \
           "Here. \n" \
           "Take a fishing rod, \n" \
           "and go wild kid.\nBut first. What is your name?\t\t"

choose_class = "What class do you want be in? Do you want to be a doctor, neurosurgeon, lawyer, fisherman, dentist, psychologist, magician, Prime Minister of Canada, Premier of Australia, astronaut, or rocket scientist?"

after_class_input = "Well, I'm a computer, so I can't hear you. Maybe hit your keyboard harder. Well, you get no autonomy anyways, so you're a fishman now. Congrats."

story_1 = "Once upon a time, a long long time ago, in a small little village, a fisherman was born.\nThat's you!\n" \
          "You came out of the womb with a fishing rod in your precious little hands. Your mother had to get a C-section just to get it out!" \
          " Poor mama-fisherman.\nOn that fateful day, a prophecy was discovered. " \
          "You alone are destined to defeat the monster of the deep.\nYour parents have trained you all of life for this." \
          "IT'S TIME TO FISH!"

random_encounter_crab = [
    "You were thoroughly enjoying the feeling of sand beneath your toes, until a crab decides your toes were looking at it the wrong way. The crab challenges you to a duel.",
    "You see a crab. You are filled with hatred. The crab is also filled with hatred. You are hatred itself. The crab one-ups you and decides that it is despisal. You and the crab lock eyes and the first one to blink loses.",
    "Crab. What more should I say? Crab.",
    "You step forward, the crab steps forward. You step left, and it, left. You try to eurostep that fool, but you are no match for the agility of the magnificent crab, and gets your ankles broken. You take immense damage to your pride (not a real stat).",
    "You see a crab. The crab sees you. It's too late to run, the only option for you now is to stand your ground, and FIGHT.",
    "Legend says that by defeating a crab, you can gain a crab's power. Do you desire to absorb the might of this crab?"
]

random_encounter_fisherman = [
    "You see another person, wearing a straw hat, holding a rod and a bucket in each hand. You both startle and point and each other in excitement. Neither of you say a word, but the intent is clear. FISH.",
    "The only living being a fisherman hates more than a crab, is another fisherman. You see another fisherman.",
    "You see a person, with a fish. What a nice fish, you think. They see a person with a fish. What a nice fish, they think.",
    "You see a person with a rod, and a bucket. There is no fish in their bucket. You are filled with overwhelming pity for them. You are filled with overwhelming self-superiority over them. This is the start of your villain arc."
]

random_encounter_fish = [
    "FSIH FISH FISHS FSIHDSF FSIFH FSIHF FISHF FISHF FISH. There's a fish.",
    "It's your lucky day! You've found a strange looking being with 21 limbs, "
    "oil and tar dripping from its skin and sliding onto the sea. It looks at you with beady, soulless eyes, "
    "and without knowing the reason, you are overcome with the desire to look away. But you must keep your eyes on it, "
    "after all, IT'S SUCH A COOL FISH!!",
    "You found a fish. Good job buddy.",
    "It looks like a fish, it smells like a fish, it sounds like a fish, it feels like a fish, it tastes like a fish. Gasp! I think you've found a fish!"
]

random_encounter_mermaid = [
    "Me-me-mermaid... Pretty.",
    "You see a person in the water! They may be drowning! "
    "You try to rush over towards them before you are met with many many many many many many many many many many many "
    "many many many many many many many many many many many many many many many many many many many many many many many "
    "many many teeth. Whew! It was only a mermaid. Mermaids can't drown silly. Don't worry about it.",
    "There's a mermaid. It's a mermaid.",
    "'Wow!' You think, 'What a big fish!' A mermaid hits you for calling them derogatory terms."
]

no_encounter_land = [
    "I don't like sand. ( ｡ •̀ ᴖ •́ ｡) It's coarse and rough and irritating and it gets everywhere.",
    "WOW! CONGRATS! YOU FOUND\nseaweed... You found wet soggy seaweed... congrats",
    "What kind of fisherman stays landlocked! Go to the sea, you'll find nothing on this barren land.",
    "The 'racle hast possess'd me, I f'resee a prophecy...\nGasp! the young gudgeon'rman finds nothing h're!"
]

no_encounter_sea = [
    "You set forward on your little boat in search of bigger fish to fry, but to your demise, you catch not even a single fly",
    "You thought you saw a fish in this direction. Turns out you thought wrong.",
    "You throw out your fishing rod. It returns you a chewed through boot with a hole in the toe.",
    "You came, you saw, you left empty handed. Ain't no fish here pal!"
]

encounter_boat = "You see an old, but sturdy sailboat. It's well loved, with the signs of time decorating its sides. " \
                 "However, the paint was recently redone a brilliant white, and you could see that the sails have been changed. " \
                 "Beside the boat, an old fisherman sits, as if waiting for a friend.\nThe fisherman beckons you towards them, and gestures at their boat. " \
                 "Behemoth, it reads. A worthy aid to help you in your journey against the monsters of the sea. " \
                 "The old fisherman tips their straw hat, a twinkle shinning in their eyes, and walks away, humming a happy little tune."

acquired_boat = "You touch the boat, and you feel an energy pulse through you. You've gotten stronger, my young friend. " \
                "The hope of all those who've come before you empowers you on your journey."

encounter_pirate = "You see a group of pirates, each with a two shovels in hand.\n\"Why are they all carrying two shovels?\" " \
                   "You ask yourself.\"WOW CAPT'N! YOU'RE ABSOLUTELY BRILLIANT. " \
                   "DIGGING WITH TWO SHOVELS MAKES US SO MUCH MORE IF-FEET-SCENT THAN ONLY DIGGING WITH ONE!\""

pirate_defeated = ""

encounter_leviathan = "Abandon hope all ye who enters here.\n" \
                      "For here lies the lair of Leviathan, ruler of the deep and vicious seas.\n" \
                      "If you unlucky sailors find yourselves in its maw, despair!\n" \
                      "<You have reached the final boss, the Leviathan! Are your stats high enough to fish or " \
                      "capture the heart of this fearsome foe? Take up your rod and find out!>"

leviathan_defeated = ""

invalid_move_land = [
    "You can't step here!",
    "There's nothing for you here.",
    "The crabs look at you with disgust. What are you, stupid? You can't go there! Go somewhere else!",
    "Error 102. Test subject is attempting to breach the wall. Alert. Alert. Alert. Alert. Alert. Al-\n"
    "The crabs look at you with disgust. What are you, stupid? You can't go there! Go somewhere else!",
    "WOW! You found a fish!... Is that what you thought would happen? You think you're so clever huh. You fool. There's nothing here!!"
]

invalid_move_water = [
    "Careful there buddy! If you go over the edge you'll fall off this world!",
    "You look into the void.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nThe void looks back.\nYou should turn back",
    "Did you know that the world is actually a hemisphere laid onto of four elephants standing onto of a giant turtle? "
    "You should be careful going that way, you might fall off the earth and onto a turtle.",
    "The water current gently brings you back on your right path. There's a monster to slay, you know! You don't want to slay it? Well, I guess there's a monster to fish!"
]

flirt_dialogue = [
    "I wish you were a fish so I could reel you in.",
    "You’re the only fish in the sea for me.",
    "You know I don’t go fishing often, But you’re quite the catch!",
    "You’re like an award-winning fish",
    "A shark just ate my girlfriend during our fishing trip. Will you be my new one?",
    "Are you Swedish? 'Cause you the sweetest fish I sea."
]

flirt_harder_dialogue = [
    "Do you believe in love at first sight, or should I float by again?",
    "Hey baby, you wanna cast a line with me?",
    "I always knew the best catch of my life would be on this ocean.",
    "I can feel a lot of tension between us.",
    "If you were a fish, you’d be an Angelfish.",
    "You just reeled me in with your beauty.",
    "You’ve got me hook, line, and sinker."
]

flirt_success = ""

flirt_fail = ""

level_up = ""

tprint("ERROR 102", "dirty")

# prints a character at a time
for statement in invalid_move_water:
    for char in statement:
        print(char, end="")
        sys.stdout.flush()
        time.sleep(0.05)
    print("")
