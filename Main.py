import os
import discord
import json
import requests
from keep_alive import keep_alive

client = discord.Client()

def get_kural(num1):
    URL = "https://api-thirukkural.vercel.app/api?num="
    response = requests.get(URL + num1)
    json_data = json.loads(response.text)
    section_tam = json_data["sect_tam"]
    chapgrp_tam = json_data["chapgrp_tam"]
    chap_tam    = json_data["chap_tam"]
    line1 = json_data["line1"]
    line2 = json_data["line2"]
    eng_exp = json_data["eng_exp"]
    kural = "Section:\t"+section_tam + "\n" + "ChapterGroup:\t"+chapgrp_tam + "\n" + "Chapter:\t"+ chap_tam + "\n"+ "Kural in Tamil:\t" + line1 + "\n" + "\t\t\t\t\t\t\t\t" + line2 + "\n" + "Translation:\t" + eng_exp 
    return (kural)






@client.event
async def on_ready():
    print('Ready!')

@client.event
async def on_message(message):
       if (message.author == client.user):
            return 

       if (message.content.startswith("/h")):
           await message.channel.send("/kural <kural number> \n Will show the corresponding kural, chapter group, chapter and the explanation of 'kural' in English." )

       if (message.content.startswith("/kural")):
           num = message.content.strip("/kural")
           if (int(num) >= 1 and int(num) <= 1330):
              kural = get_kural(num)
              await message.channel.send(kural)
           else:
              await message.channel.send("No not beyond 1330, you have to write youself one then :p")
          

           
keep_alive()
 
client.run(os.environ['TOKEN'])
