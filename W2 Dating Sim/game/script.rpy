# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define nar = Character(what_italic=True)
define e = Character("Eileen")
image eileen idle = Image("images/Miki_Casual_Smile_1_73.png")
image eileen idle2 = Image("images/Miki_Casual_Open_Blush_73.png")
image bg1 = Image("/images/lake/morning.jpg")
#image overlay = Image("/images/badend2-1.png")
transform overlay:
    alpha 0.1
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    play music "audio/default.mp3" fadeout 1.0
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
    "ALARM" "BEEP, BEEP, BEEP"
    "THUMP"
    nar "Ugh, another day of school. Better get up so I can go get some breakfast."
    
    jump day1_breakfast
    
    return
    
label day1_breakfast:

    "test"
    
    
    

    return
