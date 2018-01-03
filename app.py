import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '510269881:AAH0uAS-r5Ga5p4sfnL4iY1y3OxE2vh498k'
WEBHOOK_URL = 'https://4cb0a451.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'user',
        'rabbit',
        'rabbit_1',
        'rabbit_2',
        'rabbit_3',
        'cat',
        'cat_1',
        'cat_2',
        'cat_3',
        'dog',
        'dog_1',
        'dog_2',
        'dog_3'
    ],
    transitions=[
        {
            'trigger': 'advance',        
            'source': 'user',
            'dest': 'user',
            'conditions': 'is_going_to_user'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'rabbit',
            'conditions': 'is_going_to_rabbit'
        },
        {
            'trigger': 'advance',
            'source': 'rabbit',
            'dest': 'rabbit',
            'conditions': 'is_return_to_rabbit'
        },
        {
            'trigger': 'advance',
            'source': 'rabbit',
            'dest': 'rabbit_1',
            'conditions': 'is_going_to_1'
        },
        {
            'trigger': 'advance',
            'source': 'rabbit',
            'dest': 'rabbit_2',
            'conditions': 'is_going_to_2'
        },
        {
            'trigger': 'advance',
            'source': 'rabbit',
            'dest': 'rabbit_3',
            'conditions': 'is_going_to_3'
        },
        {
            'trigger': 'advance',
            'source':[ 
                'rabbit_1',
                'rabbit_2',
                'rabbit_3'
            ],
            'dest': 'rabbit',
            'conditions': 'is_return'
        },
        {
            'trigger': 'advance',
            'source':[ 
                'rabbit_1',
                'rabbit_2'
            ],
            'dest': 'rabbit_3',
            'conditions': 'is_more'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'cat',
            'conditions': 'is_going_to_cat'
        },
        {
            'trigger': 'advance',
            'source': 'cat',
            'dest': 'cat',
            'conditions': 'is_return_to_cat'
        },
        {
            'trigger': 'advance',
            'source': 'cat',
            'dest': 'cat_1',
            'conditions': 'is_going_to_1'
        },
        {
            'trigger': 'advance',
            'source': 'cat',
            'dest': 'cat_2',
            'conditions': 'is_going_to_2'
        },
        {
            'trigger': 'advance',
            'source': 'cat',
            'dest': 'cat_3',
            'conditions': 'is_going_to_3'
        },
        {
            'trigger': 'advance',
            'source':[ 
                'cat_1',
                'cat_2',
                'cat_3'
            ],
            'dest': 'cat',
            'conditions': 'is_return'
        },
        {
            'trigger': 'advance',
            'source':[ 
                'cat_1',
                'cat_2'
            ],
            'dest': 'cat_3',
            'conditions': 'is_more'
        },
        {
            'trigger':'advance',
            'source':'user',
            'dest':'dog',
            'conditions': 'is_going_to_dog'
        },
        {
            'trigger': 'advance',
            'source': 'dog',
            'dest': 'dog',
            'conditions': 'is_return_to_dog'
        },
        {
            'trigger':'advance',
            'source':'dog',
            'dest':'dog_1',
            'conditions': 'is_going_to_1'
        },
        {
            'trigger':'advance',
            'source':'dog',
            'dest':'dog_2',
            'conditions': 'is_going_to_2'
        },
        {
            'trigger':'advance',
            'source':'dog',
            'dest':'dog_3',
            'conditions': 'is_going_to_3'
        },
        {
            'trigger': 'advance',
            'source':[ 
                'dog_1',
                'dog_2',
                'dog_3'
            ],
            'dest': 'dog',
            'conditions': 'is_return'
        },
        {
            'trigger': 'advance',
            'source':[ 
                'dog_1',
                'dog_2'
            ],
            'dest': 'dog_3',
            'conditions': 'is_more'
        },
        {
            'trigger': 'advance',
            'source':[
                'rabbit', 
                'rabbit_1',
                'rabbit_2',
                'rabbit_3',
                'cat',
                'cat_1',
                'cat_2',
                'cat_3',
                'dog',
                'dog_1',
                'dog_2',
                'dog_3'
            ],
            'dest': 'user',
            'conditions': 'is_exit'
        },
        {
            'trigger': 'go_back',
            'source': [
                'user',
                'rabbit',
                'cat',
                'dog'
            ],
            'dest': 'user',
            'conditions': 'is_going_to_user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    print(update.message.text)
    machine.advance(update)
    return 'ok'

@app.route('/show-fsm',methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png',mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
