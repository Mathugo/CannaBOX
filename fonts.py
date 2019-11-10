from kivy.core.text import LabelBase

def loadFonts():
    LabelBase.register(name="QuickSand",
        fn_regular="fonts/Quicksand-Regular.otf",
        fn_bold="fonts/QuickSand-Bold.otf"
    )
    LabelBase.register(name="Cantarell",
        fn_regular="fonts/Cantarell-Regular.ttf",
        fn_bold="fonts/Cantarell-Bold.ttf"
    )
    LabelBase.register(name="OpenSans",
        fn_regular="fonts/OpenSans-Regular.ttf",
        fn_bold="fonts/OpenSans-Bold.ttf"
    )
    LabelBase.register(name="Amble",
        fn_regular="fonts/Amble-Regular.ttf",
        fn_bold="fonts/Amble-Bold.ttf"
    )
