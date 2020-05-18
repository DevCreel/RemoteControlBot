### Windows remote control bot ###

1. Install [Python](https://www.python.org/downloads/).
2. Start powershell as administrator and run `py -m pip install telepot`
3. Create your [Telegram bot]()https://core.telegram.org/bots
3. Run cmd (Win+R) and enter `shell:startup`. In the folder that opens, create a `RemoteControlBot.bat` file with content:
```shell script
powershell pythonw {DIR}\main.py '{TOKEN}}' '{CHAT_ID}}'
```
Where:
- {DIR} - folder with RemoteControlBot files. for example C:\Users\<username>\RemoteControlBot
- {TOKEN} - your bot token
- {CHAT_ID} - your Telegram account chat_id (optional param to secure your connection)
4. Doubleclick `RemoteControlBot.bat`
