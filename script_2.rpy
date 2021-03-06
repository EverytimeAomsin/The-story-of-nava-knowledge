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

define randomq = 1

define real = 0

define realscore = 1

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
["6.ช้างเซิร์ฟโซนเล่นพร้อมกันได้สูงสุดกี่คน","ไม่สามารถพร้อมกันได้","2 คน","3 คน","4 คน"],#2
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
["20.คาบาน่ามีทั้งหมดกี่แห่ง ","5 แห่ง","6 แห่ง","7 แห่ง","8 แห่ง"],#4
["21.ลูกค้าโรงแรมมีสายรัดข้อมือสีอะไร","สีน้ำเงินและสีส้ม","สีฟ้าและสีส้ม","ตอบ 3","ตอบ 4"],#1
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
["36.สตูดิโอใต้น้ำลึกกี่เมตร","1.8 เมตร","2 เมตร","2.5 เมตร","2.3 เมตร"],#-
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

label next:
    hide screen showanswer
    hide screen answer
    
    if points == 1:
        if ans_g1 == '1':
            $ realscore = realscore + 1
    if points == 2:
        if ans_g1 == '1':
            $ realscore = realscore + 1
    if points == 3:
        if ans_g1 == '4':
            $ realscore = realscore + 1
    if points == 4:
        if ans_g1 == '4':
            $ realscore = realscore + 1
    if points == 5:
        if ans_g1 == '1':
            $ realscore = realscore + 1
    if points == 6:
        if ans_g1 == '2':
            $ realscore = realscore + 1
    if points == 7:
        if ans_g1 == '1':
            $ realscore = realscore + 1
    if points == 8:
        if ans_g1 == '1':
            $ realscore = realscore + 1
    if points == 9:
        if ans_g1 == '1':
            $ realscore = realscore + 1
    if points == 10:
        if ans_g1 == '2':
            $ realscore = realscore + 1
    if points == 11:
        if ans_g1 == '1':
            $ realscore = realscore + 1
    if points == 12:
        if ans_g1 == '3':
            $ realscore = realscore + 1
    if points == 13:
        if ans_g1 == '4':
            $ realscore = realscore + 1
    if points == 15:
        if ans_g1 == '2':
            $ realscore = realscore + 1
    if points == 16:
        if ans_g1 == '1':
            $ realscore = realscore + 1
    if points == 17:
        if ans_g1 == '1':
            $ realscore = realscore + 1
    if points == 18:
        if ans_g1 == '1':
            $ realscore = realscore + 1
    if points == 19:
        if ans_g1 == '1':
            $ realscore = realscore + 1
    if points == 20:
        if ans_g1 == '4':
            $ realscore = realscore + 1
    if points == 21:
        if ans_g1 == '1':
            $ realscore = realscore + 1
    if points == 22:
        if ans_g1 == '2':
            $ realscore = realscore + 1
    if points == 23:
        if ans_g1 == '3':
            $ realscore = realscore + 1
    if points == 24:
        if ans_g1 == '2':
            $ realscore = realscore + 1
    if points == 25:
        if ans_g1 == '3':
            $ realscore = realscore + 1
    if points == 26:
        if ans_g1 == '4':
            $ realscore = realscore + 1
    if points == 27:
        if ans_g1 == '3':
            $ realscore = realscore + 1
    if points == 28:
        if ans_g1 == '4':
            $ realscore = realscore + 1
    if points == 29:
        if ans_g1 == '2':
            $ realscore = realscore + 1
    if points == 30:
        if ans_g1 == '1':
            $ realscore = realscore + 1
    if points == 31:
        if ans_g1 == '3':
            $ realscore = realscore + 1
    if points == 32:
        if ans_g1 == '1':
            $ realscore = realscore + 1
    if points == 33:
        if ans_g1 == '3':
            $ realscore = realscore + 1
    if points == 34:
        if ans_g1 == '2':
            $ realscore = realscore + 1
    if points == 35:
        if ans_g1 == '1':
            $ realscore = realscore + 1
    if points == 37:
        if ans_g1 == '2':
            $ realscore = realscore + 1
    if points == 38:
        if ans_g1 == '1':
            $ realscore = realscore + 1
    if points == 39:
        if ans_g1 == '2':
            $ realscore = realscore + 1
    if points == 40:
        if ans_g1 == '3':
            $ realscore = realscore + 1
    if points == 41:
        if ans_g1 == '4':
            $ realscore = realscore + 1
    if points == 42:
        if ans_g1 == '2':
            $ realscore = realscore + 1
    if points == 43:
        if ans_g1 == '3':
            $ realscore = realscore + 1
    if points == 44:
        if ans_g1 == '2':
            $ realscore = realscore + 1
    if points == 45:
        if ans_g1 == '4':
            $ realscore = realscore + 1
    $ real = real + 1
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

    # $ roll = 1

    if randomq == 1:
        if real == 1:
            $ roll = 2

        elif real == 2:
            $ roll = 1

        elif real == 3:
            $ roll = 3

        elif real == 4:
            $ roll = 4

        elif real == 5:
            $ roll = 2

        elif real == 6:
            $ roll = 1

        elif real == 7:
            $ roll = 1

        elif real == 8:
            $ roll = 2

        elif real == 9:
            $ roll = 3

        elif real == 10:
            $ roll = 2

        elif real == 11:
            $ roll = 2

        elif real == 12:
            $ roll = 2

        elif real == 13:
            $ roll = 2

        elif real == 14:
            $ roll = 3

        elif real == 15:
            $ roll = 2

        elif real == 16:
            $ roll = 2

        elif real == 17:
            $ roll = 3

        elif real == 18:
            $ roll = 1

        elif real == 19:
            $ roll = 2

        elif real == 20:
            $ roll = 1


    elif randomq == 2:
        if real == 1:
            $ roll = 1

        elif real == 2:
            $ roll = 3

        elif real == 3:
            $ roll = 1

        elif real == 4:
            $ roll = 1

        elif real == 5:
            $ roll = 3

        elif real == 6:
            $ roll = 1

        elif real == 7:
            $ roll = 2

        elif real == 8:
            $ roll = 2

        elif real == 9:
            $ roll = 2

        elif real == 10:
            $ roll = 4

        elif real == 11:
            $ roll = 2

        elif real == 12:
            $ roll = 2

        elif real == 13:
            $ roll = 3

        elif real == 14:
            $ roll = 1

        elif real == 15:
            $ roll = 2

        elif real == 16:
            $ roll = 2

        elif real == 17:
            $ roll = 5

        elif real == 18:
            $ roll = 2

        elif real == 19:
            $ roll = 1

        elif real == 20:
            $ roll = 2

    elif randomq == 3:
        if real == 1:
            $ roll = 3

        elif real == 2:
            $ roll = 1

        elif real == 3:
            $ roll = 1

        elif real == 4:
            $ roll = 2

        elif real == 5:
            $ roll = 1

        elif real == 6:
            $ roll = 3

        elif real == 7:
            $ roll = 1

        elif real == 8:
            $ roll = 2

        elif real == 9:
            $ roll = 2

        elif real == 10:
            $ roll = 1

        elif real == 11:
            $ roll = 3

        elif real == 12:
            $ roll = 1

        elif real == 13:
            $ roll = 3

        elif real == 14:
            $ roll = 1

        elif real == 15:
            $ roll = 2

        elif real == 16:
            $ roll = 2

        elif real == 17:
            $ roll = 2

        elif real == 18:
            $ roll = 4

        elif real == 19:
            $ roll = 3

        elif real == 20:
            $ roll = 2

    elif randomq == 4:
        if real == 1:
            $ roll = 5

        elif real == 2:
            $ roll = 3

        elif real == 3:
            $ roll = 1

        elif real == 4:
            $ roll = 1

        elif real == 5:
            $ roll = 2

        elif real == 6:
            $ roll = 1

        elif real == 7:
            $ roll = 1

        elif real == 8:
            $ roll = 1

        elif real == 9:
            $ roll = 2

        elif real == 10:
            $ roll = 1

        elif real == 11:
            $ roll = 2

        elif real == 12:
            $ roll = 4

        elif real == 13:
            $ roll = 1

        elif real == 14:
            $ roll = 1

        elif real == 15:
            $ roll = 2

        elif real == 16:
            $ roll = 2

        elif real == 17:
            $ roll = 2

        elif real == 18:
            $ roll = 4

        elif real == 19:
            $ roll = 3

        elif real == 20:
            $ roll = 2

    elif randomq == 5:
        if real == 1:
            $ roll = 3

        elif real == 2:
            $ roll = 4

        elif real == 3:
            $ roll = 2

        elif real == 4:
            $ roll = 2

        elif real == 5:
            $ roll = 1

        elif real == 6:
            $ roll = 2

        elif real == 7:
            $ roll = 3

        elif real == 8:
            $ roll = 3

        elif real == 9:
            $ roll = 2

        elif real == 10:
            $ roll = 2

        elif real == 11:
            $ roll = 2

        elif real == 12:
            $ roll = 1

        elif real == 13:
            $ roll = 1

        elif real == 14:
            $ roll = 1

        elif real == 15:
            $ roll = 1

        elif real == 16:
            $ roll = 4

        elif real == 17:
            $ roll = 2

        elif real == 18:
            $ roll = 2

        elif real == 19:
            $ roll = 3

        elif real == 20:
            $ roll = 1

    hide screen next
    $ check_ans = check_ans * 0
    jump ans

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
        text "{color=#000000}{size=70}ตอบถูก{/size}{/color}"
    vbox:
        xalign 0.5
        ypos 450
        text "{color=#C65A77}{size=140}[realscore] / 20{/size}{/color}"
    vbox:
        xalign 0.45
        ypos 630
        text "{color=#000000}{size=70}ตอบผิด : [scorefail_g1]{/size}{/color}"
    vbox:
        xalign 0.47
        ypos 720
        text "{color=#000000}{size=70}เปอร์เซ็น : [percent_g1] %{/size}{/color}"

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
        text "[realscore]" size 50
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
        idle "next_bt1.png"
        hover "next_bt2.png"
        action Jump("next") alt "ejection"
    vbox:
        xalign 0.958 yalign 0.71
        text "กดเพื่อไปข้อต่อไป =>" size 38








label game_2:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    show screen choice_menu(x=None) 
    image img  = Image("images/map2.png", xpos = 0, ypos = 0)
    image test1 = Image("images/test1.png", xpos = 0, ypos = 0)
    show screen scoreboard_g2
    show img with dissolve:
        xpos -110 ypos -1900-200 zoom 1.6
    
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
    
    if ans_g1 == 'null':
        pause
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
            
            $ check_ans = check_ans * 0 
            $ score_g1 = score_g1 + 1
            if stack > stack_fail:
                $ stack_fail = stack_fail + 1
            elif stack == stack_fail:
                $ stack = stack + 1
                $ stack_fail = stack_fail + 1
                
            jump wait
    elif ans_g1 == 'false' and check_ans == 0:
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
    if ans_g1 == 'true':
        $ roll = roll 
    elif ans_g1 == 'false':
        $ roll = roll - 3
        if roll > 3:
            $ roll = roll + 0
        elif roll <= 3:
            $ roll = (roll * 0)+1
    
    
    $ ans_g1 = 'null'
    jump minigamecheck

# false
    
label minigamecheck:
    if points >= 15:
        if pass_minigame1 == 'false':
            $ points = 15
            jump point15
        elif pass_minigame1 == 'true':
            if points >= 30 :
                if pass_minigame2 == 'false':
                    $ points = 30
                    jump point30
                elif pass_minigame2 == 'true':
                    jump end
                elif points < 30:
                    jump end

    elif points  < 15:
        jump end
    
    jump end
    return

label minigame1:
    $ ans_g1 = 'null'
    $ pass_minigame1 = 'true'
    $ roll = 0
    hide screen question11
    hide screen question12
    hide screen question13
    hide screen question14
    hide screen question15
    hide screen question16
    hide screen question17
    hide screen question18
    hide screen question19
    hide screen question20
    hide screen question21
    
    jump hidden_object
    return
label minigame2:
    hide screen question26
    hide screen question27
    hide screen question28
    hide screen question29
    hide screen question31
    hide screen question32
    hide screen question33
    hide screen question34
    hide screen question35
    hide screen choice_menu
    hide screen question30
    $ ans_g1 = 'null'
    $ pass_minigame2 = 'true'
    $ roll = 0
    stop  sound 
    jump inminigame2
    jump check
    return

label check:
    # $ renpy.block_rollback()
    if check_ans >=1:
        pause
        jump end
    else:
        jump check2
label check2:
    
    $ points = points + roll
    if points == 1 :
        show screen choice_menu
        show screen question1(x=None)
        if ans_g1 == '1':
            $ ans_g1 = 'true'
            jump ans
        elif ans_g1 == 'null':
            jump point1
        else:
            
            $ ans_g1 = 'false'

        jump point1
                
    elif points == 2:
            hide screen question1
            show screen question2(x=None)
            if ans_g1 == '2':
                $ ans_g1 = 'true'
            elif ans_g1 == 'null':
                jump point2
            else:
                
                $ ans_g1 = 'false'
            python:
                renpy.jump("point2")
        
    elif points == 3:
            hide screen question1
            hide screen question2
            
            show screen question3(x=None)
            if ans_g1 == '3':
                 
                $ ans_g1 = 'true'
            elif ans_g1 == 'null':
                jump point3
            else:
                $ ans_g1 = 'false'
                
            
            jump point3
    elif points == 4:
            hide screen question1
            hide screen question2
            hide screen question3
        
            show screen question4(x=None)
            if ans_g1 == '1':
                 
                $ ans_g1 = 'true'
            elif ans_g1 == 'null':
                jump point4

            else:
        
                $ ans_g1 = 'false'
            
            jump point4
    elif points == 5: ################
            hide screen question1
            hide screen question2
            hide screen question3
            hide screen question4
        
            show screen question5(x=None)
            if ans_g1 == '2':
                 
                $ ans_g1 = 'true'
            elif ans_g1 == 'null':
                jump point5
            else:
                
                $ ans_g1 = 'false'
            
            jump point5
    elif points == 6:
            hide screen question1
            hide screen question2
            hide screen question3
            hide screen question4
            hide screen question5
            
            show screen question6(x=None)
            if ans_g1 == '3':

                $ ans_g1 = 'true'
            elif ans_g1 == 'null':
                jump point6
                 
            else:
                
                $ ans_g1 = 'false'
           
            jump point6
    elif points == 7: ################
            hide screen question1
            hide screen question2
            hide screen question3
            hide screen question4
            hide screen question5
            hide screen question6
            show screen question7(x=None)
            if ans_g1 == '2':
                $ ans_g1 = 'true'
            elif ans_g1 == 'null':
                jump point7
                 
            else:
                
                $ ans_g1 = 'false'
            
            jump point7
    elif points == 8:
        hide screen question2
        hide screen question3
        hide screen question4
        hide screen question5
        hide screen question6
        hide screen question7
        show screen question8(x=None)
        $ ans_real = '1'
        if ans_g1 == '1':
            $ ans_g1 = 'true'
        elif ans_g1 == 'null':
                jump point8
        else:
            
            $ ans_g1 = 'false'
        
        jump point8
    elif points == 9:
        hide screen question3
        hide screen question4
        hide screen question5
        hide screen question6
        hide screen question7
        hide screen question8
        show screen question9(x=None)
        $ ans_real = '1'
        if ans_g1 == '1':
            $ ans_g1 = 'true'
        elif ans_g1 == 'null':
                jump point9
        else:
            $ ans_g1 = 'false'
        
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

        if points >= 15:
            jump point15
        
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

        if points >= 15:
            jump point15
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

        if points >= 15:
            jump point15
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

        if points >= 15:
            jump point15
        jump point13
    elif points == '13':
        $ ans_real = '1'
        if ans_g1 == '4':
            $ ans_g1 = 'true'
            $ points = 14
             
        else:
            
            $ ans_g1 = 'false'
            $ points = 14
        
        jump check
    elif points == 14:
        $ ans_real = '1'
        $ ans_g1 = 'null'
        if ans_g1 == '2':
            $ ans_g1 = 'true'
             
        else:
            
            $ ans_g1 = 'false'
        hide screen question7
        hide screen question8
        hide screen question9
        hide screen question10
        hide screen question11
        hide screen question12
        show screen question14
        hide screen question13
        hide screen question15
        hide screen question16
        hide screen question17
        # show screen question14(x=None)

        if points >= 15:
            jump point15
        
        jump point14
    elif points == 15:
        $ ans_real = '1'
        $ ans_g1 = 'null'
        if ans_g1 == '2':
            $ ans_g1 = 'true'
             
        else:
            
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
        jump minigame1
    elif points == 16:
        $ ans_real = '1'
        if ans_g1 == '1':
            $ ans_g1 = 'true'
             
        else:
            
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
        $ ans_real = '1'
        show screen choice_menu
        if ans_g1 == '2':
            $ ans_g1 = 'true'
             
        else:
            
            $ ans_g1 = 'false'
        show screen question36
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
        linear 0 xpos 403 ypos 513
    
    
    jump Changeview
    return

label point2:
    $ q1 = question[2][0]
    $ q2 = question[2][1]
    show test1 with dissolve  :
        linear 0 xpos 403 ypos 347
    $ realpoints = points
    jump Changeview
    return

    
label point3:
    $ q1 = question[3][0]
    $ q2 = question[3][1]
    show test1 with dissolve  :
        linear 0 xpos 620 ypos 347
    $ realpoints = points   
    jump Changeview
    return

    
label point4:
    $ q1 = question[4][0]
    $ q2 = question[4][1]
    show test1 with dissolve  :
        linear 0 xpos 835 ypos 347
    $ realpoints = points
    jump Changeview
    return

    
label point5:
    $ q1 = question[5][0]
    $ q2 = question[5][1]
    show test1 with dissolve  :
        linear 0 xpos 1055 ypos 347
    $ realpoints = points
    jump Changeview
    return

    
label point6:
    $ q1 = question[6][0]
    $ q2 = question[6][1]
    show test1 with dissolve  :
        linear 0 xpos 1310 ypos 337
    $ realpoints = points
    jump Changeview
    return

    
label point7:
    $ q1 = question[7][0]
    $ q2 = question[7][1]
    show test1 with dissolve  :
        linear 0 xpos 1313 ypos 190
    
    jump Changeview
    return

    
label point8:
    $ q1 = question[8][0]
    $ q2 = question[8][1]
    show test1 with dissolve  :
        linear 0 xpos 1055 ypos 190
    jump Changeview
    return

   

label point9:
    $ q1 = question[9][0]
    $ q2 = question[9][1]
    show test1 with dissolve  :
        linear 0 xpos 835 ypos 190
    jump Changeview
    return

    

label point10:
    $ q1 = question[10][0]
    $ q2 = question[10][1]
    show test1 with dissolve  :
        linear 0 xpos 620 ypos 190
    jump Changeview
    return

    
    
label point11:
    $ q1 = question[11][0]
    $ q2 = question[11][1]
    show test1 with dissolve  :
        linear 0 xpos 405 ypos 190
    jump Changeview
    return

   
    
label point12:
    $ q1 = question[12][0]
    $ q2 = question[12][1]
    show test1 with dissolve  :
        linear 0 xpos 405 ypos 50
    jump Changeview
    return

   
    
label point13:
    $ q1 = question[13][0]
    $ q2 = question[13][1]
    show test1 with dissolve  :
        linear 0 xpos 410 ypos 360
    jump Changeview
    return



  
    
label point14:
  
    $ q1 = question[14][0]
    $ q2 = question[14][1]
    show test1 with dissolve  :
        linear 0 xpos 445 ypos 515
    jump Changeview
    return

   
    
label point15:
    $ q1 = question[15][0]
    $ q2 = question[15][1]
    show test1 with dissolve  :
        linear 0 xpos 215 ypos 420
    # jump minigame1
    jump minigame1
    return

    
    
label point16:
    $ q1 = question[16][0]
    $ q2 = question[16][1]
    show test1 with dissolve  :
        linear 0 xpos 155 ypos 235
    jump Changeview
    return

   
    
label point17:
    $ q1 = question[17][0]
    $ q2 = question[17][1]
    show test1 with dissolve  :
        linear 0 xpos 150 ypos 35
    jump Changeview
    return

    
label point18:
    $ q1 = question[18][0]
    $ q2 = question[18][1]
    show test1 with dissolve  :
        linear 0 xpos 73 ypos 435
    jump Changeview
    return

  
    
label point19:
    $ q1 = question[19][0]
    $ q2 = question[19][1]
    show test1 with dissolve  :
        linear 0 xpos 72 ypos 270
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
        linear 0 xpos 250 ypos 520
    jump Changeview
    return


    
label point22:
    $ q1 = question[22][0]
    $ q2 = question[22][1]
    show test1 with dissolve  :
        linear 0 xpos 390 ypos 537
    jump Changeview
    return

  

label point23:
    $ q1 = question[23][0]
    $ q2 = question[23][1]
    show test1 with dissolve  :
        linear 0 xpos 535 ypos 537
    jump Changeview
    return

   
    
label point24:
    $ q1 = question[24][0]
    $ q2 = question[24][1]
    show test1 with dissolve  :
        linear 0 xpos 665 ypos 537
    jump Changeview
    return

 
    
label point25:
    $ q1 = question[25][0]
    $ q2 = question[25][1]
    show test1 with dissolve  :
        linear 0 xpos 805 ypos 425
    jump Changeview
    return

    
    
label point26:
    $ q1 = question[26][0]
    $ q2 = question[26][1]
    show test1 with dissolve  :
        linear 0 xpos 900 ypos 330
    jump Changeview
    return

    
    
label point27:
    $ q1 = question[27][0]
    $ q2 = question[27][1]
    show test1 with dissolve  :
        linear 0 xpos 990 ypos 227
    jump Changeview
    return

    
    
label point28:
    $ q1 = question[28][0]
    $ q2 = question[28][1]
    show test1 with dissolve  :
        linear 0 xpos 1130 ypos 310
    jump Changeview
    return

    
    
label point29:
    $ q1 = question[29][0]
    $ q2 = question[29][1]
    show test1 with dissolve  :
        linear 0 xpos 1270 ypos 400
    jump Changeview
    return

    
    
label point30:
    $ q1 = question[30][0]
    $ q2 = question[30][1]
    show test1 with dissolve  :
        linear 0 xpos 1260 ypos 550
    jump minigame2
    return

   
    
label point31:
    show test1 with dissolve  :
        linear 0 xpos 1230 ypos 445
    jump Changeview
    return

    



   

label point32:
    $ q1 = question[32][0]
    $ q2 = question[32][1]
    show test1 with dissolve  :
        linear 0 xpos 1210 ypos 575
    jump Changeview
    return

    
    
label point33:
    $ q1 = question[33][0]
    $ q2 = question[33][1]
    show test1 with dissolve  :
        linear 0 xpos 1160 ypos 240
    jump Changeview
    return

   
    
label point34:
    $ q1 = question[34][0]
    $ q2 = question[34][1]
    show test1 with dissolve  :
        linear 0 xpos 1050 ypos 390
    jump Changeview
    return

  
    
label point35:
    $ q1 = question[35][0]
    $ q2 = question[35][1]
    show test1 with dissolve  :
        linear 0 xpos 897 ypos 476
    jump Changeview
    return

  

label point36:
    $ q1 = question[36][0]
    $ q2 = question[36][1]
    
    show test1 with dissolve  :
        linear 0 xpos 720 ypos 443
    jump Changeview
    return

label point37:
    $ q1 = question[37][0]
    $ q2 = question[37][1]
    show test1 with dissolve  :
        linear 0 xpos 680 ypos 255
    jump Changeview
    return

    

label point38:
    $ q1 = question[38][0]
    $ q2 = question[38][1]
    show test1 with dissolve  :
        linear 0 xpos 785 ypos 415
    jump Changeview
    return

    

label point39:
    $ q1 = question[39][0]
    $ q2 = question[39][1]
    show test1 with dissolve  :
        linear 0 xpos 990 ypos 430
    jump Changeview
    return

   

label point40:
    $ q1 = question[40][0]
    $ q2 = question[40][1]
    show test1 with dissolve  :
        linear 0 xpos 1180 ypos 460
    jump Changeview
    return

  

label point41:
    $ q1 = question[41][0]
    $ q2 = question[41][1]
    show test1 with dissolve  :
        linear 0 xpos 1376 ypos 485
    jump Changeview
    return

   

label point42:
    $ q1 = question[42][0]
    $ q2 = question[42][1]
    show test1 with dissolve  :
        linear 0 xpos 1537 ypos 510
    jump Changeview
    return

   

label point43:
    
    show test1 with dissolve  :
        linear 0 xpos 1537 ypos 170
    jump Changeview
    return

   


   

label point44:
    $ q1 = question[44][0]
    $ q2 = question[44][1]
    show test1 with dissolve  :
        linear 0 xpos 1537 ypos 310
    jump Changeview
    return

   

label point45:
    $ q1 = question[45][0]
    $ q2 = question[45][1]
    show test1 with dissolve  :
        linear 0 xpos 1537 ypos 430
    jump Changeview
    return

  

label point_GG:
    hide screen next
    $ scorefail_g1 =  scorefail_g1
    $ percent_g1 = (realscore * 100) 
    $ percent_g1 = percent_g1 / 20
    $ scorefail_g1 = 20 - realscore
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
        linear 0 xpos 1537 ypos 550
    pause
    return

label realend2:
    hide screen final
    if skip == 1:
        return
    elif skip == 0:
        jump chapter3_0
    return

   
    
label Changeview:
    if points > 42:
        show img with move :
            linear 1.0 xpos -170 ypos -1980
    elif points == 42:
        show img with move :
            linear 1.0 xpos -170 ypos -1980
        show test1 with dissolve  :
            linear 0 xpos 1537 ypos 27
    elif points > 36:
        show img with move :
            linear 1.0 xpos -170 ypos -1500
    elif points == 36:
        show img with move :
            linear 1.0 xpos -170 ypos -1500
        show test1 with dissolve  :
            linear 0 xpos 720 ypos 40
    elif points > 32:
        show img with move :
            linear 1.0 xpos -170 ypos -1100
    elif points == 32:
        show img with move :
            linear 1.0 xpos -170 ypos -1100
        show test1 with dissolve  :
            linear 0 xpos 1207 ypos 79
    elif points > 29:
        show img with move :
            linear 1.0 xpos -170 ypos -600
    elif points == 29:
        show img with move :
            linear 1.0 xpos -170 ypos -600
        show test1 with dissolve  :
            linear 0 xpos 1270 ypos 160
    elif points > 20:
        show img with move :
            linear 1.0 xpos -170 ypos -350
    elif points == 20:
        show img with move :
            linear 1.0 xpos -170 ypos -350
        show test1 with dissolve  :
            linear 0 xpos 97 ypos 490
    elif points > 17:
        show img with move :
            linear 1.0 xpos -170 ypos -700
    elif points == 17:
        show img with move :
            linear 1.0 xpos -170 ypos -700
        show test1 with dissolve  :
            linear 0 xpos 70 ypos 580
    elif points == 17:
        show img with move :
            linear 1.0 xpos -110 ypos -700
        jump point17_2
    elif points > 14:
        show img with move :
            linear 1.0 xpos -110 ypos -1200
        
    elif points == 14:
        show img with move :
            linear 1.0 xpos -110 ypos -1200
        show test1 with dissolve  :
            linear 0 xpos 415 ypos 540
    elif  points== 13 :    
        show img with move :
            linear 1.0 xpos -110 ypos -1550
            
    
    elif points >= 12 and points< 13 :    
        show img with move :
            linear 1.0 xpos -110 ypos -1550
        show test1 with dissolve  :
            linear 0 xpos 405 ypos 560
        jump ans

        
        
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
        xpos 390
        ypos 840
        text "[question[1][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[1][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[1][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[1][4]]" size 45

screen question2:
    vbox:
        xpos 450 
        ypos 725
        text "[question[2][0]]" size 50
    vbox:
        xpos 390
        ypos 840
        text "[question[2][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[2][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[2][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[2][4]]" size 45

screen question3:
    vbox:
        xpos 450 
        ypos 725
        text "[question[3][0]]" size 50
    vbox:
        xpos 390
        ypos 840
        text "[question[3][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[3][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[3][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[3][4]]" size 45

screen question4:
    vbox:
        xpos 450 
        ypos 725
        text "[question[4][0]]" size 50
    vbox:
        xpos 390
        ypos 840
        text "[question[4][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[4][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[4][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[4][4]]" size 45

screen question5:
    vbox:
        xpos 450 
        ypos 725
        text "[question[5][0]]" size 50
    vbox:
        xpos 390
        ypos 840
        text "[question[5][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[5][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[5][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[5][4]]" size 45

screen question6:
    vbox:
        xpos 450 
        ypos 725
        text "[question[6][0]]" size 50
    vbox:
        xpos 390
        ypos 840
        text "[question[6][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[6][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[6][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[6][4]]" size 45

screen question7:
    vbox:
        xpos 450 
        ypos 725
        text "[question[7][0]]" size 50
    vbox:
        xpos 390
        ypos 840
        text "[question[7][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[7][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[7][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[7][4]]" size 45

screen question8:
    vbox:
        xpos 450 
        ypos 725
        text "[question[8][0]]" size 50
    vbox:
        xpos 390
        ypos 840
        text "[question[8][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[8][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[8][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[8][4]]" size 45

screen question9:
    vbox:
        xpos 450 
        ypos 725
        text "[question[9][0]]" size 50
    vbox:
        xpos 390
        ypos 840
        text "[question[9][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[9][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[9][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[9][4]]" size 45

screen question10:
    vbox:
        xpos 450 
        ypos 725
        text "[question[10][0]]" size 50
    vbox:
        xpos 390
        ypos 840
        text "[question[10][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[10][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[10][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[10][4]]" size 45

screen question11:
    vbox:
        xpos 450 
        ypos 725
        text "[question[11][0]]" size 50
    vbox:
        xpos 390
        ypos 840
        text "[question[11][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[11][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[11][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[11][4]]" size 45

screen question12:
    vbox:
        xpos 450 
        ypos 725
        text "[question[12][0]]" size 50
    vbox:
        xpos 390
        ypos 840
        text "[question[12][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[12][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[12][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[12][4]]" size 45

screen question13:
    vbox:
        xpos 450 
        ypos 725
        text "[question[13][0]]" size 50
    vbox:
        xpos 390
        ypos 840
        text "[question[13][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[13][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[13][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[13][4]]" size 45

screen question14:
    vbox:
        xpos 450 
        ypos 725
        text "[question[14][0]]" size 50
    vbox:
        xpos 390
        ypos 840
        text "[question[14][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[14][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[14][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[14][4]]" size 45

screen question15:
    vbox:
        xpos 450 
        ypos 725
        text "[question[15][0]]" size 50
    vbox:
        xpos 390
        ypos 840
        text "[question[15][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[15][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[15][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[15][4]]" size 45

screen question16:
    vbox:
        xpos 450 
        ypos 725
        text "[question[16][0]]" size 50
    vbox:
        xpos 390
        ypos 840
        text "[question[16][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[16][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[16][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[16][4]]" size 45

screen question17:
    vbox:
        xpos 450 
        ypos 725
        text "[question[17][0]]" size 50
    vbox:
        xpos 390
        ypos 840
        text "[question[17][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[17][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[17][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[17][4]]" size 45

screen question18:
    vbox:
        xpos 450 
        ypos 725
        text "[question[18][0]]" size 50
    vbox:
        xpos 390
        ypos 840
        text "[question[18][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[18][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[18][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[18][4]]" size 45

screen question19:
    vbox:
        xpos 450 
        ypos 725
        text "[question[19][0]]" size 50
    vbox:
        xpos 390
        ypos 840
        text "[question[19][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[19][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[19][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[19][4]]" size 45

screen question20:
    vbox:
        xpos 450 
        ypos 725
        text "[question[20][0]]" size 50
    vbox:
        xpos 390
        ypos 840
        text "[question[20][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[20][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[20][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[20][4]]" size 45

screen question21:
    vbox:
        xpos 450 
        ypos 725
        text "[question[21][0]]" size 50
    vbox:
        xpos 390
        ypos 840
        text "[question[21][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[21][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[21][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[21][4]]" size 45

screen question22:
    vbox:
        xpos 450 
        ypos 725
        text "[question[22][0]]" size 50
    vbox:
        xpos 390
        ypos 840
        text "[question[22][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[22][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[22][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[22][4]]" size 45

screen question23:
    vbox:
        xpos 450 
        ypos 725
        text "[question[23][0]]" size 50
    vbox:
        xpos 390
        ypos 840
        text "[question[23][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[23][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[23][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[23][4]]" size 45

screen question24:
    vbox:
        xpos 450 
        ypos 725
        text "[question[24][0]]" size 50
    vbox:
        xpos 390
        ypos 840
        text "[question[24][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[24][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[24][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[24][4]]" size 45

screen question25:
    vbox:
        xpos 450 
        ypos 725
        text "[question[25][0]]" size 50
    vbox:
        xpos 390
        ypos 840
        text "[question[25][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[25][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[25][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[25][4]]" size 45

screen question26:
    vbox:
        xpos 450 
        ypos 725
        text "[question[26][0]]" size 50
    vbox:
        xpos 390
        ypos 840
        text "[question[26][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[26][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[26][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[26][4]]" size 45

screen question27:
    vbox:
        xpos 450 
        ypos 725
        text "[question[27][0]]" size 50
    vbox:
        xpos 390
        ypos 840
        text "[question[27][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[27][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[27][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[27][4]]" size 45

screen question28:
    vbox:
        xpos 450 
        ypos 725
        text "[question[28][0]]" size 50
    vbox:
        xpos 390
        ypos 840
        text "[question[28][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[28][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[28][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[28][4]]" size 45

screen question29:
    vbox:
        xpos 450 
        ypos 725
        text "[question[29][0]]" size 50
    vbox:
        xpos 390
        ypos 840
        text "[question[29][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[29][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[29][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[29][4]]" size 45

screen question30:
    vbox:
        xpos 450 
        ypos 725
        text "[question[30][0]]" size 50
    vbox:
        xpos 390
        ypos 840
        text "[question[30][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[30][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[30][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[30][4]]" size 45

screen question31:
    vbox:
        xpos 450 
        ypos 725
        text "[question[31][0]]" size 50
    vbox:
        xpos 390
        ypos 840
        text "[question[31][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[31][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[31][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[31][4]]" size 45

screen question32:
    vbox:
        xpos 450 
        ypos 725
        text "[question[32][0]]" size 50
    vbox:
        xpos 390
        ypos 840
        text "[question[32][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[32][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[32][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[32][4]]" size 45

screen question33:
    vbox:
        xpos 450 
        ypos 725
        text "[question[33][0]]" size 50
    vbox:
        xpos 390
        ypos 840
        text "[question[33][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[33][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[33][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[33][4]]" size 45

screen question34:
    vbox:
        xpos 450 
        ypos 725
        text "[question[34][0]]" size 50
    vbox:
        xpos 390
        ypos 840
        text "[question[34][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[34][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[34][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[34][4]]" size 45

screen question35:
    vbox:
        xpos 450 
        ypos 725
        text "[question[35][0]]" size 50
    vbox:
        xpos 390
        ypos 840
        text "[question[35][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[35][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[35][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[35][4]]" size 45

screen question36:
    vbox:
        xpos 450 
        ypos 725
        text "[question[36][0]]" size 50
    vbox:
        xpos 390
        ypos 840
        text "[question[36][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[36][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[36][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[36][4]]" size 45

screen question37:
    vbox:
        xpos 450 
        ypos 725
        text "[question[37][0]]" size 50
    vbox:
        xpos 390
        ypos 840
        text "[question[37][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[37][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[37][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[37][4]]" size 45

screen question38:
    vbox:
        xpos 450 
        ypos 725
        text "[question[38][0]]" size 50
    vbox:
        xpos 390
        ypos 840
        text "[question[38][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[38][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[38][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[38][4]]" size 45

screen question39:
    vbox:
        xpos 450 
        ypos 725
        text "[question[39][0]]" size 50
    vbox:
        xpos 390
        ypos 840
        text "[question[39][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[39][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[39][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[39][4]]" size 45



screen question40:
    vbox:
        xpos 450 
        ypos 725
        text "[question[40][0]]" size 50
    vbox:
        xpos 390
        ypos 840
        text "[question[40][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[40][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[40][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[40][4]]" size 45

screen question41:
    vbox:
        xpos 450 
        ypos 725
        text "[question[41][0]]" size 50
    vbox:
        xpos 390
        ypos 840
        text "[question[41][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[41][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[41][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[41][4]]" size 45

screen question42:
    vbox:
        xpos 450 
        ypos 725
        text "[question[42][0]]" size 50
    vbox:
        xpos 390
        ypos 840
        text "[question[42][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[42][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[42][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[42][4]]" size 45

screen question43:
    vbox:
        xpos 450 
        ypos 725
        text "[question[43][0]]" size 50
    vbox:
        xpos 390
        ypos 840
        text "[question[43][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[43][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[43][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[43][4]]" size 45

screen question44:
    vbox:
        xpos 450 
        ypos 725
        text "[question[44][0]]" size 50
    vbox:
        xpos 390
        ypos 840
        text "[question[44][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[44][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[44][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[44][4]]" size 45

screen question45:
    vbox:
        xpos 450 
        ypos 725
        text "[question[45][0]]" size 50
    vbox:
        xpos 390
        ypos 840
        text "[question[45][1]]" size 45
    vbox:
        xpos 1110
        ypos 840
        text "[question[45][2]]" size 45
    vbox:
        xpos 390
        ypos 950
        text "[question[45][3]]" size 45
    vbox:
        xpos 1110
        ypos 950
        text "[question[45][4]]" size 45
