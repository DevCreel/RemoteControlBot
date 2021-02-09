### Windows remote control bot ###

1. Install [Python](https://www.python.org/downloads/)
2. Start powershell as administrator and run `py -m pip install telepot psutil`
3. Create your [Telegram bot](https://core.telegram.org/bots)
4. Clone this repository to your user dir `C:\Users\<username>\RemoteControlBot`
5. Run cmd (Win+R) and enter `shell:startup`. In the folder that opens, create a `RemoteControlBot.bat` file with content:
```shell script
powershell pythonw {DIR}\main.py '{TOKEN}}' '{CHAT_ID}}'
```
Where:
- {DIR} - folder with RemoteControlBot files
- {TOKEN} - your bot token
- {CHAT_ID} - your Telegram account chat_id (optional param to secure your connection)
6. If you are using Windows 10, then you need to start the powershell in administrator mode and run the command
`Set-ExecutionPolicy unrestricted`
7. Doubleclick `RemoteControlBot.bat` to start script
8. Send message `/start` to your bot
