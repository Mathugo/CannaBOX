from kivy.core.text import LabelBase

def loadFonts():
    LabelBase.register(name="QuickSand",
        fn_regular="fonts/QuickSand/Quicksand-Regular.otf",
    #    fn_bold="fonts/QuickSand-Bold.otf"
    )
    LabelBase.register(name="Cantarell",
        fn_regular="fonts/Cantarell/Cantarell-Regular.ttf",
        fn_bold="fonts/Cantarell/Cantarell-Bold.ttf"
    )
    LabelBase.register(name="OpenSans",
        fn_regular="fonts/OpenSans/OpenSans-Regular.ttf",
        fn_bold="fonts/OpenSans/OpenSans-Bold.ttf"
    )
    LabelBase.register(name="Amble",
        fn_regular="fonts/Amble/Amble-Regular.ttf",
        fn_bold="fonts/Amble/Amble-Bold.ttf"
    )
    LabelBase.register(name="Roboto",
        fn_regular="fonts/Roboto/Roboto-Regular.ttf",
        fn_bold="fonts/Roboto/Roboto-Bold.ttf"
    )
