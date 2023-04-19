import os
import random
import pyttsx3
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['STATIC_FOLDER'] = 'static'

def onWord(name, location, length):
   print('word', name, location, length)
   if location > 10:
      engine.stop()
      




def say(message):
    engine = pyttsx3.init()
    engine.connect('started-word', onWord)
    engine.say(message)
    engine.runAndWait()
    
# Define game route
@app.route('/game', methods=['GET', 'POST'])
def game():
    coins = {
        'one': 0,
        'two': 0,
        'five': 0,
        'ten': 0,
        'twenty': 0
    }

    if request.method == 'POST':
        coins['one'] = int(request.form['one'])
        coins['two'] = int(request.form['two'])
        coins['five'] = int(request.form['five'])
        coins['ten'] = int(request.form['ten'])
        coins['twenty'] = int(request.form['twenty'])
        total = coins['one'] + coins['two']*2 +  coins['five'] *5+ 10 * coins['ten']+20*coins['twenty']
        say('You have ' + str(total) + ' rupees in total.')
       
       
        
        return render_template('game.html', coins=coins, total=total)

    
    mytext = 'Welcome to the Money Game! Can you count your coins eh boy?'
    say(mytext)
    
    
    
    #say('Welcome to the Money Game! Can you count your coins?')
    say('How many rupees do you have? common now, i don think it is possible')
    return render_template('game.html', coins=coins)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
