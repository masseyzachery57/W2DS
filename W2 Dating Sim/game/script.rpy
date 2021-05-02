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
     
    "ALARM" "BEEP, BEEP, BEEP"
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
    play music "audio/default.mp3"

    nar "I guess I have to get up eventually."
    nar "Now where did I put my ID..."

    #Outside DC
    
    show blackscreen with Dissolve(.5)
    show dcOutside with Dissolve(.5)
    hide dormDorm
    hide blackscreen
    
    show brooks neutral at top 

    e "Oh hi Brooks! Didn't think you would be up this early...I know I almost wasn't!"
    
    brooks "Hi there! Would you like to join me for breakfast? I know we haven't sat down to talk in a long time"
    
    show cody sad at left

    nar "You see Cody sitting at a table alone out of the corner of your eye...Who do you choose to eat with?"

    menu:
        "Breakfast with Brooks":
            jump breakfastDay1Brooks
            
        "Breakfast with Cody":
            jump breakfastDay1Cody
            
    return

label breakfastDay1Brooks:

    #in DC
    
    show dcTables with Dissolve(.5)
    hide dcOutside
    #you
    e "An RA this semester? No way! That is sooooo hot!"
    
    nar "Am I drooling? I certainly hope not!"
    
    brooks "Yeah, I'm enjoying it. By the way, here's a napkin to help you with that..."
    
    nar "EEK! He noticed. I gotta change the subject."
    
    e "Uhh...thanks! Alright, I gotta head to class."
    
    brooks "No way, I do too! You going to Sociology?"
    
    e "Yeah, are you in that class?"
    
    brooks "Yes ma'am! I'll see you there!"
    
    nar "Oh my gosh, that was so fun. I can't wait to talk to him later!"

    jump class1Day1

    return
    
label breakfastDay1Cody:
    
    #In DC
    
    show dcTables with Dissolve(.5)
    hide dcOutside
    #you
    e "I would love to eat with you!"
    
    #Cody etc
    cody "...and THAT is why you should never walk with Yu-Gi-Oh cards in your left pocket!"
    
    e "Wow, that is SOOOO funny. You are hilarious Cody!"
    
    cody "Why thank you!"
    
    e "Alright, I gotta head to class. See you later."

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
    
    
    
    
    e "Oh hey Brooks, what are you doing here?"
    
    brooks "You know, the usual. I'm glad you're here though, I have a question for you."
    
    e "Oh...What is it?"
    
    nar "Could he really be asking me out???"
    
    "ALARM" "BEEP, BEEP, BEEP"
    
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
    
    brooks "Oh hey! We saved a seat for you between us if you wanted to sit here"
    
    nar "Oh, I could sit next to both!"

    menu:
        "Sit with John":
            jump class1Day1John
            
        "Sit with Brooks":
            jump class1Day1Brooks
            
        "Sit with both":
            jump class1Day1Both

    return
    
label sleepDay1Class1:

    jump dream2

    return
    
label dream2:

    brooks "Yeah, so my question is, would you like to eat lunch with me right now?"
    
    nar "OH MY WORD"
    
    e "Like a date? Are you asking me out?"
    
    brooks "Uh, you know what. S-"
    
    "ALARM" "BEEP, BEEP, BEEP"
    
    nar "Gosh darn it, not again!"

    menu:
        "Go to lunch":
            jump lunchDay1Alone
            
        "Just a couple more minutes...":
            jump sleepDay1Lunch

    return
    
label class1Day1John:

    e "Hey John! How are you today?"
    
    john "SHHHH! Class is starting, and I gotta practice my humming during it. Francoise has my notes covered."
    
    nar "Well that was weird"
    
    john "*procedes to hum the whole class period"
    
    nar "..."
    
    #stretching, you say
    e "Finally class is over!"
    
    john "Yeah. I'm gonna head to lunch now. Would you like to join me?"
    
    e "Uhhhh well it is lunch time"
    
    nar "I don't know, should I?"

    menu:
        "Lunch with John":
            e "Sure!"
            jump lunchDay1John
            
        "Lunch alone":
            e "No thanks. I uh, have plans. Sorry..."
            jump lunchDay1Alone
    
    return
    
label class1Day1Brooks:

    #IF YOU SAT BY BROOKS AT BREAKFAST SAY HI AGAIN or else say something else here?
    
    e "Well hello again Brooks."
    
    brooks "Hey!"
    
    e "Glad I could sit next to you today!"
    
    brooks "Anytime, looks like class is starting now."
    
    "..."
    
    e "Finally out! Oh hey, is that MARK?"

    menu:
        "Lunch with Mark":
            e "Hey Mark, let's go to lunch!"
            
            mark "Oh yeah sure! I'm going to FKC, meet me outside in five in my truck"
            jump lunchDay1Mark
            
        "Lunch alone":
            jump lunchDay1Alone

    return
    
label class1Day1Both:

    e "Hey guys!"
    
    brooks "Hi!"
    
    john "Sup!"
    
    #class starts and stuff
    
    nar "...class is boring today"
    
    e "Alright, see you guys later!"
    
    john "Yeah see you too."
    
    brooks "See ya!"

    menu:
        "Lunch alone":
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
    
    e "Yo what are you gonna get?"
    
    mark "FKC?"
    
    e "Yeah what from FKC?"
    
    mark "I love FKC I'm getting FKC"
    
    e "...right"
    
    nar "FKC is good"
    
    #add more probably? Not sure where to go with this
    
    mark "*wink*"
    
    e "Oh, we gotta get it to go by the way. I have class."
    
    mark "Alright lets head back."

    jump class2Day1
    
    return
    
label lunchDay1John:

    show dcLine with Dissolve(.5)

    e "Hey John, so how have you been?"
    
    john "I've been fabulous! How are you?"
    
    e "I'm good...thanks for asking!"
    
    show dcTables with Dissolve(.5)

    #Johns story
    john "...and that's why you should never sleep with a rainbow narwhal!"
    
    e "Well...right. I have class. See you later..."
    nar "Talk about disturbing..."

    jump class2Day1
    
    return

label sleepDay1Lunch:

    jump dream3
    
    return
    
label dream3:
        
    brooks "You know what, Sure! Let's call this a date."
    
    e "Oh my, of course I will, I've been waiting for so long!"
    
    brooks "In fact, let me get down on my knee..."
    
    "ALARM" "BEEP, BEEP, BEEP"
    
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
    nar "Oh! There's Cody over there, and Brooks on the other side. And of course, Trent in the middle up front."
    menu:
        "Sit with Cody":
            jump class2Day1Cody
        
        "Sit with Brooks":
            jump class2Day1Brooks
            
        "Sit with Trent":
            jump class2Day1Trent
            
    return

label class2Day1Cody:

    e "Oh hi Cody"
    cody "Oh hi"
    nar "..."
    e "Finally, bye Cody!"

    jump walkDay1
    
    return
    
label class2Day1Brooks:

    e "Oh hey there Ba- I mean Brooks"
    
    brooks "Oh uh, hi! You sitting next to me?"
    
    e "If that's ok with you~ of course!"
    
    brooks "Sure, go for it. Always a pleasure."
    
    e "Awesome!"
    
    #later
    "Class dismissed"
    nar "Wait hey what? I was too busy staring at Brooks...oh well. Grades don't matter anyways."

    jump walkDay1
    
    return
    
label class2Day1Trent:

    e "Hi Trent..."
    
    trent "Hi!"
    
    e "So quick question before class, I've heard you are a racist. Is this true?"
    
    trent "Oh class is starting. Sorry, I'm going to pay attention."
    
    "Trent stares eagerly at the front, even though the teacher hasn't arrived yet."
    
    e "...right. I'll try again later."

    jump walkDay1
    
    return
    
label sleepDay1Class2:

    nar "Ah, no dreams, that sucks. Come on and show me the end."

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
    
    caleb "Oh yeah. I'm just recharging my stamina up here."
    
    e "...huh?"
    nar "Am I about to be murdered?"
    e "Alright, well if you are fine then it's no problem."
    
    caleb "Oh, I'm fine. Mind if I join you? *hair flip*"
    
    e "...sure."
    nar "I hear that it's best to appease the robbers and follow their commands"
    
    caleb "Alright, well turn away. Me getting down from this tree will be to scandalous for you ;)"
    
    e"...right"
    nar "You turn around and immediately feel a tap on your shoulder. Strange."
    
    caleb "Alright, let's go."
    
    show blackscreen with Dissolve(.5)

    nar "You two walk for awhile in complete silence, until you finally reach the end."
    
    show fountain with Dissolve(.5)

    caleb "Well, it was great walking with you, see you around!"
    
    jump dinnerDay1
    
    return
    
label sleepDay1Walk:

    nar "Why AM I NOT DREAMING!"

    menu:
        "I'm hungry...I should go to dinner":
            jump dinnerDay1
            
        "MORE":
            jump sleepDay1Dinner
            
    return
    
label dinnerDay1:

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

    e "Oh Mark, I LOVE FKC!"
    
    mark "I know you do baby. After all, who doesn't love some fried chicken?"
    
    show fkc with Dissolve(.5)

    e "Let's eat!"
    
    nar "OM NOM NOM NOm NOM NOM NOM NOM NOM NOM!"
    
    e "Oh yeah! We have things to do tonight. Let's head back Mark."
    
    mark "Oh yeah, let's blast outta here baby girl."

    menu:
        "Watch the scary movie":
            jump movieDay1
        
        "Go to bed":
            jump sleepDay1Night
            
    return
    
label dinnerDay1BCJ:

    show dcLine with Dissolve(.5)

    e "Wow, I wonder what they have today!"
    
    cody "Probably nothing good, it is the DC after all."
    
    e "Now Cody, the DC isn't THAT bad."
    
    brooks "Yes it is."
    
    e "Oh yeah, you're right Brooks...it is unbearable after all."
    
    show dcTables with Dissolve(.5)

    john "...and that's why I agree with Kim Jong Un."
    
    e "Haha! Nice!"
    
    brooks"Oh shoot, look at the time! We really have to go. We were gonna watch a scary movie. You joining?"
    
    e "Ehhhh..."

    menu:
        "Watch the scary movie":
            e "Sure!"
            jump movieDay1
        
        "Go to bed":
            e "Nah, I'm tired. Thanks though"
            jump sleepDay1Night
            
    return
    
label dinnerDay1CT:

    show dcTables with Dissolve(.5)

    "They say nothing, but gnaw on their food and stare at you."
    
    "You promptly leave."

    menu:
        "Watch the scary movie":
            jump movieDay1
        
        "Go to bed":
            jump sleepDay1Night
            
    return
    
label sleepDay1Dinner:

    jump dream4
    
    return
    
label dream4:

    john "I'm elmo, and I'm not your friend!"
    
    john "Come here so I can gut you like a fish!"
    
    e "AHHHHH"
    
    "ALARM" "BEEP, BEEP, BEEP"
    
    e "WHAT THE FRICK WAS THAT!"
    e "THAT DREAM SUCKED!"

    menu:
        "Watch the scary movie":
            jump movieDay1
        
        "Go to bed":
            e "What ever, might as well sleep through the night then."
            jump sleepDay1Night
            
    return
    
label movieDay1:

    show beckerTheater with Dissolve(.5)

    e "It's kinda cold down here."

    brooks "Do you want my blanket? I'm not using it."

    e "Sure, thanks Brooks!"

    show blackscreen with Dissolve(.5)

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
            nar "You cling to Brooks, and he seems happy. You enjoy the rest of the movie together."
            jump movieDay1Cling
        
        "Cling to Caleb":
            $ clingee = "Caleb"
            nar "You cling to Caleb, and he seems happy. You enjoy the rest of the movie together."
            jump movieDay1Cling
            
        "Cling to Cody":
            $ clingee = "Cody"
            nar "You cling to Cody, and he seems happy. You enjoy the rest of the movie together."
            jump movieDay1Cling
            
        "Cling to Trent":
            $ clingee = "Trent"
            nar "You cling to Trent, and he seems happy. You enjoy the rest of the movie together."
            jump movieDay1Cling
            
        "Cling to Mark":
            $ clingee = "Mark"
            nar "You cling to Mark, and he seems happy. You enjoy the rest of the movie together."
            jump movieDay1Cling
            
        "Cling to John":
            $ clingee = "John"
            nar "You cling to John, and he seems happy. You enjoy the rest of the movie together."
            jump movieDay1Cling
        
    return
    
label movieDay1Cling:

    show blackscreen with Dissolve(.5)

    nar "What a long day, I suppose it is time for bed."

    jump sleepDay1Night
    
    return
    
label sleepDay1Night:

    jump dream5
    
    return
    
label dream5:

    nar "Ah, where am I? This doesn't look like a normal restaurant."
    
    nar "I'm just a salisbury steak looking to be eaten."
    
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
    
    brooks "Oh hey. What are you doing up here? You aren't supposed to be on our floor."
    nar "No way. Brooks, fresh out of the shower, and shirtless! I can't believe this!"
    #NEED SHIRTLESS BROOKS
    e "Oh yeah, I was just, you know, dropping your blanket off."
    brooks "Alright then. Thank you, now you better go before I have to fine you."
    e "Cya later"
    nar "Oh my gosh I can't believe that just happened! Now I can think about that while I do all of my homework."

    jump homeworkDay2
    
    return
    
label homeworkDay2:

    show dormDorm with Dissolve(.5)
    nar "hmmm...the square root of twenty five x squared boils down to..."
    nar "Brooks!"
    nar "Wait no, I can't get distracted, its five x."
    nar "..."
    nar "Ok, finally done! Oh, I guess I'm eating a late lunch today. That took longer than it should have because I kept thinking of Brooks..."

    jump lunchDay2
    
    return
    
label lunchDay2:

    show dcOutside Dissolve(.5)

    nar "I doubt anyone will be here to eat with me this late."

    show dcLine Dissolve(.5)

    brooks "Hey, isn't it a little ate to eat lunch?"
    e "No way, you guys are all here?"
    cody "Yeah, lost track of time. We all have different things to do, but feel free to join whoever."

    menu:
        "Lunch with Brooks":
            "I'll go with Brooks!"
            jump lunchDay2Brooks
        
        "Lunch with Caleb":
            "I'll go with Caleb!"
            jump lunchDay2Caleb
        
        "Lunch with Cody":
            "I'll go with Cody!"
            jump lunchDay2Cody
        
        "Lunch with Trent":
            "I'll go with Trent!"
            jump lunchDay2Trent
        
        "FKC with Mark":
            "I'll go with Mark!"
            jump FKCDay2Lunch
        
        "Lunch with John":
            "I'll go with John!"
            jump lunchDay2John
            
    return
    
label lunchDay2Brooks:

    e "Hey Brooks."
    
    brooks "Oh, hey there. You joining me for lunch?"
    
    e "Yeah, if that's ok with you."
    
    brooks "Of course, that's no problem."
    
    e "Great!"
    
    show dcTables with Dissolve(.5)

    "..."
    
    brooks "...and THAT'S why all the Europeans...er...yeah"
    
    e "...ok"
    
    brooks "I gotta go, cya later!"
    
    e "Alright, bye."
    
    nar "I'll go hang out with Mark now."

    jump afternoonDay2Mark
    
    return
    
label lunchDay2Caleb:

    e "Hey Caleb, what's up?"
    
    caleb "Oh just getting some lunch."
    
    e "Mind if I join you?"
    
    caleb "Sure."
    
    e "Man I can't believe we can't find a table!"
    
    caleb "That's fine, my head hurts anyways. I'm gonna go back to my dark, quiet, drippy cave."
    
    e "Well alright then."
    
    show dcTables with Dissolve(.5)

    nar "Guess I'll eat alone since Cynthia left."
    
    jump afternoonDay2Brooks
    
    return
    
label lunchDay2Cody:

    e "Hey Cody, Mr. CMC."
    
    cody "Hi."
    
    e "Can I eat dinner with you?"
    
    cody "I mean it's lunch, but ok."

    show dcTables with Dissolve(.5)
    
    cody "...and that's why being a CMC is great."
    
    e "Man, I don't know any other floor that paints for floor worship!"
    
    cody "Alright, cya later. I gotta go."
    
    e "Cya!"
    
    jump afternoonDay2Brooks
    
    return
    
label lunchDay2Trent:

    show dcTables with Dissolve(.5)

    "..."
    
    trent "And THAT is why we aren't allowed to date our students."
    
    e "I mean yeah, I feel like that was common sense and really didn't need a scientific study?"
    
    trent "Anyways, we are just talking."
    
    e "Yeah, let's go."
    
    jump afternoonDay2Brooks
    
    return
    
label FKCDay2Lunch:

    show fkc with Dissolve(.5)

    "..."

    e "I like your truck by the way, and I can't believe you listen to Rob Zombie!"
    
    mark "I love listening to him while I shuck 10 billion ears of corn!"
    
    e "You really like your farming and FKC don't you..."
    
    mark "Yeah, it's my life...well I have some homework so let's get back now."
    
    nar "Alright, time to go back and hang out with Brooks."
    
    jump afternoonDay2Brooks
    
    return
    
label lunchDay2John:

    show dcTables with Dissolve(.5)

    "..."

    e "I love your socks John!"
    
    john "Thanks, I figured if I have to wear them I might as well pick some good ones."
    
    e "Those are the best Narwhal socks I have EVER seen, trust me."
    
    john "Thanks thanks, alright. I gotta go to the MCA now so I'll see you later!"
    
    e "Bye John!"
    
    nar "Alright, time to go back and hang out with Brooks."
    
    jump afternoonDay2Brooks
    
    return
    
label afternoonDay2Mark:

    e "Yo Mark, wanna go do something?"
    
    mark "Sure! Let's go somewhere. Anywhere you had in mind?"
    
    e "I was thinking we should go to FKC in Kentucky."
    
    mark "Hey, sounds good to me. Meet me in my truck in five."
    
    e "Man, the mall is so much fun. I missed doing this because I don't have a vehicle on campus."
    
    mark "Yeah, too bad we couldn't make it to Kentucky. Sorry about not having gas and being broke."
    
    e "All good, this place is great and the FKC is fine here!"
    
    mark "I spent all my money on FKC, so that's why!"
    
    e "Wow Mark, I'm gonna miss you when you graduate."
    
    mark "Yeah, alright. Let's get walking around the mall before we leave."
    
    e "Yessir."

    jump dinnerDay2
    
    return
    
label afternoonDay2Brooks:

    show dcOutside with Dissolve(.5)

    e "Hi Brooks! What do you wanna do?"
    
    brooks "Oh hey. I was thinking we could just chill in the lounge or somewhere quiet."
    
    e "Yeah, lets do that."

    show blackscreen with Dissolve(.5)
    
    "..."

    show lounge with Dissolve(.5)
    
    e "So that's why you went to Wright 2 out of all the other choices."
    
    brooks "Yep, and I'm glad I did! It is simply the best floor...oh! Look at the time."
    
    e "Dinner already? Wow that time flew by."
    
    brooks "Yeah, let's go together."
    
    e "Ok!"

    jump dinnerDay2
    
    return
    
label dinnerDay2:

    show dcOutside with Dissolve(.5)

    e "Oh hey! You going to dinner?"
    
    caleb "Yeah we were just go..."
    
    trent "Wanna sit with us?"

    menu:
        "Dinner with Brooks, John and Cody":
            e "No, sorry, I already told these guys I would eat with them! Thanks though."
            jump dinnerDay2BJC
        
        "Dinner with Caleb and Trent":
            e "Sure!"
            
            jump dinnerDay2CTC
            
        "FKC with Mark":
            e "I'm actually gonna go find Mark and go with him!"
            
            caleb "Uhhhh...alrighty then..."
            jump FKCDay2Dinner
            
    return
    
label dinnerDay2BJC:

    show blackscreen with Dissolve(.5)

    "..."
    
    show dcTables with Dissolve(.5)

    brooks "Yeah, we have a trebs concert next week if you would like to join!"
    
    e "I think I'll pass on this one, thank you though."
    
    cody "What's the problem, you're only the wrong gender!"
    
    e "Exaaactly."
    
    john "Alright, let's bust this DC joint and get outta here."

    menu:
        "Evening stroll with Brooks":
            e "Hey Brooks, wanna go on a walk?"
            jump walkDay2
            
        "Evening stroll with John":
            e "Hey John, wanna go on a walk?"
            jump walkDay2
            
        "Evening stroll with Cody":
            e "Hey Cody, wanna go on a walk?"
            jump walkDay2
            
    return
    
label dinnerDay2CTC:

    show blackscreen with Dissolve(.5)

    "..."

    show dcTables with Dissolve(.5)
    
    caleb "Yeah, we have a Smash Bros. Tournament next week if you would like to join!"
    
    e "I might come watch, but I don't play. Besides, melee is more interesting to watch so I'd probably play that if anything."
    
    trent "Alright cool...hey."
    
    e "W-what?? *Blushes*"
    
    trent "We're just talking."

    menu:
        "Evening stroll with Trent":
            $ walker = "Trent"
            e "Hey Trent, wanna go on a walk?"
            jump walkDay2
            
        "Evening stroll with Caleb":
            $ walker = "Caleb"
            e "Hey Caleb, wanna go on a walk?"
            jump walkDay2
            
        "Evening stroll with Cole":
            $ walker = "Cole"
            e "Hey Cole, wanna go on a walk?"
            jump walkDay2
            
    return
    
label FKCDay2Dinner:

    show fkc with Dissolve(.5)

    "MUNCH MUNCH"
    
    mark "I LOVE FKC"
    
    e "MMMMMM"
    
    e "Hey Mark, let's go on a walk together."
    
    mark "OK"
    
    $ walker = "Mark"

    jump walkDay2
    
    return
   
label walkDay2:

    show fountain with Dissolve(.5)

    nar "Why isn't he saying anything?"
    
    "You walk in complete silence the entire way, and arrive at the lounge at the very end of your walk."

    jump smashBros
    
    return
    
label smashBros:

    show lounge with Dissolve(.5)

    caleb "Alright, practicing in some big free for alls! The best way to warm up."
    
    trent "We have to put items and final smash on for the tournament practice."
    
    john "Looks good to me, pick jungle japes and lets get playing."
    
    "..."
    
    "clack click clack"
    
    "..."
    
    john "Yeah, I won the most!"
    
    trent "Great job!"
    
    caleb "Good games!"
    
    john "I think we are ready, let's head to bed."
    
    trent "Night everyone."
    
    e "Night."

    jump sleepDay2Night
    
    return
    
label sleepDay2Night:

    show dormDorm with Dissolve(.5)

    nar "Oh, Church is tomorrow...I wonder who I should ask to go with me"
    
    nar "I'll decide tomorrow who to ask to Church with."

    nar "Sigh, I'm so tired. Off to bed I go."

    jump dream6
    
    return
    
label dream6:

    nar "Who should I go with to Church tomorrow..."
    
    nar "I mean, it has to be someone I like, it's basically asking them out."
    
    nar "Everything I've done comes down to this."
    
    nar "This is so important."

    nar "I can't wait."
    
    "ALARM" "BEEP BEEP BEEP"
    
    nar "Well, for once my dream was accurate."
    
    nar "Here I go."

    jump finalScene
    
    return
    
label finalScene:

    e "Hey guys."
    
    brooks "Hey, who were you thinking of going to Church with?"
    
    e "Uhhh, good question. This is very important, so give me a second to think..."

    menu:
        "Church with Brooks":
            e "Brooks, I choose you!"
            
            brooks "Alright, let's go together then!"
            jump church
            
        "Church with Cody":
            e "Cody, let's go together."
            
            cody "Ok."
            jump church
            
        "Church with John":
            e "John, John, let's get going!"
            
            john "Alright!"
            jump church
            
        "Church with Mark":
            e "Mark, let's go and get some chicken afterwards!"
            
            mark "Sounds like a plan to me!"
            jump church
            
        "Church with Caleb":
            e "Caleb, let's go."
            
            caleb "Heck yeah!"
            jump church
            
        "Church with Trent":
            e "Pineapple sauce!"
            
            trent "And pancakes!"
            jump church
            
    return
    
label church:

    "You attend Church with him and have a great time, and this is just the beginning of your future together!"

    return
            
        
            
        
            
            

        
        
