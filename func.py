import discord

cor = 0x5B087E

def  create_embed(description):

    embed = discord.Embed(
        description = description,
        color = cor,
        )
    embed.set_author(
        name="Hogwarts 2D",
        url="https://hogwarts2d.net",
        icon_url="https://marcas-logos.net/wp-content/uploads/2020/01/Hogwarts-logo.png"
        )
    
    
    return embed