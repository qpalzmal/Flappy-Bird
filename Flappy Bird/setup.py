import cx_Freeze
import os

executables = [cx_Freeze.Executable("Flappy Bird.py")]


# used for Comp #27
os.environ['TCL_LIBRARY'] = r'C:\Users\CODE\AppData\Local\Programs\Python\Python37-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\CODE\AppData\Local\Programs\Python\Python37-32\tcl\tk8.6'

# used for Comp #17
# os.environ['TCL_LIBRARY'] = r'C:\ProgramData\Anaconda3\tcl\tcl8.6'
# os.environ['TK_LIBRARY'] = r'C:\ProgramData\Anaconda3\tcl\tk8.6'

cx_Freeze.setup(
    name="Flappy Bird",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["Images/bird.png", "Images/background.png", "Images/water.png",
                                             "Sound/flappybirds music.mp3", "Sound/pickup.wav", "Sound/crash.ogg",
                                             "Sound/splash.wav", "Images/bird0.png", "Images/bird1.png",
                                             "Images/bird2.png", "Images/bird3.png", "Images/coin0.png",
                                             "Images/coin1.png", "Images/coin2.png","Images/coin3.png",
                                             "Images/coin4.png", "Images/coin5.png", "Images/water.png",
                                             "Images/pipe.png", "Images/vol0.png", "Images/vol1.png", "Images/vol2.png",
                                             "Images/vol3.png"]}},
    version="1.0.0",
    executables=executables
)
