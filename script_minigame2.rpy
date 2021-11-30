define e = Character("Eileen")
screen howmini2:
    imagebutton:
        xalign 0.5 yalign 0.2
        idle "g1_howm2.jpg"

label inminigame2:
    
    scene vana_fb
    show screen howmini2
    "เมื่อผู้เล่นผ่านช่องที่ 30 จะมี minigame ที่สอง กติกาคือผู้เล่นจะต้องกดโน็ตตามจังหวะดนตรี ยิ่งกดถูกมากจะยิ่งได้แต้มเดินเยอะ"
    "ให้ใช้ปุ่ม ลูกศรบนคีย์บอร์ดในการควบคุม ( Arrow keys )"
    "งั้นเริ่มกันเลย"
    $ ui.timer(1.5, ui.jumps("in2"))
    "จะเริ่มใน 3"
label in2:
    $ ui.timer(1.5, ui.jumps("in1"))
    "จะเริ่มใน 2"
label in1:
    $ ui.timer(1.5, ui.jumps("in0"))
    "จะเริ่มใน 1"
    $ ui.timer(1.0, ui.jumps("in0"))
    hide screen howmini2
label in0:
    
    # start the rhythm game
    # window hide
    $ quick_menu = False

    # avoid rolling back and losing game state
    # $ renpy.block_rollback()
    scene vana_fb
    call screen rhythm_game(
        'audio/my-music.mp3' , 
        'audio/my-music.beatmap.txt'
        )
    # avoid rolling back and entering the game again
    # $ renpy.block_rollback()

    # restore rollback from this point on
    $ renpy.checkpoint()

    $ quick_menu = True
    window show

    $ num_hits, num_notes = _return
    play sound "audio/gura_bgm.mp3" volume 0.5 loop
    e "คุณได้ [num_hits] จากทั้งหมด [num_notes]. ขอบคุณที่มาเล่นนะ"
    if num_hits >= 22:
        $ roll = 4
    elif num_hits >= 17:
        $ roll = 3
    elif num_hits >= 12:
        $ roll = 2
    elif num_hits < 7:
        $ roll = 1
    show screen choice_menu(x=None) 
    show screen scoreboard_g2
    show img with dissolve:
        xpos -110 ypos -1900 zoom 1.6
    jump check2

    return
