# project_piano_updated_6_motor_and_sensor - no_notes.py

import random
from machine import Pin, PWM
import time
import utime
selection = 1 # random.randint(1,5)
print(selection)

def main():
    global selection
    
    print(selection)
    
    ## this pin set-up will turn the motor CCW
    PIN_IN1 = const(15)
    PIN_IN2 = const(14)
    PIN_IN3 = const(16)
    PIN_IN4 = const(17)

    pins = [
        Pin(PIN_IN1, Pin.OUT),
        Pin(PIN_IN2, Pin.OUT),
        Pin(PIN_IN3, Pin.OUT),
        Pin(PIN_IN4, Pin.OUT)
        ]

    # this sequence makes the motor go cw
    sequence_cw = [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
        ]

    # this sequence makes the motor go ccw
    sequence_ccw = [
        [0, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [1, 0, 0, 0]
        ]

    
    Trig = Pin(27, Pin.OUT)
    Echo = Pin(26, Pin.IN, Pin.PULL_DOWN)
    
    # the distance is taken at the start of the loop (when the song is being selected)
    def CheckDistance(): # code from:https://tutorial.cytron.io/2021/06/19/ultrasonic-hc-sr04p-using-raspberry-pi-pico/
        SpeedOfSoundInCM = 0.034
        Trig.low()
        utime.sleep_us(2)
        Trig.high()
        utime.sleep_us(10)
        Trig.low()
        exitLoop = False
        loopcount = 0 #used as a failsafe if the signal doesn't return
        while Echo.value() == 0 and exitLoop == False:
            loopcount = loopcount + 1
            delaytime = utime.ticks_us()
            
            if loopcount > 3000 : exitLoop == True
        
        while Echo.value() == 1 and exitLoop == False:
            loopcount = loopcount + 1
            receivetime = utime.ticks_us()
            if loopcount > 3000 : exitLoop == True
        
        if exitLoop == True: #We failed somewhere
            return 0
        else:
            distance = ((receivetime - delaytime) * SpeedOfSoundInCM) / 2
            return distance
    distance = CheckDistance()
    
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

    button_note0 = Pin(0, Pin.IN, Pin.PULL_UP)
    button_note1 = Pin(1, Pin.IN, Pin.PULL_UP)
    button_note2 = Pin(2, Pin.IN, Pin.PULL_UP) 
    button_note3 = Pin(3, Pin.IN, Pin.PULL_UP) 
    button_note4 = Pin(4, Pin.IN, Pin.PULL_UP)
    buzzer = PWM(Pin(6))

    tune1 = [(NOTE_C3,1),(NOTE_REST,8),(NOTE_C3,1),(NOTE_REST,8),(NOTE_G3,1),(NOTE_REST,8),(NOTE_G3,1)] #song 1
    tune2 = [(NOTE_C3,1),(NOTE_REST,8),(NOTE_E3,1),(NOTE_REST,8),(NOTE_G3,1),(NOTE_REST,8),(NOTE_E3,1)] #song 2
    tune3 = [(NOTE_E3,1),(NOTE_REST,8),(NOTE_G3,1),(NOTE_REST,8),(NOTE_C3,1),(NOTE_REST,8),(NOTE_E3,1)] #song 3
    tune4 = [(NOTE_G3,1),(NOTE_REST,8),(NOTE_E3,1),(NOTE_REST,8),(NOTE_C3,1),(NOTE_REST,8),(NOTE_G3,1)] #song 4
    tune5 = [(NOTE_G3,1),(NOTE_REST,8),(NOTE_C3,1),(NOTE_REST,8),(NOTE_G3,1),(NOTE_REST,8),(NOTE_E3,1)] #song 5
    tunePeekABoo = [(1661,4),(1480,4),(1319,4),(1480,4),(1109,2.67),(NOTE_REST,32),(1109,2.67),(NOTE_REST,1), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100), (NOTE_REST,100)]
    tuneHeartShaker = [(1047,1.333),(1245,1.333),(1661,2),(1865,1.333),(1661,1),(NOTE_REST,1)]
    tuneLose = [(104,2),(98,2),(93,1),(NOTE_REST,1)]
    PWM_MAX = const((2**16)-1)
    
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

    i = 1
    listUser = []
    while i < 5:
        if button_note0.value() == 0:
            print("note C5")
            buzzer.duty_u16(1000)
            buzzer.freq(523)
            listUser.append("note C5")
            time.sleep(1)
            i += 1
            print(i-1)
            buzzer.duty_u16(0)
        elif button_note1.value() == 0:
            print("note D5")
            buzzer.duty_u16(1000)
            buzzer.freq(587)
            listUser.append("note D5")
            time.sleep(1)
            i += 1
            print(i-1)
            buzzer.duty_u16(0)
        elif button_note2.value() == 0:
            print("note E5")
            buzzer.duty_u16(1000)
            buzzer.freq(659)
            listUser.append("note E5")
            time.sleep(1)
            i += 1
            print(i-1)
            buzzer.duty_u16(0)
        elif button_note3.value() == 0:
            print("note F5")
            buzzer.duty_u16(1000)
            buzzer.freq(698)
            listUser.append("note F5")
            time.sleep(1)
            i += 1
            print(i-1)
            buzzer.duty_u16(0)
        elif button_note4.value() == 0:
            print("note G5")
            buzzer.duty_u16(1000)
            buzzer.freq(784)
            listUser.append("note G5")
            time.sleep(1)
            i += 1
            print(i-1)
            buzzer.duty_u16(0)
        else:
            buzzer.duty_u16(0)
            
    if selection == 1:
        print(selection)
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
                if distance > 20:
                    distance = CheckDistance()
                    print(distance)
                    for step in sequence_cw:
                        for i in range(len(pins)):
                            pins[i].value(step[i])
                            time.sleep(0.001)
                        distance = CheckDistance()
                if distance < 20:
                    distance = CheckDistance()
                    print(distance)
                    for n in tuneHeartShaker:
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
                        
            print("The distance is")
            print(distance)
            selection = random.randint(1,5)
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
            print("The distance is ")
            print(distance)
            selection = 1
            main()
    elif selection == 2:
        print(selection)
        if listUser == ["note C5", "note E5", "note G5", "note E5"]:
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
                if distance > 20:
                    distance = CheckDistance()
                    print(distance)
                    for step in sequence_cw:
                        for i in range(len(pins)):
                            pins[i].value(step[i])
                            time.sleep(0.001)
            selection = random.randint(1,5)
            print("The distance is ")
            print(distance)
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
            selection = 2
            print("The distance is ")
            print(distance)
            main()
    elif selection == 3:
        print(selection)
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
                if distance > 20:
                    distance = CheckDistance()
                    print(distance)
                    for step in sequence_cw:
                        for i in range(len(pins)):
                            pins[i].value(step[i])
                            time.sleep(0.001)
            selection = random.randint(1,5)
            print("The distance is ")
            print(distance)
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
            selection = 3
            print("The distance is ")
            print(distance)
            main()
    elif selection == 4:
        print(selection)
        if listUser == ["note G5", "note E5", "note C5", "note E5"]:
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
                if distance > 20:
                    distance = CheckDistance()
                    print(distance)
                    for step in sequence_cw:
                        for i in range(len(pins)):
                            pins[i].value(step[i])
                            time.sleep(0.001)
            selection = random.randint(1,5)
            print("The distance is ")
            print(distance)
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
            selection = 4
            print("The distance is ")
            print(distance)
            main()
    elif selection == 5:
        print(selection)
        if listUser == ["note G5", "note C5", "note G5", "note E5"]:
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
                if distance > 20:
                    distance = CheckDistance()
                    print(distance)
                    for step in sequence_cw:
                        for i in range(len(pins)):
                            pins[i].value(step[i])
                            time.sleep(0.001)
            selection = random.randint(1,5)
            print("The distance is ")
            print(distance)
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
            selection = 5
            print("The distance is ")
            print(distance)
            main()
            
main()