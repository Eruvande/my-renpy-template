screen change_preferences():
    $ hide = Hide("change_preferences")

    vbox:
        button:
            text "Go back to Stories":
                idle_color '#fff'
                hover_color "#00ff00"
            action [hide, Show("choose_story")]