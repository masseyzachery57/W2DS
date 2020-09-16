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
            jump sleepDay1_no
    
        "Just a few more minutes...":
            jump sleepDay1_yes
    
label sleepDay1_no:

    $ sleepDay1_flag = False

    show defaultroom with Dissolve(.5)
    play music "audio/default.mp3"

    nar "I guess I have to get up eventually."
    nar "Now where did I put my ID..."

    jump sleepDay1_done

label sleepDay1_yes:
    $ sleepDay1_flag = True

    nar "Five more minutes couldn't hurt anything..."

    jump dream

label dream:
    scene bg room
    show bg1
    show eileen idle at top 
    play music "audio/love.mp3"

    e "Welcome back dear!"
    e "Would you like dinner? {p}A swim in the lake? {p}Or perhaps..."

    show eileen idle2 at top
    e "Me"

    return
label sleepDay1_done:
    return
