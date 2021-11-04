define e = Character("Eileen")

label inminigame2:
    
    scene vana_fb
    "ถึงเวลาเล่นเกม minigame ที่สองแล้ว กติกาคือผู้เล่นจะต้องกดโน็ตตามจังหวะดนตรี ยิ่งกดถูกมากจะยิ่งได้แต้มเดินเยอะ"
    "ให้ใช้ปุ่ม ลูกศรบนคีย์บอร์ดในการควบคุม ( Arrow keys )"
    "งั้นเริ่มกันเลย"
    # start the rhythm game
    # window hide
    $ quick_menu = False

    # avoid rolling back and losing game state
    $ renpy.block_rollback()
    
    call screen rhythm_game(
        'audio/my-music.mp3', 
        'audio/my-music.beatmap.txt'
        )
    # avoid rolling back and entering the game again
    $ renpy.block_rollback()

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
