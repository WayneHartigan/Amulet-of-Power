
label splashscreen:
    scene black
    with Pause(1)

    show text "Developed by Shark Tank Studios" with dissolve
    with Pause(2)
    
    hide text with dissolve
    with Pause(1)
    
    return

label start:
    
    define m = Character(_('Mage'), color="#c8ffc8")
    
    define v = Character(_('Volmar'), color="#c8ffc8")
    
    define gk = Character(_('Goblin King'), color="#c8ffc8")
    
    define g = Character(_('Goblin'), color="c8ffc8")
    
    define k = Character(_('King'), color="c8ffc8") 
    
label prologueone:
    
    scene black
    
    show text "The story so far." with dissolve
    with Pause(2)
    
    hide text with dissolve
    with Pause(1)
    
label prologuetwo:
    
    scene black

    show text "It is told that the Amulet Of Power holds a secret and sacred power. There are many tales and folklore about the amulets power, yet nobody knows for sure what mysterious powers this amulet holds. The Battle Mages of Ivoria lead by Agnar White Beard are sworn protectors of the amulet as they state the power of the amulet is too strong for any race in the world of Efamar." with dissolve
    with Pause(17)

    hide text with dissolve
    with Pause(1)
    
label prologuethree:
    
    scene black

    show text "For the last 50 years an all out battle has been raging the lands of Efamar. The Knights Of The Grey Order stated that the power of the amulet shouldn’t go to waste and its power should be used for military dominance and in turn peace. The Grey Orders King, Cydare The Great, demanded the handing over of the amulet to the Grey Order. When the Battle Mages refused, the Grey Order attacked the Mages beginning a war that to this day rages on. There has been many casualties on both sides of the war yet neither side is willing to give up for their ideals and the amulet." with dissolve
    with Pause(17)

    hide text with dissolve
    with Pause(1)
    
label prologuefour:
    
    scene black
    
    show text "A secret special forces group of spies were sent out by the Grey Order to retrieve the amulet from the mages military camp. Under the blanket of the night sky the spies infiltrated the camp killing Agnar and retrieving the amulet without raising an alarm." with dissolve
    with Pause(17)

    hide text with dissolve
    with Pause(1)
    
label prologuefive:
    
    scene black
    
    show text "All tides of war had turned on the success mission of the spies until they got ambushed by a group of Goblins, the surprising ambush alongside the shear number of the Goblins wiped out the party and stealing the precious cargo on board." with dissolve
    with Pause(17)

    hide text with dissolve
    with Pause(1)
    
label prologuesix:
    
    scene black
    
    show text "You play a young warrior hired by the Grey Order to retrieve the amulet from the goblins. The Grey Order has heard about your skills in close combat and the ability to move undetected. With the retrieval of the amulet many riches are promised, yet will you choose riches. Or the amulet? The choices are yours, the story is not yet written.Pathe your own path on this adventure." with dissolve
    with Pause(17)

    hide text with dissolve
    with Pause(1)
    
label prologueseven:
    
    scene black
    
    show text "Pathe your own path on this adventure." with dissolve
    with Pause(3)
    
    hide text with dissolve
    with Pause(1)

label name:
    scene black
    
    $ player_name = renpy.input("What is your name?")


label scene1:     
## Code for placing player names in textboxes %(player_name)s

    scene opening

    "After weeks of tracking, %(player_name)s finally caught up with the stolen cargo cart. "

    "The cart is protected by well equipped goblin warriors."

    " Analysing the situation %(player_name)s decides he has two options"
    
    menu:
        
        "Attack the Goblin delivering party":
            jump scene2
    
        "Wait till nightfall when the goblins are resting.":
            jump scene3

    
label scene2:
    
    define choiceone = "Attack the Goblin delivering party"
    
    scene death
    
    "Your stealth skills prove valuable as you managed to attack the party undetected."
    
    "After killing a large number of the goblin warriors, they finally club you down, killing %(player_name)s"
    
    return

label scene3:

    define choiceone = "Wait till nightfall when the goblins are resting."
    
    scene opening
    "%(player_name)s continues to follow the Goblins until they stop at a cave on the outskirts of the forest. "
    
    "The Goblins set up camp for the night as the sun slowly creeps behind the mountains."
    
    scene cavenight
    
    "A Ogre Guard emerges from the cave and stands guard"
    
    "Human slaves are seen shackled to steel ball and chain and forced to chop down trees by the goblins."
    
    "The delivering party enter the cave with the cargo. %(player_name)s decides he has two options. "
    
    
    menu:
    
        "He could use magical fire bombs to bombard the Goblin camp, killing the goblins but also the slaves, risking the destruction of the cargo.":
            jump scene4
    
        "Under the cloaks of the night sneak into the cave.":
            jump scene5
    
    
label scene4:
    
    scene scene4
    
    define choicetwo = "He could use magical fire bombs to bombard the Goblin camp, killing the goblins but also the slaves, risking the destruction of the cargo."
    
    "%(player_name)s bombs the camp killing all the goblins, but also the slaves, while the ogre protector is set on fire he swings his club knocking %(player_name)s out unconscious before the he collapses and dies."
    
    jump scene8
    
    
    
    
label scene5:
    
    scene cavenight
    define choicetwo = "Under the cloaks of the night sneak into the cave."
    
    "%(player_name)s approaches the camp walking along the tree line of the forest."
    
    "%(player_name)s waits for a perfect time window."
    
    "When the Ogre guard gets distracted by a running away slave %(player_name)s sneaks into the cave undetected. "
    
    scene cavetent
    
    "The cave is dark and low lit, the cave walls are grimey and wet, disgusting living conditions for anyone but a goblin."
    
    
    menu:
        "Save the slaves":
            jump scene6
        
        "Focus on the mission":
            jump scene7
    
    
label scene6:
    
    scene cavetent
    define choicethree = "Save the slaves"
    
    "%(player_name)s see's a large cage of human slaves, the goblin guard is asleep."
    
    "%(player_name)s notices the keys to the cage are dangling from the goblins neck on a wire that seems to be creating a necklace."
    
    "%(player_name)s approaches the goblin and silent starts lifting the necklace."
    
    "Undetected you take the necklace off. A goblin warrior enters the room shouting at you."
    
    "The sleepy goblin guard wakes up from the noise and tackles you, picking up a rock and knocking you out."
    
    scene death 
    
    return 
    
label scene7:
    
    scene scene7
    define choicethree = "Focus on the mission"
    "%(player_name)s disregards the slaves and proceeds into the next section of the cave."
    
    "Inside,  find a green tent, surprisingly unguarded you decide to enter it. Inside you find the amulet."
    
    "%(player_name)s lifts the amulet and places it into his pouch."
    
    "Swiftly %(player_name)s takes out his dagger and slits the throat of a goblin sneaking up on him, leaps over the lifeless body of the goblin round house kicking the goblin behind him, attacking him in the face."
    
    "%(player_name)s proceeds to run forward knowing he’s been discovered"
    
    "Running out of the cave, now in the open, %(player_name)s realises he has run into another problem"
    
    jump scene8
    
label scene8:
    
    scene orbontable
    
    "You wake up, A mysterious hooded figure speaks with a faint monotone voice. %(player_name)s opens his eyes dazed and confused."
    
    show spritemagehappy at left
    
    show spriteplayeridle at right
    
    m "You got a serious knock to the head friend! You’re lucky I got to you, or you would be the goblins next feast, They love human meat."
    
    "You Notice the elephant sigil, this man is one of the Knights of Ivoria."
                                                                              
    menu:
        "Thank the stranger":
            jump scene9
            
        "Kill the Ivorian scum":
            jump scene10
            

label scene9:
    
    scene orbontable
    define choicefour = "Thank the stranger"
    
    show spritemageidle at left
    
    show spriteplayerhappy at right
    
    (player_name) "Thank you for your bravery, I can’t remember much, my head is pounding. Did you come across an Amulet with a ruby jewel."
    
    hide spritemageidle
    
    show spritemageinterested at left
    
    m "Ahh the Amulet of Power, strange our paths have crossed. No unfortunately i had to teleport us out of there as soon as i could get a hold of you."
    
    m "My power is not great enough to fight a goblin troop of that size."
    
    hide spritemageinterested
    
    show spritemagehappy at left
    
    v "Let me introduce myself, My name is Volmar"
    
    v "I’m a battle mage from the land of Ivoria. We are the true protectors of the amulet."
    
    v "I've been Following my dark orb which will lead me to the amulet for some weeks."
    
    v "I was hoping to track down the whereabouts of the amulet and call for backup from the Mages."
    
    v "The Battle Mages of Ivoria have spent generations researching and understanding the amulet."
    
    v "The legend says the chosen one can wear the amulet and receive powers unimaginable to mear humans. If an unworthy person wears the amulet, There would be grave consequences."
    
    v "You seem well able to handle yourself in a fight after you get this healing potion into you, will you help me on my quest?"
    
    menu:
        "Sorry, not interested":
            jump scene11
        
        "Yes, you saved me so the least i can do is help you":
            jump scene12
            
label scene10:
    
    scene orbontable
    define choicefour = "Kill the Ivorian scum"
    
    show spritemagemagic at left
    
    show spriteplayerhostile at right
    
    
    (player_name) "I know who you are Ivorian, you cannot fool me."
    
    hide spritemagemagic

    scene death
    "The mage flees and leaves behind a toxic gas which was too strong for you to escape."
     
    menu:
        "Would you like to retry this scene?":
            jump scene8
         
        "Restart Game":
            jump scene1
            
        "Quit":
            return
    
label scene11:
    scene orbontable
    define choicefive = "Sorry, not interested"
    
    show spritemageidle at left
    
    show spriteplayerangry at right
    
    (player_name) "Sorry, mage, I don’t have an interest in your tale."
    
    (player_name) "I’m a sword for hire and I have my own mission to track these goblins and retrieve the stolen loot"
    
    (player_name) "As I see our paths have crossed and we have the same mission, you can help me on my quest, or we can part ways."
    
    (player_name) "Being short with you is not my desire Mage, but this mishap has set me back and time is money my friend."
    
label scene12:
    
    scene orbontable
    define choicefive = "Yes, you saved me so the least i can do is help you"
    
    show spritemageidle at left
    
    show spriteplayerdetermined at right
    
    (player_name) "The goblins have it, we must find them now, and retrieve the amulet before they use it for the destruction of mankind"
    
    (player_name) "If the goblins can use the power of the amulet this can potentially cause a bigger mess than we already have."
    
    (player_name) "Please mage, I owe you my life, but let me track these scum and stop a disaster."
    
    hide spritemageidle
    
    hide spriteplayerdetermined
    
    show spritemageinterested at left
    
    show spriteplayeridle at right
    
    v "Well %(player_name)s, I believe our paths have really crossed for a reason. I will help you find the amulet."
    
    hide spritemageinterested
    
    show spritemagemagic at left
    
    "Volmar whispers in a foreign language you cannot comprehend"
    
    scene orbofftable
    
    show spriteplayeridle at right
    
    hide spritemagemagic
    
    show spritemageorb at left
    
    v "Take this orb a light will shine the direction of the amulet, follow the light and you will soon find the amulet."
    
    v "I have placed a tracking spell on the orb as soon as the orb is within close range of the amulet it will send me a signal."
    
    hide spriteplayeridle 
    
    hide spritemageorb
    
    show spritemageidle at left
    
    show spriteplayerorb at right
    
    (player_name) "Thank you mage for all you have done."
    
   
label scene13:

    scene start1
    
    "After days of traveling, %(player_name)s finally finds the goblin lair."
    
    "%(player_name)s enters through as it is unguarded, as he get further in the cave he can hear the sounds for a giant amount of goblins"
    
    scene start2
    
    "He enters a giant opening and below he sees a goblin celebration."
    
    scene goblinkinghappy 

    gk "We’ve done it! Let us celebrate tonight, and tomorrow we get our revenge and slaughter the humans"
    
    menu:
        "Jump down and attack":
            jump scene14
        
        "Warn the Goblin King of the power the amulet holds":
            jump scene15
            
        "Stay in the shadows and try to move closer":
            jump scene16
            

label scene14:

    scene fightlair
    define choicesix = "Jump down and attack"
        
    "%(player_name)s fights well, due to the numbers of goblins protecting the amulet and their king, %(player_name)s get’s struck down and dies."
        
    scene death
    
    "Bad choice"
    
    return
    
    
label scene15:

    scene playerchoice
    define choicesix = "Warn the Goblin King of the power the amulet holds"
    
    
    
    (player_name) "STOP GOBLIN KING!!!!! If you wear the amulet, it will kill you!"
    
    (player_name) "The amulet won’t deliver you the promised power unless you are the chosen one."
    
    (player_name) "Hear my plea and don’t wear it!"
    
    scene fool
    
    gk "Petty human, im the goblin king the i fought to have this position, i am the chosen one."
    
    gk "Your lies won’t stop me from the power I deserve. Is this your masterful plan to stop me?"
    
    gk "HAH! No HUMAN! I SHALL CRUSH YOU WITH THE AMULETS POWER, I SHALL BURN YOUR KIND WITH THE FIRES OF HELL"
    
    gk "NOW IS THE TIME MY MINIONS TO END THIS WAR!!!"
    
    jump scene19
    


label scene16:
    
    define choicesix = "Stay in the shadows and try to move closer"
    
    (player_name) "It wouldn’t be smart to go in detected."
    
    (player_name) "I’ll use the shadows to my advantage."
    
    scene advantagepoint
    
    gk "Good job my followers, with this successful attack on The Grey Order we have finally retrieved the amulet"
    
    gk "Bring me the amulet, it’s time for me to wear it, gain its power and become the god that I was destined to be."
    
    
    menu:
        "Attack Now":
            jump scene17
        
        "See how this plays out":
            jump scene18


label scene17:

    scene fightlair
    define choiceseven = "Attack Now"
    
    "%(player_name)s attacks the goblins, killing many, yet the goblin king is left untouched due to the sheer number of goblins protecting the king."
    
    gk "No followers, leave him. HE SHALL BE THE FIRST VICTIM OF THE AMULETS POWER!!"
    
    jump scene19




label scene18:
    
    define choiceseven = "See how this plays out"
    
    "%(player_name)s remains in the shadows, watching the Goblin King planning his next move."
    
    gk "WE WILL NO LONGER BE LOOKED AT AS FEEBLE CREATURES. WITH THE AMULET WE WILL BE CONSIDERED GODS"
    
    gk "THE SUPERIOR SPECIES, ALL WILL FEAR US. NO MORE LIVING IN CAVES AND SEWERS. WE SHALL LIVE LIKE ROYALTY NOW!”"
    
    jump scene19




label scene19:
    
    scene amulet
    
    gk "YES, I CAN FEEL THE POWER! FLOWING THROUGH MY BLOOD. "
    
    gk "YEEEEESSSSS! ULTIMATE POWER!!!!!!!!"
    
    gk "HAHAHAHAHAHAHAHA!!!!"
    
    gk "Something doesnt feel right"
    
    scene explosion
    
    "The power of the amulet was too much for the Goblin King to handle"
    
    "The power overwhelmed his body, with the power exploding from inside his body"
    
    g "Run, it must be is the Ivorian Grand Mage, i've never seen such power"
    
    "As the goblins leave the lair, %(player_name)s approcahes the amulet"
    
    scene amuletglow
    
    "The Amulet starts to glow as %(player_name)s picks it up"
    
    jump scene20
    

label scene20:
    
    scene leavescave
    
    "%(player_name)s collects himself from the even that has just happend and leaves the cave"
    
    "As the player leaves the cave he hears the same ancienct spell being spoken inside his mind"
    
    scene portal
    
    "A Blue portal appears in front of %(player_name)s"
    
    scene congrats
    
    m "Congratulations champion, you’ve managed to retrieve the amulet and now we can protect it from the people who will use it to cause harm and wage war."
    
    m "We’re eternally grateful for doing this for us, come back with me through the portal, Volmar would love to congratulate you personally."
    
    menu:
        "Return with mage":
            jump scene21
            
        "Refuse":
            jump scene22
    
    
label scene21:
    
    scene sure
    define choiceeight = "Return with mage"
    
    (player_name) "Very well Mage, I’d be more than happy to accompany back to your stronghold."
    
    scene transport
    
    "Mage starts whispering a teleportation spell"

    scene entertheorder

    "....."
    
    scene talk1
    
    v "Ahh %(player_name)s ! It’s a pleasure to see you again."
    
    v "Congratulations %(player_name)s, I always knew you had a good heart!"
    
    v "Please show me the amulet"
    
    scene talk2

    (player_name) "Hold on Volmar, I do owe you my life, but The Grey Order still offered me land, riches and titles for the amulet."
    
    scene talk3
    
    v "Don’t worry friend, you’ve done us a great deed."
    
    v "Keeping the amulet in the hands of our order matters greatly to us."
    
    v "For returning the amulet we are forever grateful."
    
    v "Let us offer you land in our beautiful country, we’ll give you the title of  Protector of the land alongside our food resources."
    
    scene talk4
    
    (player_name) "Thank you Mage, I owe my life to the order. I’d be happy to accept your offer."
    
    scene talk5
    
    v "The, the amulet, it’s glowing! It, it can’t be, the prophecy speaks of the chosen one. A powerful mage that can wield the true power of the amulet."
    
    v "We’ve always thought it would be one of our kin. We’ve been so clouded this whole time."
    
    v "Nevertheless my mind is clear now."
    
    v "%(player_name)s, You are the chosen one! Please, let us teach you the ways of the order and let us research the powers of the amulet."
    
    v "Together we can bring true peace the world."

    scene talk6
    
    (player_name) "Your mind might be clear mage but mine has never been more clouded."
    
    (player_name) "If you say I’m the chosen one, I believe you, yet I know nothing of the life of a mage, nor anything to do with magic."
    
    (player_name) "I know the amulet is only safe with the order. I shall stay and learn, thank you Volmar."
    
    
    jump fadetoblack
    



label fadetoblack:
    
    ## INPUT CODE TO FADE GAME TO BLACK WITH THE TEXT BELOW POPPING UP
    
    "Volmar and %(player_name)s began their training. %(player_name)s settled down in a small and beautiful house outside the mages order"
    
    "Him and Volmar became great friends, such friends that Volmar allowed X to take his sisters hand in marriage creating their own family in the kingdom."
    
    ## break
    
    "The Battle Mages never disclosed the fact they’ve found the amulet."
    
    "The war between the Grey Order and Battle Mages still rages on as the Grey Order search for the amulet."

    "The future of %(player_name)s and the Battle Mages is uncertain, yet we know %(player_name)s is happy with his current life as he trains in the arts of magic."


    jump creditsend
    
    
label scene22:
    
    define choiceeight = "Refuse"
    scene nope
    
    (player_name) "Why should I trust you, I’m a man of my word, I’ve been given a mission to retrieve the amulet."
    
    (player_name) "I have given my word and honor that I’ll retrieve the amulet and return it back to the King Of The Grey Order. I cannot return with you."

    m "Sorry %(player_name)s, it wasn’t an invitation."
    
    m "The amulet must return to us, you either come with us willingly or we’ll have to take it from you."
    
    scene attack
    
    (player_name) "I can not do that, farwell Mages."
    
    scene fight
    
    "The Mage attack %(player_name)s with fireballs"
    
    "The amulet lights up releasing a shield protecting %(player_name)s"
    
    scene protection
    
    m "It can be!!! You are the chosen one, it has to be him."
    
    m "The amulet it protected him, the amulet doesn’t server anyone except the one it chooses!"
    
    scene stabbed
    
    (player_name) "This amulet is proving to be an amazing asset."
    
    scene choice
    
    menu:
        "Return Home":
            jump scene23
            
        "Report back to your employer":
            jump scene24


label scene23:
    
    define choicenine = "Return Home"
    scene blackscreen
    
    "After days of travelling %(player_name)s returns Home"
    
    scene plotting
    
    (player_name) "The amulet, the power it beholds is un-thinkable."
    
    (player_name) "The mages spells they had no affect on me. I am the chosen one, why, i’m not sure."
    
    (player_name) "But to give away this power to any order would be foolish."
    
    (player_name) "I’ve always been used by many, always being told what to do, always been looked at as a weapon for hire nothing else."
    
    (player_name) "With this amulet I can become a god, start my own city, my own country, my own kingdom."
    
    (player_name) "But why stop there, I can take over the world, kingdoms would perish under my strengths, seas dry up and desserts flourish back to life."
    
    (player_name) "With this amulet I am the god of life and death. Of light and dark, of monsters, but also men."
    
    (player_name) "No one can stop me."
    
    (player_name) "It’s time to unleash"
    
    (player_name) "The Amulet of Power......."
    
    jump creditsend

label scene24:
    
    define choicenine = "Report back to your employer"
    scene blackscreen

    "After days of travelling %(player_name)s returns to his employer"
    
    scene kingmeeting
    
    (player_name) "My king I have returned!"
    
    k "%(player_name)s, my good sir, my champion! Welcome back"
    
    k "I’ve heard about your success the tails of a brave warrior infiltrating and taking down the goblins has traveled across the land."
    
    scene kingtell
    
    (player_name) "Indeed my king, I’ve retrieved the amulet, yet I have one more thing to tell you sir."
    
    (player_name) "I’ve found out that I’m the chosen one, the amulet protects me, and I it."
    
    (player_name) "It has prevented any magic, monster or man from laying a hand on me."
    
    (player_name) "I have become indestructible."
    
    k "Show me this, I need proof champion."
    
    scene kingamuletshow
    
    (player_name) "You see my king, not only am I holding the amulet and still alive, It’s shining while I hold it."
    
    (player_name) "King, the Battle Mages offered me great titles, riches and land for this amulet, yet I stayed true to my word and honor."
    
    (player_name) "Let me become an ultimate weapon for you, let me lead your armies in the name of the Grey Order and yourself."
    
    scene kinghasamulet
    
    k "%(player_name)s, you’ve done a great deed for the land, I believe your word, yet I am not a scholar."
    
    k "My mages will research this further, if turns out to be true, I shall give you everything the Battle mages promised plus more."
    
    k "None the less you have retrieved the amulet for me."
    
    k "Pick any plot of land in my land and it’s yours %(player_name)s, the payment shall be delivered post haste to your quarters."
    
    k "I hear grant you the title of Lord %(player_name)s, Champion Of The Grey Order."
    
    k "Live on and prosper %(player_name)s, we shall be in contact soon."
    
    k "The Battle Mages need to be dealt with."
    
    
    jump creditsend
    
label creditsend:
    $ creditsend_speed = 25 #scrolling speed in seconds
    scene cavetent #replace this with a fancy background
    with dissolve
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide theend
    show credend at Move((0.5, 2.1), (0.5, 0.0), creditsend_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(creditsend_speed)

label credits:
    $ credits_speed = 25 #scrolling speed in seconds
    scene cavetent #replace this with a fancy background
    with dissolve
    show choicedisplay:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide choicedisplay
    show cred at Move((0.5, 1.8), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    jump aftercredits
    
label aftercredits:

    menu:
        "Start Adventure Again?":
            jump scene1

        "Finish Adventure":
            jump finishedgame

label finishedgame:
    "From all of our team, thank you for playing!"
    return

init python:
    credits = ('Choice One:', (choiceone)), ('Choice Two:', (choicetwo)), ('Choice Three:', (choicethree)), ('Choice Four:', (choicefour)), ('Choice Five:', (choicefive)), ('Choice Six:', (choicesix)), ('Choice Seven:', (choiceseven)), ('Choice Eight:', (choiceeight)), ('Choice Nine:', (choicenine)), 
    credits_s = "{size=60}Your Choices!\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=25}" + c[0] + "\n"
        credits_s += "{size=40}" + c[1] + "\n"
        c1=c[0]

init python:

    creditsend = ('MVP', 'Wayne'), ('Loser', 'Choward')
    creditsend_s = "{size=100}Credits\n\n"
    c1 = ''
    for c in creditsend:
        if not c1==c[0]:
            creditsend_s += "\n{size=40}" + c[0] + "\n"
        creditsend_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    creditsend_s += "\n{size=10}Engine\n{size=20}Ren'py\n6.99.14.3135" #Don't forget to set this to your Ren'py version
    
    
init:
    #image cred = Text(credits_s, font="myfont.ttf", text_align=0.5) #use this if you want to use special fonts
    image cred = Text(credits_s, text_align=0.5)
    image credend = Text(creditsend_s, text_align=0.5)
    image choicedisplay = Text("{size=100}And with that your adventure comes to a close!", text_align=0.5) 
    image theend = Text("{size=100}You've been a great warrior!", text_align=0.5)

    

    
    
    
    
    
    
    
    



