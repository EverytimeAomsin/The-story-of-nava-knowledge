﻿# Define some point and click objects
default classroom_apple = pnco(
    "Apple",
    "hidden object/classroom/apple.png",
    (69, 590),
    items = ["ตุ๊กตา"]
    )
default classroom_book = pnco(
    "Book",
    "hidden object/classroom/book.png",
    (980, 780),
    items = ["หนังสือ"]
    )
default classroom_knife = pnco(
    "Knife",
    "hidden object/classroom/knife.png",
    (1588, 940),
    items = ["ห่วงยาง"]
    )
default classroom_kobe = pnco(
    "Phone",
    "hidden object/classroom/kobe.png",
    (1317, 972),
    items = ["มือถือ"]
    )
default classroom_lube = pnco(
    "Lube",
    "hidden object/classroom/lube.png",
    (1182, 849),
    items = ["ขวด"]
    )
default classroom_note = pnco(
    "Note",
    "hidden object/classroom/note.png",
    (805, 513),
    items = ["โปสเตอร์"]
    )
default classroom_scissors = pnco(
    "Scissors",
    "hidden object/classroom/scissors.png",
    (158, 901),
    items = ["เสื้อชูชีพ"]
    )

# Define a point and click location
default hidden_object = pncs(
    "Classroom",
    [
        classroom_apple,
        classroom_book,
        classroom_knife,
        classroom_kobe,
        classroom_lube,
        classroom_note,
        classroom_scissors,
    ],
    darkness = "darkness"
    
)


label hidden_object:
    show screen hide_item
    "ยินดีต้อนรับสู่ minigame รอบที่ 1 นะ กติกาก็คือต้องช่วยฉันหาของต่อไปนี้คือ"
    "ของที่ต้องหา\nแอปเปิ้ล  หนังสือ  มีด  ขวด มือถือ และกระดาษโน็ต\nถ้าหาได้ครบจะได้โอกาศเดินฟรี 4-8 ช่อง ถ้าไม่ครบจะได้แค่่ 1-4 ช่อง"
    hide screen hide_item
    hide img with dissolve
    hide test1 with dissolve
    hide screen question8
    hide screen question9
    hide screen question10
    hide screen question11
    hide screen question12
    hide screen question13
    hide screen scoreboard_g2
    hide screen choice_menu
    show office
    call screen pnc(p = None, g=hidden_object)
    if _return:
        "นี้เจอหมดทุกอย่างเลยเหรอ"
        "เก่งจริงๆ ขอบคุณที่มาเล่นด้วยนะ"
        $ roll = renpy.random.randint(4, 8)
        show screen choice_menu(x=None) 
        image img  = Image("images/map2.png", xpos = 0, ypos = 0)
        image test1 = Image("images/test1.jpg", xpos = 0, ypos = 0)
        show screen scoreboard_g2
        show img with dissolve:
            xpos -110 ypos -1900 zoom 1.6
        

        jump check
    else:
        "ยังหาได้ไม่ครบเลย ขอบคุณที่มาเล่นด้วยนะ"
        $ roll = renpy.random.randint(1, 4)
        show screen choice_menu(x=None) 
        show screen scoreboard_g2
        show img with dissolve:
            xpos -110 ypos -1900 zoom 1.6
        
        jump check

    screen hide_item:
        imagebutton:
            xalign 0.8 yalign 0.84
            idle "hide_item.png"
 
