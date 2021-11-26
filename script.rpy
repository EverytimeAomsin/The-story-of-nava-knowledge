# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Player  =    Character("[Player] (ผู้เล่น)")
define Bell    =    Character("เบล")
define Kai     =    Character("กาย")
define Fah     =    Character("ฟ้า")
define Yuri    =    Character("ยูริ")
define Unknown =    Character("บุคคลปริศนา")

define Npc     =    Character("ผู้ร่วมแข่งขันคนอื่นๆ")
define Mc      =    Character("เจ้าหน้าที่")



 #ค่าคะแนนด่าน1
define Player_Score1 = 0 #คะแนนตัวผู้เล่น
define Bell_Score1   = 0 #คะแนนเบล
define Kai_Score1    = 0 #คะแนนผู้เล่นกา




#ค่าคะแนนด่าน 2
define Player_Score2 = 0 #คะแนนตัวผู้เล่น
define Bell_Score2   = 0 #คะแนนเบล
define Kai_Score2    = 0 #คะแนนผู้เล่นกา

define skip = 0
#ค่าตัวละคร Player 
define Currently_Score = 0
#ค่าตัวละคร Bell
define B_Relation = 5 #ค่าความสัมพันธ์
define B_Intelligent = 0 #ต่าความฉลา
#ค่าตัวละคร Kai
define K_Relation    = 5 #ค่าความสัมพันธ์
# The game starts here.

#animation ตัวละคร
image bell_idle = Movie(play="images/movies/bell_idle.webm", mask="images/movies/bell_idle2.webm")
image fah_idle = Movie(play="images/movies/fah_idle.webm", mask="images/movies/fah_idle2.webm")
image fah1 = Movie(play="images/movies/fah1.webm", mask="images/movies/fah12.webm")
image fah2 = Movie(play="images/movies/fah2.webm", mask="images/movies/fah22.webm")
image fah3 = Movie(play="images/movies/fah3.webm", mask="images/movies/fah32.webm")
image yuri1 = Movie(play="images/movies/yuri1.webm", mask="images/movies/yuri12.webm")
image yuri_idle = Movie(play="images/movies/yuri_idle.webm", mask="images/movies/yuri_idle2.webm")


label start:
    scene bg room
    jump menu0
screen mainmenu:
    imagebutton:
        xalign 0.05 yalign 0.5
        idle "menu_story2.png"
        hover "menu_story.png"
        action Jump("menu1") alt "ejection"
    imagebutton:
        xalign 0.5 yalign 0.5
        idle "menu_jigsaw2.png"
        hover "menu_jigsaw.png"
        action Jump("menu2") alt "ejection"
    imagebutton:
        xalign 0.95 yalign 0.5
        idle "menu_quiz2.png"
        hover "menu_quiz.png"
        action Jump("menu3") alt "ejection"
label menu0:
    scene menu_bg
    show screen mainmenu
    pause
    jump menu0
label menu1:
    scene menu_bg2
    show screen mainmenu
    hide screen mainmenu
    jump intro
label menu2:
    scene menu_bg2
    $ skip = 1
    hide screen mainmenu
    $ Player = renpy.input("ใส่ชื่อของคุณ \nกด Enter เพื่อเริ่ม", length=25)
    jump chapter2_1
label menu3:
    scene menu_bg
    $ skip = 1
    hide screen mainmenu
    $ Player = renpy.input("ใส่ชื่อของคุณ \nกด Enter เพื่อเริ่ม", length=25)
    jump chapter3_1

label intro:
        play sound "audio/mumei_bgm.mp3" volume 1.0 loop


        #จุดเริ่มต้น
#วาดฉาก lobby
        Unknown "ยินดีต้อนรับ ก่อนเริ่มเกมโปรดจำไว้ว่าการออกเกมโดยการกดปิดเกมที่ไม่ใช่วิธีปิดผ่านเมนูเกมอาจจะทำให้ความคืบหน้าหายได้"
        "คุณคือใครเหรอ"
        
        Unknown "ฉันคือผู้ที่บันทึกและจัดการระบบเกม"
        Unknown "ว่าแต่ชื่ออะไรเหรอ ฉันขอชื่อหน่อยนะ \n(ระบบจะบันทึกชื่อคุณ เพื่อที่จะบันทึกประวัติการเล่น)"

        #ใส่ชื่อผู้เล่น
        $ Player = renpy.input("ชื่อของคุณ \nกด Enter เพื่อเริ่ม", length=25)

        Unknown "สวัสดี คุณ[Player] ยินดีต้อนรับ สามารถคลิกเพื่อเริ่มเกมได้เลย ^^"
        jump chapter1
        return
label chapter1 :
    
    scene house
    "ณ เวลา 8.40"
    Player  "อ่า....อากาศดีจัง"
    Player  "หลับเต็มอิ่มนี่มันรู้สึกดีจริงๆ"
    Player   "นานๆทีจะตื่นก่อนได้ยินเสียงปลุกด้วยสิ"
    Player   "เอาล่ะ ต้องเตรียมตัวไปแล้วสิ"

#วาดตอนดูมือถือปิด
    scene phone_c
    Player          "เอ...ทำไมโทรศัพท์มันไม่ปลุกล่ะ มันควรจะต้องดังแล้วล่ะ"
    Player          "ตั้งเวลาไว้ตั้ง 6 รอบแล้วแท้ๆ ไม่ดังแม้แต่ครั้งเดียว"
    scene phone_c_house
    Player          "อย่า..อย่าบอกนะว่าจะเผลอกดปิดอีกแล้ว"
    scene phone_o_house with dissolve
#วาดตอนกดเปิดมือถือ
    "เอ๋!!!!!!!!!!!!!!"
    Player          "นี่...มันสายแล้วนี่หว่า"
    scene fronthouse
    Player          "ต้องรีบแล้วววว"
    Player          "เราชื่อ[Player] เป็นเด็กมหาลัยคนหนึ่งที่ได้รับการให้ทำการทดสอบการคัดเลือกเข้าทำงานของที่นี่"
    Player          "ถึงวันนี้จะไม่ใช่วันคัดเลือกก็เถอะนะ"
    Player          "แต่ก็จะไปสายแต่่วันแรกไม่ได้"
    Player          "แย่แล้ว"
    Player          "แย่แน่เลย"

#วาด / รูปหน้าบริษัท
        #ที่บริษัท
    scene frontco
    "ณ บริษัท"

    Player          "รอดแล้ว"
    Player          "เท่านี้ก็ทันเวลา"
    Player          "แล้วเราจะทำยังไงต่อดีละเนี่ย"

                #คำถาม
#วาด / รูปหน้า office   4
    scene office   
    "ณ office"
    show fah1 :
        xzoom 1.5 yzoom 1.5
    Fah             "สวัสดีน้อง คือคนที่มาฝึกงานที่นี่ใช่ไหมคะ "
    Player          "ผมคือผู้ที่ถูกเลือกให้มาฝึกงานที่นี่"
    hide fah1
    show fah2:
        xzoom 1.5 yzoom 1.5
    Fah             "สวัสดี พี่ชื่อฟ้า จะเป็นคนแนะนำสถานที่นี้ในองค์กรคร่าวๆให้นะ"
    Fah             "ถ้ามีอะไรไม่เข้าใจก็ถามได้เลยนะ"
    Player          "ได้เลย ยินดีที่ได้รู้จัก"
    
    #--------------------------แนะนำสถานที่
    scene matchroom
    hide fah2
    show fah3:
        xzoom 1.5 yzoom 1.5
#รูปลานจอดรถ
    Fah             "พี่จะแนะนำสถานที่นะคะ เดินตามมาได้เลย"          
    Player          "ขอถามหน่อย\nมาสคอตหน้าทางเข้ามีชื่อเรียกไหม"
#รูปมาสคอต
    Fah "สองตัวนั้นชื่อวานะและนาวะ"
    Fah "วานะหมายถึงป่า \nนาวะหมายถึงน้ำ"

    #รูปจุดวาดตั๋ว
    scene matchroom1
    Fah             "เริ่มแรกจะเป็นจุด Ticketing นะคะ ซึ่งจุดนี้จะต้องซื้อริสแบนด์ที่ใช้เข้าสวนน้ำชื่อว่า RFID ซึ่งริสแบนด์จะสามารถสแกนเพื่อเป็นบัตรผ่านเข้าไปในสวนน้ำ"
    Fah             "นอกจากนี้ยังสามารถเป็นแทนบัตรเช่าล็อกเกอร์และเติมเงินเพื่อซื้อสินค้าภายในสวนน้ำ ตัวอย่างเช่นร้านอาหารต่างๆ"

#รูปรีเทล
    scene matchroom2
    Fah             "ต่อไปจะเป็นร้านขายของวานา นาวา ที่นี่จะขายของที่ระลึก เช่น ตุ๊กตาน้องวานะและนาวะ  ชุดว่ายน้ำ ครีมกันแดด"

#รูปวานา วันเดอร์แลนด์
    scene matchroom3
    Fah             "เมื่อเดินออกมาจะเจอเครื่องเล่นสำหรับเด็ก เครื่องเล่นนี้ชื่อว่าวานา วันเดอร์แลนด์มีพื้นที่ถึง 550 ตารางเมตร ประกอบด้วยเครื่องเล่นสำหรับเด็กหลาดหลายสีสัน สำหรับที่นี่ผู้เล่นจะต้องมีความสูงไม่ต่ำกว่า 90 เซนติเมตรและไม่เกิน 140 เซนติเมตร"
#รูปเดอะโกรฟ
    scene matchroom3_1
    Fah             "เมื่อเดินกลับมาจะเจอศูนย์อาหาร "
    scene matchroom4
    Fah             "ที่นี่มีชื่อว่าเดอะโกรฟ ที่นี่จะขายอาหารนานาชาติ เช่น "
    Fah             "เวสเทิร์นคอร์เนอร์-มุมอาหารตะวันตก \nช้อปสติ๊กส์-มุมอาหารจีน \nนู้ดเดิ้ลบาร์-มุมอาหารเส้น \nไทยไรซ์” มุมอาหารไทย \n"
    Fah             "และ ซีฟู๊ดกริลล์-มุมอาหารซีฟู๊ด"
    Fah             "ที่นี่สามารถจ่ายได้ผ่าน RFID จากริสแบนด์"

#รูปล็อกเกอร์
    scene matchroom4_1
    Fah             "เมื่อเดินออกจากเดอะโกรฟ"
    scene matchroom5
    Fah             "จะเจอชั้นใต้ดินจะเจอตู้ล็อกเกอร์ ที่นี่สามารถเปิดได้ด้วย RFID"

#รูปเครื่องเล่นไต่เชือก
    scene matchroom5_1
    Fah             "ข้างหน้าจะเป็นกิจกรรมที่เกียวกับ Activity และยังเป็นสองกิจกรรมที่จำเป็นต้องสวมรองเท้าหุ้มส้นพร้อมทั้งอุปกรณ์ช่วยเหลือ"

#รูปโรพส์คอร์ส+วิธีการเล่น
    scene matchroom7
    Fah             "ฝั่งซ้ายจะเป็นที่ชื่อว่าโรพส์คอร์ส  เป้าหมายของเครื่องเล่นนี้คือไต่เชือกจนไปถึงจุดบนสุดให้ได้ซึ่งสูงถึง 13.4 เมตร" 
    Fah             "โดยผู้เล่นจะต้องมีส่วนสูงเกิน 122 เซนติเมตร \n น้ำหนักมากกว่า 136 เซนติเมตร \n และสวมรองเท้าหุ้มส้น"
    Fah             "โดยผู้เล่นจะต้องเชื่อฟังพี่ๆพนักงานอย่างเคร่งครัด"
#รูปหน้าผมจำลอง+วิธีการเล่น
    scene matchroom8
    Fah             "ฝั่งขวาจะชื่อหน้าผาจำลองที่มีความสูงถึง 12.2 เมตร ผู้เล่นจะต้องสูงมากกว่า 150 เซนติเมตร"
    Fah             "โดยผู้เล่นจะต้องเชื่อฟังพี่ๆพนักงานอย่างเคร่งครัดเช่นเดียวกัน"

# #รูปริพเคิร์ล เซิร์ฟช้อป
    Fah             "เมื่อเดินต่อจะเจอร้านเสื้อผ้า ริพเคิร์ล เซิร์ฟช้อป เป็นร้านขายสินค้าแบรนด์แฟชั่นชั้นนำระดับโลกผู้จัดจำหน่ายผลิตภัณฑ์เสื้อผ้า อุปกรณ์และเครื่องประดับสำหรับกีฬาประเภทเซิร์ฟ"

# #รูปช้างเซิร์ฟโซน
    Fah             "ข้างๆชื่อว่า flow ridder บริเวณด้านข้างๆ ริพเคิร์ล เซิร์ฟช้อป สถานที่โต้คลื่นจำลอง สามารถรอบรับผู้เล่นเล่นมากถึงสองคนพร้อมกันได้ ซึ่งผู้เล่นต้องเช็นเอกสารยินยอมเพราะเครื่องเล่นมีความอันตรายเป็นอย่างมาก()"

#รูปแผนกนวด
    scene matchroom8_1
    Fah             "เมื่อออกจากบริเวณ ช้างเชริพโซน"
    scene matchroom9
    Fah             "จะเห็นร้านนวดแผนของวานา นาวา ข้างๆใต้สไลค์เดอร์บูมเบอร์แรงโก้" 
    Player          "บูมเมอร์แรงโก้คืออะไร?"
    Fah             "บูมเมอร์แรงโก้คือเครื่องเล่นสีเหลืองดำที่ช้างหน้านั้นไง"

#รูปวานาดิโอ
    scene matchroom10
    Fah             "ตรงนี้จะเป็นสตูดิโอใต้น้ำ ชื่อว่าวานาดิโอ เป็นสถานที่รูปใต้น้ำมีความลึกถึง xx เมตร มีอุปกรณ์ครบครัน มีให้เลือกบรรยากาศถึง 10 แบบ"

#รูปโคโคนัทบีช
    scene matchroom10_1
    Fah             "ตรงนี้จะชื่อว่าโคโคนัทบีชหรือเวฟพูลเป็นทะเลจำลองมีพื้นที่มากถึง 1,600 ตารางเมตร ลึกสูงสุดถึง 183 เซนติเมตร ทรายของที่นี่เป็นทรายจริงอีกด้วย"
    scene matchroom11
    Fah             "รอบๆนี้จะมีที่นั้งหลังศาลาคอยให้บริการ ชื่อว่าคาบาน่าและบีชฮัท ในส่วนที่เป็นศาลาบีชฮัทจะมีสำหรับการพักผ่อนในพื้นที่ส่วนตัว พร้อมติดตั้งพัดลมเพดานเพิ่มความเย็นสบาย\nสามารถติดต่อได้ที่ฟิชเชอร์แมนส์คาเฟ่"

#รูปเลซี่ริเวอร์
    scene matchroom11_1
    Fah             "ที่เห็นสระว่ายน้ำเป็นลักษณะคล้ายๆแม่น้ำมีชื่อว่าเลซี่ริเวอร์มีความยาวกว่า 345 เมตร มีความลึก 90 เซนติเมตร"

#รูปโรงแรม ทางเข้าสวนน้ำ
    scene matchroom12
    Fah             "เส้นทางนี้จะนำทางไปสู่โรงแรม Holiday inn เส้นทางนี้จะมีล็อกเกอร์และเป็นจุดเข้าออกของลูกค้าโรงแรม โดยริสแบนด์ที่ใช้เข้าสวนน้ำจะเป็นของโรงแรมโดยเฉพาะ"

#รูปฟิชเชอร์แมนส์คาเฟ่
    scene matchroom12_1
    Fah             "เมื่อข้ามสะพานมา"
    scene matchroom14
    Fah             "จะเจอร้านอาหารชื่อว่าฟิชเชอร์แมนส์คาเฟ่จะให้บริการอาหารและของว่างที่ทานสะดวกและรวดเร็ว"

#รูปอควาคอร์ส
    scene matchroom13
    Fah             "ทางซ้ายจะเจอเครื่องเล่นชื่ออควาคอร์ส เป็นเครื่องเล่นแห่งแรกของประเทศไทยที่ให้คุณสามารถตอบโต้กับผู้เล่นคนอื่นได้"
    Fah             "ทดสอบทักษะการทรงตัวบนเส้นทางแห่งการผจญภัย ท้าทายด้วยสิ่งกีดขวาง และปืนฉีดน้ำที่ยิงโต้ตอบกับผู้เล่น"
    Fah             "ผู้เล่นจะต้องสูง 122 เซนติเมตรขึ้นไปและน้ำหนักไม่เกิน 136 กิโลกรัม"

#รูปเรนฟอร์เทรส
    scene matchroom15
    Fah             "ทางขวาจะมีเครื่องเล่นชื่อเรนฟอร์เทรสเป็นเครื่องเล่นที่รวมความสนุกของเด็กๆที่รวม 7 สไลด์เข้าไว้ด้วยกันและมีถังน้ำขนาดยักษ์ที่ค่อยเทน้ำสาดลงมาโดยจะสาดน้ำลงมาทุกๆ 5 นาที"
    Fah             "จะต้องมีส่วนสูง 91.4 - 122 เซนติเมตรขึ้นไป และน้ำหนักไม่เกิน 136 กิโลกรัมขึ้นไป"

#รูปวานา เคฟ คาเฟ่
    scene matchroom17
    Fah             "ในส่วนของตรงถ้ำนี้จะชื่อว่าวานา เคฟ คาเฟ่ หลังจากที่สามารถมานั่งพักหลังจากสนุกไปกับเครื่องเล่นภายในสวนน้ำ อีกทั้งยังมีร้านอาหาร-เครื่องดื่มอีกมากมายไว้คอยให้บริการ และพิเศษสุดกับเครื่องดื่มซิกเนเจอร์สุดชิคจากบาร์คาดี้"
#รูปคิดดี้โคฟ
    scene matchroom16
    Fah             "ข้างๆจะมีเครื่องเล่นชื่อว่าคิดดี้โคฟสระว่ายน้ำสำหรับเด็กที่มีน้ำพุ เครื่องเล่น และสไลเดอร์สำหรับเด็ก"

#รูปฟิชเชอร์แมนส์ทาเวิร์น
    scene matchroom19
    Fah             "ตรงบาร์ตรงนั้นจะเรียกว่าฟิชเชอร์แมนส์ทาเวิร์น ผ่อนคลายพร้อมไปกับเครื่องดื่มเย็นๆ และสัมผัสกับบรรยากาศของวานา นาวา ฟอลส์ ได้ที่ฟิชเชอร์แมนส์ทาเวิร์น ในสระอินฟินิตี้"

#ภาพ 2 tower
    scene matchroom_1
    Fah             "เราจะมาต่อสำหรับเครื่องเล่นสไลด์ในแต่ละ tower "
    scene matchroomb_1
    Fah             "เราจะมาเริ่ม Tower นี้ก่อน Tower นี้เรียกว่า Tower B ประกอบด้วย 2 เครื่องเล่นคือ"
#รูปบูมเบอร์แรงโก้
    scene matchroombboomerango
    Fah             "สอง บูมเมอร์แรงโก้ มีสีเหลืองเป็นสไลเดอร์ที่ยาวที่สุดในประเทศไทย เล่นสูงสุด 6 คนต่อครั้ง ด้วยความเร็วสูงถึง 45 กิโลเมตรต่อชั่วโมง\nตัวผู้เล่นต้องมีส่วนสูงมากกว่า 122 กิโลเมตร น้ำหนักทั้งกลุ่มต้องมากกว่า 200 กิโลกรัม "
#รูปอะบิส
    scene matchroombabyss
    Fah             "หนึ่ง อะบิส เครื่องเล่นสีเขียวสไลเดอร์ขนาดใหญ่ที่สุดในประเทศไทย เล่นสูงสุด 6 คนต่อครั้ง ด้วยความเร็วสูงถึง 45 กิโลเมตรต่อชั่วโมง\nตัวผู้เล่นต้องมีส่วนสูงมากกว่า 137 กิโลเมตร น้ำหนักทั้งกลุ่มต้องมากกว่า 200 กิโลกรัม และผู้เล่นต้องมีอายุมากกว่า 12 ปี"

#รูปแผนที่ T A
    scene matchrooma1f
    Fah             "ต่อมา Tower นี้จะเรียก Tower A จะมี 5 เครื่องเล่น"
    Fah             "ชั้นแรกจะมี 4 เครื่องเล่น"
#รูปซุปเปอร์โบวล์
    scene matchroomasuper
    Fah             "เครื่องเล่นแรกคือ ซุปเปอร์โบวล์ สไลด์ดิ่งไต่ขอบไหลวนลงสู่ชามยักษ์สู่สระน้ำเบื้องล่าง ด้วยความเร็ว 18-50 กม./ชม ผู้เล่นจะต้องมีส่วนสูงมากกว่า 122 เซนติเมตร"
#รูปอินเนอร์ทูป 
    scene matchroomainner
    Fah             "อินเนอร์ทูป เครื่องเล่นสีส้ม เคลื่อนที่ความเร็วมากกว่า 25 กิโลเมตรต่อชั่วโมงผู้เล่นจะต้องมีส่วนสูงมากกว่า 122 เซนติเมตร"
#รูปมาสเตอร์บลาสเตอร์
    scene matchroomamaster
    Fah             "มาสเตอร์บลาสเตอร์ เป็นสไลค์สีเหลืองเคลื่องที่ด้วยความเร็ว 45 กิโลเมตรต่อชั่วโมง เป็นสไลค์ที่มีเทคโนโลยีจำลองภาพเสมือนจริงแบบ 360 องศา จากสหรัฐอเมริกา\nมีให้เลือก 3 แบบ\nผู้เล่นจะต้องมีส่วนสูงมากกว่า 122 เซนติเมตร"

#รูปแรทเลอร์
    scene matchroomarattler
    Fah             "แรทเลอร์ เครื่องเล่นที่ไหลไปตามท่อ จากความสูงกว่า 13 เมตรด้วยความเร็วมากกว่า 25 กิโลเมตรต่อชั่วโมง ผู้เล่นจะต้องมีส่วนสูงมากกว่า 122 เซนติเมตร"

#รูปแผนที่ชั้นสอง
    scene matchrooma2f
    Fah             "ชั้นสองจะมีเครื่องเล่นสองตัวคือ"
#รูปฟรีฟอลล์
    scene matchroomafreefall
    Fah             "ฟรีฟอลล์ เป็นสไลด์ดิ่งด้วยความเร็วสูง ด้วยความเร็วมากกว่า 50 กิโลเมตรต่อชั่วโมง\nผู้เล่นจะต้องมีส่วนสูงมากกว่า 122 เซนติเมตร และน้ำหนักไม่เกิน 136.4 กิโลกรัม"
#รูปอควาลูป
    scene matchroomaaqualoop
    Fah             "และเครื่องเล่นสุดท้าย อควาลูป สไลด์แห่งแรกของประเทศไทยที่มีสไลด์เหวี่ยงหมุน 360 องศา ด้วยความเร็วสูงสุดมากกว่า 60 กิโลเมตรต่อชั่วโมง\nผู้เล่นจะต้องมีส่วนสูงมากกว่า 122 เซนติเมตร และน้ำหนักไม่เกิน 136.4 กิโลกรัม"
    scene office

    jump chapter1_2
label chapter1_2:
    show fah3:
        xzoom 1.5 yzoom 1.5
    Fah             "สำหรับการแนะนำสถานที่คร่าวๆเสร็จเป็นที่เรียบร้อยที่อะไรสอบถามไหมค่ะ"
    menu:
            "เครื่องเล่นสำหรับเด็กมีอะไรบ้าง":
                "สำหรับครื่องเล่นสำหรับเด็กก็มี คิดดี้โคฟ และ วานา วันเดอร์แลนด์"
                jump chapter1_2
            "tower A มีอะไรบ้าง":
                "เครื่องเล่นของ tower A ก็จะมี"
                "ซุปเปอร์โบวล์  มาสเตอร์บลาสเตอร์ แรทเลอร์ ฟรีฟอลล์ อควาลูป"
                jump chapter1_2
            "tower B มีอะไรบ้าง":
                "บูมเมอร์แรงโก้ มีสีเหลืองเป็นสไลเดอร์ที่ยาวที่สุดในประเทศไทย เล่นสูงสุด 6 คนต่อครั้ง ด้วยความเร็วสูงถึง 45 กิโลเมตรต่อชั่วโมง\nตัวผู้เล่นต้องมีส่วนสูงมากกว่า 122 กิโลเมตร น้ำหนักทั้งกลุ่มต้องมากกว่า 200 กิโลกรัม"
                "อะบิส เครื่องเล่นสีเขียวสไลเดอร์ขนาดใหญ่ที่สุดในประเทศไทย เล่นสูงสุด 6 คนต่อครั้ง ด้วยความเร็วสูงถึง 45 กิโลเมตรต่อชั่วโมง\nตัวผู้เล่นต้องมีส่วนสูงมากกว่า 137 กิโลเมตร น้ำหนักทั้งกลุ่มต้องมากกว่า 200 กิโลกรัม และผู้เล่นต้องมีอายุมากกว่า 12 ปี"
                jump chapter1_2
            "เครื่องเล่นสำหรับผู้ใหญ่":
                "เครื่องเล่นสำหรับผู้ใหญ่ก็จะมีสไลเดอร์จากที่สูงทั้งหมด ก็จะมี"
                "เครื่องเล่นของ tower A ก็จะมี"
                "ซุปเปอร์โบวล์  มาสเตอร์บลาสเตอร์ แรทเลอร์ ฟรีฟอลล์ อควาลูป"
                "บูมเมอร์แรงโก้ มีสีเหลืองเป็นสไลเดอร์ที่ยาวที่สุดในประเทศไทย เล่นสูงสุด 6 คนต่อครั้ง ด้วยความเร็วสูงถึง 45 กิโลเมตรต่อชั่วโมง\nตัวผู้เล่นต้องมีส่วนสูงมากกว่า 122 กิโลเมตร น้ำหนักทั้งกลุ่มต้องมากกว่า 200 กิโลกรัม"
                "อะบิส เครื่องเล่นสีเขียวสไลเดอร์ขนาดใหญ่ที่สุดในประเทศไทย เล่นสูงสุด 6 คนต่อครั้ง ด้วยความเร็วสูงถึง 45 กิโลเมตรต่อชั่วโมง\nตัวผู้เล่นต้องมีส่วนสูงมากกว่า 137 กิโลเมตร น้ำหนักทั้งกลุ่มต้องมากกว่า 200 กิโลกรัม และผู้เล่นต้องมีอายุมากกว่า 12 ปี"
                jump chapter1_2
            "ไม่มีอะไรถามแล้ว":
                "งั้นเรามาต่อกันเลยนะคะ"


    Fah             "สำหรับการฝึกงานของเทอมนี้จะมีระยะเวลา 4 เดือน "
    Fah             "หลังฝึกเสร็จจะมีการทดสอบเพื่อทำการคัดเลือกเข้าฝึกงาน ขอให้โชคดีค่ะ"
    hide screen Fah
    scene computer
    Player          "วันแรกเหนื่อยจัง เอาจริงการทำงานที่นี่ก็เหมือนๆหลายๆที่นะ ไม่ได้ยากอย่างที่คิด"
    scene computer2
    
    Bell            "นี่ๆ "
    scene computer
    Player          "...."
    scene office
    show bell_idle:
        xzoom 1.5 yzoom 1.5
    Bell            "เป็นอะไรหรือดู หน้าตาดูเครียดเลย"
    Player          "อ้อๆเปล่าเลยๆ สบายดีๆ มีอะไรหรอก"
    Player          "เอ๊ะ เบลเหรอ"
    Bell            "เอ นี่นายคือ[Player]ใช่ไหม ที่เรียนตอน ม.ปลายที่เดียวกัน"
    scene officeb with dissolve
    "(แย่แล้วดันมาเจอมาตอนนี้ ถ้าเป็นคู่แข่งละก็ แย่แน่เลย)"
    scene office
    show bell_idle:
        xzoom 1.5 yzoom 1.5
    Bell            "ว่าไง...เป็นไงบ้าง ไม่ได้เจอกันนานเลยนะ ^^"
    Player          "เออ คือ ก็สบายดีนะ แล้วเธอละ"
    Bell            "ก็สบายดี ฉันก็เริ่มฝึกงานเหมือนกับนายเลย"
    Player          "นี่เบล เสร็จจากนี่ไปกินข้าวด้วยกันไหมมีเรื่องให้คุยกันเยอะเลย"
    "ฮิ ต้องรีบตัดบทสนทนาก่อนที่เธอจะพูดอะไรออกมา"
    Bell            "เบล ก็ได้นะ"
    "เย้ สำเร็จ ชวนสำเร็จแล้ว"
    Player          "โอเค แล้วเราจะรอนะ"

    #ตัวละครฟ้าด้านข้าง
    Fah             "นั้นแฟนเก่าเหรอ"
    Player          "จะเป็นไปได้ยังไงละครับ"
    Player          "คือว่าพวกเราเรียนที่เดียวกันตอนมัธยมต้นและปลายกัน"
    Fah             "บังเอิญจังนะ"
    "ผมได้มองหน้าเบล"
    Player          "แล้วเบลมีอะไรหรืออะไรหรือเปล่า"

    Bell            "อ้อใช่ เกิอบ ลืมเลยนี่ค่ะงานอาร์ตที่พี่ฟ้าได้สั่งไว้คะ"


    scene showdrawing
    #รูปวาดเบล
    "เมื่อเบลได้ให้งานให้ผมกับพี่ฟ้าดู ผมก็ได้เห็นความสามารถที่ของเบล ซึ่งมันเป็นงานที่ดีกว่าคนทั่วไปมาก"
    "เพราะงานดีมากๆ ไม่นึกว่าแค่ไม่เจอกัน 3-4 ปี จะเปลียนไปขนาดนี้"

    menu :
                "ว้าว เบลนี้เปลี่ยนไปเยอะเลยนะ":
                        scene office
                        show bell_idle:
                            xzoom 1.5 yzoom 1.5
                        Bell  "อ่า ขอบคุณมากๆนะ ที่ผ่านมาเบลได้ไปฝึกอย่างหนักหน่วง "
                        Fah   "งานดีมากๆเลยละ ขอบใจมากนะ"
                        Bell  "ขอบคุณค่ะ งั้นเบลไปก่อน"
                        Bell  "เจอกันที่ร้านอาหารหลังเลิกงานนะ"
                        $ B_Relation = B_Relation + 1

                "ผลงานเธอยังเหมือนเดิมฮะ":
                        scene office
                        show bell_idle:
                            xzoom 1.5 yzoom 1.5
                        Bell "ว่าไงนะ เราฝึกมาตั้งนานนะ"
                        Fah   "โอเคเลย ขอบใจมากๆเลยนะ"
                        Bell  "งั้นเจอกันตอนร้านอาหารแล้วกัน"
                        $ B_Relation = B_Relation -1
    
    #ฉากร้านอาหาร
    scene restaurant
    show bell_idle:
        xzoom 1.5 yzoom 1.5
        #ที่ร้านอาหาร
    Player          "ใครมันจะไปคิดว่าจะมาเจอเธอที่นี่ละ"
#ฉากในร้านอาหาร+เบล
    Bell            "นั้นสินะ บังเอิญจัง แล้วนายเป็นยังไงบ้างที่ผ่านมา"
                #คำถาม
    menu :
        "ก็เหนื่อยอยู่นะ เจอเรื่องอะไรหลายๆอย่างเลยกว่าจะถึงจุดนี้":
                Bell "เหมือนกันเลย เราคิดว่าสกิลเราเยอะกว่าแต่ก่อนมากเลย 555"
                Bell "เออ...ใช่"
                $ B_Relation = B_Relation + 1
                
        "สบายๆอยู่แล้ว ระดับเราแล้ว":
                Bell "จริงสิ อย่างนายเก่งอยู่แล้วละ ระดับนายละนะ"
                $ B_Relation = B_Relation - 0
        "ยุ่งเรื่องคนอื่นจังน้า เธอเนี่ย":
                Bell "กวนประสาทเก่งไม่เปลียนนะนายเนี่ย"
                Player "แฮะ โทษทีๆนะ"
                Bell "หึ เออ...ใช่"
                $ B_Relation = B_Relation -1

    #ทำเป็นรูปนึก
    Bell            "นายรู้ไหม กายที่นายชอบแข่งสร้างกันผลงานกันประจำก็มาแข่งเหมือนกันนะ"
    Player          "หืม จริงเหรอ หมอนั้นไม่รู้ตอนนี้เก่งขนาดไหนแล้วนี่สิ"
    Bell            "แต่ก็คงไม่เก่งไปกว่านายหรอก 555"
    Player          "ถ้าเป็นอย่างนั้นก็ดีสินะ"
    stop sound fadeout 1.0
    jump chapter2_1
    return

label chapter2_1 :

#วาดฉากห้องแข่ง
        play sound "audio/gura_bgm.mp3" volume 0.9 loop
        scene matchroom
        show yuri1 :
            xzoom 1.5 yzoom 1.5
        #การทดสอบครั้งที่ 1
        Yuri            "เอาละคะ ขอแนะนำก่อนนะคะ พี่ชื่อยูริ พี่จะมาแนะนำวิธีการแข่งขันนะค่ะ"
        Yuri            "เริ่มแรกจากผู้เข้าคัดเลือก 15 คน จะมีผู้เข้าผ่านการเข้าเลือก 2 คน ที่นอกจากจบการฝึกงานแล้วยังได้มีโอกาสเข้ารับการทำงาน"
        jump g1how1
screen playg1: 
    imagebutton:
        xalign 0.5 yalign 0.95
        idle "g1_play.png"
        action Jump("playg1") alt "ejection"
screen g1h1: 
    imagebutton:
        xalign 0.5 yalign 0.5
        idle "g1_how1.png"
    imagebutton:
        xalign 0.05 yalign 0.5
        idle "g1_next1.png"
    imagebutton:
        xalign 0.95 yalign 0.5
        idle "g1_next2.png"
        action Jump("g1how2") alt "ejection"
screen g1h2: 
    imagebutton:
        xalign 0.5 yalign 0.5
        idle "g1_how2.png"
    imagebutton:
        xalign 0.05 yalign 0.5
        idle "g1_next1.png"
        action Jump("g1how1") alt "ejection"
    imagebutton:
        xalign 0.95 yalign 0.5
        idle "g1_next2.png"
        action Jump("g1how3") alt "ejection"
screen g1h3: 
    imagebutton:
        xalign 0.5 yalign 0.5
        idle "g1_how3.jpg"
    imagebutton:
        xalign 0.05 yalign 0.5
        idle "g1_next1.png"
        action Jump("g1how2") alt "ejection"
    imagebutton:
        xalign 0.95 yalign 0.5
        idle "g1_next2.png"
        action Jump("g1how4") alt "ejection"
screen g1h4: 
    imagebutton:
        xalign 0.5 yalign 0.5
        idle "g1_how4.jpg"
    imagebutton:
        xalign 0.05 yalign 0.5
        idle "g1_next1.png"
        action Jump("g1how3") alt "ejection"
    imagebutton:
        xalign 0.95 yalign 0.5
        idle "g1_next2.png"
label waithow2:
        window hide   
        pause
        
        jump waitend
        return
label g1how1:
        show screen playg1  
        show screen g1h1
        hide screen g1h2
        jump waithow2
        # jump game_1  
label g1how2:
        hide screen g1h1
        show screen g1h2
        hide screen g1h3
        jump waithow2
        # jump game_1     
label g1how3:
        hide screen g1h2
        show screen g1h3
        hide screen g1h4
        jump waithow2
        # jump game_1  
label g1how4:
        hide screen g1h3
        show screen g1h4
        jump waithow2
        # jump game_1   
label playg1:
        hide screen g1h1
        hide screen g1h2
        hide screen g1h3
        hide screen g1h4
        hide screen playg1
        jump game_1            
label chapter2_1_1:
        
        
        Yuri            "สำหรับการแข่งวันนี้ก็เสร็จสิ้นแล้ว ขอบคุณทุกคนมากค่ะ"
        Yuri            "สำหรับผลการแข่งขันโปรดดูในเมล์ของผู้เข้าแข่งขันได้เลยค่ะ"
#วาดมุมเห็นกางเกงเกม + ส่งเสียง
        #หน้าประกาศผล
        if grade_g2 == 'F':
            jump fail_1
        else:
            jump chapter2_2
  
        return

label chapter2_2 :
#รูปร้านอาหาร
        scene restaurant
        show bell_idle:
            xzoom 1.5 yzoom 1.5
        Bell            "วันแรกเป็นไงบ้างละ"
        Player          "อืม..ก็ยากอยู่นะ วันนี้"
        Bell            "วันนี้เขาจะประกาศผลใช่ไหมคืนนี้"

      
        "เสียง discord"
        Player          "ทาง บ. เขาได้ส่งคะแนนมาแล้ว"
        Bell            "นายคิดว่านายจะได้รอบหน้าจะเป็นยังไง"
        Player          "ก็คงได้คะแนนกลางๆ คงไม่ได้เยอะหรอก"

        Bell            "ก็อยู่ที่ดวงแล้วอะนะ ^^"
        Player          "ไม่จริงน่า ฉันกับเธอเนี่ยนะ บังเอิญไปป่าว"
        Bell            "นั้นสินะ บังเอิญจังแต่ก็ดีแล้วละ"
        Player          "นั้นเรามาคุยกันพรุ่งนี้กันดีกว่า คำถามพรุ่งนี้เกียวกับอะไรนะ"
        Bell            "เหมือนจะเป็นเกี่ยวกับพวกสถานที่ภายในสวนน้ำนะ ถ้าเราจำได้ก็คงไม่ยากหรอก"
        jump chapter3
#วาดหนังสือ img maping
        return

label chapter2_3 : 
#รูปร้านอาหาร
        scene restaurant
        show bell_idle:
            xzoom 1.5 yzoom 1.5
                #ร้านอาหาร
        Bell            "เป็นไงบ้างละวันนี้"      
        Player          "เฮ้อออ ยากอยู่ แต่ก็ผ่านมาได้ "
                #คำถาม
        menu:
                "แล้วเขาจะประกาศคู่ตอนไหนเหรอ":
                        Bell "คืนนี้ละ อย่าเครียดเลย ทำให้ดีที่สุดก็พอแล้ว"
                        $ B_Relation = B_Relation -0
                "พูดถึง นายอยากคู่กับฉันไหม":
                        Bell "ก็ได้นะ นายเองเก่งเหมือนกันนี่ ><"
                        Player "แล้วเขาจะประกาศคู่ตอนไหนเหรอ"
                        Bell "คืนนี้ละ อย่าเครียดเลย ทำให้ดีที่สุดก็พอแล้ว"
                        $ B_Relation = B_Relation + 1
        
      
        "เสียง discord"

        Player          "เอ๊ะ เสียงแจ้งเตือน"
        Player          "ทาง บ. เขาได้ส่งผลมาแล้ว"
        Bell            "นายคิดว่าคู่ของนายจะเป็นคนแบบไหนเหรอ"
        Player          "ก็น่าจะเป็นจะเป็นธรรมดาทั่วไปละ คงไม่ได้เป็นคนเก่งอะไรหรอก"
        Bell            "ก็อยู่ที่ดวงแล้วอะนะ ^^"
        Bell            "เอ๋...นายกับฉันอยู่ทีมเดียวกันละ"
        Player          "ไม่จริงน่า ฉันกับเธอเนี่ยนะ บังเอิญไปป่าว"
        Bell            "นั้นสินะ บังเอิญจังแต่ก็ดีแล้วล่ะ"
        Player          "นั้นเรามาคุยกันพรุ่งนี้กันดีกว่า คำถามพรุ่งนี้เกียวกับอะไรนะ"
        Bell            "เหมือนจะเป็นเกียวกับพวกสถานที่ภายในสวนน้ำนะ ถ้าเราจำได้ก็คงไม่อยากหรอก"
        Bell            "เรามีหนังสือรวมข้อมูลสถานที่ด้วย อยากรู้ตรงไหนเป็นพิเศษไหม"
        Bell            "อ่าฮะ"
#วาดหนังสือ img maping
        jump chapter3
        return


label chapter3:
        scene matchroom
#วาดฉากห้องแข่ง
        #การทดสอบครั้งที่ 2
        "การทดสอบครั้งที่ 2"
        "มาถึง บ. ซะที"
#ตัวละครกาย

        Kai             "เป็นไงบ้างละ ได้ข่าวว่านายได้คะแนนน้อยจนผ่านแบบเกือบไม่รอด"
                #คำถาม
        menu : 
                "เราพลาดหลายข้อไปหน่อย":
                        Kai "ระวังคะแนนนายจะถูกเรานำนะ 555 "
                        Kai "แค่ตอนนี้คะแนนเรายังมากกว่านายเยอะ"
                        $ K_Relation = K_Relation - 1
                "เราพลาดแค่ครั้งนี้ละ ครั้งต่อไปคะแนนเราก็นำนายอยู่ดี":
                        Kai "แล้วเราจะเคยดูละ แค่ตอนนี้คะแนนเรายังกว่านาย"
                        $ K_Relation = K_Relation - 2
        show yuri1:
            xzoom 1.5 yzoom 1.5
        Yuri            "เอาละคะๆ ก่อนอื่นก็ขอต้อนรับและยินดีทุนคนที่ผ่านเข้ารอบนะค่ะ ยินดีด้วย เย้"
        Npc             "เย้....."
        Yuri            "ก่อนอื่นขออธิบายด่านนี้ซ้ำอีกรอบนะคะ"
        jump chapter3_1
label chapter3_1:
        scene matchroom
        hide screen yuri1
        show yuri1:
            xzoom 1.5 yzoom 1.5
        Yuri            "การทดสอบรอบที่ 2 "
        Yuri            "กติกาก็คือผู้เข้าแข่งขันจะต้องตอบคำถามจากคำถามที่เจอ"
        Yuri            "หากตอบถูกจะสุ่มการเดินโดยอ้างอิงจากกาารสุ่มลูกเต๋ามากถึง 6 ช่อง หากตอบผิดจะสุ่มได้มมากสุ่ม 3 ช่อง"
        Yuri            "ในนั้นจะมีมินิเกม 2 เกมคือเกมหาของ และ เกมทำอาหาร"
        jump g2how1

screen playg2: 
    imagebutton:
        xalign 0.5 yalign 0.95
        idle "g1_play.png"
        action Jump("playg2") alt "ejection"
screen g2h1: 
    imagebutton:
        xalign 0.5 yalign 0.5
        idle "g1_how1.png"
    imagebutton:
        xalign 0.05 yalign 0.5
        idle "g1_next1.png"
    imagebutton:
        xalign 0.95 yalign 0.5
        idle "g1_next2.png"
        action Jump("g2how2") alt "ejection"
screen g2h2: 
    imagebutton:
        xalign 0.5 yalign 0.5
        idle "g2_how2.png"
    imagebutton:
        xalign 0.05 yalign 0.5
        idle "g1_next1.png"
        action Jump("g2how1") alt "ejection"
    imagebutton:
        xalign 0.95 yalign 0.5
        idle "g1_next2.png"
        action Jump("g2how3") alt "ejection"
screen g2h3: 
    imagebutton:
        xalign 0.5 yalign 0.5
        idle "g2_how3.png"
    imagebutton:
        xalign 0.05 yalign 0.5
        idle "g1_next1.png"
        action Jump("g2how2") alt "ejection"
    imagebutton:
        xalign 0.95 yalign 0.5
        idle "g1_next2.png"
        action Jump("g2how4") alt "ejection"
screen g2h4: 
    imagebutton:
        xalign 0.5 yalign 0.5
        idle "g2_how4.png"
    imagebutton:
        xalign 0.05 yalign 0.5
        idle "g1_next1.png"
        action Jump("g2how3") alt "ejection"
    imagebutton:
        xalign 0.95 yalign 0.5
        idle "g1_next2.png"
label waithow:
        window hide   
        pause
        
        jump waitend
        return
label g2how1:
        show screen playg2 
        show screen g2h1
        hide screen g2h2
        jump waithow
        # jump game_1  
label g2how2:
        hide screen g1h1
        show screen g2h2
        hide screen g2h3
        jump waithow
        # jump game_1     
label g2how3:
        hide screen g2h2
        show screen g2h3
        hide screen g2h4
        jump waithow
        # jump game_1  
label g2how4:
        hide screen g2h3
        show screen g2h4
        jump waithow
        # jump game_1   
label playg2:
        hide screen g2h1
        hide screen g2h2
        hide screen g2h3
        hide screen g2h4
        hide screen playg2
        scene bgg2
        jump game_2
label chapter3_0:
        hide screen scoreboard_g1
        hide screen finalscore
        show yuri1:
            xzoom 1.5 yzoom 1.5
        Yuri            "สำหรับการแข่งขันวันนี้ก็จบลงแล้ว ขอบคุณทุกคนมาก"
        if B_Relation >=3 :
            jump chapter4_1
        elif B_Relation >=1 and B_Relation <=2  :
            jump chapter4_2
        else:
            jump chapter4_3
        
        return


label chapter4_1 :
#ฉากร้านอาหารฑ
        scene house
        show bell_idle:
            xzoom 1.5 yzoom 1.5
        #ตอนจบ
        Bell            "นี่ๆหนึ่ง ทาง บ. เขาส่งคะแนนมาแล้วละ"
        Player          "แล้ว คะแนนของพวกเราเป็นยังไงบ้างละ"
        Bell            "ทีมเราผ่านการคัดเลือกได้คะแนนรวมทั้งสิ้น"
        Player          "เอ๋....มีโทรศัพท์เข้า"
        Player          "สวัสดีครับ นี่ [Player]"
        Fah             "ยินดีด้วยนะพวกเธอ หวังว่าพวกเธอจะเป็นเพื่อนร่วมงานที่ดีนะ"
        Bell            "ได้เลยค่ะ ขอบคุณมากเลยนะคะ"
        jump ending
        return
label chapter4_2 :
#ฉากร้านอาหาร
        scene house
        show bell_idle:
            xzoom 1.5 yzoom 1.5
        #ตอนจบ
        Bell            "นี่ๆ[Player] ทาง บ. เขาส่งคะแนนมาแล้วละ"
        Player          "แล้ว คะแนนของพวกเราเป็นยังไงบ้างละ"
        Bell            "ทีมเราผ่านการคัดเลือกได้คะแนนรวมทั้งสิ้น"
        Player          "เอ๋....มีโทรศัพท์เข้า"
        Player          "สวัสดี นี้[player]ครับ"
        Fah             "ยินดีด้วยนะพวกเธอ หวังว่าพวกเธอจะเป็นเพื่อนร่วมงานที่ดีนะ"
        Bell            "ขอบคุณนะคะ"
        jump ending
        return
label chapter4_3 :
#ฉากร้านอาหาร

        scene house
        show bell_idle:
            xzoom 1.5 yzoom 1.5
        #ตอนจบ
        Bell            "นี่ๆ[Player] ทาง บ. เขาส่งคะแนนมาแล้วละ"
        Player          "แล้ว คะแนนของพวกเราเป็นยังไงบ้างละ"
        Bell            "ทีมเราผ่านการคัดเลือกได้คะแนนรวมทั้งสิ้น"
        Player          "เอ๋....มีโทรศัพท์เข้า"
        Player          "สวัสดี นี้[Player]ครับ"
        Fah             "ยินดีด้วยนะพวกเธอ หวังว่าพวกเธอจะเป็นเพื่อนร่วมงานที่ดีนะ"
        Bell            "ก็หวังว่านะ....."
        jump ending
        return

label fail_waiting :
        return

label fail_1 :          #ถ้าตกรอบครั้งที่ 1
#วาดฉาก lobby
        Unknown         "อืม นายตกรอบเหรอ ฉันจะให้โอกาสนายอีกครั้ง ฉันจะทำการย้อนเวลาให้นายไปตอนคืนก่อนวันทดสอบ"
        $ G2 = 0
        $ scoreG2 = 0
        $ picturecheck = 0
        $ ingame2_score = 0
        $ picture1 = 0
        $ picture2 = 0
        $ picture3 = 0
        $ picture4 = 0
        $ picture5 = 0
        "......ย้อนกลับก่อนการทดสอบ......"
        jump chapter2_1
        return



label ending_fail :          #แพ้เกม
#วาดฉาก lobby
        Unknown         "ฉันให้โอกาศนายแล้ว แต่นายกลับแพ้ได้ยังไง"
        Unknown         "มันจบละ เจอกันใหม่ครั้งหน้า ขอให้เตรียมให้ดีนะ"
        ".............."
        
        return

label ending :
#วาดฉาก lobby
        scene menu_bg
        #สรุปคะแนน
        Unknown "เอาละ ยินดีต้อนรับกลับนะ  ยินดีด้วยที่สามารถเอาชนะเกมนี้ได้"
        show screen final_g1
        show screen  final_g2
        Unknown "นี่คือสรุปคะแนนที่ทำได้"
        Unknown "สุดท้ายนี้ก่อนลาจากกัน ขอบคุณที่เล่นมาถึงตรงนี้นะ  \nกด Enter หรือ คลิกเพือกลับสู่เมนูหลัก"
        return
        # 
screen final_g1:
    
    imagebutton:
        xalign 0.15 yalign 0.1
        idle "final.png"
    imagebutton:
        xalign 0.155 yalign 0.02
        idle "gamename1.png"
    vbox:
        xalign 0.26
        ypos -40
        text "{color=#C65A77}{size=400}[grade_g2]{/size}{/color}"
    vbox:
        xalign 0.23
        ypos 350
        text "{color=#000000}{size=70}คุณได้ตอบถูก{/size}{/color}"
    vbox:
        xalign 0.23
        ypos 390
        text "{color=#C65A77}{size=140}[scoreG2] / 100{/size}{/color}"
    vbox:
        xpos 0.15
        ypos 550
        text "{color=#000000}{size=55}ภาพที่ 1 : {color=#C65A77}[picture1]{/color}{/size}{/color}"
    vbox:
        xalign 0.35
        ypos 550
        text "{color=#000000}{size=55}ภาพที่ 2 : {color=#C65A77}[picture2]{/color}{/size}{/color}"
    vbox:
        xpos 0.15
        ypos 630
        text "{color=#000000}{size=55}ภาพที่ 3 : {color=#C65A77}[picture3]{/color}{/size}{/color}"
    vbox:
        xalign 0.35
        ypos 630
        text "{color=#000000}{size=55}ภาพที่ 4 : {color=#C65A77}[picture4]{/color} {/size}{/color}"
    vbox:
        xpos 0.23
        ypos 700
        text "{color=#000000}{size=55}ภาพที่ 5 : {color=#C65A77}[picture4]{/color} {/size}{/color}"


screen final_g2:
    imagebutton:
        xalign 0.85 yalign 0.1
        idle "final.png"
    imagebutton:
        xalign 0.845 yalign 0.02
        idle "gamename2.png"
    vbox:
        xalign 0.76
        ypos -40
        text "{color=#C65A77}{size=400}[grade]{/size}{/color}"
    vbox:
        xalign 0.78
        ypos 350
        text "{color=#000000}{size=70}คุณได้ตอบถูก{/size}{/color}"
    vbox:
        xalign 0.76
        ypos 390
        text "{color=#C65A77}{size=140}[realscore] / [totalAns_g1]{/size}{/color}"
    vbox:
        xalign 0.76
        ypos 550
        text "{color=#000000}{size=70}ได้ตอบผิด : [scorefail_g1]{/size}{/color}"
    vbox:
        xalign 0.78
        ypos 630
        text "{color=#000000}{size=70}เป็นเปอร์เซ็น : [percent_g1] %{/size}{/color}"