screen choose_story():
    $ hide = Hide("choose_story")

    vbox:
        button: 
            text "Change Preferences":
                idle_color '#fff'
                hover_color "#00ff00"
            action [hide, Show("change_preferences")]