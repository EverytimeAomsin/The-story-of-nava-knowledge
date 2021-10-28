# The script of the game goes in this file.
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define totalAns_g1 = 0
define ans_g1 = 'null'
define ans_real = 'null'
define check_ans = 0
define percent_g1 = 0
define points = 1
define score_g1 = 0
define scorefail_g1 = 0
define stack = 0
define stack_fail = 0
define start_g1 = 0
define ans_true = "null"
define pass_minigame1 = "false"
define pass_minigame2 = "false"
define realpoints = 1
define roll = 0
define grade = 'null'

define q1 = 'null'
define q2 = 'null'
# The game starts here.
define question = [
["                คำถาม                 "],
["1.มาสคอตของสวนน้ำวานา นาวา มีชื่อว่าอะไร","วานะและนาวะ","วานาและนาวา","วานาและนาวะ","วานาและนาวะ"], #1
["2.สวนน้ำวานา นาวาเปิดบริการเวลาใด","11.00 น.- 16.00 น.","10.00 น.- 17.00 น.","10.00 น.- 16.00 น.","11.00 น.- 18.00 น."],#1
["3.วานา วันเดอร์แลนด์มีเครื่องเล่นกี่ชิด","5 ชนิด","7 ชนิด","9 ชนิด","10 ชนิด"],#4
["4.วานา วันเดอร์แลนด์ผู้เล่นจะต้องสูงไม่เกินเท่าไร","140 เซนติเมตร","145 เซนติเมตร","150 เซนติเมตร","155 เซนติเมตร"],#4
["5.วานา วันเดอร์แลนด์มีพื้นที่มั้งหมดเท่าไร","450 ตารางเมตร","500 ตารางเมตร","550 ตารางเมตร","600 ตารางเมตร"],#1
["7.ช้างเซิร์ฟโซนเล่นพร้อมกันได้สูงสุดกี่คน","ไม่สามารถพร้อมกันได้","2 คน","3 คน","4 คน"],#2
["7.วานามีร้านขายเสื้อผ้า อุปกรณ์และเครื่องประดับมีชื่อว่าอะไร","Ripcurl","Ripcure","Rapcurl","Rapcube"],#1
["8.ประเภทอาหารต่อไปนี้ไม่มีขายในเดอะโกรฟ","อาหารญี่ปุ่น","อาหารจีน","อาหารประเภทเส้น","อาหารซีฟู๊ด"],#1
["9.เดอะโกรฟเปิดเวลาใด","11.00 น.- 16.00 น.","10.00 น.- 15.00 น.","11.00 น.- 15.00 น.","10.00 น.- 17.00 น."],#1
["10.ล็อกเกอร์ให้บริการทั้งหมดกี่จุด","1 จุด","2 จุด","3 จุด","4 จุด"],#2
["11.ล็อกเกอร์สามารถเปิดใช้บริการได้ด้วยวิธีใด","ใช้สายรัดข้อมือ","ใช้บัตรเครดิส","ใช้คีย์การ์ด","ใช้รหัสผ่าน"],#1
["12.โรพส์คอร์สอยู่สูงจากพื้นดินกี่เมตร","12.4 เมตร","12.5 เมตร","13.4 เมตร","14.4 เมตร"],#3
["13.หน้าผาจำลองผู้เล่นที่จะเล่นต้องมีส่วนสูงเท่าไร","140 เซนติเมตร","135 เซนติเมตร","150 เซนติเมตร","122 เซนติเมตร"], #4
["14.ช้างเซิร์ฟโซนเล่นพร้อมกันได้สูงสุดกี่คน","ไม่สามารถพร้อมกันได้","2 คน","3 คน","4 คน"],
["15.ร้านนวดไทยอยู่ใกล้กับเครื่องเล่นอะไรมากที่สุด","อะบิส","บูมเมอแรงโก้","เรนฟอร์เทรส","อควาคอร์ส"],#2
["16.สตูดิโอใต้น้ำมีชื่อว่าอะไร","วานาดิโอ","วานาโฟโต้","โฟโต้นาวา","โฟโต้ดิโอ"],#1
["17.สตูดิโอใต้น้ำมีธีมให้เลือกกี่แบบ","10 แบบ","9 แบบ","8 แบบ","11 แบบ"],#1
["18.สตูดิโอใต้น้ำลึกกี่เมตร","1.8 เมตร","2 เมตร","2.5 เมตร","2.3 เมตร"],#-
["19.เครื่อง้ล่นที่มีการสร้างคลื่นจำลองคือเครื่องเล่นอะไร","โคโคนัทบีช","บีชฮัท","คาบาน่า","วานา บีช"],#1
["20.คาบาน่ามีทั้งหมดกี่แห่ง ","ตอบ 1","ตอบ 2","ตอบ 3","ตอบ 4"],#-
["21.ลูกค้าโรงแรมมีสายรัดข้อมือสีอะไร","ตอบ 1","ตอบ 2","ตอบ 3","ตอบ 4"],#-
["22.โคโคนัทบีชมีความลึกสูงสุดเท่าไร","150 เซนติเมตร","183 เซนติเมตร","200 เซนติเมตร","215 เซนติเมตร"],#2
["23.โคโคนัทมีพื้นที่กี่ตารางเมตร","1400 ตารางเมตร","1500 ตารางเมตร","1600 ตารางเมตร","1700 ตารางเมตร"],#3
["24.เลซี่ริเวอร์มีความยาวกี่เมตร","335 เมตร","345 เมตร","355 เมตร","365 เมตร"],#2
["25.เลซี่ริเวอร์มีความลึกเท่าไร","70 เซนติเมตร","85 เซนติเมตร","90 เซนติเมตร","95 เซนติเมตร"],#3
["26.เครื่องเล่นอะไรที่มีถังน้ำยักษ์เทน้ำสาด","เลซี่ริเวอร์","อควาคอร์ส","ฟิชเชอร์แมนส์คาเฟ่","เรนฟอร์เทรส"],#4
["27.เรนฟอร์เทรสมีสไลเดอร์มีทั้งหมดกี่สไลเดอร์","5 สไลเดอร์","6 สไลเดอร์","7 สไลเดอร์","8 สไลเดอร์"],#3
["28.อควาคอร์สมีอะไรที่แตกต่างจากเครื่องเล่นน้ำประเภทอื่น","เป็นเครื่องเล่นที่เหมาะสำหรับเด็กเท่านั้น","เล่นได้เฉพาะผู้ใหญ่เท่านั้น","ต้องใส่เสื้อชูชีพก่อนเล่น","ต้องใส่สายนิรภัยก่อนเล่น"],#4
["29.ผู้เล่นอควาคอร์สต้องมีส่วนสูงมากกว่าเท่าไร","110 เซนติเมตร","122 เซนติเมตร","125 เซนติเมตร","130 เซนติเมตร"],#2
["30.ฟิชเชอร์แมนส์คาเฟ่ขายอาหารประเภทใด","ขายของว่างทานสะดวก","อาหารจีน","อาหารทะเล","อาหารตะวันตก"],#1
["31.คิดดี้โคฟเหมาะสำหรับใคร","เล่นได้เฉพาะผู้ใหญ่เท่านั้น","เป็นเครื่องเล่นที่เหมาะสำหรับเด็กเท่านั้น","เล่นได้ทั้งเด็กและผู้ใหญ่","ได้เฉพาะเด็ก ผู้ใหญ่เล่นสไลเดอร์ไม่ได้"],
["32.สถานที่ที่มีบาร์อยู่ภายในถ้ำเรียกว่าอะไร","วานา เคฟ คาเฟ่","เดอะ เคฟ","วานาอินเนอร์บาร์","เคฟ"],#1
["33.แพยางที่ใช้เล่นเครื่องเล่นอะบิสมีชื่อว่าอะไร","Ring","Tube","Raft","Double Tube"],#3
["34.อะบิสมีความเร็วในการเคลื่อนที่สูงสุดเท่าไร","35 กม./ชม.","45 กม./ชม.","50 กม./ชม.","55 กม./ชม."],#2
["35.เครื่องเล่นบูมเมอร์แรงโก้มีจุดเด่นอย่างไร","สไลเดอร์ที่ยาวที่สุดในประเทศไทย","สไลเดอร์ขนาดใหญ่ที่สุดในประทศไทย","ถูกทั้งสองข้อ","ไม่มีข้อใดถูก"],#1
["36 X 27","ตอบ 1","ตอบ 2","ตอบ 3","ตอบ 4"],
["37.สระว่ายน้ำของฟิชเชอร์แมนส์ทาเวิร์นมีชื่อว่าอะไร7","เดอะ ฟิชเชอร์แมนส์","ฟิชเชอร์แมนส์พู","สระอินฟินิตี้","สระเดอะทาเวิร์น"],#2
["38.เครื่องเล่นที่มีชามยักษ์ก่อนจะตกสู่สระน้ำมีชื่อว่าอะไร","ซุปเปอร์โบวล์","มาสเตอร์บลาสเตอร์","แรทเลอร์","อินเนอร์ทูป"],#1
["39.เครื่องเล่นที่มี VR คือเครื่องเล่นอะไร","ซุปเปอร์โบวล์","มาสเตอร์บลาสเตอร์","แรทเลอร์","อินเนอร์ทูป"],#2
["40.มาสเตอร์บลาสเตอร์มี VR ให้เลือกกี่แบบ","1 แบบ","2 แบบ","3 แบบ","4 แบบ"],#3
["41.อุปกรณ์ใดที่ใช้เล่นเครื่องเล่นอินเนอร์ทูปมีชื่อว่าอะไร","Ring","Inner tube","Raft","Double Tube"],#4
["42.เครื่องเล่นที่มีความเร็วสูงที่สุดคือเครื่องเล่นอะไร","ฟรีฟอลล์","อควาลูป","แรทเลอร์","อินเนอร์ทูป"],#2
["43.เครื่องเล่นที่สามารถเล่นพร้อมกันมากที่สุดใน Tower A","ซุปเปอร์โบวล์","มาสเตอร์บลาสเตอร์","แรทเลอร์","อินเนอร์ทูป"],#3
["44.เครื่องเล่นที่มีสไลเดอร์หมุน 360 องศา","ฟรีฟอลล์","อควาลูป","แรทเลอร์","อินเนอร์ทูป"],#2
["45.วานา นาวามีสไลเดอร์และเครื่องเล่นกี่ชนิด","17 ชนิด","18 ชนิด","19 ชนิด","20 ชนิด"],#4
]

screen final:
    imagebutton:
        xalign 0.5 yalign 0.3
        idle "final.png"
    vbox:
        xalign 0.5
        ypos -30
        text "{color=#C65A77}{size=400}[grade]{/size}{/color}"
    vbox:
        xalign 0.5
        ypos 400
        text "{color=#000000}{size=70}คุณได้ตอบถูก{/size}{/color}"
    vbox:
        xalign 0.5
        ypos 450
        text "{color=#C65A77}{size=140}[score_g1] / [totalAns_g1]{/size}{/color}"
    vbox:
        xalign 0.435
        ypos 630
        text "{color=#000000}{size=70}ได้ตอบผิด : [scorefail_g1]{/size}{/color}"
    vbox:
        xalign 0.43
        ypos 720
        text "{color=#000000}{size=70}เป็นเปอร์เซ็น : [percent_g1] %{/size}{/color}"
    imagebutton:
        xalign 0.4 yalign 0.84
        idle "final_bt1.png"
        hover "final_bt2.png"
        action Jump("process2") alt "ejection"
    vbox:
        xalign 0.4 yalign 0.835
        text "แสดงข้อถูก / ข้อผิด" size 45
    imagebutton:
        xalign 0.605 yalign 0.84
        idle "final_bt1.png"
        hover "final_bt2.png"
        action Jump("realend2") alt "ejection"
    vbox:
        xalign 0.605 yalign 0.835
        text "ดำเนินการต่อไป =>" size 45

screen scoreboard_g2:
    
    imagebutton:
        xpos 0 ypos 0
        idle "scoreboard.png"
    vbox:
        xpos 10
        ypos 15
        text "คะแนน" size 50
    vbox:
        xpos 180
        ypos 15
        text "[score_g1]" size 50
    vbox:
        xpos 180
        ypos 100
        text "[points]" size 50
    vbox:
        xpos 10
        ypos 100
        text "ตำแหน่ง" size 50


screen choice_menu:
    imagebutton:
        xalign 0.228 yalign 0.99 
        idle "menu.png"
    imagebutton:
        xalign 0.21 yalign 0.84
        idle "ans1.png"
        hover "ans1_2.png"
        action Jump("process1") alt "ejection"

    imagebutton:
        xalign 0.8 yalign 0.84
        idle "ans2.png"
        hover "ans2_2.png"
        action Jump("process2") alt "ejection"

    imagebutton:
        xalign 0.21 yalign 0.95
        idle "ans3.png"
        hover "ans3_2.png"
        action Jump("process3") alt "ejection"

    imagebutton:
        xalign 0.8 yalign 0.95
        idle "ans4.png"
        hover "ans4_2.png"
        action Jump("process4") alt "ejection"

screen next:

    imagebutton:
        xalign 0.975 yalign 0.71
        idle "final_bt1.png"
        hover "final_bt2.png"
        action Jump("next") alt "ejection"
    vbox:
        xalign 0.969 yalign 0.71
        text "กดเพื่อไปข้อต่อไป =>" size 43



label next:
    hide screen showanswer
    hide screen answer
    hide screen true 
    hide screen false
    hide screen next
    
    $ check_ans = check_ans * 0
    jump ans




label game_2:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    show screen choice_menu(x=None) 
    image img  = Image("images/map2.png", xpos = 0, ypos = 0)
    image test1 = Image("images/test1.jpg", xpos = 0, ypos = 0)
    show screen scoreboard_g2
    show img with dissolve:
        xpos -110 ypos -1900 zoom 1.6
    
    show screen question1(x=None)
    
    jump check
label process1:
    $ ans_g1 = '1'
    $ check_ans = check_ans + 1
    show screen next
    show screen answer
    show screen showanswer
    $ totalAns_g1 = totalAns_g1 +1
    jump check
    return

label process2:
    $ ans_g1 = '2'
    $ check_ans = check_ans + 1
    show screen next
    show screen answer
    show screen showanswer
    $ totalAns_g1 = totalAns_g1 +1
    jump check
    return

label process3:
    $ ans_g1 = '3'
    $ check_ans = check_ans + 1
    show screen next

    show screen answer
    show screen showanswer

    $ totalAns_g1 = totalAns_g1 +1
    jump check
    return

label process4:
    $ ans_g1 = '4'
    $ check_ans = check_ans + 1
    show screen next
    show screen answer
    show screen showanswer
    $ totalAns_g1 = totalAns_g1 +1
    jump check
    return
label end:

    window hide   
    pause
    if ans_g1 == 'null':
        jump end
    else:
        jump check

    return

screen answer:
    imagebutton:
        xalign 0.21 yalign 0.84
        idle "ans_w1.png"
    imagebutton:
        xalign 0.8 yalign 0.84
        idle "ans_w1.png"

    imagebutton:
        xalign 0.21 yalign 0.95
        idle "ans_w1.png"

    imagebutton:
        xalign 0.8 yalign 0.95
        idle "ans_w1.png"

    

screen true:

    imagebutton:
        xalign 0.39 yalign 0.32
        idle "xt.png"
    imagebutton:
        xalign 0.613 yalign 0.32
        idle "xt.png"
    vbox:
        xalign 0.5 yalign 0.31
        text "{color=#10621A}คุณได้ตอบถูก{/color}" size 70
screen false:
    imagebutton:
        xalign 0.368 yalign 0.31
        idle "x.png"
    imagebutton:
        xalign 0.63 yalign 0.31
        idle "x.png"
    vbox:
        xalign 0.5 yalign 0.31
        text "{color=#CD1400}คุณตอบผิดข้อนี้{/color}" size 70

screen showanswer:
    imagebutton:
        xalign 0.5 yalign 0.41
        idle "ans.png"
    vbox:
        xalign 0.5 yalign 0.43
        text "{color=#000000}คำถาม : [q1]{/color}" size 43
    vbox:
        xalign 0.5 yalign 0.5
        text "{color=#000000}คำตอบที่ถูกต้อง : [q2]{/color}" size 43
label ans:
    if ans_g1 == 'true' and check_ans == 0:
            $ ans_g1 = 'null'
            $ check_ans = check_ans * 0 
            $ score_g1 = score_g1 + 1
            if stack > stack_fail:
                $ stack_fail = stack_fail + 1
            elif stack == stack_fail:
                $ stack = stack + 1
                $ stack_fail = stack_fail + 1
                
            jump wait
    elif ans_g1 == 'false' and check_ans == 0:
            $ ans_g1 = 'null'
            $ check_ans = check_ans * 0 
            $ scorefail_g1 = scorefail_g1 + 1
            if stack > stack_fail:
                $ stack_fail = stack_fail * 0
            elif stack == stack_fail:
                $ stack = stack + 0
                $ stack_fail = stack_fail * 0
                
            jump wait
    elif check_ans > 0:
            $ roll = roll * 0
            jump end
    else:
        jump end

    jump wait
label wait:
    $ roll = renpy.random.choice([1, 2, 3, 4,'c'])
    if roll == 'c':
        if roll == 'c':
            $ roll = renpy.random.choice([2, 3,5,'c'])
            if roll == 'c':
                $ roll = renpy.random.choice([3, 4,5,6])
            else:
                $ roll = roll
        else:
            $ roll = roll
    else:
        $ roll = roll
    jump processroll
label processroll:
    if ans_true == 'true':
        $ roll = roll 
    elif ans_true == 'false':
        $ roll = roll - 3
        if roll > 3:
            $ roll = roll + 0
        elif roll <= 3:
            $ roll = (roll * 0)+1
    
    
    $ ans_g1 = 'null'
    jump minigamecheck


    
label minigamecheck:
    if points >= 14:
        if pass_minigame1 == 'false':
            $ points = 14
            jump point14
        elif pass_minigame1 == 'true':
            if points >= 36 :
                if pass_minigame2 == 'false':
                    $ points = 36
                    jump point36
                elif pass_minigame2 == 'true':
                    jump end
                elif points < 36:
                    jump end

    elif points  < 14:
        jump end
    
    jump end
    return

label minigame1:
    $ ans_g1 = 'null'
    $ pass_minigame1 = 'true'
    $ roll = 0
    jump hidden_object
    return
label minigame2:
    $ ans_g1 = 'null'
    $ pass_minigame2 = 'true'
    $ roll = 0
    jump inminigame2
    jump check
    return

label check:
    if check_ans >=1:
        jump end
    else:
        jump check2
label check2:
    
    $ points = points + roll
    if points == 1 :
        
        # $ points = str(points)
        
        python:
            
            renpy.jump("point1")
    elif points == 2:
        if check_ans >= 1:
            jump end
        else:
            hide screen question1
            show screen question2(x=None)
            $ ans_real = '1'
            if ans_g1 == '1':
                 
                $ ans_g1 = 'true'
            else:
                show screen false
                $ ans_g1 = 'false'
            python:
                renpy.jump("point2")
        
    elif points == 3:
        if check_ans >= 4 or ans_g1 == 'null':
            ""
            hide screen true 
            hide screen false 
            jump end
        
        else:
            $ ans_real = '1'
            if ans_g1 == '1':
                 
                $ ans_g1 = 'true'
            else:
                $ ans_g1 = 'false'
                
            hide screen question1
            hide screen question2
            
            show screen question3(x=None)
            jump point3
    elif points == 4:
        if check_ans >= 4 or ans_g1 == 'null':
            hide screen true 
            hide screen false 
            jump end
        
        else:
            if ans_g1 == '1':
                 
                $ ans_g1 = 'true'

            else:
        
                $ ans_g1 = 'false'
            hide screen question1
            hide screen question2
            hide screen question3
        
            show screen question4(x=None)
            jump point4
    elif points == 5:
        if check_ans >= 1 or ans_g1 == 'null':
            hide screen true 
            hide screen false 
            jump end
        
        else:
            if ans_g1 == '1':
                 
                $ ans_g1 = 'true'
            else:
                show screen false
                $ ans_g1 = 'false'
            hide screen question1
            hide screen question2
            hide screen question3
            hide screen question4
        
            show screen question5(x=None)
            jump point5
    elif points == 6:
        if check_ans >= 1 or ans_g1 == 'null':
            ""
            hide screen true 
            hide screen false 
            jump end
        
        else:
            if ans_g1 == '1':

                $ ans_g1 = 'true'
                 
            else:
                show screen false
                $ ans_g1 = 'false'
            hide screen question1
            hide screen question2
            hide screen question3
            hide screen question4
            hide screen question5
            
            show screen question6(x=None)
            jump point6
    elif points == 7:
        if check_ans >= 2 or ans_g1 == 'null':
            hide screen true 
            hide screen false 
            jump end
        
        else:
            if ans_g1 == '1':
                $ ans_g1 = 'true'
                 
            else:
                
                $ ans_g1 = 'false'
            hide screen question1
            hide screen question2
            hide screen question3
            hide screen question4
            hide screen question5
            hide screen question6
            show screen question7(x=None)
            jump point7
    elif points == 8:
        $ ans_real = '1'
        if ans_g1 == '1':
            $ ans_g1 = 'true'
             
        else:
            
            $ ans_g1 = 'false'
        hide screen question2
        hide screen question3
        hide screen question4
        hide screen question5
        hide screen question6
        hide screen question7
        show screen question8(x=None)
        jump point8
    elif points == 9:
        $ ans_real = '1'
        if ans_g1 == '1':
            $ ans_g1 = 'true'
        else:
            $ ans_g1 = 'false'
        hide screen question3
        hide screen question4
        hide screen question5
        hide screen question6
        hide screen question7
        hide screen question8
        show screen question9(x=None)
        jump point9
    elif points == 10:
        $ ans_real = '1'
        if ans_g1 == '2':
            $ ans_g1 = 'true'
             
        else:
            
            $ ans_g1 = 'false'
        hide screen question3
        hide screen question4
        hide screen question5
        hide screen question6
        hide screen question7
        hide screen question8
        hide screen question9
        show screen question10(x=None)
        jump point10
    elif points == 11:
        $ ans_real = '1'
        if ans_g1 == '1':
            $ ans_g1 = 'true'
             
        else:
            
            $ ans_g1 = 'false'
        hide screen question4
        hide screen question5
        hide screen question6
        hide screen question7
        hide screen question8
        hide screen question9
        hide screen question10
        show screen question11(x=None)
        jump point11
    elif points == 12:
        $ ans_real = '1'
        if ans_g1 == '3':
            $ ans_g1 = 'true'
             
        else:
            
            $ ans_g1 = 'false'
        hide screen question5
        hide screen question6
        hide screen question7
        hide screen question8
        hide screen question9
        hide screen question10
        hide screen question11
        show screen question12(x=None)
        jump point12
    elif points == 13:
       
        if ans_g1 == '4':
            $ ans_g1 = 'true'
             
        else:
            
            $ ans_g1 = 'false'
        hide screen question6
        hide screen question7
        hide screen question8
        hide screen question9
        hide screen question10
        hide screen question11
        hide screen question12
        show screen question13(x=None)
        jump point13
    elif points == '13':
        $ ans_real = '1'
        if ans_g1 == '4':
            $ ans_g1 = 'true'
            $ points = 14
            "[points]"
             
        else:
            show screen false
            $ ans_g1 = 'false'
            $ points = 14
        
        jump check
    elif points == 14:

        hide screen question7
        hide screen question8
        hide screen question9
        hide screen question10
        hide screen question11
        hide screen question12
        hide screen question13
        # show screen question14(x=None)
        hide screen choice_menu
        jump point14
    elif points == 15:
        $ ans_real = '1'
        $ ans_g1 = 'null'
        if ans_g1 == '2':
            $ ans_g1 = 'true'
             
        else:
            show screen false
            $ ans_g1 = 'false'
        show screen choice_menu
        hide screen question8
        hide screen question9
        hide screen question10
        hide screen question11
        hide screen question12
        hide screen question13
        hide screen question14
        show screen question15(x=None)
        jump point15
    elif points == 16:
        $ ans_real = '1'
        if ans_g1 == '1':
            $ ans_g1 = 'true'
             
        else:
            show screen false
            $ ans_g1 = 'false'
        show screen choice_menu
        hide screen question9
        hide screen question10
        hide screen question11
        hide screen question12
        hide screen question13
        hide screen question14
        hide screen question15
        show screen question16(x=None)
        jump point16
    elif points == 17:
        $ ans_real = '1'
        if ans_g1 == '1':
            $ ans_g1 = 'true'
             
        else:
            show screen false
            $ ans_g1 = 'false'
        show screen choice_menu
        hide screen question10
        hide screen question11
        hide screen question12
        hide screen question13
        hide screen question14
        hide screen question15
        hide screen question16
        show screen question17(x=None)
        jump point17
    
    elif points == 18:
        $ ans_real = '1'
        if ans_g1 == '1':
            $ ans_g1 = 'true'
             
        else:
            show screen false
            $ ans_g1 = 'false'
        show screen choice_menu
        hide screen question11
        hide screen question12
        hide screen question13
        hide screen question14
        hide screen question15
        hide screen question16
        hide screen question17
        show screen question18(x=None)
        jump point18
    elif points == 19:
        $ ans_real = '1'
        if ans_g1 == '1':
            $ ans_g1 = 'true'
             
        else:
            show screen false
            $ ans_g1 = 'false'
        show screen choice_menu
        hide screen question12
        hide screen question13
        hide screen question14
        hide screen question15
        hide screen question16
        hide screen question17
        hide screen question18
        show screen question19(x=None)
        jump point19
    elif points == 20:
        $ ans_real = '1'
        if ans_g1 == '1':
            $ ans_g1 = 'true'
             
        else:
            show screen false
            $ ans_g1 = 'false'
        show screen choice_menu
        hide screen question13
        hide screen question14
        hide screen question15
        hide screen question16
        hide screen question17
        hide screen question18
        hide screen question19
        show screen question20(x=None)
        jump point20
    elif points == 21:
        $ ans_real = '1'
        if ans_g1 == '1':
            $ ans_g1 = 'true'
             
        else:
            show screen false
            $ ans_g1 = 'false'
        show screen choice_menu
        hide screen question14
        hide screen question15
        hide screen question16
        hide screen question17
        hide screen question18
        hide screen question19
        hide screen question20
        show screen question21(x=None)
        jump point21
    elif points == 22:
        $ ans_real = '1'
        if ans_g1 == '2':
            $ ans_g1 = 'true'
             
        else:
            show screen false
            $ ans_g1 = 'false'
        hide screen question15
        hide screen question16
        hide screen question17
        hide screen question18
        hide screen question19
        hide screen question20
        hide screen question21
        show screen question22(x=None)
        jump point22
    elif points == 23:
        $ ans_real = '1'
        if ans_g1 == '3':
            $ ans_g1 = 'true'
             
        else:
            show screen false
            $ ans_g1 = 'false'
        hide screen question16
        hide screen question17
        hide screen question18
        hide screen question19
        hide screen question20
        hide screen question21
        hide screen question22
        show screen question23(x=None)
        jump point23
    elif points == 24:
        $ ans_real = '1'
        if ans_g1 == '2':
            $ ans_g1 = 'true'
             
        else:
            show screen false
            $ ans_g1 = 'false'
        hide screen question17
        hide screen question18
        hide screen question19
        hide screen question20
        hide screen question21
        hide screen question22
        hide screen question23
        show screen question24(x=None)
        jump point24
    elif points == 25:
        $ ans_real = '1'
        if ans_g1 == '3':
            $ ans_g1 = 'true'
             
        else:
            show screen false
            $ ans_g1 = 'false'
        hide screen question18
        hide screen question19
        hide screen question20
        hide screen question21
        hide screen question22
        hide screen question23
        hide screen question24
        show screen question25(x=None)
        jump point25
    elif points == 26:
        $ ans_real = '1'
        if ans_g1 == '4':
            $ ans_g1 = 'true'
             
        else:
            show screen false
            $ ans_g1 = 'false'
        hide screen question19
        hide screen question20
        hide screen question21
        hide screen question22
        hide screen question23
        hide screen question24
        hide screen question25
        show screen question26(x=None)
        jump point26
    elif points == 27:
        $ ans_real = '1'
        if ans_g1 == '3':
            $ ans_g1 = 'true'
             
        else:
            show screen false
            $ ans_g1 = 'false'
        hide screen question20
        hide screen question21
        hide screen question22
        hide screen question23
        hide screen question24
        hide screen question25
        hide screen question26
        show screen question27(x=None)
        jump point27
    elif points == 28:
        $ ans_real = '1'
        if ans_g1 == '4':
            $ ans_g1 = 'true'
             
        else:
            show screen false
            $ ans_g1 = 'false'
        hide screen question21
        hide screen question22
        hide screen question23
        hide screen question24
        hide screen question25
        hide screen question26
        hide screen question27
        show screen question28(x=None)
        jump point28
    elif points == 29:
        $ ans_real = '1'
        if ans_g1 == '2':
            $ ans_g1 = 'true'
             
        else:
            show screen false
            $ ans_g1 = 'false'
        hide screen question22
        hide screen question23
        hide screen question24
        hide screen question25
        hide screen question26
        hide screen question27
        hide screen question28
        show screen question29(x=None)
        jump point29
    elif points == 30:
        $ ans_real = '1'
        if ans_g1 == '1':
            $ ans_g1 = 'true'
             
        else:
            show screen false
            $ ans_g1 = 'false'
        hide screen question23
        hide screen question24
        hide screen question25
        hide screen question26
        hide screen question27
        hide screen question28
        hide screen question29
        show screen question30(x=None)
        jump point30
    elif points == 31:
        $ ans_real = '1'
        if ans_g1 == '1':
            $ ans_g1 = 'true'
             
        else:
            show screen false
            $ ans_g1 = 'false'

        hide screen question24
        hide screen question25
        hide screen question26
        hide screen question27
        hide screen question28
        hide screen question29
        hide screen question30
        show screen question31
        # show screen question31(x=None)
        jump point31
    elif points == 32:
        $ ans_real = '1'
        if ans_g1 == '1':
            $ ans_g1 = 'true'
             
        else:
            show screen false
            $ ans_g1 = 'false'
        hide screen question25
        hide screen question26
        hide screen question27
        hide screen question28
        hide screen question29
        hide screen question30
        hide screen question31
        show screen question32(x=None)
        jump point32
    elif points == 33:
        $ ans_real = '1'
        if ans_g1 == '3':
            $ ans_g1 = 'true'
             
        else:
            show screen false
            $ ans_g1 = 'false'
        hide screen question26
        hide screen question27
        hide screen question28
        hide screen question29
        hide screen question30
        hide screen question31
        hide screen question32
        show screen question33(x=None)
        jump point33
    elif points == 34:
        $ ans_real = '1'
        if ans_g1 == '2':
            $ ans_g1 = 'true'
             
        else:
            show screen false
            $ ans_g1 = 'false'
        hide screen question26
        hide screen question27
        hide screen question28
        hide screen question29
        hide screen question30
        hide screen question31
        hide screen question32
        hide screen question33
        show screen question34(x=None)
        jump point34
    elif points == 35:
        $ ans_real = '1'
        if ans_g1 == '1':
            $ ans_g1 = 'true'
             
        else:
            show screen false
            $ ans_g1 = 'false'
        hide screen question28
        hide screen question29
        hide screen question30
        hide screen question31
        hide screen question32
        hide screen question33
        hide screen question34
        show screen question35(x=None)
        jump point35
    elif points == 36:
        
        hide screen choice_menu
        hide screen question29
        hide screen question30
        hide screen question31
        hide screen question32
        hide screen question33
        hide screen question34
        hide screen question35
        jump point36
    elif points == 37:
        $ ans_real = '1'
        show screen choice_menu
        if ans_g1 == '2':
            $ ans_g1 = 'true'
             
        else:
            show screen false
            $ ans_g1 = 'false'
        hide screen question30
        hide screen question31
        hide screen question32
        hide screen question33
        hide screen question34
        hide screen question35
        hide screen question36
        show screen question37(x=None)
        jump point37
    elif points == 38:
        $ ans_real = '1'
        show screen choice_menu
        if ans_g1 == '1':
            $ ans_g1 = 'true'
             
        else:
            show screen false
            $ ans_g1 = 'false'
        hide screen question32
        hide screen question33
        hide screen question34
        hide screen question35
        hide screen question36
        hide screen question37
        show screen question38(x=None)
        jump point38
    elif points == 39:
        $ ans_real = '1'
        show screen choice_menu
        if ans_g1 == '2':
            $ ans_g1 = 'true'
             
        else:
            show screen false
            $ ans_g1 = 'false'
        hide screen question32
        hide screen question33
        hide screen question34
        hide screen question35
        hide screen question36
        hide screen question37
        hide screen question38
        show screen question39(x=None)
        jump point39
    elif points == 40:
        $ ans_real = '1'
        show screen choice_menu
        if ans_g1 == '3':
            $ ans_g1 = 'true'
             
        else:
            show screen false
            $ ans_g1 = 'false'
        hide screen question33
        hide screen question34
        hide screen question35
        hide screen question36
        hide screen question37
        hide screen question38
        hide screen question39
        show screen question40(x=None)
        jump point40
    elif points == 41:
        $ ans_real = '1'
        show screen choice_menu
        if ans_g1 == '4':
            $ ans_g1 = 'true'
             
        else:
            show screen false
            $ ans_g1 = 'false'
        hide screen question34
        hide screen question35
        hide screen question36
        hide screen question37
        hide screen question38
        hide screen question39
        hide screen question40
        show screen question41(x=None)
        jump point41
    elif points == 42:
        $ ans_real = '1'
        show screen choice_menu
        if ans_g1 == '2':
            $ ans_g1 = 'true'
             
        else:
            show screen false
            $ ans_g1 = 'false'
        hide screen question35
        hide screen question36
        hide screen question37
        hide screen question38
        hide screen question39
        hide screen question40
        hide screen question41
        show screen question42(x=None)
        jump point42
    elif points == 43:
        $ ans_real = '1'
        if ans_g1 == '3':
            $ ans_g1 = 'true'
             
        else:
            show screen false
            $ ans_g1 = 'false'
        hide screen question36
        hide screen question37
        hide screen question38
        hide screen question39
        hide screen question40
        hide screen question41
        hide screen question42
        show screen question43(x=None)
        jump point43
    elif points == 44:
        $ ans_real = '1'
        if ans_g1 == '2':
            $ ans_g1 = 'true'
             
        else:
            show screen false
            $ ans_g1 = 'false'
        hide screen question37
        hide screen question38
        hide screen question39
        hide screen question40
        hide screen question41
        hide screen question42
        hide screen question43
        show screen question44(x=None)
        jump point44
    elif points == 45:
        $ ans_real = '1'
        if ans_g1 == '4':
            $ ans_g1 = 'true'
             
        else:
            show screen false
            $ ans_g1 = 'false'
        hide screen question38
        hide screen question39
        hide screen question40
        hide screen question41
        hide screen question42
        hide screen question43
        hide screen question44
        show screen question45(x=None)
        jump point45
    else:
        $ points = 'Final'
        hide screen question39
        hide screen question40
        hide screen question41
        hide screen question42
        hide screen question43
        hide screen question44
        hide screen question45
        jump point_GG
    
    jump point_GG
    return



label point1:
    $ q1 = question[1][0]
    $ q2 = question[1][1]
    $ ans_real = '1'
    show test1 with dissolve  :
        linear 0 xpos 445 ypos 740
    if ans_g1 == '1':
             
            $ ans_g1 = 'true'
    elif ans_g1 == 'null':
            jump end       
    else:
            
            $ ans_g1 = 'false'
    
    jump Changeview
    return

label point2:
    $ q1 = question[2][0]
    $ q2 = question[2][1]
    show test1 with dissolve  :
        linear 0 xpos 447 ypos 565
    $ realpoints = points
    jump Changeview
    return

    
label point3:
    $ q1 = question[3][0]
    $ q2 = question[3][1]
    show test1 with dissolve  :
        linear 0 xpos 660 ypos 565
    $ realpoints = points   
    jump Changeview
    return

    
label point4:
    $ q1 = question[4][0]
    $ q2 = question[4][1]
    show test1 with dissolve  :
        linear 0 xpos 835+45 ypos 565
    $ realpoints = points
    jump Changeview
    return

    
label point5:
    $ q1 = question[5][0]
    $ q2 = question[5][1]
    show test1 with dissolve  :
        linear 0 xpos 1095 ypos 565
    $ realpoints = points
    jump Changeview
    return

    
label point6:
    $ q1 = question[6][0]
    $ q2 = question[6][1]
    show test1 with dissolve  :
        linear 0 xpos 1355 ypos 565
    $ realpoints = points
    jump Changeview
    return

    
label point7:
    $ q1 = question[7][0]
    $ q2 = question[7][1]
    show test1 with dissolve  :
        linear 0 xpos 1355 ypos 410
    
    jump Changeview
    return

    
label point8:
    $ q1 = question[8][0]
    $ q2 = question[8][1]
    show test1 with dissolve  :
        linear 0 xpos 1100 ypos 410
    jump Changeview
    return

   

label point9:
    $ q1 = question[9][0]
    $ q2 = question[9][1]
    show test1 with dissolve  :
        linear 0 xpos 880 ypos 410
    jump Changeview
    return

    

label point10:
    $ q1 = question[10][0]
    $ q2 = question[10][1]
    show test1 with dissolve  :
        linear 0 xpos 660 ypos 410
    jump Changeview
    return

    
    
label point11:
    $ q1 = question[11][0]
    $ q2 = question[11][1]
    show test1 with dissolve  :
        linear 0 xpos 445 ypos 410
    jump Changeview
    return

   
    
label point12:
    $ q1 = question[12][0]
    $ q2 = question[12][1]
    show test1 with dissolve  :
        linear 0 xpos 450 ypos 225
    jump Changeview
    return

   
    
label point13:
    $ q1 = question[13][0]
    $ q2 = question[13][1]
    show test1 with dissolve  :
        linear 0 xpos 445 ypos 30
    $ points = '13'
    jump Changeview
    return

label point13_2:
    show test1 with dissolve  :
        linear 0 xpos 445 ypos 690
    $ ans_g1 = 'null' 
    $ points = 14
    jump ans
    return

  
    
label point14:
    hide screen true 
    hide screen false
    show test1 with dissolve  :
        linear 0 xpos 445 ypos 515
    jump Changeview
    return

   
    
label point15:
    $ q1 = question[15][0]
    $ q2 = question[15][1]
    show test1 with dissolve  :
        linear 0 xpos 255 ypos 395
    jump Changeview
    return

    
    
label point16:
    $ q1 = question[16][0]
    $ q2 = question[16][1]
    show test1 with dissolve  :
        linear 0 xpos 190 ypos 210
    jump Changeview
    return

   
    
label point17:
    $ q1 = question[17][0]
    $ q2 = question[17][1]
    show test1 with dissolve  :
        linear 0 xpos 170 ypos 50
    jump Changeview
    return

label point17_2:
    $ q1 = question[17][0]
    $ q2 = question[17][1]
    show test1 with dissolve  :
        linear 0 xpos 175 ypos 865
    jump wait
    return 
    
label point18:
    $ q1 = question[18][0]
    $ q2 = question[18][1]
    show test1 with dissolve  :
        linear 0 xpos 175 ypos 730
    jump Changeview
    return

  
    
label point19:
    $ q1 = question[19][0]
    $ q2 = question[19][1]
    show test1 with dissolve  :
        linear 0 xpos 175 ypos 560
    jump Changeview
    return

  
    
label point20:
    $ q1 = question[20][0]
    $ q2 = question[20][1]
    show test1 with dissolve  :
        linear 0 xpos 195 ypos 420
    jump Changeview
    return

  
    
label point21:
    $ q1 = question[21][0]
    $ q2 = question[21][1]
    show test1 with dissolve  :
        linear 0 xpos 350 ypos 460
    jump Changeview
    return


    
label point22:
    $ q1 = question[22][0]
    $ q2 = question[22][1]
    show test1 with dissolve  :
        linear 0 xpos 495 ypos 480
    jump Changeview
    return

  

label point23:
    $ q1 = question[23][0]
    $ q2 = question[23][1]
    show test1 with dissolve  :
        linear 0 xpos 630 ypos 485
    jump Changeview
    return

   
    
label point24:
    $ q1 = question[24][0]
    $ q2 = question[24][1]
    show test1 with dissolve  :
        linear 0 xpos 765 ypos 475
    jump Changeview
    return

 
    
label point25:
    $ q1 = question[25][0]
    $ q2 = question[25][1]
    show test1 with dissolve  :
        linear 0 xpos 900 ypos 370
    jump Changeview
    return

    
    
label point26:
    $ q1 = question[26][0]
    $ q2 = question[26][1]
    show test1 with dissolve  :
        linear 0 xpos 1000 ypos 260
    jump Changeview
    return

    
    
label point27:
    $ q1 = question[27][0]
    $ q2 = question[27][1]
    show test1 with dissolve  :
        linear 0 xpos 1090 ypos 175
    jump Changeview
    return

    
    
label point28:
    $ q1 = question[28][0]
    $ q2 = question[28][1]
    show test1 with dissolve  :
        linear 0 xpos 1235 ypos 250
    jump Changeview
    return

    
    
label point29:
    $ q1 = question[29][0]
    $ q2 = question[29][1]
    show test1 with dissolve  :
        linear 0 xpos 1370 ypos 340
    jump Changeview
    return

    
    
label point30:
    $ q1 = question[30][0]
    $ q2 = question[30][1]
    show test1 with dissolve  :
        linear 0 xpos 1355 ypos 515
    jump Changeview
    return

   
    
label point31:
    show test1 with dissolve  :
        linear 0 xpos 1335 ypos 640
    jump Changeview
    return

    

label point31_2:
    $ q1 = question[31][0]
    $ q2 = question[31][1]
    show test1 with dissolve  :
        linear 0 xpos 1335 ypos 65
    jump wait
    return

   

label point32:
    $ q1 = question[32][0]
    $ q2 = question[32][1]
    show test1 with dissolve  :
        linear 0 xpos 1310 ypos 195
    jump Changeview
    return

    
    
label point33:
    $ q1 = question[33][0]
    $ q2 = question[33][1]
    show test1 with dissolve  :
        linear 0 xpos 1270 ypos 360
    jump Changeview
    return

   
    
label point34:
    $ q1 = question[34][0]
    $ q2 = question[34][1]
    show test1 with dissolve  :
        linear 0 xpos 1150 ypos 515
    jump Changeview
    return

  
    
label point35:
    $ q1 = question[35][0]
    $ q2 = question[35][1]
    show test1 with dissolve  :
        linear 0 xpos 1000 ypos 600
    jump Changeview
    return

  

label point36:
    hide screen true 
    hide screen false
    show test1 with dissolve  :
        linear 0 xpos 830 ypos 565
    jump Changeview
    return

    

label point36_2:
    show test1 with dissolve  :
        linear 0 xpos 815 ypos -30
    jump minigame2
    return

    

label point37:
    $ q1 = question[37][0]
    $ q2 = question[37][1]
    show test1 with dissolve  :
        linear 0 xpos 780 ypos 180
    jump Changeview
    return

    

label point38:
    $ q1 = question[38][0]
    $ q2 = question[38][1]
    show test1 with dissolve  :
        linear 0 xpos 890 ypos 340
    jump Changeview
    return

    

label point39:
    $ q1 = question[39][0]
    $ q2 = question[39][1]
    show test1 with dissolve  :
        linear 0 xpos 1090 ypos 360
    jump Changeview
    return

   

label point40:
    $ q1 = question[40][0]
    $ q2 = question[40][1]
    show test1 with dissolve  :
        linear 0 xpos 1290 ypos 380
    jump Changeview
    return

  

label point41:
    $ q1 = question[41][0]
    $ q2 = question[41][1]
    show test1 with dissolve  :
        linear 0 xpos 1480 ypos 415
    jump Changeview
    return

   

label point42:
    $ q1 = question[42][0]
    $ q2 = question[42][1]
    show test1 with dissolve  :
        linear 0 xpos 1640 ypos 430
    jump Changeview
    return

   

label point43:
    
    show test1 with dissolve  :
        linear 0 xpos 1640 ypos 585
    jump Changeview
    return

   
label point43_2:
    $ q1 = question[43][0]
    $ q2 = question[43][1]
    show test1 with dissolve  :
        linear 0 xpos 1640 ypos 285
    jump wait
    return

   

label point44:
    $ q1 = question[44][0]
    $ q2 = question[44][1]
    show test1 with dissolve  :
        linear 0 xpos 1640 ypos 410
    jump Changeview
    return

   

label point45:
    $ q1 = question[45][0]
    $ q2 = question[45][1]
    show test1 with dissolve  :
        linear 0 xpos 1640 ypos 535
    jump Changeview
    return

  

label point_GG:
    hide screen next
    $ scorefail_g1 =  scorefail_g1
    $ percent_g1 = (score_g1 * 100) 
    $ percent_g1 = percent_g1 / totalAns_g1
    $ scorefail_g1 = totalAns_g1 - score_g1
    hide screen choice_menu
    if percent_g1 >= 80:
        $ grade = 'A'
        show screen final 
    elif percent_g1 >= 70:
        $ grade = 'B'
        show screen final 
    elif percent_g1 >= 60:
        $ grade = 'C'
        show screen final 
    elif percent_g1 >= 50:
        $ grade = 'D'
        show screen final 
    else:
        $ grade = 'F'
        show screen final 
    show test1 with dissolve  :
        linear 0 xpos 1640 ypos 690
    pause
    return

label realend2:
    jump chapter3_0
    return

   
    
label Changeview:
    if points == 43:
        show img with move :
            linear 1.0 xpos -110 ypos -1900
        jump point43_2
    if points >= 43 :
        show img with move :
            linear 1.0 xpos -110 ypos -1900
    elif points >= 37 :
        show img with move :
            linear 1.0 xpos -110 ypos -1600
    elif points == 36 :
        show img with move :
            linear 1.0 xpos -110 ypos -1600
        jump point36_2
    elif points == 31:
        show img with move :
            linear 1.0 xpos -110 ypos -1000
        jump point31_2
    elif points >= 31:
        show img with move :
            linear 1.0 xpos -110 ypos -1000
    elif points == 17:
        show img with move :
            linear 1.0 xpos -110 ypos -430
        jump point17_2
    elif points >= 17:
        show img with move :
            linear 1.0 xpos -110 ypos -430
            
    elif points == 13:
            
        show img with move :
            linear 1.0 xpos -110 ypos -1250
        jump point13_2
    elif points == 14:    
        show img with move :
            linear 1.0 xpos -110 ypos -1250
        show test1 with dissolve  :
            linear 0 xpos 445 ypos 30
        jump minigame1

        
        
    else:
        jump ans
    
    jump ans
    return


screen question1:
    
    vbox:
        xpos 450 
        ypos 725
        text "[question[1][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[1][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[1][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[1][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[1][4]]" size 50

screen question2:
    vbox:
        xpos 450 
        ypos 725
        text "[question[2][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[2][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[2][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[2][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[2][4]]" size 50

screen question3:
    vbox:
        xpos 450 
        ypos 725
        text "[question[3][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[3][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[3][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[3][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[3][4]]" size 50

screen question4:
    vbox:
        xpos 450 
        ypos 725
        text "[question[4][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[4][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[4][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[4][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[4][4]]" size 50

screen question5:
    vbox:
        xpos 450 
        ypos 725
        text "[question[5][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[5][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[5][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[5][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[5][4]]" size 50

screen question6:
    vbox:
        xpos 450 
        ypos 725
        text "[question[6][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[6][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[6][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[6][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[6][4]]" size 50

screen question7:
    vbox:
        xpos 450 
        ypos 725
        text "[question[7][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[7][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[7][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[7][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[7][4]]" size 50

screen question8:
    vbox:
        xpos 450 
        ypos 725
        text "[question[8][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[8][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[8][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[8][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[8][4]]" size 50

screen question9:
    vbox:
        xpos 450 
        ypos 725
        text "[question[9][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[9][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[9][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[9][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[9][4]]" size 50

screen question10:
    vbox:
        xpos 450 
        ypos 725
        text "[question[10][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[10][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[10][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[10][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[10][4]]" size 50

screen question11:
    vbox:
        xpos 450 
        ypos 725
        text "[question[11][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[11][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[11][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[11][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[11][4]]" size 50

screen question12:
    vbox:
        xpos 450 
        ypos 725
        text "[question[12][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[12][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[12][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[12][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[12][4]]" size 50

screen question13:
    vbox:
        xpos 450 
        ypos 725
        text "[question[13][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[13][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[13][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[13][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[13][4]]" size 50

screen question14:
    vbox:
        xpos 450 
        ypos 725
        text "[question[14][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[14][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[14][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[14][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[14][4]]" size 50

screen question15:
    vbox:
        xpos 450 
        ypos 725
        text "[question[15][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[15][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[15][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[15][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[15][4]]" size 50

screen question16:
    vbox:
        xpos 450 
        ypos 725
        text "[question[16][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[16][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[16][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[16][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[16][4]]" size 50

screen question17:
    vbox:
        xpos 450 
        ypos 725
        text "[question[17][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[17][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[17][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[17][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[17][4]]" size 50

screen question18:
    vbox:
        xpos 450 
        ypos 725
        text "[question[18][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[18][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[18][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[18][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[18][4]]" size 50

screen question19:
    vbox:
        xpos 450 
        ypos 725
        text "[question[19][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[19][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[19][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[19][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[19][4]]" size 50

screen question20:
    vbox:
        xpos 450 
        ypos 725
        text "[question[20][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[20][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[20][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[20][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[20][4]]" size 50

screen question21:
    vbox:
        xpos 450 
        ypos 725
        text "[question[21][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[21][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[21][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[21][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[21][4]]" size 50

screen question22:
    vbox:
        xpos 450 
        ypos 725
        text "[question[22][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[22][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[22][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[22][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[22][4]]" size 50

screen question23:
    vbox:
        xpos 450 
        ypos 725
        text "[question[23][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[23][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[23][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[23][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[23][4]]" size 50

screen question24:
    vbox:
        xpos 450 
        ypos 725
        text "[question[24][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[24][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[24][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[24][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[24][4]]" size 50

screen question25:
    vbox:
        xpos 450 
        ypos 725
        text "[question[25][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[25][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[25][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[25][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[25][4]]" size 50

screen question26:
    vbox:
        xpos 450 
        ypos 725
        text "[question[26][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[26][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[26][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[26][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[26][4]]" size 50

screen question27:
    vbox:
        xpos 450 
        ypos 725
        text "[question[27][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[27][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[27][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[27][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[27][4]]" size 50

screen question28:
    vbox:
        xpos 450 
        ypos 725
        text "[question[28][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[28][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[28][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[28][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[28][4]]" size 50

screen question29:
    vbox:
        xpos 450 
        ypos 725
        text "[question[29][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[29][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[29][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[29][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[29][4]]" size 50

screen question30:
    vbox:
        xpos 450 
        ypos 725
        text "[question[30][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[30][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[30][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[30][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[30][4]]" size 50

screen question31:
    vbox:
        xpos 450 
        ypos 725
        text "[question[31][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[31][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[31][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[31][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[31][4]]" size 50

screen question32:
    vbox:
        xpos 450 
        ypos 725
        text "[question[32][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[32][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[32][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[32][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[32][4]]" size 50

screen question33:
    vbox:
        xpos 450 
        ypos 725
        text "[question[33][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[33][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[33][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[33][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[33][4]]" size 50

screen question34:
    vbox:
        xpos 450 
        ypos 725
        text "[question[34][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[34][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[34][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[34][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[34][4]]" size 50

screen question35:
    vbox:
        xpos 450 
        ypos 725
        text "[question[35][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[35][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[35][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[35][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[35][4]]" size 50

screen question36:
    vbox:
        xpos 450 
        ypos 725
        text "[question[36][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[36][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[36][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[36][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[36][4]]" size 50

screen question37:
    vbox:
        xpos 450 
        ypos 725
        text "[question[37][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[37][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[37][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[37][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[37][4]]" size 50

screen question38:
    vbox:
        xpos 450 
        ypos 725
        text "[question[38][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[38][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[38][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[38][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[38][4]]" size 50

screen question39:
    vbox:
        xpos 450 
        ypos 725
        text "[question[39][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[39][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[39][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[39][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[39][4]]" size 50



screen question40:
    vbox:
        xpos 450 
        ypos 725
        text "[question[40][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[40][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[40][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[40][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[40][4]]" size 50

screen question41:
    vbox:
        xpos 450 
        ypos 725
        text "[question[41][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[41][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[41][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[41][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[41][4]]" size 50

screen question42:
    vbox:
        xpos 450 
        ypos 725
        text "[question[42][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[42][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[42][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[42][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[42][4]]" size 50

screen question43:
    vbox:
        xpos 450 
        ypos 725
        text "[question[43][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[43][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[43][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[43][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[43][4]]" size 50

screen question44:
    vbox:
        xpos 450 
        ypos 725
        text "[question[44][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[44][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[44][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[44][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[44][4]]" size 50

screen question45:
    vbox:
        xpos 450 
        ypos 725
        text "[question[45][0]]" size 50
    vbox:
        xpos 300
        ypos 840
        text "[question[45][1]]" size 50
    vbox:
        xpos 1020
        ypos 840
        text "[question[45][2]]" size 50
    vbox:
        xpos 300
        ypos 950
        text "[question[45][3]]" size 50
    vbox:
        xpos 1020
        ypos 950
        text "[question[45][4]]" size 50
