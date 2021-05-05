# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define nar = Character(what_italic=True)
define e = Character("Eileen")
define brooks = Character("Brooks")
define caleb = Character("Caleb")
define cody = Character("Cody")
define john = Character("John")
define trent = Character("Trent")
define mark = Character("Mark")
default clingee = "Nobody"
default walker = "Nobody"
image eileen idle = Image("images/Miki_Casual_Smile_1_73.png")
image eileen idle2 = Image("images/Miki_Casual_Open_Blush_73.png")
image bg1 = Image("/images/lake/morning.jpg")
image bgHell = Image("images/lake/night.jpg")
image blackscreen = Image("/images/blackscreen.jpg")
image defaultroom = Image("/images/apartment/day.jpg")
image shClass = Image("/images/sh/shClass.png")
image shLobby = Image("/images/sh/shLobby.png")
image shOutside = Image("/images/sh/shOutside.png")
image plexTrack = Image("/images/plex/plexTrack.png")
image entrance = Image("/images/outside/entrance.png")
image outside = Image("/images/outside/fkc.png")
image fountain = Image("/images/outside/fountain.png")
image snowtip = Image("/images/outside/snowtip.png")
image woods = Image("/images/outside/woods.png")
image mcaInside = Image("/images/mca/mcaInside.png")
image library = Image("/images/library/library.png")
image lbhClass = Image("/images/lbh/lbhClass.png")
image lbhOutside = Image("/images/lbh/lbhOutside.png")
image dormDorm = Image("/images/dorm/dorm.png")
image dormHallway = Image("/images/dorm/Hallway.png")
image dormLounge = Image("/images/dorm/lounge.png")
image dcLine = Image("/images/dc/dcLine.png")
image dcOutside = Image("/images/dc/dcOutside.png")
image dcTables = Image("/images/dc/dcTables.png")
image beckerOutside = Image("/images/becker/beckerOutside.png")
image beckerTheater = Image("/images/becker/beckerTheater.png")

image brooks embarrassed = Image("/images/guys/done/brooksembarrassed.png")
image brooks flirt = Image("/images/guys/done/brooksflirt.png")
image brooks neutral= Image("/images/guys/done/brooksneutral.png")
image brooks sad = Image("/images/guys/done/brookssad.png")
image brooks shirtless = Image("/images/guys/done/brooksshirtless.png")
image brooks smile = Image("/images/guys/done/brookssmile.png")
image brooks surprised = Image("/images/guys/done/brookssurprised.png")
image brooks talking = Image("/images/guys/done/brookstalking.png")

image caleb embarrassed = Image("/images/guys/done/calebembarrassed.png")
image caleb flirt = Image("/images/guys/done/calebflirt.png")
image caleb neutral= Image("/images/guys/done/calebneutral.png")
image caleb sad = Image("/images/guys/done/calebsad.png")
image caleb smile = Image("/images/guys/done/calebsmile.png")
image caleb surprised = Image("/images/guys/done/calebsurprised.png")
image caleb talking = Image("/images/guys/done/calebtalking.png")

image cody embarrassed = Image("/images/guys/done/codyembarrassed.png")
image cody flirt = Image("/images/guys/done/codyflirt.png")
image cody neutral= Image("/images/guys/done/codyneutral.png")
image cody sad = Image("/images/guys/done/codysad.png")
image cody smile = Image("/images/guys/done/codysmile.png")
image cody surprised = Image("/images/guys/done/codysurprised.png")
image cody talking = Image("/images/guys/done/codytalking.png")

image john embarrassed = Image("/images/guys/done/johnembarrassed.png")
image john flirt = Image("/images/guys/done/johnflirt.png")
image john neutral= Image("/images/guys/done/johnneutral.png")
image john sad = Image("/images/guys/done/johnsad.png")
image john smile = Image("/images/guys/done/johnsmile.png")
image john surprised = Image("/images/guys/done/johnsurprised.png")
image john talking = Image("/images/guys/done/johntalking.png")

image trent embarrassed = Image("/images/guys/done/trentembarrassed.png")
image trent flirt = Image("/images/guys/done/trentflirt.png")
image trent neutral= Image("/images/guys/done/trentneutral.png")
image trent sad = Image("/images/guys/done/trentsad.png")
image trent smile = Image("/images/guys/done/trentsmile.png")
image trent surprised = Image("/images/guys/done/trentsurprised.png")
image trent talking = Image("/images/guys/done/trenttalking.png")

image mark embarrassed = Image("/images/guys/done/markembarrassed.png")
image mark flirt = Image("/images/guys/done/markflirt.png")
image mark neutral = Image("/images/guys/done/markneutral.png")
image mark sad = Image("/images/guys/done/marksad.png")
image mark smile = Image("/images/guys/done/marksmile.png")
image mark surprised = Image("/images/guys/done/marksurprised.png")
image mark talking = Image("/images/guys/done/marktalking.png")

transform left_left: 
    pos(.255, 1.1) 
    anchor (.5,1.0)
transform right_right: 
    pos(.705, 1.1) 
    anchor (.5,1.0)
transform right_right_right:
    pos(.805, 1.1)
    anchor (.5,1.0)
transform left_left_left:
    pos(.105, 1.1)
    anchor (.5,1.0)
transform leftish:
    pos(.405, 1.1)
    anchor (.5,1.0)
transform rightish:
    pos(.605, 1.1)
    anchor (.5,1.0)

define fade = Fade(0.5, 0.0, 0.5)
#image overlay = Image("/images/badend2-1.png")
transform overlay:
    alpha 0.1
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    play music "audio/love.mp3"
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    show bg1
    show eileen idle at top
    
    # These display lines of dialogue.
    
    e "Hey, you. You're finally awake."

    #show overlay at center
    show eileen idle2 at top
    
    e "Wait... was that my line?!?"

    # This ends the game.
    
    #Start of actual dialogue
    hide eileen idle
    hide eileen idle2
    show blackscreen with Dissolve(.5)
    stop music
    
    play music "audio/soundEffects/alarm.mp3"
    "ALARM" "BEEP, BEEP, BEEP"
    stop music
    play music "audio/default.mp3"
    "THUMP"
    nar "Ugh, another day of school."

    menu:

        "Go to Breakfast.":
            jump breakfastDay1
    
        "Just a few more minutes...":
            jump sleepDay1Breakfast
    
label breakfastDay1:

    $ sleepDay1_flag = False

    show dormDorm with Dissolve(.5)
    hide blackscreen

    nar "I guess I have to get up eventually."
    nar "Now where did I put my ID..."

    #Outside DC
    
    show blackscreen with Dissolve(.5)
    show dcOutside with Dissolve(.5)
    hide dormDorm
    hide blackscreen
    
    show brooks neutral at top 

    e "Oh hi Brooks! Didn't think you would be up this early...I know I almost wasn't!"
    
    hide brooks neutral
    show brooks smile at top
    
    brooks "Hi there! Would you like to join me for breakfast? I know we haven't sat down to talk in a long time."
    
    show cody sad at left_left

    nar "You see Cody sitting at a table alone out of the corner of your eye...Who do you choose to eat with?"

    menu:
        "Breakfast with Brooks":
            hide brooks smile
            hide cody sad
            jump breakfastDay1Brooks
            
        "Breakfast with Cody":
            hide brooks smile
            hide cody sad
            jump breakfastDay1Cody
            
    return

label breakfastDay1Brooks:

    #in DC
    
    show dcTables with Dissolve(.5)
    hide dcOutside
    show brooks smile at top
    
    #you
    e "An RA this semester? No way! That is sooooo hot!"
    
    nar "Am I drooling? I certainly hope not!"
    
    hide brooks smile
    show brooks talking at top
    
    brooks "Yeah, I'm enjoying it. By the way, here's a napkin to help you with that..."
    
    hide brooks talking
    show brooks smile at top
    
    nar "EEK! He noticed. I gotta change the subject."
    
    e "Uhh...thanks! Alright, I gotta head to class."
    
    hide brooks smile
    show brooks surprised at top
    
    brooks "No way, I do too! You going to Sociology?"
    
    hide brooks surprised
    show brooks smile at top
    
    e "Yeah, are you in that class?"
    
    hide brooks smile
    show brooks talking at top
    
    brooks "Yes ma'am! I'll see you there!"
    
    hide brooks talking
    
    nar "Oh my gosh, that was so fun. I can't wait to talk to him later!"

    jump class1Day1

    return
    
label breakfastDay1Cody:

    #you
    e "I would love to eat with you!"
    
    #In DC
    
    show dcTables with Dissolve(.5)
    hide dcOutside
    show cody talking at top
    
    #Cody etc
    cody "...and THAT is why you should never walk with Yu-Gi-Oh cards in your left pocket!"
    
    hide cody talking
    show cody neutral at top
    
    e "Wow, that is SOOOO funny. You are hilarious Cody!"
    
    hide cody neutral
    show cody talking at top
    
    cody "Why thank you!"
    
    hide cody talking
    show cody smile at top
    
    e "Alright, I gotta head to class. See you later."
    
    hide cody smile

    jump class1Day1
    
    return

label sleepDay1Breakfast:
    $ sleepDay1Breakfast_flag = True

    nar "Five more minutes couldn't hurt anything..."

    jump dream1

label dream1:
    scene bg room
    show bg1
    show eileen idle at top 
    play music "audio/love.mp3"

    e "Welcome back dear!"
    e "Would you like dinner? {p}A swim in the lake? {p}Or perhaps..."

    show eileen idle2 at top
    #e "Me"
    
    hide eileen
    show brooks neutral at top
    
    e "Oh hey Brooks, what are you doing here?"
    
    hide brooks neutral
    show brooks talking at top
    
    brooks "You know, the usual. I'm glad you're here though, I have a question for you."
    
    hide brooks talking
    show brooks flirt at top
    
    e "Oh...What is it?"
    
    nar "Could he really be asking me out???"
    
    hide brooks flirt
    hide blackscreen
    show blackscreen with Dissolve(.5)
    hide bg1

    stop music
    play music "audio/soundEffects/alarm.mp3"
    "ALARM" "BEEP, BEEP, BEEP"
    stop music
    play music "audio/default.mp3"
    
    nar "ughhhh...my dreaaaaam."
    
    menu:
        "Go to first class?":
            jump class1Day1
            
        "Just a little more sleep...":
            jump sleepDay1Class1

    return
    
label class1Day1:
    show lbhOutside with Dissolve(.5)
    nar "Finally here...let's see."
    show lbhClass with Dissolve(.5)
    nar "Oh, I know a bunch of people in this class!"
    nar "Let's see...I can sit with Brooks or I could go sit with John. I haven't seen him yet."
    
    show brooks talking at top
    show john neutral at right_right
    
    brooks "Oh hey! We saved a seat for you between us if you wanted to sit here"
    
    nar "Oh, I could sit next to both!"

    menu:
        "Sit with John":
            hide brooks talking
            hide john neutral
            jump class1Day1John
            
        "Sit with Brooks":
            hide brooks talking
            hide john neutral
            jump class1Day1Brooks
            
        "Sit with both":
            hide brooks talking
            hide john neutral
            jump class1Day1Both

    return
    
label sleepDay1Class1:

    jump dream2

    return
    
label dream2:

    stop music
    play music "audio/love.mp3"
    show bg1 with Dissolve(.5)
    show brooks embarrassed at top

    brooks "Yeah, so my question is, would you like to eat lunch with me right now?"
    
    nar "OH MY WORD"
    
    e "Like a date? Are you asking me out?"
    
    hide brooks embarrassed
    show brooks talking at top
    
    brooks "Uh, you know what. S-"
    
    hide brooks talking
    hide blackscreen
    show blackscreen with Dissolve(.5)
    hide bg1

    stop music
    play music "audio/soundEffects/alarm.mp3"
    "ALARM" "BEEP, BEEP, BEEP"
    stop music
    play music "audio/default.mp3"
    
    nar "Gosh darn it, not again!"

    menu:
        "Go to lunch":
            jump lunchDay1Alone
            
        "Just a couple more minutes...":
            jump sleepDay1Lunch

    return
    
label class1Day1John:

    show john neutral at top

    e "Hey John! How are you today?"
    
    hide john neutral
    show john talking at top
    
    john "SHHHH! Class is starting, and I gotta practice my humming during it. Francoise has my notes covered."
    
    hide john talking
    show john smile at top
    
    nar "Well that was weird"
    
    john "*procedes to hum the whole class period"
    
    hide john smile
    
    nar "..."
    
    #stretching, you say
    e "Finally class is over!"
    
    show john flirt at top
    
    john "Yeah. I'm gonna head to lunch now. Would you like to join me?"
    
    hide john flirt
    show john smile
    
    e "Uhhhh well it is lunch time"
    
    nar "I don't know, should I?"

    menu:
        "Lunch with John":
            hide john smile
            show john surprised at top
            e "Sure!"
            hide john surprised
            jump lunchDay1John
            
        "Lunch alone":
            hide john smile
            show john sad at top
            e "No thanks. I uh, have plans. Sorry..."
            hide john sad
            jump lunchDay1Alone
    
    return
    
label class1Day1Brooks:

    #IF YOU SAT BY BROOKS AT BREAKFAST SAY HI AGAIN or else say something else here? nah not worth it rn
    
    show brooks neutral at top
    
    e "Well hello again Brooks."
    
    hide brooks neutral
    show brooks talking at top
    
    brooks "Hey!"
    
    hide brooks talking
    show brooks smile at top
    
    e "Glad I could sit next to you today!"
    
    hide brooks smile
    show brooks talking at top
    
    brooks "Anytime, looks like class is starting now."
    
    hide brooks talking
    
    "..."
    
    show mark neutral at left_left
    
    e "Finally out! Oh hey, is that MARK?"

    menu:
        "Lunch with Mark":
            e "Hey Mark, let's go to lunch!"
            
            hide mark neutral
            show mark talking at left_left
            
            mark "Oh yeah sure! I'm going to FKC, meet me outside in five in my truck"
            
            hide mark talking
            jump lunchDay1Mark
            
        "Lunch alone":
            hide mark neutral
            jump lunchDay1Alone

    return
    
label class1Day1Both:

    show brooks neutral at top
    show john neutral at right_right

    e "Hey guys!"
    
    hide brooks neutral
    show brooks talking at top
    
    brooks "Hi!"
    
    hide john neutral
    show john talking at right_right
    
    john "Sup!"
    
    hide brooks talking
    hide john talking
    
    #class starts and stuff
    
    nar "...class is boring today"
    
    show brooks neutral at top
    show john neutral at right_right
    
    e "Alright, see you guys later!"
    
    hide john neutral
    show john talking at right_right
    
    john "Yeah see you too."
    
    hide brooks neutral
    show brooks talking at top
    
    brooks "See ya!"

    menu:
        "Lunch alone":
            hide brooks talking
            hide john talking
            nar "Time for lunch!"
            jump lunchDay1Alone

    return

label lunchDay1Alone:

    show dcTables with Dissolve(.5)

    nar "Well this is lame...where are the Wright second boyyyys"
    
    nar "Anyways, time for another class..."

    jump class2Day1

    return

label lunchDay1Mark:

    show fkc with Dissolve(.5)
    
    show mark smile at top
    
    e "Yo what are you gonna get?"
    
    hide mark smile
    show mark talking at top
    
    mark "FKC?"
    
    hide mark talking
    show mark neutral at top
    
    e "Yeah what from FKC?"
    
    hide mark neutral
    show mark surprised at top
    
    mark "I love FKC I'm getting FKC"
    
    
    e "...right"
    
    hide mark surprised
    show mark embarrassed at top
    
    e "FKC is good I suppose"
    
    #add more probably? Not sure where to go with this
    
    hide mark embarrassed
    show mark flirt at top
    
    mark "*wink*"
    
    hide mark flirt
    show mark smile at top
    
    e "Oh, we gotta get it to go by the way. I have class."
    
    hide mark smile
    show mark talking at top
    
    mark "Alright lets head back."
    
    hide mark talking

    jump class2Day1
    
    return
    
label lunchDay1John:

    show dcLine with Dissolve(.5)
    show john smile at top

    e "Hey John, so how have you been?"
    
    hide john smile
    show john talking at top
    
    john "I've been fabulous! How are you?"
    
    hide john talking
    show john smile at top
    
    e "I'm good...thanks for asking!"
    
    hide john smile
    hide dcTables
    show dcTables with Dissolve(.5)
    hide dcLine
    #Johns story
    show john talking at top
    
    john "...and that's why you should never sleep with a rainbow narwhal!"
    
    hide john talking
    show john smile at top
    
    e "Well...right. I have class. See you later..."
    nar "Talk about disturbing..."
    
    hide john smile

    jump class2Day1
    
    return

label sleepDay1Lunch:

    jump dream3
    
    return
    
label dream3:

    stop music 
    play music "audio/love.mp3"
    hide bg1
    show bg1 with Dissolve(.5)
    show brooks embarrassed at top
        
    brooks "You know what, Sure! Let's call this a date."
    
    e "Oh my, of course I will, I've been waiting for so long!"
    
    hide brooks embarrassed
    show brooks flirt at top
    
    brooks "In fact, let me get down on my knee..."
    
    hide brooks flirt
    hide blackscreen
    show blackscreen with Dissolve(.5)
    hide bg1

    stop music
    play music "audio/soundEffects/alarm.mp3"
    "ALARM" "BEEP, BEEP, BEEP"
    stop music
    play music "audio/default.mp3"
    
    nar "NOOOOOOOOOOOOOOOOOOOOOOOO!"

    menu:
        "Go to second class":
            jump class2Day1
            
        "So tired...":
            jump sleepDay1Class2

    return

label class2Day1:

    show shOutside with Dissolve(.5)

    nar "Ah! Time for my next class..."
    
    show shClass with Dissolve(.5)
    
    nar "let's see...is anyone I know here?"
    
    show brooks neutral at right_right
    show cody neutral at left_left
    show trent neutral at top
    
    nar "Oh! There's Cody over there, and Brooks on the other side. And of course, Trent in the middle up front."
    menu:
        "Sit with Cody":
            hide brooks neutral
            hide cody neutral
            hide trent neutral
            jump class2Day1Cody
        
        "Sit with Brooks":
            hide brooks neutral
            hide cody neutral
            hide trent neutral
            jump class2Day1Brooks
            
        "Sit with Trent":
            hide brooks neutral
            hide cody neutral
            hide trent neutral
            jump class2Day1Trent
            
    return

label class2Day1Cody:

    show cody neutral at top

    e "Oh hi Cody"
    
    hide cody neutral
    show cody talking at top
    
    cody "Oh hi"
    
    hide cody talking
    
    nar "..."
    "blah blah blah"
    "..."
    
    show cody neutral at top
    
    e "Finally, bye Cody!"
    
    hide cody neutral

    jump walkDay1
    
    return
    
label class2Day1Brooks:

    show brooks neutral at top

    e "Oh hey there Ba- I mean Brooks"
    
    hide brooks neutral
    show brooks surprised at top
    
    brooks "Oh uh, hi! You sitting next to me?"
    
    hide brooks surprised
    show brooks smile at top
    
    e "If that's ok with you~ of course!"
    
    hide brooks smile
    show brooks talking at top
    
    brooks "Sure, go for it. Always a pleasure."
    
    hide brooks talking
    show brooks neutral at top
    
    e "Awesome!"
    
    #later
    "..."
    "..."
    "..."
    "..."
    "..."
    "Class dismissed"
    nar "Wait hey what? I was too busy staring at Brooks...oh well. Grades don't matter anyways."
    
    hide brooks neutral

    jump walkDay1
    
    return
    
label class2Day1Trent:

    show trent neutral at top

    e "Hi Trent..."
    
    hide trent neutral
    show trent talking at top
    
    trent "Hi!"
    
    hide trent talking
    show trent smile at top
    
    e "So quick question before class, I've heard you are a racist. Is this true?"
    
    hide trent smile
    show trent sad at top
    
    trent "Oh class is starting. Sorry, I'm going to pay attention."
    
    hide trent sad
    
    "Trent stares eagerly at the front, even though the teacher hasn't arrived yet."
    
    e "...right. I'll try again later."

    jump walkDay1
    
    return
    
label sleepDay1Class2:

    hide blackscreen
    show blackscreen with Dissolve(.5)

    nar "Ah, no dreams, that sucks. Come on and show me the end of BROOKS AND I."

    menu:
        "I should take a walk through the woods":
            jump walkDay1
            
        "I want to dream more":
            jump sleepDay1Walk
            
    return
    
label walkDay1:

    show fountain with Dissolve(.5)

    nar "Wow...it's beautiful out today!"
    nar "..."

    show woods with Dissolve(.5)

    nar "Is that someone in a tree?"
    
    e "Hey! Are you ok?"
    
    show caleb smile at top
    
    caleb "Oh yeah. I'm just recharging my stamina up here."
    
    e "...huh?"
    nar "Am I about to be murdered?"
    e "Alright, well if you are fine then it's no problem."
    
    hide caleb smile
    show caleb flirt at top
    
    caleb "Oh, I'm fine. Mind if I join you? *hair flip*"
    
    e "...sure."
    nar "I hear that it's best to appease the robbers and follow their commands"
    
    hide caleb flirt
    
    caleb "Alright, well turn away. Me getting down from this tree will be to scandalous for you ;)"
    
    hide caleb flirt
    show caleb smile at top
    
    e"...right"
    
    hide caleb smile
    
    nar "You turn around and immediately feel a tap on your shoulder. Strange."
    
    show caleb neutral at top
    
    caleb "Alright, let's go."
    
    hide caleb neutral
    
    hide blackscreen
    show blackscreen with Dissolve(.5)

    nar "You two walk for awhile in complete silence, until you finally reach the end."
    
    hide fountain
    show fountain with Dissolve(.5)
    hide blackscreen

    show caleb talking at top

    caleb "Well, it was great walking with you, see you around!"
    
    hide caleb
    
    jump dinnerDay1
    
    return
    
label sleepDay1Walk:

    hide blackscreen
    show blackscreen with Dissolve(.5)

    nar "Why AM I NOT DREAMING!"

    menu:
        "I'm hungry...I should go to dinner":
            jump dinnerDay1
            
        "MORE":
            jump sleepDay1Dinner
            
    return
    
label dinnerDay1:

    hide blackscreen

    show dcOutside with Dissolve(.5)

    nar "Hm, what should I do for dinner?"

    menu:
        "FKC with Mark":
            jump FKCDay1
            
        "Dinner with Brooks, Cody and John":
            jump dinnerDay1BCJ
            
        "Dinner with Caleb and Trent":
            jump dinnerDay1CT
            
    return
    
label FKCDay1:

    show mark neutral at top

    e "Oh Mark, I LOVE FKC!"
    
    hide mark neutral
    show mark flirt at top
    
    mark "I know you do baby. After all, who doesn't love some fried chicken?"
    
    hide mark flirt
    hide fkc
    show fkc with Dissolve(.5)
    
    show mark smile at top

    e "Let's eat!"
    
    nar "OM NOM NOM NOm NOM NOM NOM NOM NOM NOM!"
    
    e "Oh yeah! We have things to do tonight. Let's head back Mark."
    
    hide mark smile
    show mark flirt at top
    
    mark "Oh yeah, let's blast outta here baby girl."
    
    hide mark flirt
    
    nar "What to do..."

    menu:
        "Watch a scary movie":
            jump movieDay1
        
        "Go to bed":
            jump sleepDay1Night
            
    return
    
label dinnerDay1BCJ:

    show dcLine with Dissolve(.5)
    
    show cody neutral at left_left
    show brooks neutral at right_right

    e "Wow, I wonder what they have today!"
    
    hide cody neutral
    show cody talking at left_left
    
    cody "Probably nothing good, it is the DC after all."
    
    hide cody talking
    show cody neutral at left_left
    
    e "Now Cody, the DC isn't THAT bad."
    
    hide brooks neutral
    show brooks talking at right_right
    
    brooks "Yes it is."
    
    hide brooks talking
    show brooks neutral at right_right
    
    e "Oh yeah, you're right Brooks...it is unbearable after all."
    
    show dcTables with Dissolve(.5)
    
    show john talking at top

    john "...and that's why I agree with Kim Jong Un."
    
    hide john talking
    show john smile at top
    hide brooks neutral
    hide cody neutral
    show brooks smile at right_right
    show cody smile at left_left
    
    e "Haha! Nice!"
    
    hide brooks smile
    show brooks talking at right_right
    
    brooks "Oh shoot, look at the time! We really have to go. We were gonna watch a scary movie. You joining?"
    
    e "Ehhhh..."

    menu:
        "Watch the scary movie":
            e "Sure!"
            hide brooks talking
            jump movieDay1
        
        "Go to bed":
            e "Nah, I'm tired. Thanks though"
            hide brooks talking
            jump sleepDay1Night
            
    return
    
label dinnerDay1CT:

    show dcTables with Dissolve(.5)
    
    show caleb neutral at left_left
    show trent neutral at right_right

    "They say nothing, but gnaw on their food and stare at you."
    
    hide trent neutral
    hide caleb neutral
    
    "You promptly leave."

    menu:
        "Watch a scary movie":
            jump movieDay1
        
        "Go to bed":
            jump sleepDay1Night
            
    return
    
label sleepDay1Dinner:

    jump dream4
    
    return
    
label dream4:

    stop music
    play music "audio/love.mp3"

    show bg1 with Dissolve(.5)
    show john smile at top

    john "I'm elmo, and I'm not your friend!"
    
    show bgHell with Dissolve(.5)
    stop music
    hide john smile
    show john surprised at top

    john "Come here so I can gut you like a fish!"
    
    e "AHHHHH"
    
    hide john surprised
    
    play music "audio/soundEffects/alarm.mp3"
    "ALARM" "BEEP, BEEP, BEEP"
    stop music
    play music "audio/default.mp3"

    hide blackscreen
    show blackscreen with Dissolve(.5)

    e "WHAT THE FRICK WAS THAT!"
    e "THAT DREAM SUCKED!"


    menu:
        "Watch a scary movie":
            jump movieDay1
        
        "Go to bed":
            e "What ever, might as well sleep through the night then."
            jump sleepDay1Night
            
    return
    
label movieDay1:

    show beckerTheater with Dissolve(.5)

    e "It's kinda cold down here."
    
    show brooks talking at right_right

    brooks "Do you want my blanket? I'm not using it."

    e "Sure, thanks Brooks!"
    
    hide brooks talking
    hide blackscreen
    
    show blackscreen with Dissolve(.5)
    hide beckerTheater

    nar "..."
    nar "..."
    nar "..."

    "RAWR"

    show beckerTheater with Dissolve(.5)

    e "EEEEEEK!"
    e "Oh gosh this movie is scary! It got me again...I need to relax and be safe"

    menu:
        "Cling to Brooks":
            $ clingee = "Brooks"
            show brooks smile at right_right
            nar "You cling to Brooks, and he seems happy. You enjoy the rest of the movie together."
            hide brooks smile
            jump movieDay1Cling
        
        "Cling to Caleb":
            $ clingee = "Caleb"
            show caleb smile at right_right
            nar "You cling to Caleb, and he seems happy. You enjoy the rest of the movie together."
            hide caleb smile
            jump movieDay1Cling
            
        "Cling to Cody":
            $ clingee = "Cody"
            show cody smile at right_right
            nar "You cling to Cody, and he seems happy. You enjoy the rest of the movie together."
            hide cody smile
            jump movieDay1Cling
            
        "Cling to Trent":
            $ clingee = "Trent"
            show trent smile at right_right
            nar "You cling to Trent, and he seems happy. You enjoy the rest of the movie together."
            hide trent smile
            jump movieDay1Cling
            
        "Cling to Mark":
            $ clingee = "Mark"
            show mark smile at right_right
            nar "You cling to Mark, and he seems happy. You enjoy the rest of the movie together."
            hide mark smile
            jump movieDay1Cling
            
        "Cling to John":
            $ clingee = "John"
            show john smile at right_right
            nar "You cling to John, and he seems happy. You enjoy the rest of the movie together."
            hide john smile
            jump movieDay1Cling
        
    return
    
label movieDay1Cling:

    hide blackscreen
    show blackscreen with Dissolve(.5)

    nar "What a long day, I suppose it is time for bed."

    jump sleepDay1Night
    
    return
    
label sleepDay1Night:

    jump dream5
    
    return
    
label dream5:

    nar "Ah, where am I? This doesn't look like a normal restaurant."
    
    nar "Oh yeah...I'm just a salisbury steak looking to be eaten."
    
    nar "Wait...these ingredients. What do they have in common..."
    
    nar "Barley, oats, quinoa...tofu, beans, peanuts...OH NO!"
    
    nar "I'M IN A VEGAN RESTAURANT! I'LL NEVER GET EATEN!"

    nar "NOOOOOOOOOOOOOOOOOOOOOOOOOO!"
    
    "ALARM" "BEEP BEEP BEEP"
    
    e "what."

    jump breakfastDay2
    
    return
    
label breakfastDay2:

    show dcLine with Dissolve(.5)

    nar "Oh man I'm so tired. At least it's Saturday so I could sleep in some."
    nar "Breakfast should help me put some pep in my step."

    show dcTables with Dissolve(.5)

    nar "gosh I love eggs."
    nar "Oh yeah, I still have Brook's blanket from last night! I should run up to his room and return that real quick."

    jump blanketReturn
    
    return
    
label blanketReturn:

    show dormHallway with Dissolve(.5)

    nar "Knock knock"
    e "Brooks, you in there?"
    nar "..."
    nar "He still hasn't answered..."
    
    stop music
    play music "audio/love.mp3"

    show brooks shirtless at left_left
    
    brooks "Oh hey. What are you doing up here? You aren't supposed to be on our floor."
    nar "No way. Brooks, fresh out of the shower, and shirtless! I can't believe this!"
    #NEED SHIRTLESS BROOKS
    e "Oh yeah, I was just, you know, dropping your blanket off."
    brooks "Alright then. Thank you, now you better go before I have to fine you."
    e "Cya later"
    
    hide brooks shirtless
    stop music
    play music "audio/default.mp3"

    nar "Oh my gosh I can't believe that just happened! Now I can think about that while I do all of my homework."

    jump homeworkDay2
    
    return
    
label homeworkDay2:

    show dormDorm with Dissolve(.5)
    
    nar "hmmm...the square root of twenty five x squared boils down to..."
    show brooks smile at top
    nar "Brooks!"
    nar "Wait no, I can't get distracted, its five x."
    hide brooks smile
    nar "..."
    nar "Ok, finally done! Oh, I guess I'm eating a late lunch today. That took longer than it should have because I kept thinking of Brooks..."

    jump lunchDay2
    
    return
    
label lunchDay2:
    hide dcOutside
    show dcOutside with Dissolve(.5)
    hide dormDorm

    nar "I doubt anyone will be here to eat with me this late."

    hide dcLine
    show dcLine with Dissolve(.5)
    hide dcOutside

    show brooks talking at right_right

    brooks "Hey, isn't it a little ate to eat lunch?"
    
    hide brooks talking
    show brooks smile at right_right
    show cody smile at left_left
    
    e "No way, you guys are all here?"
    
    hide cody smile
    show cody talking at left_left
    
    cody "Yeah, lost track of time. We all have different things to do, but feel free to join whoever."
    
    hide cody talking
    hide brooks smile

    menu:
        "Lunch with Brooks":
            show cody sad at left_left
            "I'll go with Brooks!"
            hide cody sad
            jump lunchDay2Brooks
        
        "Lunch with Caleb":
            show cody sad at left_left
            "I'll go with Caleb!"
            hide cody sad
            jump lunchDay2Caleb
        
        "Lunch with Cody":
            show cody surprised at left_left
            "I'll go with Cody!"
            hide cody surprised
            jump lunchDay2Cody
        
        "Lunch with Trent":
            show cody sad at left_left
            "I'll go with Trent!"
            hide cody sad
            jump lunchDay2Trent
        
        "FKC with Mark":
            show cody sad at left_left
            "I'll go with Mark!"
            hide cody sad
            jump FKCDay2Lunch
        
        "Lunch with John":
            show cody sad at left_left
            "I'll go with John!"
            hide cody sad
            jump lunchDay2John
            
    return
    
label lunchDay2Brooks:

    e "Hey Brooks."
    
    show brooks talking at top
    
    brooks "Oh, hey there. You joining me for lunch?"
    
    hide brooks talking
    show brooks smile at top
    
    e "Yeah, if that's ok with you."
    
    hide brooks smile
    show brooks talking at top
    
    brooks "Of course, that's no problem."
    
    hide brooks talking
    show brooks smile at top
    
    e "Great!"
    
    hide dcTables
    show dcTables with Dissolve(.5)
    
    hide brooks smile
    show brooks talking at top

    "..."
    
    brooks "...and THAT'S why all the Europeans...er...yeah"
    
    hide brooks talking
    show brooks smile at top
    
    e "...ok"
    
    hide brooks smile
    show brooks talking at top
    
    brooks "I gotta go, cya later!"
    
    hide brooks talking
    show brooks smile at top
    
    e "Alright, bye."
    
    nar "I'll go hang out with Mark now."

    jump afternoonDay2Mark
    
    return
    
label lunchDay2Caleb:

    show caleb neutral at top

    e "Hey Caleb, what's up?"
    
    hide caleb neutral
    show caleb talking at top
    
    caleb "Oh, just getting some lunch."
    
    hide caleb talking
    show caleb neutral at top
    
    e "Mind if I join you?"
    
    hide caleb neutral
    show caleb embarrassed at top
    
    caleb "Sure..."
    
    e "Man I can't believe we can't find a table!"
    
    hide caleb embarrassed
    show caleb sad at top
    
    caleb "That's fine, my head hurts anyways. I'm gonna go back to my dark, quiet, drippy cave."
    
    e "Well alright then."
    
    hide caleb sad
    
    hide dcTables
    show dcTables with Dissolve(.5)

    nar "Guess I'll eat alone since Cynthia left."
    
    jump afternoonDay2Brooks
    
    return
    
label lunchDay2Cody:

    show cody flirt at top

    e "Hey Cody, Mr. CMC."
    
    cody "Hi."
    
    e "Can I eat dinner with you?"
    
    hide cody flirt
    show cody embarrassed at top
    
    cody "I mean it's lunch, but ok."

    hide dcTables
    show dcTables with Dissolve(.5)
    
    hide cody embarrassed
    show cody talking at top
    
    cody "...and that's why being a CMC is great."
    
    hide cody talking
    show cody smile at top
    
    e "Man, I don't know any other floor that paints for floor worship!"
    
    hide cody smile
    show cody talking at top
    
    cody "Alright, cya later. I gotta go."
    
    hide cody talking
    
    e "Cya!"
    
    jump afternoonDay2Brooks
    
    return
    
label lunchDay2Trent:

    hide dcTables
    show dcTables with Dissolve(.5)
    
    show trent talking at top

    "..."
    
    hide trent talking
    show trent sad at top
    
    trent "And THAT is why we aren't allowed to date our students."
    
    e "I mean yeah, I feel like that was common sense and really didn't need a scientific study?"
    
    hide trent sad
    show trent talking at top
    
    trent "Anyways, we are just talking."
    
    hide trent talking
    show trent neutral at top
    
    e "Yeah, let's go."
    
    hide trent neutral
    
    jump afternoonDay2Brooks
    
    return
    
label FKCDay2Lunch:

    hide fkc
    show fkc with Dissolve(.5)

    "..."
    
    show mark neutral at top

    e "I like your truck by the way, and I can't believe you listen to Rob Zombie!"
    
    hide mark neutral
    show mark surprised at top
    
    mark "I love listening to him while I shuck 10 billion ears of corn!"
    
    hide mark surprised
    show mark smile at top
    
    e "You really like your farming and FKC don't you..."
    
    mark "Yeah, it's my life..."
    
    hide mark smile
    show mark sad at top
    
    mark "Well I have some homework so let's get back now."
    
    nar "Alright, time to go back and hang out with Brooks."
    
    hide mark sad
    
    jump afternoonDay2Brooks
    
    return
    
label lunchDay2John:

    hide dcTables
    show dcTables with Dissolve(.5)

    "..."
    
    show john neutral at top

    e "I love your socks John!"
    
    hide john neutral
    show john talking at top
    
    john "Thanks, I figured if I have to wear them I might as well pick some good ones."
    
    hide john talking
    show john smile at top
    
    e "Those are the best Narwhal socks I have EVER seen, trust me."
    
    hide john smile
    show john talking
    
    john "Thanks thanks, alright. I gotta go to the MCA now so I'll see you later!"
    
    hide john talking
    
    e "Bye John!"
    
    nar "Alright, time to go back and hang out with Brooks."
    
    jump afternoonDay2Brooks
    
    return
    
label afternoonDay2Mark:

    show mark neutral at top

    e "Yo Mark, wanna go do something?"
    
    hide mark neutral
    show mark talking at top
    
    mark "Sure! Let's go somewhere. Anywhere you had in mind?"
    
    hide mark talking
    show mark smile at top
    
    e "I was thinking we should go to FKC in Kentucky."
    
    hide mark neutral
    show mark talking at top
    
    mark "Hey, sounds good to me. Meet me in my truck in five."
    
    hide mark talking
    show mark smile at top
    
    e "Man, the mall is so much fun. I missed doing this because I don't have a vehicle on campus."
    
    hide mark neutral
    show mark talking at top
    
    mark "Yeah, too bad we couldn't make it to Kentucky. Sorry about not having gas and being broke."
    
    hide mark talking
    show mark smile at top
    
    e "All good, this place is great and the FKC is fine here!"
    
    hide mark neutral
    show mark talking at top
    
    mark "I spent all my money on FKC, so that's why!"
    
    hide mark talking
    show mark smile at top
    
    e "Wow Mark, I'm gonna miss you when you graduate."
    
    hide mark neutral
    show mark talking at top
    
    mark "Yeah, alright. Let's get walking around the mall before we leave."
    
    hide mark talking
    show mark smile at top
    
    e "Yessir."
    
    hide mark neutral

    jump dinnerDay2
    
    return
    
label afternoonDay2Brooks:

    hide dcOutside
    show dcOutside with Dissolve(.5)
    
    show brooks smile at top

    e "Hi Brooks! What do you wanna do?"
    
    hide brooks smile
    show brooks talking at top
    
    brooks "Oh hey. I was thinking we could just chill in the lounge or somewhere quiet."
    
    hide brooks talking
    show brooks smile at top
    
    e "Yeah, lets do that."
    
    hide brooks smile

    hide blackscreen
    show blackscreen with Dissolve(.5)
    
    "..."

    hide dormLounge
    show dormLounge with Dissolve(.5)
    
    e "So that's why you went to Wright 2 out of all the other choices."
    
    hide brooks smile
    show brooks talking at top
    
    brooks "Yep, and I'm glad I did! It is simply the best floor...oh! Look at the time."
    
    hide brooks talking
    show brooks smile at top
    
    e "Dinner already? Wow that time flew by."
    
    hide brooks smile
    show brooks talking at top
    
    brooks "Yeah, let's go together."
    
    hide brooks talking
    show brooks smile at top
    
    e "Ok!"
    
    hide brooks smile

    jump dinnerDay2
    
    return
    
label dinnerDay2:

    hide dcOutside
    show dcOutside with Dissolve(.5)
    
    show caleb neutral at top
    show trent neutral at right_right

    e "Oh hey! You going to dinner?"
    
    hide caleb neutral
    show caleb talking at top
    
    caleb "Yeah we were just go..."
    
    hide trent neutral
    show trent talking at right_right
    
    trent "Wanna sit with us?"

    menu:
        "Dinner with Brooks, John and Cody":
            e "No, sorry, I already told these guys I would eat with them! Thanks though."
            hide caleb talking
            hide trent talking
            jump dinnerDay2BJC
        
        "Dinner with Caleb and Trent":
            e "Sure!"
            hide trent talking
            hide caleb talking
            jump dinnerDay2CTC
            
        "FKC with Mark":
            e "I'm actually gonna go find Mark and go with him!"
            hide trent talking
            caleb "Uhhhh...alrighty then..."
            hide caleb talking
            jump FKCDay2Dinner
            
    return
    
label dinnerDay2BJC:

    hide blackscreen
    show blackscreen with Dissolve(.5)

    "..."
    
    hide dcTables
    show dcTables with Dissolve(.5)
    
    show brooks talking at left_left
    show cody neutral at top
    show john neutral at right_right

    brooks "Yeah, we have a trebs concert next week if you would like to join!"
    
    hide brooks talking
    show brooks neutral at left_left
    
    e "I think I'll pass on this one, thank you though."
    
    hide cody neutral
    show cody talking at top
    
    cody "What's the problem, you're only the wrong gender!"
    
    hide cody talking
    show cody smile at top
    hide john neutral
    show john smile at right_right
    
    e "Exaaactly."
    
    hide john smile
    show john talking at right_right
    
    john "Alright, let's bust this DC joint and get outta here."

    menu:
        "Evening stroll with Brooks":
            hide john talking
            hide cody smile
            e "Hey Brooks, wanna go on a walk?"
            $ walker = "brooks"
            hide brooks neutral
            jump walkDay2
            
        "Evening stroll with John":
            hide brooks neutral
            hide cody smile
            e "Hey John, wanna go on a walk?"
            $ walker = "john"
            hide john talking
            jump walkDay2
            
        "Evening stroll with Cody":
            hide brooks neutral
            hide john talking
            e "Hey Cody, wanna go on a walk?"
            $ walker = "cody"
            hide cody smile
            jump walkDay2
            
    return
    
label dinnerDay2CTC:

    hide blackscreen
    show blackscreen with Dissolve(.5)

    "..."

    hide dcTables
    show dcTables with Dissolve(.5)
    
    show caleb talking at top
    show trent neutral at left_left
    
    caleb "Yeah, we have a Smash Bros. Tournament next week if you would like to join!"
    
    hide caleb talking
    show caleb smile at top
    
    e "I might come watch, but I don't play. Besides, melee is more interesting to watch so I'd probably play that if anything."
    
    hide trent neutral
    show trent flirt at left_left
    
    trent "Alright cool...hey."
    
    e "W-what?? *Blushes*"
    
    hide trent flirt
    show trent talking at left_left
    
    trent "We're just talking."

    menu:
        "Evening stroll with Trent":
            hide caleb smile
            $ walker = "trent"
            e "Hey Trent, wanna go on a walk?"
            hide trent talking
            jump walkDay2
            
        "Evening stroll with Caleb":
            $ walker = "caleb"
            hide trent talking
            e "Hey Caleb, wanna go on a walk?"
            hide caleb smile
            jump walkDay2
            
        #"Evening stroll with Cole":
        #    $ walker = "Cole"
        #    e "Hey Cole, wanna go on a walk?"
        #    jump walkDay2
            
    return
    
label FKCDay2Dinner:

    hide fkc
    show fkc with Dissolve(.5)
    
    show mark talking at top

    "MUNCH MUNCH"
    
    mark "I LOVE FKC"
    
    hide mark talking
    show mark embarrassed at top
    
    e "MMMMMM"
    
    e "Hey Mark, let's go on a walk together."
    
    hide mark embarrassed
    show mark flirt at top
    
    mark "OK"
    
    hide mark flirt
    
    $ walker = "mark"

    jump walkDay2
    
    return
   
label walkDay2:

    hide fountain
    show fountain with Dissolve(.5)
    
    if walker == "brooks":
        show brooks neutral at left_left
        nar "Why isn't he saying anything?"
        "You walk in complete silence the entire way, and arrive at the lounge at the very end of your walk."
        hide brooks neutral
    if walker == "mark":
        show mark neutral at left_left
        nar "Why isn't he saying anything?"
        "You walk in complete silence the entire way, and arrive at the lounge at the very end of your walk."
        hide mark neutral
    if walker == "cody":
        show cody neutral at left_left
        nar "Why isn't he saying anything?"
        "You walk in complete silence the entire way, and arrive at the lounge at the very end of your walk."
        hide cody neutral
    if walker == "john":
        show john neutral at left_left
        nar "Why isn't he saying anything?"
        "You walk in complete silence the entire way, and arrive at the lounge at the very end of your walk."
        hide john neutral
    if walker == "caleb":
        show caleb neutral at left_left
        nar "Why isn't he saying anything?"
        "You walk in complete silence the entire way, and arrive at the lounge at the very end of your walk."
        hide caleb neutral
    if walker == "trent":
        show trent neutral at left_left
        nar "Why isn't he saying anything?"
        "You walk in complete silence the entire way, and arrive at the lounge at the very end of your walk."
        hide trent neutral

    jump smashBros
    
    return
    
label smashBros:

    stop music
    play music "audio/soundEffects/melee.mp3"
    hide dormLounge
    show dormLounge with Dissolve(.5)
    
    show caleb talking at top
    show trent neutral at left_left
    show john neutral at right_right

    caleb "Alright, practicing in some big free for alls! The best way to warm up."
    
    hide caleb talking
    show caleb neutral at top
    hide trent neutral
    show trent talking at left_left
    
    trent "We have to put items and final smash on for the tournament practice."
    
    hide john neutral
    show john talking at right_right
    
    john "Looks good to me, pick jungle japes and lets get playing."
    
    hide john talking
    hide trent talking
    show john neutral at right_right
    show trent neutral at left_left
    
    "..."
    
    "clack click clack"
    
    "..."
    
    hide john neutral
    show john smile at right_right
    
    john "Yeah, I won the most!"
    
    hide trent neutral
    show trent smile at left_left
    
    trent "Great job!"
    
    hide caleb neutral
    show caleb smile at top
    
    caleb "Good games!"
    
    john "I think we are ready, let's head to bed."
    
    trent "Night everyone."
    
    e "Night."

    stop music
    jump sleepDay2Night
    
    return
    
label sleepDay2Night:

    hide dormDorm
    show dormDorm with Dissolve(.5)

    nar "Oh, Church is tomorrow...I wonder who I should ask to go with me"
    
    nar "I'll decide tomorrow who to ask to Church with."

    nar "Sigh, I'm so tired. Off to bed I go."

    jump dream6
    
    return
    
label dream6:

    hide blackscreen
    show blackscreen with Dissolve(.5)

    nar "Who should I go with to Church tomorrow..."
    
    nar "I mean, it has to be someone I like, it's basically asking them out."
    
    nar "Everything I've done comes down to this."
    
    nar "This is so important."

    nar "I can't wait."
    
    play music "audio/soundEffects/alarm.mp3"
    "ALARM" "BEEP BEEP BEEP"
    stop music

    nar "Well, for once my dream was accurate."
    
    nar "Here I go."

    jump finalScene
    
    return
    
label finalScene:

    #NEED TO DIVIDE THESE UP WITH POSITIONS
    hide dormHallway
    show dormHallway with Dissolve(.5)

    play music "audio/love.mp3"
    hide cody
    hide brooks
    hide caleb
    hide trent
    hide mark
    hide john

    show cody neutral at leftish
    show caleb neutral at right_right
    show trent neutral at left_left
    show mark neutral at left_left_left
    show john neutral at right_right_right
    show brooks neutral at rightish

    e "Hey guys."
    
    hide brooks neutral
    show brooks talking at top
    
    brooks "Hey, who were you thinking of going to Church with?"
    
    hide brooks talking
    show brooks neutral at top
    
    e "Uhhh, good question. This is very important, so give me a second to think..."

    menu:
        "Church with Brooks":
            e "Brooks, I choose you!"
            hide caleb neutral
            hide trent neutral
            hide mark neutral
            hide john neutral
            hide cody neutral
            hide brooks neutral
            show brooks smile at top
            
            brooks "Alright, let's go together then!"
            jump church
            
        "Church with Cody":
            e "Cody, let's go together."
            hide caleb neutral
            hide trent neutral
            hide mark neutral
            hide john neutral
            hide cody neutral
            hide brooks neutral
            show cody smile at top
            
            cody "Ok."
            jump church
            
        "Church with John":
            e "John, John, let's get going!"
            hide caleb neutral
            hide trent neutral
            hide mark neutral
            hide john neutral
            hide cody neutral
            hide brooks neutral
            show john smile at top
            
            john "Alright!"
            jump church
            
        "Church with Mark":
            e "Mark, let's go and get some chicken afterwards!"
            hide caleb neutral
            hide trent neutral
            hide mark neutral
            hide john neutral
            hide cody neutral
            hide brooks neutral
            show mark smile at top
            
            mark "Sounds like a plan to me!"
            jump church
            
        "Church with Caleb":
            e "Caleb, let's go."
            hide caleb neutral
            hide trent neutral
            hide mark neutral
            hide john neutral
            hide cody neutral
            hide brooks neutral
            show caleb smile at top
            
            caleb "Heck yeah!"
            jump church
            
        "Church with Trent":
            e "Pineapple sauce!"
            hide caleb neutral
            hide trent neutral
            hide mark neutral
            hide john neutral
            hide cody neutral
            hide brooks neutral
            show trent smile at top
            
            trent "And pancakes!"
            jump church
            
    return
    
label church:

    "You attend Church with him and have a great time, and this is just the beginning of your future together!"
    "..."

    return
            
        
            
        
            
            

        
        
