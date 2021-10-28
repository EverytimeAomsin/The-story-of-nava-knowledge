define e = Character("Eileen")

label inminigame2:
    
    scene vana_fb
    e "Let's play a rhythm game!"

    # start the rhythm game
    # window hide
    $ quick_menu = False

    # avoid rolling back and losing game state
    $ renpy.block_rollback()
    
    call screen rhythm_game(
        'audio/my-music.ogg', 
        'audio/my-music.beatmap.txt'
        )
    # avoid rolling back and entering the game again
    $ renpy.block_rollback()

    # restore rollback from this point on
    $ renpy.checkpoint()

    $ quick_menu = True
    window show

    $ num_hits, num_notes = _return
    e "You hit [num_hits] notes out of [num_notes]. Good work!"
    show screen choice_menu(x=None) 
    show screen scoreboard_g2
    show img with dissolve:
        xpos -110 ypos -1900 zoom 1.6
    jump check

    return
