init python:
    class pnco:
        def __init__(self, name, img, pos,
            act = None, enabled = True, items = []
        ):
            self.name = name
            self.img = img
            self.pos = pos
            self.act = act
            self.enabled = enabled
            self.items = items

    class pncs:
        def __init__(self, name, clicks = [], darkness = None):
            self.name = name
            self.clicks = clicks
            self.darkness = darkness
        def clicked(self, o, p):
            if o.items:
                # p.got(i[0], i[1])
                msg.msg("ได้เจอ {}.".format(o.items[0]))
                self.clicks.remove(o)
        def add(self, click):
            if not click in self.clicks:
                self.clicks.append(click)
                msg.msg("New location: {}".format(click.name))
        def rem(self, click):
            if click in self.clicks:
                self.clicks.remove(click)
        def items_left(self):
            for i in self.clicks:
                if len(i.items):
                    return True
            else:
                return False

screen pnc(p , g, isMap = False):
    modal True
    for i in g.clicks:
        if isinstance(i, basestring):
            add i
        else:
            button:
                background None padding 0,0
                pos i.pos
                add i.img
                focus_mask True
                if isMap:
                    anchor .9,1.0
                    at btn
                else:
                    anchor 0.0,0.0
                    at map_btn
                if i.enabled:
                    if i.act:
                        action Function(g.clicked, i, p), i.act
                    else:
                        action Function(g.clicked, i, p)



    default mouse = (0,0)
    if g.darkness:
        timer 0.02 repeat True action SetScreenVariable("mouse", renpy.get_mouse_pos())
        add g.darkness pos mouse align .5,.5 at additive(.02)

    if g.items_left():
        imagebutton:
            xalign 0.24 yalign 0.05
            idle "minig1p.jpg"
        button:
            align 1.0,0.0 background "#944" padding 10,10 margin 20,20
            text "ค้นหาเสร็จสิ้น"
            action Return(False)
    else:
        button:
            align 1.0,0.0 background "#944" padding 10,10 margin 20,20
            text "Done"
            action Return(True)
init python:
    def return_mouse_pos():
        return renpy.get_mouse_pos()




transform map_btn:
    on idle:
        easein .2 additive 0
    on hover:
        easein .2 additive .3

    on insensitive:
        easein .2 additive 0


