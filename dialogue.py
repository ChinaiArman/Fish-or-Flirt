"""
Arman Chinai | A01317650
Lex Wong | A01322278

A python module containing the dialogue for Fish or Flirt.
"""

import sys
import time
import ascii_art as asc
from time import sleep


def slow_print(dialogue: str) -> None:
    """
    Prints characters slowly, in batches in the console.

    :param dialogue: A string containing any characters.
    :precondition: dialogue must be a string character.
    :postcondition: dialogue will be printed into the console slowly, in batches of characters.
    :return: None.
    """
    for char in dialogue:
        print(char, end="")
        sys.stdout.flush()
        time.sleep(0.04)
    print("")


def loading(times: int) -> None:
    """
    Creates a buffer in the console a variable number of times.

    :param times: An integer greater than or equal to 0,
    :precondition: times must be an integer greater than or equal to 0.
    :postcondition: Will print in the console the string "...", then sleep for a second a variable number of times.
    :return: None,
    """
    for i in range(times):
        print("...\n\n")
        sleep(1)


# tprint("True Final Boss")

welcome_message = "Welcome to Fish or Flirt, by Arman Chinai and Lex Wong. In this game, you can fish\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nor flirt. Let's start!"

choose_class = "What class do you want be in? Do you want to be a:"

class_options = ["doctor", "neurosurgeon", "lawyer", "fisherman", "dentist", "psychologist", "magician", "Prime Minister of Canada", "Premier of Australia", "astronaut", "rocket scientist"]

after_class_input = "Well, I'm a computer, so I can't hear you. Maybe hit your keyboard harder next time. Well, you get no autonomy anyways, so you're a fisherman now. Congrats.\n"

story_1 = "Let me set the scene. Once upon a time, a long long time ago, in a small little village, a fisherman was born.\nThat's you!\n" \
          "You came out of the womb with a fishing rod in your precious little hands. Your mother had to get a C-section just to get it out!" \
          " Poor mama-fisherman.\nOn that fateful day, a prophecy was discovered. " \
          "You alone are destined to defeat the monster of the deep.\nYour parents have trained you all of life for this."

get_name = "So now, we all know why you're here.\n" \
           "You wish to fish.\n" \
           "You want to warp a carp,\n" \
           "getta a betta, net a flounder ten-pounder, snag a daring red haring–\n" \
           "OK.\n" \
           "I'll stop embarrassing you.\n" \
           "Here.\n" \
           "Take this fishing rod,\n" \
           "and go wild kid.\nBut first. What is your name?\n"

random_encounter_crab = [
    "You were thoroughly enjoying the feeling of sand beneath your toes, until a crab decides your toes were looking at it the wrong way. The crab challenges you to a duel.",
    "You see a crab.\nYou are filled with hatred.\nThe crab is also filled with hatred.\nYou are hatred itself.\nThe crab one-ups you and decides that it is despisal.\nYou and the crab lock eyes and the first one to blink loses.",
    "Crab. What more should I say? Crab.",
    "You step forward, the crab steps forward.\nYou step left, and it, left.\nYou try to eurostep that fool, but you are no match for the agility of the magnificent crab, and gets your ankles broken.\nYou take immense damage to your pride (not a real stat).",
    "You see a crab. The crab sees you. It's too late to run, the only option for you now is to stand your ground,\nand FIGHT.",
    "Legend says that by defeating a crab, you can gain a crab's power. Do you desire to absorb the might of this crab?"
]

random_encounter_fisherman = [
    "You see another person, wearing a straw hat, holding a rod and a bucket in each hand.\nYou both startle and point and each other in excitement.\nNeither of you say a word, but the intent is clear.\nFISH.",
    "The only living being a fisherman hates more than a crab, is another fisherman. You see another fisherman.",
    "You see a person, with a fish. What a nice fish, you think. They see a person with a fish. What a nice fish, they think.",
    "You see a person with a rod, and a bucket.\nThere is no fish in their bucket.\nYou are filled with overwhelming pity for them.\nYou are filled with overwhelming self-superiority over them.\nThis is the start of your villain arc."
]

random_encounter_mermaid = [
    "Me-me-mermaid... Pretty.",
    "You see a person in the water! They may be drowning!\n"
    "You try to rush over towards them before you are met with many many many many many many many many many many many\n"
    "many many many many many many many many many many many many many many many many many many many many many many many\n"
    "many many teeth.\nWhew! It was only a mermaid.\nMermaids can't drown silly. Don't worry about it.",
    "There's a mermaid. It's a mermaid.",
    "\"Wow!\" You think, \"What a big fish!\" A mermaid hits you for calling them derogatory terms."
]

random_encounter_whale = [
    "\"Wow!\" You think, \"What a big fish!\" The whale looks at you blankly.",
    "The whale tries to swallow you into their stomach. You call your mom to ask for consent. Your mom says \"No.\"\n"
    "The whale legally cannot swallow yoo without your mother's consent.",
    "It's a bird! It's a plane! No! It's a flying whale- wait no you were just looking into the water. It's a regular whale."
]

no_encounter_land = [
    "I don't like sand. ( ｡ •̀ ᴖ •́ ｡) It's coarse and rough and irritating and it gets everywhere.",
    "What kind of fisherman stays landlocked! Go to the sea, you'll find nothing on this barren land.",
    "The 'racle hast possess'd me, I f'resee a prophecy...\nGasp! the young gudgeon'rman finds nothing h're!"
]

no_encounter_sea = [
    "You set forward on your little boat in search of bigger fish to fry, but to your demise, you catch not even a single fly",
    "You thought you saw a fish in this direction. Turns out you thought wrong.",
    "You throw out your fishing rod. It returns you a chewed through boot with a hole in the toe.",
    "You came, you saw, you left empty handed. Ain't no fish here pal!"
]

encounter_boat = "You see an old, but sturdy sailboat. It's well loved, with the signs of time decorating its sides.\n" \
                 "However, the paint was recently redone a brilliant white, and you could see that the sails have been changed.\n" \
                 "Beside the boat, an old fisherman sits, as if waiting for a friend.\nThe fisherman beckons you towards them, and gestures at their boat.\n" \
                 "Behemoth, it reads. A worthy aid to help you in your journey against the monsters of the sea.\n" \
                 "The old fisherman tips their straw hat, a twinkle shinning in their eyes, and walks away, humming a happy little tune."

acquired_boat = "You touch the boat, and you feel an energy pulse through you. You've gotten stronger, my young friend. " \
                "The hope of all those who've come before you empowers you on your journey."

acquired_trident = "You reel in your catch.\nIt's so much heavier than any fish you've caught before, and a mix of anxiety and excitement races through you.\n" \
                   "Will the string hold? You're really not looking forward to changing the fishing wire.\n" \
                   "Your old man said it was his favourite past time, but to you, any time spent not fishing is a waste of time.\n...\n" \
                   "This lack of struggle scares you. What kind of fish is this???\n" \
                   "Your \"fish\" starts rising out of the water.\n" \
                   "Hmm, it has a shinny tip... A swordfish? But you've never seen a swordfish with three prongs on it––" \
                   "CONGRATULATIONS! You have reeled in the weapons of Pelagaeus, Aegaeon, the One Who Dashes Against,\n" \
                   "He who's Full of Seaweed, the Dark-Haired One, The One Who Secures Safe Voyage, Watcher, The Flooder,\n" \
                   "Earth-Shaker, Holder of the Earth, He Who Must Not Be Named--I'm joking.\n" \
                   "You've reeled in Poseidon's Trident! What does it do? Who knows ;)\n\n" \
                   "[LEGENDARY] POSEIDON'S TRIDENT has been added to your inventory."

encounter_island = "There's a small island in the midst of the angry waves. There's a forest of palm trees on that island.\n" \
                   "Through them, you think you can glimpse movement.\n" \
                   "You're not sure if it's friend or foe, but there's only one (or two) real choices anyways."

encounter_pirate = "You see a group of pirates, each with two shovels in hand.\n\"Why are they all carrying two shovels?\" " \
                   "You ask yourself.\n\"WOW CAPT'N! YOU'RE ABSOLUTELY BILLY-ANT. " \
                   "DIGGING WITH TWO SHOVELS MAKES US SO MUCH MORE IF-FEET-SEE-ENT THAN ONLY DIGGING WITH ONE!\"\n" \
                   "Oh, what, interesting(?) pirates. " \
                   "You see a big map lying behind them, with \"LOCATION OF LEVIANTHAN\" scrawled in the most horrendous writing you've seen.\n" \
                   "Actually, it's a wonder you were able to read it in the first place. To get to it, you must get through all the shovel carrying pirates. " \
                   "Good luc-\nOh. One of the pirates accidentally smacked all the other pirates in the head.\n...\nThat sure was a very very very loud noise." \
                   "All of them are now unconscious. I'm not even sure if all of them are breathing.\n" \
                   "Well then, 1 pirate isn't that hard to deal with. I'll feel bad for the poor pirate if I wished you luck.\nGo on then."

pirate_defeated = "You've successfully wooed the pirate. They swoon romantically and fall into your inventory.\nYou've acquired the location of the terror of the sea, the Leviathan."

encounter_leviathan = "Abandon hope all ye who enters here.\n" \
                      "For here lies the lair of Leviathan, ruler of the deep and vicious seas.\n" \
                      "If you unlucky sailors find yourselves in its maw, despair!\n" \
                      "<You have reached the final boss, the Leviathan! Are your stats high enough to fish AND " \
                      "capture the heart of this fearsome foe? Take up your rod and find out!>"

leviathan_fish_and_flirt = "You shout into the sea! Your voice travels to the Leviathan's ears, wooing with sweet honeyed words.\n" \
                           "If the Leviathan accepts your declaration of romance, maybe it will allow itself to be fished easily."

leviathan_defeated_fish = "With your strong rod and amazing fishing skills, you've fished the Leviathan from the sea!\n" \
                          "I can't believe you even have enough bicep strength to do that! Amazing!\n" \
                          "You've fulfilled the prophecy, and your parents will finally love you, I mean what."

leviathan_defeated = "You should be jailed! Your irresistible charm and dashing good looks have stolen the Leviathan's heart.\n" \
                           "When talking with the Leviathan, you discovered that the only reason it was terrorizing the seas was because it had a terrible stomach ache.\n" \
                           "After giving the Leviathan drugs, I MEAN, asprin, it felt a lot better, and no longer terrorizes the sea.\n" \
                           "You and the Leviathan, and all the other animals and people you've wooed along the way now live happily ever after.\n\n" \
                           "[LEGENDARY] Leviathan has been added to your inventory\n" \
                           "[LEGENDARY] An Unspoken Level of Rod-ly-ness has been added to your inventory"

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

invalid_move_island = [
    "I don't know how you got here. You can't even move incorrectly on this island. How did you manage to make an invalid move?",
    "Let's review our NUMBERS. 1 for NORTH. 2 for SOUTH. 3 for EAST. 4 for SOUTH. Try again.",
    "How did you get here again? We should change your name into little Alice Liddell. Stop following the White Rabbit and go."
]

invalid_fish = [
    "There are no fish in the sand. Cease your foolish antics.",
    "There are plenty of fish in the sea. This ain't no sea.",
    "I'll be surprised if you can reel in any fish here, seeing as there are no fish here.",
    "Even Jesus needed two fish to create more, how are you gonna get fish without any in the first place?"
]

start_fish = [
    "You throw your rod into the sea. The bobber creates small ripples in the water, growing larger as they expand outwards. You feel one with the sea.",
    "The ocean breeze gently blows across your face like soft and loving caresses. You think you'll find good fish today.",
    "In the distance, you hear the call of seagulls. They too, are accompanying you in your fishing.",
    "You throw your rod into the sea. The ocean's crystalline surface breaks for a moment, before returning to its original calm.",
    "You hum a soft tune under your breath as you wait for a fish to take the bait. You're not sure where it came from, but it comforts your soul."
]

fishing_success = [
    "FSIH FISH FISHS FSIHDSF FSIFH FSIHF FISHF FISHF FISH. There's a fish.",
    "It's your lucky day! You've found a strange looking being with 21 limbs,\n"
    "oil and tar dripping from its skin and sliding onto the sea. It looks at you with beady, soulless eyes,\n"
    "and without knowing the reason, you are overcome with the desire to look away. But you must keep your eyes on it,\n"
    "after all, IT'S SUCH A COOL FISH!!",
    "You found a fish. Good job buddy.",
    "It looks like a fish, it smells like a fish, it sounds like a fish, it feels like a fish, it tastes like a fish.\nGasp!\nI think you've found a fish!"
]

fishing_game_fail = [
    "Your wire broke. Unlucky.",
    "WOW! I never thought the Chosen One can suck so much at fishing!",
    "YOU CAUUUUUUUUGHT, oh wow how rare, NOTHING!!!"
]

fish_whale_success = "You caught a whale! Cue Pokemon sounds."

fish_mermaid_success = "You've caught a mermaid! Or has the mermaid caught you?"

fish_whale_fail = "What are you thinking? Trying to fish a whale with such a flimsy fishing rod."

fish_mermaid_fail = "The mermaid quickly ties a heavy rock to the end of your line. You nearly fall into the water."

fishing_fail = "You failed to catch a fish. Perhaps you should try again?"

start_flirt = "You decided that a good fisherman can both fish AND woo their opponents into being fished."

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

seduce_pirate = [
    "A good captain goes down with his ship, wanna go down with me?",
    "Arrrrrrrrrrrrr you free this Saturday?",
    "You may be burying treasure, but you're the only treasure I see.",
    "I can sail through any storm if it's with you!",
    "I have the latest copy of Windows 11 with cracked product activation. ;)",
    "I've sailed the seven seas, and you're the sleekest schooner I've ever sighted."
]

flee_from_pirate = [
    "No fleeing, only flirting",
    "Fish or Flirt's Art of War-If equally matched, you can offer flirts;\n"
    "if slightly inferior in numbers, you should've just avoided the enemy in the first place;\n"
    "if quite unequal in every way, we can flee from him.\n"
    "You are equally matched. GO WOE THE POOR THING.",
    "You try to run away, only to trip on one of the pirate's unconscious, or dead, friends.\n"
    "Fisher-mama taught you better than to kick people in their sleep!"
]

invalid_flirt = "That's not flirting kid. You suck."

flirt_success_crab = "Your amazing flirting skills have surpassed the fishermen's and crabs' hatred of each other.\nIt's like a modern day Romeo and Juliet!"

flirt_fail_crab = "The crab looks at you with even more disgust. To it, you are beneath the sand it crawls on."

flirt_success_fisherman = "You both gave deeply into each other's eyes, and exchange a prized fish."

flirt_fail_fisherman = "The fisherman humphs and turns their back on you. Maybe if you gave them a bigger fish they'll accept you."

flirt_success_mermaid = "The mermaid tells you they are willing to exchange voice to gain legs to live with you.\n" \
                        "You tell them it's alright, and that legs don't really live up to the hype."

flirt_fail_mermaid = "The mermaid bears their many many teeth at you. They weren't amused at your fish based flirts."

flirt_success_whale = "The whale is enamored by your sweet words."

flirt_fail_whale = "The whale does not care for you puny human flirtations."

flirt_success_pirate = "\"AYE! If you be my new CAPT'N I'll be your first mate!\"\nTranslation: Your flirt was a success."

flirt_fail_pirate = "The pirate waves their shovel around. It almost hits you in the head. I don't think they appreciated your pick-up lines."

flirt_fail_leviathan = "The Leviathan thrashes their many arms. You dodged skillfully. If only your flirting skills were just as skillful."

level_up = "You levelled up! Your rod is now stronger."

congratulations_pt1 = "CONGRATULATIONS! You have completed..."

congratulations_pt2 = "Let's take a look at how you did!"

end_of_game_shenanigans = "Thank you for playing our game! We hope you had lots of fun fishing and flirting with everyone.\n" \
                          "Come back again soon!"

tallying_message = "That's a big haul, let's see the totals"

final_point_total_display = "Wow! That's a lot of points, maybe your parents will finally love you- I mean what"

final_legendary_item_display = "But first, let's remember the legendary items you unlocked throughout your journey!"

transition_to_point_total = "And now, the point total!"

# tprint("ERROR 102", "dirty")
    

BOAT_DIALOGUE = {
    "entity": "Sail Boat",
    "ascii_encounter": asc.boat,
    "encounter": encounter_boat,
    "acquisition": acquired_boat
}

PIRATE_DIALOGUE = {
    "entity": "Pirate",
    "encounter": encounter_pirate,
    "start_flirt": start_flirt,
    "seduction": seduce_pirate,
    "success": flirt_success_pirate,
    "blush": asc.pirate_seduce_success,
    "fail": flirt_fail_pirate,
    "skulls": asc.pirate_seduce_fail,
    "run_away": asc.flee,
    "invalid": invalid_flirt,
    "flee": flee_from_pirate
}

LEVIATHAN_DIALOGUE = {
    "entity": "Leviathan",
    "reward": "An Unspoken Level of Rod-ly-ness",
    "ascii_encounter": asc.leviathan,
    "encounter": encounter_leviathan,
    "fish_and_flirt": leviathan_fish_and_flirt,
    "success": asc.leviathan_success,
    "fail": asc.leviathan_fail,
    "action_failed": flirt_fail_leviathan,
    "defeated": leviathan_defeated
}

CRAB_DIALOGUE = {
    "entity": "Crab",
    "ascii_encounter": asc.crab,
    "encounter": random_encounter_crab,
    "start_flirt": start_flirt,
    "flirt_dialogue": flirt_dialogue,
    "flirt_harder_dialogue": flirt_harder_dialogue,
    "invalid_flirt": invalid_flirt,
    "ascii_blushing": asc.blushing,
    "success_dialogue": flirt_success_crab,
    "ascii_fail": asc.flirt_fail,
    "fail_dialogue": flirt_fail_crab
}

FISHERMAN_DIALOGUE = {
    "entity": "Fisherman",
    "ascii_encounter": asc.fisherman,
    "encounter": random_encounter_fisherman,
    "start_flirt": start_flirt,
    "flirt_dialogue": flirt_dialogue,
    "flirt_harder_dialogue": flirt_harder_dialogue,
    "invalid_flirt": invalid_flirt,
    "ascii_blushing": asc.blushing,
    "success_dialogue": flirt_success_fisherman,
    "ascii_fail": asc.flirt_fail,
    "fail_dialogue": flirt_fail_fisherman
}

MERMAID_DIALOGUE = {
    "entity": "Mermaid",
    "ascii_encounter": asc.mermaid,
    "encounter": random_encounter_mermaid,
    "fishing_rod": asc.fishing_rod,
    "start_fish": start_fish,
    "ascii_bucket": asc.bucket,
    "fishing_success_dialogue": fish_mermaid_success,
    "ascii_fishing_fail": asc.fishing_fail,
    "fishing_fail_dialogue": fish_mermaid_fail,
    "start_flirt": start_flirt,
    "flirt_dialogue": flirt_dialogue,
    "ascii_blushing": asc.blushing,
    "flirt_success": flirt_success_mermaid,
    "ascii_fail": asc.flirt_fail,
    "flirt_fail": flirt_fail_mermaid,
    "invalid_flirt": invalid_flirt
}

WHALE_DIALOGUE = {
    "entity": "Whale",
    "ascii_encounter": asc.whale,
    "encounter": random_encounter_whale,
    "fishing_rod": asc.fishing_rod,
    "start_fish": start_fish,
    "ascii_bucket": asc.bucket,
    "fishing_success_dialogue": fish_whale_success,
    "ascii_fishing_fail": asc.fishing_fail,
    "fishing_fail_dialogue": fish_whale_fail,
    "start_flirt": start_flirt,
    "flirt_dialogue": flirt_dialogue,
    "ascii_blushing": asc.blushing,
    "flirt_success": flirt_success_whale,
    "ascii_fail": asc.flirt_fail,
    "flirt_fail": flirt_fail_whale,
    "invalid_flirt": invalid_flirt
}


def main():
    """
    Drive the program.
    """
    pass


if __name__ == "__main__":
    main()
