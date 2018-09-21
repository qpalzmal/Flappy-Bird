import cx_Freeze

executables = [cx_Freeze.Executable("Flappy Bird.py")]

cx_Freeze.setup(
    name="Flappy Bird",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["bird.png", "background.png", "water.png", "flappybirds music.mp3",
                                             "pickup.wav", "crash.ogg", "splash.wav", "bird0.png", "bird1.png",
                                             "bird2.png", "bird3.png", "coin0.png", "coin1.png", "coin2.png",
                                             "coin3.png", "coin4.png", "coin5.png", "water.png", "pipe.png", "vol0.png",
                                             "vol1.png", "vol2.png", "vol3.png"]}},
    executables=executables
)
