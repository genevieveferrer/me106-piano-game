# project_piano_updated - sound.py

def main():    
    from machine import Pin, PWM
    import time
    import random

    tones = {
    "B0": 31,
    "C1": 33,
    "CS1": 35,
    "D1": 37,
    "DS1": 39,
    "E1": 41,
    "F1": 44,
    "FS1": 46,
    "G1": 49,
    "GS1": 52,
    "A1": 55,
    "AS1": 58,
    "B1": 62,
    "C2": 65,
    "CS2": 69,
    "D2": 73,
    "DS2": 78,
    "E2": 82,
    "F2": 87,
    "FS2": 93,
    "G2": 98,
    "GS2": 104,
    "A2": 110,
    "AS2": 117,
    "B2": 123,
    "C3": 131,
    "CS3": 139,
    "D3": 147,
    "DS3": 156,
    "E3": 165,
    "F3": 175,
    "FS3": 185,
    "G3": 196,
    "GS3": 208,
    "A3": 220,
    "AS3": 233,
    "B3": 247,
    "C4": 262,
    "CS4": 277,
    "D4": 294,
    "DS4": 311,
    "E4": 330,
    "F4": 349,
    "FS4": 370,
    "G4": 392,
    "GS4": 415,
    "A4": 440,
    "AS4": 466,
    "B4": 494,
    "C5": 523,
    "CS5": 554,
    "D5": 587,
    "DS5": 622,
    "E5": 659,
    "F5": 698,
    "FS5": 740,
    "G5": 784,
    "GS5": 831,
    "A5": 880,
    "AS5": 932,
    "B5": 988,
    "C6": 1047,
    "CS6": 1109,
    "D6": 1175,
    "DS6": 1245,
    "E6": 1319,
    "F6": 1397,
    "FS6": 1480,
    "G6": 1568,
    "GS6": 1661,
    "A6": 1760,
    "AS6": 1865,
    "B6": 1976,
    "C7": 2093,
    "CS7": 2217,
    "D7": 2349,
    "DS7": 2489,
    "E7": 2637,
    "F7": 2794,
    "FS7": 2960,
    "G7": 3136,
    "GS7": 3322,
    "A7": 3520,
    "AS7": 3729,
    "B7": 3951,
    "C8": 4186,
    "CS8": 4435,
    "D8": 4699,
    "DS8": 4978
    }
    NOTE_REST = const(0)
    NOTE_C3   = const(131) #button 1
    NOTE_CS3  = const(139) #button 2
    NOTE_D3   = const(147) #button 3
    NOTE_DS3  = const(156) #button 4
    NOTE_E3   = const(165) #button 5
    NOTE_F3   = const(175) #button 6
    NOTE_FS3  = const(185) #button 7
    NOTE_G3   = const(196) #button 8
    NOTE_GS3  = const(208) #button 9
    NOTE_A3   = const(220) #button 10
    NOTE_AS3  = const(233) #button 11
    NOTE_B3   = const(247) #button 12

    button_note0 = Pin(10, Pin.IN, Pin.PULL_UP)
    button_note1 = Pin(22, Pin.IN, Pin.PULL_UP)
    button_note2 = Pin(9, Pin.IN, Pin.PULL_UP)
    button_note3 = Pin(27, Pin.IN, Pin.PULL_UP)
    button_note4 = Pin(16, Pin.IN, Pin.PULL_UP)
    button_note5 = Pin(14, Pin.IN, Pin.PULL_UP)
    button_note6 = Pin(13, Pin.IN, Pin.PULL_UP)
    button_note7 = Pin(3, Pin.IN, Pin.PULL_UP)
    button_note8 = Pin(0, Pin.IN, Pin.PULL_UP)
    buzzer = PWM(Pin(11))

    tune1 = [(NOTE_C3,1),(NOTE_REST,8),(NOTE_C3,1),(NOTE_REST,8),(NOTE_G3,1),(NOTE_REST,8),(NOTE_G3,1)] #song 1
    tune2 = [(NOTE_C3,1),(NOTE_REST,8),(NOTE_E3,1),(NOTE_REST,8),(NOTE_G3,1),(NOTE_REST,8),(NOTE_E3,1)] #song 2
    tune3 = [(NOTE_E3,1),(NOTE_REST,8),(NOTE_G3,1),(NOTE_REST,8),(NOTE_C3,1),(NOTE_REST,8),(NOTE_E3,1)] #song 3
    tune4 = [(NOTE_G3,1),(NOTE_REST,8),(NOTE_E3,1),(NOTE_REST,8),(NOTE_C3,1),(NOTE_REST,8),(NOTE_G3,1)] #song 4
    tune5 = [(69,1),(NOTE_REST,8),(NOTE_C3,1),(NOTE_REST,8),(NOTE_G3,1),(NOTE_REST,8),(392,1)] #song 4
    tunePeekABoo = [(1661,4),(1480,4),(1319,4),(1480,4),(1109,2),(1109,2),(NOTE_REST,1)]
    tuneHartShaker = [(1047,1.333),(1245,1.333),(1661,2),(1865,1.333),(1661,1),(NOTE_REST,1)]
    tuneLose = [(104,2),(98,2),(93,1),(NOTE_REST,1)]
    PWM_MAX = const((2**16)-1)
    selection = random.randint(1,5)
    print(selection)

    if selection == 1:
        stored_tune = tune1
        for n in tune1:
            (freq,note) = n
            secs = 1/note
            print("({:3}, {:6.4f})".format(freq,secs))
            if freq == 0:
                buzzer.duty_u16(0)
                time.sleep(secs)
            else:
                buzzer.freq(freq)
                buzzer.duty_u16(PWM_MAX//2)
                time.sleep(secs)
                buzzer.duty_u16(0)

    elif selection == 2:
        stored_tune = tune2
        for n in tune2:
            (freq,note) = n
            secs = 1/note
            print("({:3}, {:6.4f})".format(freq,secs))
            if freq == 0:
                buzzer.duty_u16(0)
                time.sleep(secs)
            else:
                buzzer.freq(freq)
                buzzer.duty_u16(PWM_MAX//2)
                time.sleep(secs)
                buzzer.duty_u16(0)
    elif selection == 3:
        stored_tune = tune3
        for n in tune3:
            (freq,note) = n
            secs = 1/note
            print("({:3}, {:6.4f})".format(freq,secs))
            if freq == 0:
                buzzer.duty_u16(0)
                time.sleep(secs)
            else:
                buzzer.freq(freq)
                buzzer.duty_u16(PWM_MAX//2)
                time.sleep(secs)
                buzzer.duty_u16(0)
    elif selection == 4:
        stored_tune = tune4
        for n in tune4:
            (freq,note) = n
            secs = 1/note
            print("({:3}, {:6.4f})".format(freq,secs))
            if freq == 0:
                buzzer.duty_u16(0)
                time.sleep(secs)
            else:
                buzzer.freq(freq)
                buzzer.duty_u16(PWM_MAX//2)
                time.sleep(secs)
                buzzer.duty_u16(0)
    elif selection == 5:
        stored_tune = tune5
        for n in tune5:
            (freq,note) = n
            secs = 1/note
            print("({:3}, {:6.4f})".format(freq,secs))
            if freq == 0:
                buzzer.duty_u16(0)
                time.sleep(secs)
            else:
                buzzer.freq(freq)
                buzzer.duty_u16(PWM_MAX//2)
                time.sleep(secs)
                buzzer.duty_u16(0)
                
    #print(stored_tune)

    i = 1
    listUser = []
    while i < 5:
        if button_note0.value() == 0:
            print("note G4")
            buzzer.duty_u16(1000)
            buzzer.freq(392)
            time.sleep(1)
            i += 1
            print(i-1)
        elif button_note1.value() == 0:
            print("note A4")
            buzzer.duty_u16(1000)
            buzzer.freq(440)
            time.sleep(1)
            i += 1
            print(i)
        elif button_note2.value() == 0:
            print("note B5")
            buzzer.duty_u16(1000)
            buzzer.freq(494)
            time.sleep(1)
            i += 1
            print(i)
        elif button_note3.value() == 0:
            print("note C5")
            buzzer.duty_u16(1000)
            buzzer.freq(523)
            listUser.append("note C5")
            time.sleep(1)
            i += 1
            print(i-1)
            buzzer.duty_u16(0)
        elif button_note4.value() == 0:
            print("note D5")
            buzzer.duty_u16(1000)
            buzzer.freq(587)
            time.sleep(0.1)
        elif button_note5.value() == 0:
            print("note E5")
            buzzer.duty_u16(1000)
            buzzer.freq(659)
            time.sleep(0.5)
            listUser.append("note E5")
            time.sleep(0.5)
            i += 1
            print(i-1)
            buzzer.duty_u16(0)
        elif button_note6.value() == 0:
            print("note FS5")
            buzzer.duty_u16(1000)
            buzzer.freq(740)
            time.sleep(0.1)
        elif button_note7.value() == 0:
            print("note G5")
            buzzer.duty_u16(1000)
            buzzer.freq(784)
            time.sleep(0.5)
            listUser.append("note G5")
            time.sleep(0.5)
            i += 1
            print(i-1)
            buzzer.duty_u16(0)
        elif button_note8.value() == 0:
            print("note A5")
            buzzer.duty_u16(1000)
            buzzer.freq(880)
            time.sleep(0.1)
        else:
            buzzer.duty_u16(0)
            
    #print(listUser)

    if selection == 1:
        if listUser == ["note C5", "note C5", "note G5", "note G5"]:
            print("Correct!")
            for n in tunePeekABoo:
                (freq,note) = n
                secs = 1/note
                print("({:3}, {:6.4f})".format(freq,secs))
                if freq == 0:
                    buzzer.duty_u16(0)
                    time.sleep(secs)
                else:
                    buzzer.freq(freq)
                    buzzer.duty_u16(PWM_MAX//2)
                    time.sleep(secs)
                    buzzer.duty_u16(0)
            main()
        else:
            print("Incorrect")
            for n in tuneLose:
                (freq,note) = n
                secs = 1/note
                print("({:3}, {:6.4f})".format(freq,secs))
                if freq == 0:
                    buzzer.duty_u16(0)
                    time.sleep(secs)
                else:
                    buzzer.freq(freq)
                    buzzer.duty_u16(PWM_MAX//2)
                    time.sleep(secs)
                    buzzer.duty_u16(0)
            main()
    elif selection == 2:
        if listUser == ["note C5", "note E5", "note G5", "note E5"]:
            print("Correct!")
            for n in tuneHartShaker:
                (freq,note) = n
                secs = 1/note
                print("({:3}, {:6.4f})".format(freq,secs))
                if freq == 0:
                    buzzer.duty_u16(0)
                    time.sleep(secs)
                else:
                    buzzer.freq(freq)
                    buzzer.duty_u16(PWM_MAX//2)
                    time.sleep(secs)
                    buzzer.duty_u16(0)
            main()
        else:
            print("Incorrect")
            for n in tuneLose:
                (freq,note) = n
                secs = 1/note
                print("({:3}, {:6.4f})".format(freq,secs))
                if freq == 0:
                    buzzer.duty_u16(0)
                    time.sleep(secs)
                else:
                    buzzer.freq(freq)
                    buzzer.duty_u16(PWM_MAX//2)
                    time.sleep(secs)
                    buzzer.duty_u16(0)
            main()
    elif selection == 3:
        if listUser == ["note E5", "note G5", "note C5", "note E5"]:
            print("Correct!")
            for n in tunePeekABoo:
                (freq,note) = n
                secs = 1/note
                print("({:3}, {:6.4f})".format(freq,secs))
                if freq == 0:
                    buzzer.duty_u16(0)
                    time.sleep(secs)
                else:
                    buzzer.freq(freq)
                    buzzer.duty_u16(PWM_MAX//2)
                    time.sleep(secs)
                    buzzer.duty_u16(0)
            main()
        else:
            print("Incorrect")
            for n in tuneLose:
                (freq,note) = n
                secs = 1/note
                print("({:3}, {:6.4f})".format(freq,secs))
                if freq == 0:
                    buzzer.duty_u16(0)
                    time.sleep(secs)
                else:
                    buzzer.freq(freq)
                    buzzer.duty_u16(PWM_MAX//2)
                    time.sleep(secs)
                    buzzer.duty_u16(0)
            main()
    elif selection == 4:
        if listUser == ["note G5", "note E5", "note C5", "note E5"]:
            print("Correct!")
            for n in tuneHartShaker:
                (freq,note) = n
                secs = 1/note
                print("({:3}, {:6.4f})".format(freq,secs))
                if freq == 0:
                    buzzer.duty_u16(0)
                    time.sleep(secs)
                else:
                    buzzer.freq(freq)
                    buzzer.duty_u16(PWM_MAX//2)
                    time.sleep(secs)
                    buzzer.duty_u16(0)
            main()
        else:
            print("Incorrect")
            for n in tuneLose:
                (freq,note) = n
                secs = 1/note
                print("({:3}, {:6.4f})".format(freq,secs))
                if freq == 0:
                    buzzer.duty_u16(0)
                    time.sleep(secs)
                else:
                    buzzer.freq(freq)
                    buzzer.duty_u16(PWM_MAX//2)
                    time.sleep(secs)
                    buzzer.duty_u16(0)
            main()
    if selection == 5:
        if listUser == ["note C5", "note C5", "note G5", "note G5"]:
            print("Correct!")
            for n in tunePeekABoo:
                (freq,note) = n
                secs = 1/note
                print("({:3}, {:6.4f})".format(freq,secs))
                if freq == 0:
                    buzzer.duty_u16(0)
                    time.sleep(secs)
                else:
                    buzzer.freq(freq)
                    buzzer.duty_u16(PWM_MAX//2)
                    time.sleep(secs)
                    buzzer.duty_u16(0)
            main()
        else:
            print("Incorrect")
            for n in tuneLose:
                (freq,note) = n
                secs = 1/note
                print("({:3}, {:6.4f})".format(freq,secs))
                if freq == 0:
                    buzzer.duty_u16(0)
                    time.sleep(secs)
                else:
                    buzzer.freq(freq)
                    buzzer.duty_u16(PWM_MAX//2)
                    time.sleep(secs)
                    buzzer.duty_u16(0)
            main()

main()