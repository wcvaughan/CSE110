# Used a while loop to allow player to choose to play again.

play_again = 'YES'
choose_correct = True
introduction = 'Hey, you. You\'re finally awake. How\'d you get those scars on your head?\nReaching up you feel your forehead and remember the brands and the pain. The wagon continues rattling and your head bounces against the bars.\nA blue ribbon zips from the distance and flits in and out of the bars.'
acknowledge = "The light stops in front of the bars and takes the shape of a silhouette. 'Hey Listen!'\n'You\'ve been dreaming and need to wake up!'\n'Eat this blue leaf and you\'ll regain your memories!'\nYou notice a leaf in your hand that wasn\'t there before. To your right is the bowl of mush holding your food for the day."
blue = 'Crumpling the blue leaf in your mouth you feel an immediate tug behind your navel and you open your eyes to see a sunset resting on an azure sea. Do you want to SWIM in the sea or WALK along the beach?'
swim = 'Easing yourself into the waters you find it warm and inviting. You don\'t seem to tire and swim far into the distance, never seeming to leave sight of land.'
walk = 'Strolling along the beach you discover the sand sparkles like the stars and your footsteps leave black prints against the starkly white sand.'
slop = 'The slop tastes as awful as it did the day before. In the distance you see jagged peaks rising in the distance. The first person to talk to you wants to talk again do you ENGAGE him or go to SLEEP?'
engage = 'In talking with the stranger you notice his eyes don\'t seem to track and on closer inspection you notice wires streaming from his shoulders to the back of the wagon. Lights come up from the sky, brighter than the sun and someone yells, "CUT".'
sleep = 'Laying your head down to sleep you dream. In your dream you see an azure sea and a sunset.'
ignore = 'The light zips off into the distance and the wagon rattles on.\n Days pass and you see jagged peaks rising in the distance.\nWhat seemed like mountains now appear to be the remains of buildings blasted and scorched. Ruined remains of some immense city.\nJust before arriving at a meager settlement marked by smoke from fires the wagon is launched suddenly and you are thrown clear from the caravan.\nA swarthy man in a black vest holding what appears to be some firearm rushes to your side.\nWithout looking down he fires a few times and yells to take his hand.'
steal = 'You manage to yank the gun out of his hands and he looks down in shock.\nDo you GIVE him the gun back? SHOOT first or ASK who he is?'
give = 'After handing him his sidearm back he knocks you across the head and you black out. Moments later you feeling a jostling and hear the rumble of a wagon.'
shoot = "The fellow\'s gang catches up as they catch sight of their leader crumpling. They look to you and begin yelling, 'BANGARANG'. Do you yell BANGARANG along with them or THROW the firearm to the ground."
bangarang = 'Yelling bangarang alongside them they begin to cheer. Their firearms ring into the distance but instead of bullets they spray confetti. Their leader stands and throws streamers of blue and gold and congratulates you on reaching your 47th birthday.'
throw = 'Throwing the firearm to the side the followers throw theirs as well and pull out drums. They begin to dance and build fires. You wander into the wilderness.'
ask = 'The man looks down and flashes a grin before bursting into thousands of blue butterflies.'
hand = 'Taking his hand he yanks you to your feet and hands you a trumpet and tells you to start playing flight of the bumblebees or else.\nUnsure what would happen if you disobeyed you do your best and find yourself unwittingly recruited as bard to the infamous dreaded pirate Roberts.'
while play_again.upper() == 'YES':
    user_choice = ''
    print(introduction)
    user_choice = input('ACKNOWLEDGE the swirling light or IGNORE it?')
    if user_choice.upper() == 'ACKNOWLEDGE':
        print(acknowledge)
        user_choice = input('Eat the BLUE leaf or eat your SLOP?')
        while choose_correct == True:
            if user_choice.upper() == 'BLUE':
                user_choice = input(blue)
                if user_choice.upper() == 'SWIM':
                    print(swim)
                    break
                elif user_choice.upper() == 'WALK':
                    print(walk)
                    break
                else:
                    choose_correct = False
                    print('Please choose one of the two options.')
                    break
            elif user_choice.upper() == 'SLOP':
                user_choice = input(slop)
                if user_choice.upper() == 'ENGAGE':
                    print(engage)
                    break
                elif user_choice.upper() == 'SLEEP':
                    print(sleep)
                    break
                else:
                    choose_correct = False
                    print('Please choose one of the two options.')
                    break
            else:
                choose_correct = False
                print('Please choose one of the two options.')
                break
    elif user_choice.upper() == 'IGNORE':
        print(ignore)
        user_choice = input('STEAL the man\'s firearm or take his HAND.')
        while choose_correct == True:
            if user_choice.upper() == 'STEAL':
                user_choice = input(steal)
                while choose_correct == True:
                    if user_choice.upper() == 'GIVE':
                        print(give)
                        break
                    elif user_choice.upper() == 'SHOOT':
                        user_choice = input(shoot)
                        if user_choice.upper() == 'BANGARANG':
                            print(bangarang)
                            break
                        elif user_choice.upper() == 'THROW':
                            print(throw)
                            break
                        else:
                            choose_correct = False
                            print('Please choose one of the two options.')
                            break
                    elif user_choice.upper() == 'ASK':
                        print(ask)
                        break
                    else:
                        choose_correct = False
                        print('Please choose one of the three options.')
                        break
            elif user_choice.upper() == 'HAND':
                print(hand)
                break
            else:
                choose_correct = False
                print('Please choose one of the two options.')
                break
    else:
        choose_correct = False
        print('Please choose one of the two options.')
        break
    play_again = input('Do you want to play again?')

# You need to have at least three levels of scenarios with possible choices. 

# (This means that every time the user plays the game they should answer at least 
 
#  three questions because every branch of the game should go three levels deep.)

# Scenarios that follow an earlier answer should be handled with nested if statements.

# In other words, the body/block of the first if statement will contain a print statement 

# and then another if statement inside it.

# At least one of your scenarios must have more than two possible choices.

# In each prompt, write the choices in ALL CAPS, so that the user knows which 

# words are possible responses to choose.

# When checking the users responses, you should match on the keyword, regardless 

# of the uppercase/lowercase used in the response (e.g., "match", "MATCH", "Match" should all work).

# Making different choices should take you to different scenarios. (You shouldn't have the same result for different choices.)

# Choices should only work for the correct question.

# In other words, if one scenario resulted in choices of Run/Hide, but another 

# resulted in choices Follow/Look, you should not be able to respond with "Follow" to the question that asked for Run/Hide.

# A good way to accomplish this is to have a series of nested if statements. 

# (That is, the print and then the next if statement will be within the body/block of the first if statement.)

# For each question, you should provide an "else" clause to handle the case that 

# the user tries to type something other than the possible choices. It is up to you how to handle this case.

