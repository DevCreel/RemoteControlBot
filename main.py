import sys, telepot, time, subprocess, os
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if (content_type == 'text' and chat_id and msg['chat']['id'] == chat_id):
        cmd_repeat = 1
        command = msg['text']
        markup = ReplyKeyboardMarkup(keyboard=[
            ['⏮ Previous track', '⏯ Play/Pause', '⏭ Next track'],
            ['🔽 Volume down', '🔈 Mute', '🔼 Volume up'],
            ['🖥 Turn off screen', '🔅 Set brightness 10%', '🔆 Set brightness 100%']
        ])

        bot.sendMessage(chat_id, 'Got command: %s' % command, reply_markup=markup)

        if command == '/start':
            bot.sendMessage (chat_id, str("Hi! Which one do you want? choose from the below keyboard buttons."), reply_markup=markup)

        elif '🔅 Set brightness 10%' == command:
            cmd = brightness % 10

        elif  '🔆 Set brightness 100%' == command:
            cmd = brightness % 100

        elif  '🖥 Turn off screen' == command:
            cmd = screen_off

        elif  '🔈 Mute' == command:
            cmd = keypress % '0xAD'

        elif  '🔼 Volume up' == command:
            cmd = keypress % '0xAF'
            cmd_repeat = 2

        elif  '🔽 Volume down' == command:
            cmd = keypress % '0xAE'
            cmd_repeat = 2

        elif  '⏭ Next track' == command:
            cmd = keypress % '0xB0'

        elif  '⏮ Previous track' == command:
            cmd = keypress % '0xB1'

        elif  '⏯ Play/Pause' == command:
            cmd = keypress % '0xB3'

        else:
            cmd_repeat = None

        if cmd_repeat:
            for number in range(cmd_repeat):
                subprocess.Popen(cmd, shell=True)

# get settings from command-line
TOKEN = sys.argv[1]

if len(sys.argv) > 2:
    chat_id = sys.argv[2]
else:
    chat_id = None

bot = telepot.Bot(TOKEN)

path = os.path.dirname(os.path.abspath(__file__))
screen_off = 'powershell ' + path + '\screen_off.ps1'
keypress = 'powershell ' + path + '\keypress.ps1 -KeyCode %s'
brightness = 'powershell (Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(0,%d)'

bot.message_loop(handle)

while 1:
    time.sleep(20)
