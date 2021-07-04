import discord
import asyncio
import func
from decouple import config
from discord.ext import commands
from time import sleep

cor = 0xFF0000
client = discord.Client()
bot = commands.Bot(command_prefix='!')
key = config('KEY_DISCORD')
staff_id = {'Gustavo':175846992927391744,'Alexandre':239012360973582347,'Carlos':357714935784144896,'Dowser':[259510786009858048,]}
staff_id_list = [staff_id['Gustavo'],staff_id['Alexandre'],staff_id['Carlos'],staff_id['Dowser'][0]]
list_keys = {}
@client.event
async def on_ready():
    print('Bot ON')
    print(client.user.name)
    print(client.user.id)
    await client.change_presence(activity=discord.Game(name="Vendendo servidores Discord 💎"))
@client.event
async def on_message(message) :

    if message.content.lower().startswith('!pay ') and len(message.content.lower().split()) :

        message = message.content.lower().split()
        channel = message.channel

        valor_do_euro = float(message(1))
        valor_do_serviço = float(message(2))
        valor_em_reais = valor_do_serviço * valor_do_euro
        advertiser = 15 * valor_em_reais / 100
        cut = advertiser - valor_em_reais

        await channel.purge(limit=1)

        embed = discord.Embed(
            title = 'Payment',
            description = 'Cut: R$'+str(cut),
            color = cor,
        )
        embed.set_thumbnail(url='https://cdn.discordapp.com/icons/838541121713471548/b2dd19ce2e73db32e92ab2dd30bd888f.webp?size=1024')
        await channel.send(embed=embed)

    if message.content.lower().startswith('!verify') and len(message.content.lower().split()) :
        sleep(2)
        channel = message.channel
        message = message.content.upper().split()
        await channel.purge(limit=2)

    if message.content.lower().startswith('!1') and len(message.content.lower().split()) :
        if message.author.id in staff_id_list:
            print(message.author.id , ' Executou !1')
            channel = message.channel
            await channel.purge(limit=20)

            embed = func.create_embed('Olá, Como posso ajudar ? :slight_smile:')

            await channel.send(embed=embed)
    
    if message.content.lower().startswith('set!') and len(message.content.lower().split()) :
        message1 = message.content.lower().split('!')
        list_keys[message.author.name] = message1[1]
        channel = message.channel
        await channel.purge(limit=10)
        key_embed = str(list_keys)
        key_embed = key_embed.replace(',','\n')
        key_embed = key_embed.replace('{','')
        key_embed = key_embed.replace('}','')
        key_embed = key_embed.replace("'",'')
        key_embed = key_embed.replace(':',' -')

        embed = discord.Embed(
                title = 'KEYSTONE',
                description = key_embed,
                color = cor
            )
        embed.set_thumbnail(url='https://cdn.discordapp.com/icons/838541121713471548/b2dd19ce2e73db32e92ab2dd30bd888f.webp?size=1024')
        await channel.send(embed=embed)

    if message.content.lower().startswith('!3') and len(message.content.lower().split()) :
        if message.author.id in staff_id_list:
            print(message.author.id , ' Executou !3')
            channel = message.channel
            await channel.purge(limit=1)

            embed = func.create_embed('Por favor mande o comprovante e seu nick. :slight_smile:')

            await channel.send(embed=embed)

    if message.content.lower().startswith('!4') and len(message.content.lower().split()) :
        if message.author.id in staff_id_list:
            print(message.author.id , ' Executou !4')
            channel = message.channel
            await channel.purge(limit=1)

            embed = func.create_embed('Seus distintivos será creditados assim que relogar, obrigado, aproveite o game :heart:')

            await channel.send(embed=embed)

    if message.content.lower().startswith('!off') and len(message.content.lower().split()) :
        if message.author.id in staff_id_list:
            print(message.author.id , ' Executou !off')
            channel = message.channel
            await channel.purge(limit=2)

            embed = func.create_embed('@everyone \n Servidor OFF :red_circle:')

            await channel.send(embed=embed)

    if message.content.lower().startswith('!manager') and len(message.content.lower().split()) :
        if message.author.id in staff_id_list:
            print(message.author.id , ' Executou !manager')
            channel = message.channel
            await channel.purge(limit=2)

            embed = func.create_embed('@everyone \nServidor em manutenção :gear:')

            await channel.send(embed=embed)

    if message.content.lower().startswith('!on') and len(message.content.lower().split()) :
        if message.author.id in staff_id_list:
            print(message.author.id , ' Executou !on')
            channel = message.channel
            await channel.purge(limit=2)

            embed = func.create_embed('@everyone \nServidor ON :green_circle:')

            await channel.send(embed=embed)

    if message.content.lower().startswith('!download') and len(message.content.lower().split()) :
        if message.author.id in staff_id_list:
            print(message.author.id , ' Executou !download')
            channel = message.channel
            await channel.purge(limit=1)

            embed = discord.Embed(
                title = 'Download',
                description = 'Ao clicar em download você será redirecionado para nosso site.',
                color = cor,
                url = 'https://www.hogwarts2d.net'
            )
            embed.set_thumbnail(url='https://marcas-logos.net/wp-content/uploads/2020/01/Hogwarts-logo.png')
            await channel.send(embed=embed)

    if message.content.lower().startswith('!pre') and len(message.content.lower().split()) :
        if message.author.id in staff_id_list:
            print(message.author.id , ' Executou !4')
            channel = message.channel
            await channel.purge(limit=1)

            embed = func.create_embed('!1 - Olá, Como posso ajudar ? :slight_smile:\n'
                                      '!2 - Ticket registrado, obrigado por relatar. :slight_smile:\n'
                                      '!3 - Por favor mande o comprovante e seu nick. :slight_smile:\n'
                                      '!4 - Seus distintivos será creditados assim que relogar, obrigado, aproveite o game :heart:\n'
                                      '!on - @everyone \n Servidor ON :green_circle:\n'
                                      '!off - @everyone \n Servidor OFF :red_circle:\n'
                                      '!manager - @everyone \nServidor em manutenção :gear: \n'
                                      '!download - mensagem para redirecionar ao site\n'
                                      )

            await channel.send(embed=embed)
client.run(key)