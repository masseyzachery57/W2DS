# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define nar = Character(what_italic=True)
define e = Character("Eileen")
image eileen idle = Image("images/Miki_Casual_Smile_1_73.png")
image eileen idle2 = Image("images/Miki_Casual_Open_Blush_73.png")
image bg1 = Image("/images/lake/morning.jpg")
image blackscreen = Image("/images/blackscreen.jpg")
image defaultroom = Image("/images/apartment/day.jpg")

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

    show defaultroom with Dissolve(.5)
    play music "audio/default.mp3"

    nar "I guess I have to get up eventually."
    nar "Now where did I put my ID..."

    menu:
        "Breakfast with Brooks"
            jump breakfastDay1Brooks
            
        "Breakfast with Cody"
            jump breakfastDay1Cody
            
    return

label breakfastDay1Brooks:

    jump class1Day1

    return
    
label breakfastDay1Cody:

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
    e "Me"
    
    menu:
        "Go to first class?"
            jump class1Day1
            
        "Just a little more sleep..."
            jump sleepDay1Class1

    return
    
label class1Day1

    menu:
        "Sit with John"
            jump class1Day1John
            
        "Sit with Brooks"
            jump class1Day1Brooks
            
        "Sit with both"
            jump class1Day1Both

    return
    
label sleepDay1Class1:

    jump dream2

    return
    
label dream2:

    menu:
        "Go to lunch"
            jump lunchDay1Alone
            
        "Just a couple more minutes..."
            jump sleepDay1Lunch

    return
    
label class1Day1John:

    menu:
        "Lunch with John"
            jump lunchDay1John
            
        "Lunch alone"
            jump lunchDay1Alone
    
    return
    
label class1Day1Brooks:

    menu:
        "Lunch with Mark"
            jump lunchDay1Mark
            
        "Lunch alone"
            jump lunchDay1Alone

    return
    
label class1Day1Both:

    menu:
        "Lunch alone"
            jump lunchDay1Alone

    return

label lunchDay1Alone:

    jump class2Day1

    return

label lunchDay1Mark:

    jump class2Day1
    
    return
    
label lunchDay1John:

    jump class2Day1
    
    return

label sleepDay1Lunch:

    jump dream3
    
    return
    
label dream3:

    menu:
        "Go to second class"
            jump class2Day1
            
        "So tired..."
            jump sleepDay1Class2

    return

label class2Day1:

    menu:
        "Sit with Cody"
            jump class2Day1Cody
        
        "Sit with Brooks"
            jump class2Day1Brooks
            
        "Sit with Trent"
            jump class2Day1Trent
            
    return

label class2Day1Cody:

    jump walkDay1
    
    return
    
label class2Day1Brooks:

    jump walkDay1
    
    return
    
label class2Day1Trent:

    jump walkDay1
    
    return
    
label sleepDay1Class2:

    menu:
        "I should take a walk through the woods"
            jump walkDay1
            
        "I want to dream more"
            jump sleepDay1Walk
            
    return
    
label walkDay1:
    
    jump dinnerDay1
    
    return
    
label sleepDay1Walk:

    menu:
        "I'm hungry...I should go to dinner"
            jump dinnerDay1
            
        "MORE"
            jump sleepDay1Dinner
            
    return
    
label dinnerDay1:

    menu:
        "FKC with Mark"
            jump kfcDay1
            
        "Dinner with Brooks, Cody and John"
            jump dinnerDay1BCJ
            
        "Dinner with Caleb and Trent"
            jump dinnerDay1CT
            
    return
    
label kfcDay1:

    menu:
        "Watch the scary movie"
            jump movieDay1
        
        "Go to bed"
            jump sleepDay1Night
            
    return
    
label dinnerDay1BCJ:

    menu:
        "Watch the scary movie"
            jump movieDay1
        
        "Go to bed"
            jump sleepDay1Night
            
    return
    
label dinnerDay1CT:

    menu:
        "Watch the scary movie"
            jump movieDay1
        
        "Go to bed"
            jump sleepDay1Night
            
    return
    
label sleepDay1Dinner:

    jump dream4
    
    return
    
label dream4

    menu:
        "Watch the scary movie"
            jump movieDay1
        
        "Go to bed"
            jump sleepDay1Night
            
    return
    
label movieDay1:

    menu:
        "Cling to Brooks"
            jump movieDay1Cling
        
        "Cling to Caleb"
            jump movieDay1Cling
            
        "Cling to Cody"
            jump movieDay1Cling
            
        "Cling to Trent"
            jump movieDay1Cling
            
        "Cling to Mark"
            jump movieDay1Cling
            
        "Cling to John"
            jump movieDay1Cling
        
    return
    
label movieDay1Cling:

    jump sleepDay1Night
    
    return
    
label sleepDay1Night:

    jump dream5
    
    return
    
label dream5:

    jump breakfastDay2
    
    return
    
label breakfastDay2:

    jump blanketReturn
    
    return
    
label blanketReturn:

    jump homeworkDay2
    
    return
    
label homeworkDay2:

    jump lunchDay2
    
    return
    
label lunchDay2:

    menu:
        "Lunch with Brooks"
            jump lunchDay2Brooks
        
        "Lunch with Caleb"
            jump lunchDay2Caleb
        
        "Lunch with Cody"
            jump lunchDay2Cody
        
        "Lunch with Trent"
            jump lunchDay2Trent
        
        "FKC with Mark"
            jump kfcDay2Lunch
        
        "Lunch with John"
            jump lunchDay2John
            
    return
    
label lunchDay2Brooks:

    jump afternoonDay2Mark
    
    return
    
label lunchDay2Caleb:
    
    jump afternoonDay2Brooks
    
    return
    
label lunchDay2Cody:
    
    jump afternoonDay2Brooks
    
    return
    
label lunchDay2Trent:
    
    jump afternoonDay2Brooks
    
    return
    
label kfcDay2Lunch:
    
    jump afternoonDay2Brooks
    
    return
    
label lunchDay2John:
    
    jump afternoonDay2Brooks
    
    return
    
label afternoonDay2Mark:

    jump dinnerDay2
    
    return
    
label afternoonDay2Brooks:

    jump dinnerDay2
    
    return
    
label dinnerDay2

    menu:
        "Dinner with Brooks, John and Cody"
            label dinnerDay2BJC
        
        "Dinner with Caleb, Trent and Cole"
            label dinnerDay2CTC
            
        "FKC with Mark"
            label kfcDay2Dinner
            
    return
    
label dinnerDay2BJC:

    menu:
        "Evening stroll with Brooks"
            jump walkDay2
            
        "Evening stroll with John"
            jump walkDay2
            
        "Evening stroll with Cody"
            jump walkDay2
            
    return
    
label dinnerDay2CTC:

    menu:
        "Evening stroll with Trent"
            jump walkDay2
            
        "Evening stroll with Caleb"
            jump walkDay2
            
        "Evening stroll with Cole"
            jump walkDay2
            
    return
    
label kfcDay2Dinner:

    jump walkDay2
    
    return
   
label walkDay2:

    jump smashBros
    
    return
    
label smashBros:

    jump sleepDay2Night
    
    return
    
label sleepDay2Night:

    jump dream6
    
    return
    
label dream6:

    jump finalScene
    
    return
    
label finalScene:

    menu:
        "Church with Brooks"
            jump church
            
        "Church with Cody"
            jump church
            
        "Church with John"
            jump church
            
        "Church with Mark"
            jump church
            
        "Church with Caleb"
            jump church
            
        "Church with Trent"
            jump church
            
        "Church with Caleb"
            jump church
            
    return
    
label church:

    return
            
        
            
        
            
            

        
        
