import discord
import asyncio

client = discord.Client ()

@client.event
async def on_ready():
    print(client.user.name)
    print('Ola Usuario')
    print('Sistema iniciado. O Bot foi iniciado e está Online no Discord')
    print('Não se esqueça, o Bot está em desenvolvimento, Por Favor não entre em contato para dar sugestões. Espere até a versão final para avaliação')

@client.event
async def on_message(message):
    if message.content.lower().startswith('/play'):
        await client.send_message(message.channel, "Bot em desenvolvimento. Aguarde que este comando estara em breve disponivel para usa-lo :wink:")


client.run('Token')