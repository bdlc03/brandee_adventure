import time


def north():
    print("\nYou walk for miles, by sunset, you reach a Jeep stranded in the sand.")
    time.sleep(1.5)
    time.sleep(2)
    print("\nYou walk towards the Jeep.")
    time.sleep(1)
    print("\n1)Yell, 'Anybody home?' at the Jeep.\n2)Start searching the Jeep.")
    jeep = input()
    if jeep == 1:
        yell()
    else:
        search()


def yell():
    time.sleep(1)
    print("\nYou shout. No response.")
    time.sleep(1)
    search()


def search():
    print("\nYou decide to search the Jeep.")
    time.sleep(1.5)
    print("\nYou tug at the door handle, it's unlocked.")
    time.sleep(1.5)
    print("\nAs you open the door, an awful stench hits your nose.")
    time.sleep(2)
    print("\nSomething tumbles out of the passengers side.")
    time.sleep(2.5)
    print("It's a dead body.")
    time.sleep(2)
    print("You gag at the sight of the lifeless figure slumped on the ground.")
    time.sleep(2)
    print("\nShould you bury it?")
    print("\n1)Yes.\n2)No.")
    body = input()
    if body == 1:
        print("You drag the body into the sand and cover it.")
        time.sleep(2)
    else:
        print("You drag the body away from the car and leave it.")
        time.sleep(2)

    print("\nYou continue searching around the Jeep and discover a small supply of food and water.")
    time.sleep(2.5)
    print("The keys are still in the ignition and the gas tank is half full.")
    time.sleep(2)
    print("\n1)Drive during the night\n2)Rest until morning.")
    time.sleep(1)
    d = input()
    if d == 1:
        print("\nYou drive north for a few hours and then stop and rest till mid afternoon.")
        time.sleep(2)
        print("\nYou squint in the distance and see something.")
        time.sleep(1.5)
        print("\nThere's a caravan.")
        time.sleep(1)
        print("\nChapter 2 Complete.")
        time.sleep(2.5)
        south()
    else:
        print("\nYou decide to sleep in the Jeep.\n")
        time.sleep(1)
        print("\nIn the early hours of morning, you set off driving until the afternoon.")
        time.sleep(2)
        print("\nIn the distance, you spot something.")
        time.sleep(2)
        print("\nIt's a caravan!")
        time.sleep(1)
        print("Chapter 2 complete.")
        time.sleep(2.5)
        south()


def east():
    print("\nYou walk for a day and a half, barely resting.")
    time.sleep(1.5)
    print("\nYour mouth burns from dehydration.")
    time.sleep(1)
    print("\nAs the world fades around you, with your last burst of energy, you sprint towards the illusive oasis.")
    time.sleep(2)
    print("\nIt was only a mirage.")
    time.sleep(1)
    print("\nYou died.")


def south():
    time.sleep(1)
    print("\n1)Approach the caravan.\n2)Yell at the group.")
    caravan = input()
    if caravan == 1:
        print("They greet you happily.")
        greeting()
    if caravan == 2:
        print("They wave to you, gesturing to come over.")
        time.sleep(1.5)
        print("\nYou approach the caravan.")
        time.sleep(1)
        print("\nThey greet you happily.")
        time.sleep(1)
        greeting()


def greeting():
    time.sleep(1)
    print("\n1)Bow in front of them.\n2)Smile and nod enthusiastically.")
    g = input()
    if g == 1:
        print("They were offended by your actions.")
        time.sleep(1.5)
        print("You died.")
    else:
        print("To your surprise, they speak English.")
        time.sleep(1.5)
        print("They ask if you need any water.")
        time.sleep(1)
        water()


def water():
    print("\n1)Take the water.\n2)Politely decline.")
    drink = input()
    if drink == 1:
        print("You gratefully accept the water.")
        time.sleep(1)
        walk()
    else:
        print("You decline.")
        time.sleep(1)
        print("\nYour mouth burns from dehydration.")
        time.sleep(1.5)
        walk()


def walk():
    print("\nYou tell them you woke up in the desert and you're not sure how you got there.")
    time.sleep(2)
    print("\nThey ask if you'd like to travel with them.")
    time.sleep(1)
    print("\nYou agree, knowing you need help getting home.")
    time.sleep(1)
    print("\nThey feed you a small meal, alleviating your hunger pains.")
    time.sleep(2)
    print("\nThey take you to their camp, explaining that you could take one of their Jeeps to a nearby town.")
    time.sleep(2.5)
    print("\nThere you could probably catch a flight home.")
    time.sleep(1.5)
    print("\nThey stock a Jeep full of food, water, and extra fuel.")
    time.sleep(2)
    print("\n'The nearest town is about 100 miles away, north,' one says.")
    time.sleep(2)
    print("\nThey offer you a place to stay for the night. Should you stay?")
    time.sleep(1)
    print("\n1)Yes.\n2)No.")
    n = input()
    if n == 1:
        night()
    else:
        print("\nYou decline, knowing you want to get home as soon as possible.")
        time.sleep(2)
        drive()


def night():
    print("You happily accept their offer, knowing you need the rest.")
    time.sleep(2)
    print("In the morning, you say your goodbyes.")
    time.sleep(2)
    drive()


def drive():
    print("\nYou get in the Jeep and thank them for everything.")
    time.sleep(2)
    print("\nYou drive away, hoping you'll make it home.")
    time.sleep(1.5)
    print("\nChapter 3 complete.")
    time.sleep(2.5)
    print("\nYou drive until the next morning.")
    time.sleep(1.5)
    print("\nYou check the map they gave you. Did you go the wrong way?")
    time.sleep(2.5)
    print("\n1)Turn around the Jeep and go back the way you came.\n2)Continue in the same direction.")
    d = input()
    if d == 1:
        print("\nYou decide to go back the way you came.")
        time.sleep(2)
        print("\nMaybe then you can find the right way.")
        time.sleep(2)
        print("\nAfter driving for hours, you still see none of the landmarks on the map.")
        time.sleep(2)
        print("\n1)Keep going.\n2)Turn around again.")
        p = input()
        if p == 1:
            end2()
        else:
            print("You decide to turn around again, hoping to find your way.")
            time.sleep(1)
            end()
    else:
        print("\nGoing in the same direction seems best.")
        time.sleep(1.5)
        print("Maybe you'll get somewhere before running out of supplies.")
        time.sleep(3)
        end()


def end():
    print("\nAfter driving for a bit, you decide to rest your eyes.")
    time.sleep(2)
    print("\nWhen you wake up, you continue driving.")
    time.sleep(2)
    print("\nThis turns into an endless cycle, sleep, then drive, sleep, then drive.")
    time.sleep(3)
    print("\nYou drive for days, still lost.")
    time.sleep(2)
    print("\nYour supplies are almost out.")
    time.sleep(3)
    print("\n\nYou drive still, until you have no more gas.")
    time.sleep(2)
    print("\nYou are stranded.")
    time.sleep(3)
    print("\nYou end up dying alone in the desert, lost.")
    time.sleep(2)
    print("Chapter 4 complete.")
    time.sleep(2.5)
    print("The End.")
    time.sleep(2)


def end2():
    print("\nYou keep driving.")
    time.sleep(1.5)
    print("\nYou start to lose hope that you'll find home.")
    time.sleep(2)
    print("\n1)Keep going.\n2)Go a different way.\n3)Give up on life.")
    last = input()
    if last == 1:
        print("You continue going in the same direction, blindly searching for any sign you're going the right way.")
        time.sleep(2.5)
        print("Finally, you see something familiar from the map.")
        time.sleep(2)
        print("You end up getting to the city to get a flight home.")
        time.sleep(2)
        print("\nYou live happily ever after.")
        time.sleep(2)
        print("Chapter 4 complete.")
        time.sleep(2.5)
        print("\nThe End.")
        time.sleep(2)
    elif last == 2:
        print("You turn the car around, hoping that maybe, just maybe, you'll get somewhere.")
        time.sleep(2)
        end()
    else:
        print("\nYou decide to give up on life.")
        time.sleep(2)
        print("You die.")
        time.sleep(2)
        print("The End.")
        time.sleep(2)


def west():
    print("\nYou walk in the direction the sun will set.")
    time.sleep(1)
    print("\nChapter 1 complete.")
    time.sleep(2)
    print("\nAfter walking for most of the day, the sun sets and the cool of night sets in.")
    time.sleep(2)
    print("\nContinue walking or rest?")
    print("\n1)Walk.\n2)Rest.")
    wr = input()
    if wr == 1:
        print("You walk until the early hours of morning, exhausted.")
        time.sleep(1.5)
        print("\nYou notice something in the distance...")
        time.sleep(2)
        print("\nIt's a caravan!")
        time.sleep(1)
        print("Chapter 2 complete.")
        time.sleep(2)
        south()
    if wr == 2:
        print("You rest underneath the stars, falling asleep under a blanket of darkness.")
        time.sleep(1.5)
        print("\nIn the morning you continue your journey.")
        time.sleep(1)
        print("\nWhile walking, you notice something in the distance...")
        time.sleep(1)
        print("\nA caravan!")
        time.sleep(1)
        print("Chapter 2 Complete.")
        time.sleep(2)
        south()


def s():
    print("\nYour mouth burns, you need water.")
    time.sleep(1.5)
    print("\nTry to get water from a cactus?")
    time.sleep(1)
    print("\n1)Yes.\n2)No.")
    cactus = input()
    if cactus == 1:
        print("You pick up a stick on the ground.")
        c()
    if cactus == 2:
        print("\nGetting water from the cactus seemed too risky.")
        time.sleep(2)
        print("\nYou decide to keep walking.")
        time.sleep(1.5)
        print("\nAfter walking for a bit, you notice something in the distance...")
        time.sleep(2)
        print("\nIt's a caravan.")
        time.sleep(1)
        print("\nChapter 2 complete.")
        time.sleep(2)
        south()


def c():
    print("\nYou puncture the cactus with the stick, hoping to try to get some water.")
    time.sleep(2.5)
    print("\nYou use the stick to try and take the spines off of it.")
    time.sleep(2)
    print("\nAfter removing most of the spines, you take the top off of the cactus.")
    time.sleep(2)
    print("\nInside, cool water fills the cactus.")
    time.sleep(1.5)
    print("\nYou enjoy the water before continuing your journey.")
    time.sleep(2)
    print("\nYou continue walking and notice something in the distance.")
    time.sleep(2)
    print("\nIt's a caravan.")
    time.sleep(2)
    print("\nChapter 2 complete.")
    time.sleep(2)
    south()


def main():
    print("Home: A Text-Based Adventure")
    time.sleep(1)
    print("\nYou blink your eyes groggily under the blazing heat of the sun.")
    time.sleep(2)
    print("\nWhere are you?")
    time.sleep(1)
    print("\nThe last thing you remember is falling asleep under the shade of a tree in your backyard.")
    time.sleep(2.5)
    print("You slowly get up and observe your surroundings.")
    time.sleep(2)
    print("By the look of the sun, it's around noon.")
    time.sleep(1)
    print("\nYou must get home!")
    time.sleep(2.5)
    print("\nIn every direction you're surrounding by a vast desert.")
    time.sleep(2)
    print("\nBehind you, east, there seems to be an oasis in the distance.\n")
    time.sleep(2)
    print("What direction do you go?")
    print("\n1)Go north.\n2)Go east.\n3)Go south.\n4)Go west.")
    choice = input()
    if choice == 1:
        print("\nYou decide to go north on your journey.")
        time.sleep(1.5)
        print("\nChapter 1 complete.")
        time.sleep(2.5)
        north()
    elif choice == 2:
        east()
    elif choice == 3:
        print("\nSomething compels you to go south.")
        time.sleep(1)
        print("\nYou walk for three miles in the heat and then decide to rest.")
        time.sleep(2)
        print("\nChapter 1 complete.")
        time.sleep(2)
        s()
    else:
        west()

main()
