# PancakeSwap-API-Telegram-Bot
A telegram bot used to check the price of a cryptocurrency using the PancakeSwap API. Use the command /price in a telegram group to check the price.


In the file bot.py where it says (telegram_bot_token = "YOUR TELEGRAM BOT API") add your telegram bot API. Talk to @BotFather on telegram to get your key.

Once you have done that visit "https://api.pancakeswap.info/api/tokens" and you will see a list of all the coins/tokens you can use. 
To find your coin click 'Control F' and then type for the coin. Copy and paste what ever the token is called in the name section which is in the file tracker.py
     
     
   E.g. For the token below you would type "Pitbull" in the file tracker.py where it says name. Like this:    name = "Pitbull"     {"name":"Pitbull","symbol":"PIT","price":"0.0000000006208932128878219505510341564126764","price_BNB":"0.000000000001489559886379574585620542089008064"},"0x7083609fCE4d1d8Dc0C979AAb8c869Ea2C873402":


To run the bot make sure both bot.py and tracker.py are in one folder. Then you can run the file bot.py
  To run the code you can use many softwares but I use VS code as that's the easiest to understand.
  
  
 If you need any help just write a comment and I'll try and help.
