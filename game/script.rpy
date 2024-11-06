# Kamu dapat taruh script game mu di file ini.
# Deklarasikan karakter yang digunakan di game.
define c = Character('Cinderella', color="#c8ffc8")
define p = Character(_("Prince"), color="#c8c8ff")

# Game dimulai disini.
label start:
    
    # Memutar musik dengan loop (agar terus berulang)
    play music "strauss.mp3" loop
    $ renpy.music.set_volume(1.0, channel='music')

    # Menampilkan video di layar menggunakan Movie displayable
    show expression Movie(play="images/scenesatu.webm", size=(1920, 1080))
    with fade

    # Teks dialog dan voice over
    voice "audio/voice/satu.mp3"
    "On a clear and magical night, Cinderella, once a simple girl, found herself at the heart of a royal ball."
     
    show expression Movie(play="images/scene3.webm", size=(1920, 1080))
    with fade

    voice "audio/voice/dua.mp3"
    "Her gown shimmered under the crystal chandeliers, and the Prince couldn’t take his eyes off her."
 
    show expression Movie(play="images/scene2.webm", size=(1920, 1080))
    with dissolve
    voice "audio/voice/tiga.mp3"
    p "You look so beautiful tonight. I wish we could dance forever."

    voice "audio/voice/empat.mp3"
    c "Thank you, Your Highness. But I must leave soon."

    show expression Movie(play="images/scene1.webm", size=(1920, 1080))
    with fade
    play sound "jam.mp3" loop
    $ renpy.sound.set_volume(1.0, channel='sound')

    $ renpy.music.set_volume(0.5, channel='music')

    voice "audio/voice/lima.mp3"
    "But time was running out. The clock struck midnight, and Cinderella knew that the magic of this night would soon fade away."
    
    show expression Movie(play="images/jam.webm", size=(1920, 1080))

    voice "audio/voice/enam.mp3"
    c "Oh no, it's midnight already!"

    voice "audio/voice/tujuh.mp3"
    p "Wait, wait! Who are you really?"

    stop sound

    show expression Movie(play="images/scene4.webm", size=(1920, 1080))
    with fade
    play sound "langkah.mp3" loop
    $ renpy.sound.set_volume(1.0, channel='sound')

    $ renpy.music.set_volume(0.5, channel='music')

    voice "audio/voice/delapan.mp3"
    "In a hurry, Cinderella fled from the ball. As she ran down the stairs, one of her glass slippers slipped off without her noticing."

    stop sound
    menu:
        "Here, a choice appears. Should Cinderella return to retrieve her slipper, or should she keep running without looking back?"
    
        "Leave the slipper behind and run without looking back.":
            jump leave

        "Pick up the slipper and continue running.":
            jump pickup

label pickup:

    show expression Movie(play="images/scene5a.webm", size=(1920, 1080))
    with dissolve

    voice "audio/voice/sepuluh.mp3"
    "Cinderella decided to go back and pick up her slipper. She knew it was her only chance to avoid suspicion. But it caused her a slight delay."

    show expression Movie(play="images/scene6a.webm", size=(1920, 1080))
    with dissolve

    voice "audio/voice/sebelas.mp3"
    "But with no slipper left behind, the Prince had no clue about who the mysterious girl was that fled from the ball."

    voice "audio/voice/duabelas.mp3"
    p "Where did she go? She left no trace."

    show expression Movie(play="images/simple.webm", size=(1920, 1080))
    voice "audio/voice/tigabelas.mp3"
    "Without any clue, the Prince continued searching but never found Cinderella. The girl returned to her simple life."

    "END"

    return

label leave:

    show expression Movie(play="images/scene4.webm", size=(1920, 1080))

    voice "audio/voice/empatbelas.mp3"
    "Without a second thought, Cinderella decided to leave the slipper. For her, escaping before the magic wore off was more important."

    show expression Movie(play="images/scene6b.webm", size=(1920, 1080))
    with dissolve

    menu:
        "As the Prince contemplates his feelings and the search for Cinderella, he faces a crucial decision. What should he do next?"

        "I will find her, no matter how long it takes!":
            jump search

        "Perhaps it's best to let her go and move on.":
            jump nosearch

label search:
    voice "audio/voice/enambelas.mp3"
    "When the Prince saw the glass slipper, he knew it was the key to finding the mysterious woman who had captured his heart."

    voice "audio/voice/duaenam.mp3"
    p "This is my only clue to finding her."

    show expression Movie(play="images/news.webm", size=(1920, 1080))
    with dissolve

    voice "audio/voice/tujuhbelas.mp3"
    "News of the Prince's quest spread quickly through the kingdom. The townsfolk were curious, eager to see who would fit the glass slipper."

    show expression Movie(play="images/travel.webm", size=(1920, 1080))

    voice "audio/voice/delapanbelas.mp3"
    "The Prince traveled from house to house, hoping to find the girl whose foot would perfectly fit the slipper."

    show expression Movie(play="images/arrived.webm", size=(1920, 1080))
    with fade

    voice "audio/voice/sembilanbelas.mp3"
    "The prince arrived at the girl's house."

    show expression Movie(play="images/meets.webm", size=(1920, 1080))
    voice "audio/voice/duapuluh.mp3"
    p "Please, try the slipper on!"

    menu:
        "As the girl gazes at the glowing glass slipper, she must decide what to do next. Will she take the chance?"

        "I will try on the slipper and see if it fits!":
            jump bahagia

        "Maybe I shouldn't. What if it doesn't fit?":
            jump sedih

    label bahagia:
        show expression Movie(play="images/happy.webm", size=(1920, 1080))
        with fade
        stop music
        play music "bahagia.mp3" loop
    
        voice "audio/voice/duadua.mp3"
        "With the glass slipper as his guide, the Prince finally found Cinderella. They reunited and lived happily ever after."
    
        "END"

        return

    label sedih:
        stop music
        play music "sedih.mp3" loop
    
        show expression Movie(play="images/notry.webm", size=(1920, 1080))

        voice "audio/voice/duatiga.mp3"
        "The shoes were not tried on by the girl of his choice and the prince eventually gave up looking for more."
       
        show expression Movie(play="images/back.webm", size=(1920, 1080))

        voice "audio/voice/duaempat.mp3"
        "The prince returned to the palace and resumed his life."

        "END"

        return

label nosearch:
    voice "audio/voice/dualima.mp3"
    show expression Movie(play="images/back.webm", size=(1920, 1080))

    "The prince returned to the party room."

    "END"

    return
