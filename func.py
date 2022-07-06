import discord

cor = 0xFFFAF0

def  create_embed(description,q):

    embed = discord.Embed(
        description = description,
        color = cor,
        )
    embed.set_author(
        name='⭐️ '+q+' ⭐️',
        )
  
    return embed