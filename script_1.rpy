
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define scoreG2 = 0

define ingame2_score = 0


define randomG2 = 'null'
define limitG2 = 1

define anscheck = 0
define picturecheck = 0
define picture1 = 0
define picture2 = 0
define picture3 = 0
define picture4 = 0
define picture5 = 0
define grade_g2 = 'null'


define G2 = 1 # จำนวนเกมที่ต้องเล่นในทดสอบ 2

define abyss = 1
define fisherman = 1
define fishermanstavern = 1
define cabana = 1
define coconut = 1
define lockers = 1
define massage = 1
define ropes = 1
define wonderland = 1

screen ejection:
    vbox:
        xalign 0.500 yalign 0.12
        text "ได้เอาป้ายออกเหลือ [ingame2_score] คะแนน เลือกป้ายต่อไปได้เลย" size 50
screen true:
    vbox:
        xalign 0.500 yalign 0.12
        text "{color=#57FF22}คุณได้ตอบถูก{/color}" size 70
screen fail:
    vbox:
        xalign 0.500 yalign 0.12
        text "{color=#FF0035}คุณได้ตอบผิด{/color}" size 70

screen ans_label:
    imagebutton:
        xalign 0.99 yalign 0.45
        idle "next.png"
        hover "next2.png"
        action Jump("game_1") alt "ejection"

screen scoreboard_g1:
    
    imagebutton:
        xpos 0 ypos 0
        idle "scoreboard.png"
    vbox:
        xpos 10
        ypos 15
        text "ข้อที่" size 50
    vbox:
        xpos 180
        ypos 15
        text "[picturecheck] / 5" size 50
    vbox:
        xpos 180
        ypos 100
        text "[scoreG2]" size 50
    vbox:
        xpos 10
        ypos 100
        text "คะแนน" size 50
screen finalscore:
    imagebutton:
        xalign 0.5 yalign 0.3
        idle "final.png"
    vbox:
        xalign 0.5
        ypos -35
        text "{color=#C65A77}{size=400}[grade_g2]{/size}{/color}"
    vbox:
        xalign 0.5
        ypos 405
        text "{color=#000000}{size=70}คุณได้ตอบถูก{/size}{/color}"
    vbox:
        xalign 0.5
        ypos 455
        text "{color=#C65A77}{size=140}[scoreG2] / 100{/size}{/color}"
    vbox:
        xpos 0.365
        ypos 620
        text "{color=#000000}{size=55}ภาพที่ 1 : {color=#C65A77}[picture1]{/color}{/size}{/color}"
    vbox:
        xalign 0.595
        ypos 620
        text "{color=#000000}{size=55}ภาพที่ 2 : {color=#C65A77}[picture2]{/color}{/size}{/color}"
    vbox:
        xpos 0.365
        ypos 685
        text "{color=#000000}{size=55}ภาพที่ 3 : {color=#C65A77}[picture3]{/color}{/size}{/color}"
    vbox:
        xalign 0.595
        ypos 685
        text "{color=#000000}{size=55}ภาพที่ 4 : {color=#C65A77}[picture4]{/color} {/size}{/color}"
    vbox:
        xpos 0.365
        ypos 750
        text "{color=#000000}{size=55}ภาพที่ 5 : {color=#C65A77}[picture4]{/color} {/size}{/color}"

    imagebutton:
        xalign 0.5 yalign 0.85
        idle "final_bt1.png"
        hover "final_bt2.png"
        action Jump("realend") alt "ejection"
    vbox:
        xalign 0.5 yalign 0.845
        text "ดำเนินการต่อไป" size 50
# The game starts here.
label realend:
    hide screen scoreboard_g1
    hide screen finalscore
    if skip == 1:
        return
    elif skip == 0:
        scene matchroom
        jump chapter2_1_1
    return


screen ans1:
    imagebutton:
        xalign 0.99 yalign 0.45
        idle "ans.jpg"
        hover "ans2.jpg"
        insensitive "hide3.png"
        action Jump("score") alt "ans"
    

screen choiceppicture:
    vbox:
        xalign 0.500 yalign 0.12
        text "ให้เลือกแผ่นป้ายที่จะหยิบ" size 70






        

label game_1:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
   
    
    show screen my_button1(x=None)
    show screen my_button2(x=None)
    show screen my_button3(x=None)
    show screen my_button4(x=None)
    show screen my_button5(x=None)
    show screen my_button6(x=None)
    show screen my_button7(x=None)
    show screen my_button8(x=None)
    show screen my_button9(x=None)
    show screen my_button10(x=None)
    show screen my_button11(x=None)
    show screen my_button12(x=None)
    show screen my_button13(x=None)
    show screen my_button14(x=None)
    show screen my_button15(x=None)
    
    hide screen true
    hide screen fail
    hide screen ans_label
    show screen scoreboard_g1
    
    jump random
    return

label random:
    if G2 >= 6:
        scene end_g2
        hide screen my_button1
        hide screen my_button2
        hide screen my_button3
        hide screen my_button4
        hide screen my_button5
        hide screen my_button6
        hide screen my_button7
        hide screen my_button8
        hide screen my_button9
        hide screen my_button10
        hide screen my_button11
        hide screen my_button12
        hide screen my_button13
        hide screen my_button14
        hide screen my_button15
        jump end1
    else :
        $ picturecheck = picturecheck + 1
        
        
        $ ingame2_score = ingame2_score * 0
        $ ingame2_score = ingame2_score + 25
        $ randomG2 = renpy.random.choice(['abyss', 'fisherman','ropes','fishermanstavern','cabana','wonderland','lockers','massage','cabana'])
        if randomG2 == 'abyss':
            if abyss == 1:
                scene abyss_background
                $ abyss = 0
                jump ans1
            elif abyss == 0:
                $ picturecheck = picturecheck - 1
                jump random
                
        elif randomG2 == 'fisherman':
            if fisherman == 1:
                scene fisherman_background
                $ fisherman = 0
                jump ans1
            elif fisherman == 0:
                $ picturecheck = picturecheck - 1
                jump random
        elif randomG2 == 'fishermanstavern':
            if fishermanstavern == 1:
                scene fishermanstavern_background
                $ fishermanstavern = 0
                jump ans1
            elif fishermanstavern == 0:
                $ picturecheck = picturecheck - 1
                jump random
        elif randomG2 == 'cabana':
            if cabana == 1:
                scene cabana_background
                $ cabana = 0
                jump ans1
            elif cabana == 0:
                $ picturecheck = picturecheck - 1
                jump random
        elif randomG2 == 'wonderland':
            if wonderland == 1:
                scene wonderland_background
                $ wonderland = 0
                jump ans1
            elif wonderland == 0:
                $ picturecheck = picturecheck - 1
                jump random
        elif randomG2 == 'coconut':
            if wonderland == 1:
                scene coconut_background
                $ wonderland = 0
                jump ans1
            elif wonderland == 0:
                $ picturecheck = picturecheck - 1
                jump random
        elif randomG2 == 'lockers':
            if lockers == 1:
                scene lockers_background
                $ fishermanstavern = 0
                jump ans1
            elif lockers == 0:
                $ picturecheck = picturecheck - 1
                jump random
        elif randomG2 == 'massage':
            if massage == 1:
                scene massage_background
                $ massage = 0
                jump ans1
            elif massage == 0:
                $ picturecheck = picturecheck - 1
                jump random
        elif randomG2 == 'ropes':
            if ropes == 1:
                scene ropes_background
                $ ropes = 0
                jump ans1
            elif ropes == 0:
                $ picturecheck = picturecheck - 1
                jump random

    
        
    return
screen cancel:
    imagebutton:
        xalign 0.99 yalign 0.45
        idle "cancel.png"
        hover "cancel2.png"
        action Jump("ans1") alt "ejection"
    vbox:
        xalign 0.500 yalign 0.12
        text "คุณจะตอบอะไร" size 70
label ans1:
    hide screen choiceppicture
    hide screen ejection
    hide screen cant_g1
    hide screen cancel
    show screen ans1(x=None)
    $ anscheck = anscheck * 0
    jump waitroom
label score:
    hide screen ejection
    hide screen choiceppicture
    show screen cant_g1
    show screen cancel
    $ anscheck = anscheck + 1

label choices1: 
    menu:
        "อะบิส":
            $ anscheck = anscheck * 0
            if randomG2 == 'abyss':
                $ ingame2_score = ingame2_score + 5
                $ scoreG2 = scoreG2 + ingame2_score
                
                show screen true
            else:
                $ ingame2_score = ingame2_score * 0
                $ scoreG2 = scoreG2 + ingame2_score
                show screen fail
        "ฟิชเชอร์แมนส์คาเฟ่":
            $ anscheck = anscheck * 0
            if randomG2 == 'fisherman':
                $ ingame2_score = ingame2_score + 5
                $ scoreG2 = scoreG2 + ingame2_score
                show screen true
            else:
                $ ingame2_score = ingame2_score * 0
                $ scoreG2 = scoreG2 + ingame2_score
                show screen fail
        "ฟิชเชอร์แมนส์ทาเวิร์น":
            $ anscheck = anscheck * 0
            if randomG2 == 'fishermanstavern':
                $ ingame2_score = ingame2_score + 5
                $ scoreG2 = scoreG2 + ingame2_score
                show screen true
            else:
                $ ingame2_score = ingame2_score * 0
                $ scoreG2 = scoreG2 + ingame2_score
                show screen fail
        "คาบาน่าและบีชฮัท":
            $ anscheck = anscheck * 0
            if randomG2 == 'cabana':
                $ ingame2_score = ingame2_score + 5
                $ scoreG2 = scoreG2 + ingame2_score
                show screen true
            else:
                $ ingame2_score = ingame2_score * 0
                $ scoreG2 = scoreG2 + ingame2_score
                show screen fail
        "ตัวเลือกเพิ่มเติม (ตัวเลือกหน้า 2)":
            jump choices2
    jump score2
       

label choices2:
    menu:
            "วานา วันเดอร์แลนด์":
                $ anscheck = anscheck * 0
                if randomG2 == 'wonderland':
                    $ ingame2_score = ingame2_score + 5
                    $ scoreG2 = scoreG2 + ingame2_score
                    show screen true
                else:
                    $ ingame2_score = ingame2_score * 0
                    $ scoreG2 = scoreG2 + ingame2_score
                    show screen fail
            "โคโคนัทบีช":
                $ anscheck = anscheck * 0
                if randomG2 == 'coconut':
                    $ ingame2_score = ingame2_score + 5
                    $ scoreG2 = scoreG2 + ingame2_score
                    show screen true
                else:
                    $ ingame2_score = ingame2_score * 0
                    $ scoreG2 = scoreG2 + ingame2_score
                    show screen fail
            "ล็อกเกอร์และห้องอาบน้ำ":
                $ anscheck = anscheck * 0
                if randomG2 == 'lockers':
                    $ ingame2_score = ingame2_score + 5
                    $ scoreG2 = scoreG2 + ingame2_score
                    show screen true
                else:
                    $ ingame2_score = ingame2_score * 0
                    $ scoreG2 = scoreG2 + ingame2_score
                    show screen fail
            "ร้านนวดไทย":
                $ anscheck = anscheck * 0
                if randomG2 == 'massage':
                    $ ingame2_score = ingame2_score + 5
                    $ scoreG2 = scoreG2 + ingame2_score
                    show screen true
                else:
                    $ ingame2_score = ingame2_score * 0
                    $ scoreG2 = scoreG2 + ingame2_score
                    show screen fail
            "โรพส์คอร์ส":
                $ anscheck = anscheck * 0
                if randomG2 == 'ropes':
                    $ ingame2_score = ingame2_score + 5
                    $ scoreG2 = scoreG2 + ingame2_score
                    show screen true
                else:
                    $ ingame2_score = ingame2_score * 0
                    $ scoreG2 = scoreG2 + ingame2_score
                    show screen fail
            "ตัวเลือกเพิ่มเติม (ตัวเลือกหน้า 1)":
                jump choices1
    jump score2

label score2:
    if anscheck > 0 :
        jump ans1
    else:
        hide screen cant_g1
        hide screen  cancel
        hide screen  ejection
        hide screen choiceppicture
        hide screen my_button1
        hide screen my_button2
        hide screen my_button3
        hide screen my_button4
        hide screen my_button5
        hide screen my_button6
        hide screen my_button7
        hide screen my_button8
        hide screen my_button9
        hide screen my_button10
        hide screen my_button11
        hide screen my_button12
        hide screen my_button13
        hide screen my_button14
        hide screen my_button15
        hide screen ans1
        show screen ans_label
        $ G2 = G2+1
        if picturecheck == 1:
            $ picture1 = picture1 + ingame2_score
        elif picturecheck == 2:
            $ picture2 = picture2 + ingame2_score
        elif picturecheck == 3:
            $ picture3 = picture3 + ingame2_score
        elif picturecheck == 4:
            $ picture4 = picture4 + ingame2_score
        elif picturecheck == 5:
            $ picture5 = picture5 + ingame2_score
        jump waitend
    return
label waitend:
    window hide   
    pause
    jump waitend
    return


label waitroom:
    show screen choiceppicture
    window hide   
    pause
    jump waitroom
    return
label end1:
    show screen finalscore
    if scoreG2 >= 80:
        $ grade_g2 = 'A'
    elif scoreG2 >=70:
        $ grade_g2 = 'B'
    elif scoreG2 >=60:
        $ grade_g2 = 'C'
    elif scoreG2 >= 50 :
        $ grade_g2 = 'D'
    else:
        $ grade_g2 = 'F'
    jump waitend
    return
label wait1:
    if ingame2_score == 5:
        jump score
    elif ingame2_score < 4:
        $ ingame2_score = ingame2_score * 0
        jump score
    else : 
        jump waitend
    return
screen cant_g1:
    imagebutton:
        xpos 0.2  ypos 0.21
        idle "cant_g1.png"
        action Jump("ans") alt "ejection"

label ejection1 :
    if anscheck > 0:
        
        jump waitend
    else:
        hide screen choiceppicture
        show screen  ejection
        hide screen my_button1
        if limitG2 == 1 :
            $ ingame2_score = ingame2_score-5
            $ limitG2 = limitG2-1
        elif limitG2 == 0:
            $ ingame2_score = ingame2_score-0
        jump wait1
    return

label ejection2 :
    if anscheck > 0:
        
        jump waitend
    else:
        hide screen choiceppicture
        show screen  ejection
        hide screen my_button2
        $ ingame2_score = ingame2_score-5
        jump wait1
    return

label ejection3 :
    hide screen choiceppicture
    show screen  ejection
    hide screen my_button3
    $ ingame2_score = ingame2_score-5
    jump wait1
    return

label ejection4 :
    hide screen choiceppicture
    show screen  ejection
    hide screen my_button4
    $ ingame2_score = ingame2_score-5
    jump wait1
    return

label ejection5 :
    hide screen choiceppicture
    show screen  ejection
    hide screen my_button5
    $ ingame2_score = ingame2_score-5
    jump wait1
    return

label ejection6 :
    hide screen choiceppicture
    show screen  ejection
    hide screen my_button6
    $ ingame2_score = ingame2_score-5
    jump wait1
    return
    
label ejection7 :
    hide screen choiceppicture
    show screen  ejection
    hide screen my_button7
    $ ingame2_score = ingame2_score-5
    jump wait1
    return

label ejection8 :
    hide screen choiceppicture
    show screen  ejection
    hide screen my_button8
    $ ingame2_score = ingame2_score-5
    jump wait1
    return

label ejection9 :
    hide screen choiceppicture
    show screen  ejection
    hide screen my_button9
    $ ingame2_score = ingame2_score-5
    jump wait1
    return

label ejection10 :
    hide screen choiceppicture
    show screen  ejection
    hide screen my_button10
    $ ingame2_score = ingame2_score-5
    jump wait1
    return

label ejection11 :
    hide screen choiceppicture
    show screen  ejection
    hide screen my_button11
    $ ingame2_score = ingame2_score-5
    jump wait1
    return

label ejection12 :
    hide screen choiceppicture
    show screen  ejection
    hide screen my_button12
    $ ingame2_score = ingame2_score-5
    jump wait1
    return

label ejection13 :
    hide screen choiceppicture
    show screen  ejection
    hide screen my_button13
    $ ingame2_score = ingame2_score-5
    jump wait1
    return

label ejection14 :
    hide screen choiceppicture
    show screen  ejection
    hide screen my_button14
    $ ingame2_score = ingame2_score-5
    jump wait1
    return

label ejection15 :
    hide screen choiceppicture
    show screen  ejection
    hide screen my_button15
    $ ingame2_score = ingame2_score-5
    jump wait1
    return

screen my_button1:
    imagebutton:
        xalign 0.228 yalign 0.266
        idle "hide_1.jpg"
        hover "hide2_1.jpg"
        insensitive "hide3.png"
        action Jump("ejection1") alt "ejection"
screen my_button2:
    imagebutton:
        xalign 0.364 yalign 0.266
        idle "hide_2.jpg"
        hover "hide2_2.jpg"
        insensitive "hide3.png"
        action Jump("ejection2") alt "ejection"

screen my_button3:
    imagebutton:
        xalign 0.5 yalign 0.266
        idle "hide_3.jpg"
        hover "hide2_3.jpg"
        insensitive "hide3.png"
        action Jump("ejection3") alt "ejection"

screen my_button4:
    imagebutton:
        xalign 0.636 yalign 0.266
        idle "hide_4.jpg"
        hover "hide2_4.jpg"
        insensitive "hide3.png"
        action Jump("ejection4") alt "ejection"

screen my_button5:
    imagebutton:
        xalign 0.772 yalign 0.266
        idle "hide_5.jpg"
        hover "hide2_5.jpg"
        insensitive "hide3.png"
        action Jump("ejection5") alt "ejection"

screen my_button6:
    imagebutton:
        xalign 0.228 yalign 0.537
        idle "hide_6.jpg"
        hover "hide2_6.jpg"
        insensitive "hide3.png"
        action Jump("ejection6") alt "ejection"

screen my_button7:
    imagebutton:
        xalign 0.364 yalign 0.537
        idle "hide_7.jpg"
        hover "hide2_7.jpg"
        insensitive "hide3.png"
        action Jump("ejection7") alt "ejection"

screen my_button8:
    imagebutton:
        xalign 0.5 yalign 0.537
        idle "hide_8.jpg"
        hover "hide2_8.jpg"
        insensitive "hide3.png"
        action Jump("ejection8") alt "ejection"

screen my_button9:
    imagebutton:
        xalign 0.636 yalign 0.537
        idle "hide_9.jpg"
        hover "hide2_9.jpg"
        insensitive "hide3.png"
        action Jump("ejection9") alt "ejection"

screen my_button10:
    imagebutton:
        xalign 0.772 yalign 0.537
        idle "hide_10.jpg"
        hover "hide2_10.jpg"
        insensitive "hide3.png"
        action Jump("ejection10") alt "ejection"

screen my_button11:
    imagebutton:
        xalign 0.228 yalign 0.808
        idle "hide_11.jpg"
        hover "hide2_11.jpg"
        insensitive "hide3.png"
        action Jump("ejection11") alt "ejection"

screen my_button12:
    imagebutton:
        xalign 0.364 yalign 0.808
        idle "hide_12.jpg"
        hover "hide2_12.jpg"
        insensitive "hide3.png"
        action Jump("ejection12") alt "ejection"

screen my_button13:
    imagebutton:
        xalign 0.5 yalign 0.808
        idle "hide_13.jpg"
        hover "hide2_13.jpg"
        insensitive "hide3.png"
        action Jump("ejection13") alt "ejection"

screen my_button14:
    imagebutton:
        xalign 0.636 yalign 0.808
        idle "hide_14.jpg"
        hover "hide2_14.jpg"
        insensitive "hide3.png"
        action Jump("ejection14") alt "ejection"

screen my_button15:
    imagebutton:
        xalign 0.772 yalign 0.808
        idle "hide_15.jpg"
        hover "hide2_15.jpg"
        insensitive "hide3.png"
        action Jump("ejection15") alt "ejection"

