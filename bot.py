import discord
import json
import urllib.request
from pprint import pprint
from discord.ext import commands, tasks


client = commands.Bot(command_prefix="bk ")


@client.event
async def on_ready():
    killbot.start()
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Albion Online"))
    print("Bot is ready")

'''
@client.event
async def on_member_join(member):
    print("{} has joined a server".format(member))


@client.event
async def on_member_remove(member):
    print("{} has left a server".format(member))
'''
'''
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Comando no valido.")
'''


last_kills = []


@tasks.loop(seconds=20)
async def killbot():
    URL = "https://gameinfo.albiononline.com/api/gameinfo/events?limit=50&offset=0"
    channel = client.get_channel(692768105906176064)

    with urllib.request.urlopen(URL) as url:
        data = json.loads(url.read().decode())

    #pprint(data)
    for kill_info in data:
        if kill_info['Killer']['GuildName'] == 'barbarian kingdom' or kill_info['Victim']['GuildName'] == 'barbarian kingdom':
            
            event_id = kill_info['EventId']

            
            if event_id


            battle_id = kill_info['BattleId']
            kill_area = kill_info['KillArea']
            time_stamp = kill_info['TimeStamp']
            
            #TODO-----------------------
            killer_info = kill_info['Killer']

            killer_guild_name = killer_info['GuildName']
            killer_alliance_tag = killer_info['AllianceTag']
            killer_item_power = round(killer_info['AverageItemPower'])
            killer_kill_fame = killer_info['KillFame']
            killer_name = killer_info['Name']

            killer_equipment_info = killer_info['Equipment']

            killer_equipment = []

            #pprint(killer_equipment_info)

            for key in killer_equipment_info:
                #print(f'equipo:{killer_equipment_info[key]}, tipo: {type(killer_equipment_info[key])}')
                if killer_equipment_info[key] != None:
                    killer_equipment.append((key, killer_equipment_info[key]['Type']))
                else:
                    killer_equipment.append((key, 'None'))
            #print(killer_equipment)


            #TODO-----------------------
            participants_info = kill_info['Participants']
            participants_damage_healing = []
            for participant_info in participants_info:
                participant_damage_done = round(participant_info['DamageDone'])
                participant_healing_done = round(participant_info['SupportHealingDone'])
                participant_name = participant_info['Name']
                if participant_damage_done > 0:
                    participants_damage_healing.append((participant_name, participant_damage_done))
                if participant_healing_done > 0:
                    participants_damage_healing.append((participant_name, participant_healing_done))

            #TODO-----------------------
            victim_info = kill_info['Victim']

            victim_guild = victim_info['GuildName']
            victim_alliance_tag = victim_info['AllianceTag']
            victim_item_power = round(victim_info['AverageItemPower'])
            victim_name = victim_info['Name']

            victim_equipment_info = victim_info['Equipment']

            victim_equipment = []

            for key in victim_equipment_info:
                if victim_equipment_info[key] != None:
                    victim_equipment.append((key, victim_equipment_info[key]['Type']))
                else:
                    victim_equipment.append((key, 'None'))
                        
            #print(victim_equipment)

            victim_inventory_info = victim_info['Inventory']

            victim_inventory = []

            for item_info in victim_inventory_info:
                if item_info != None:
                    victim_inventory.append(item_info['Type'])
            


            print(f'{killer_name} has killed {victim_name}')
            #await ctx.send(f'{killer_name} has killed {victim_name}')
            await channel.send(f'{killer_name} has killed {victim_name}')
            continue
        #print('nope')


@client.command(aliases=["lag"])
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")


@client.command(aliases=["embed"])
async def displayEmbed(ctx):
    #channel = client.get_channel(692768105906176064)
    embed = discord.Embed(
        title = 'Title',
        description = 'Description',
        colour = discord.Color(1))

    embed.set_footer(text='this is a footer')
    embed.set_image(url='https://gameinfo.albiononline.com/api/gameinfo/items/T8_2H_DOUBLEBLADEDSTAFF.png?count=1&quality=3')
    embed.set_thumbnail(url='https://albiononline2d.ams3.cdn.digitaloceanspaces.com/thumbnails/orig/T6_ARMOR_CLOTH_SET1')
    embed.set_author(name='Joaquin Calderon', icon_url='https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.messagescollection.com%2Fwp-content%2Fuploads%2F2015%2F04%2Fcute-cat-profile-for-facebook.jpg&f=1&nofb=1')
    embed.add_field(name='field name', value='field value', inline=False)
    embed.add_field(name='field name2', value='field value2', inline=True)
    embed.add_field(name='field name3', value='field value3', inline=True)

    await ctx.send(embed=embed)
    #await channel.send(embed=embed)


@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount + 1)
    print(f"Cleared {amount + 1} messages")


@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)


@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)


client.run("NjkyNzczNTE2MjU2NDc3MTk2.XoAUGQ.l67Jb9HsfjwjcbUdyWjvjWN5uZE")
