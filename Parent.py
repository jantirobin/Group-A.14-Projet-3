from microbit import *
import radio
import log
import music

radio.config(group=32) #l'alimentation pour recevoir les msgs etc pour microbit

radio.on()
radio.send('message')
radio.config(group=32, power=6) #avoir access a recevoir les msgs

currentTemp = temperature()
max = currentTemp
min = currentTemp
#detecter le max et min de temperature

count = 0
score = 0
score += 1
display.scroll(score)

name = 'Parent'
display.scroll(name) #nommee la microbit

log.set_labels('temperature','sound','light')
log.add({
    'temperature' : temperature(),
    'sound' : microphone.sound_level(),
    'light' : display.read_light_level()
}) #crees les valeurs pour temp son et lumiere

def log_data():
    log.add({
    'temperature' : temperature(),
    'sound' : microphone.sound_level(),
    'light' : display.read_light_level()
    })
    #log les entrees chaque 30 sec

running = False
while True:
    message = radio.receive()
    if message:
        display.scroll(message)
        #recevoir les msgs

    if button_a.is_pressed() and button_b.is_pressed():
        display.scroll('A and B')
    elif button_a.is_pressed():
        display.scroll('A')
    elif button_b.is_pressed():
        display.scroll('B')
    sleep(100)
    #si les boutons A et B sont appuyer

    sleep(10000)

    if button_a.was_pressed():
        running = not running
    if running:
        display.show(1)
    else:
        display.show(0)
         #sauvegrader du data

    display.show('.')
    currentTemp = temperature()
    if currentTemp < min:
        min = currentTemp
    elif currentTemp > max:
        max = currentTemp
    if button_a.was_pressed():
        display.scroll(min)
    if button_b.was_pressed():
        display.scroll(max)
    sleep(1000)
    display.clear()
    sleep(1000)
    #apres avoir appure les boutons A ou B (appui long) A va afficher la temp min, et B va afficher la temp max

#def de la boucle de demande de nourrir et son clear
def nourrir() :

    index = 0
    
    while True  :
        
        if  button_b.was_pressed() :

            display.clear()

            index += 1 

            return index

        else :

            faim = [Image.ANGRY, Image.ARROW_S]

            display.show(faim, delay=1000, loop=False)

            music.play(music.BA_DING)

#fait en sorrte que l'alarme se joue toute les 3h et que on puisse utiliser les boutons peit importe le moment.
while True :

    index = 1
    temps_alerte = 10000
    
    début = running_time()
  
    while True :
        
        if button_a.was_pressed() :
            
            display.show(index)
            
            sleep(2000)
            
            display.clear()

           
        
        elif running_time() - début >= temps_alerte : 

            nourrir() 
                
            index +=1

            début = running_time()
            
