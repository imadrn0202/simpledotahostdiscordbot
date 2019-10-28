# BSD 3-Clause License
# Copyright (c) 2019, Hugonun(https://github.com/hugonun)
# All rights reserved.

import discord
from discord.ext import commands
from discord.utils import get



client = commands.Bot(command_prefix='#')
#do not edit this part
hostname =''
slot = 0
members = []
membersId = []



#edit this part
max_slot = 10

main_lobby_channel = 'beginner-lobby-1'
main_lobby_channel_id = 633000398252277798

admin_lobby_channel = 'testadmin'
admin_lobby_channel_id = 632186558807670784


    
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def hostlobby(ctx, arg):
    if ctx.channel.name == admin_lobby_channel:

        global hostname

        if hostname == '':
            
            hostname = arg
       
            lobbymain =  client.get_channel(main_lobby_channel_id)
            
            await lobbymain.send('Hey @everyone ' + ctx.author.name + ' has created a lobby! to join just type #joinlobby ' + hostname )

        else:
            await ctx.channel.send('Lobby ' + hostname +' is still running')

@client.command()
async def joinlobby(ctx, arg):
    if ctx.channel.name == main_lobby_channel:

        if arg == hostname:


            global slot
            global members
            global membersId
            global max_slot

            
            slot = slot + 1

            
            existing = set(membersId)

            member = ctx.author.name
            memberId = ctx.author.id

            if slot <= max_slot:
                if memberId not in existing:
                    strslot = str(slot)
                    existing.add(memberId)
                    members.append(member)
                    membersId.append(memberId)
                    await ctx.channel.send(ctx.author.mention +' has joined the lobby!, to join the match type #joinlobby ' + hostname + ' (' +  strslot + '/'+  str(max_slot) + ') ')
                else:
                    await ctx.channel.send(ctx.author.mention +' you are already in the lobby ' + hostname)
            else:
                memberList = ",".join(members)

                lobbyadmin =  client.get_channel(admin_lobby_channel)

                await lobbyadmin.send('Hey <@&629623683958177793>es The lobby ' + hostname + ' is full PLEASE #startlobby ' + hostname + '\n\nPlayers\n' + memberList)
          
                await ctx.channel.send(ctx.author.mention + ' Sorry ' + hostname +' lobby is full')

@client.command()
async def startlobby(ctx, arg1, arg2, arg3):


    if ctx.channel.name == admin_lobby_channel:
        global hostname
        if arg1 == hostname:
            global slot
            global max_slot

            if slot == max_slot:
                global membersId
                global members
              
        
                for discordId in membersId:
                    user = client.get_user(discordId)
                    await user.send('Hey!  The lobby has started ! \nTo join the lobby \n1. Go to your DOTA 2 Client\n2. Click the Play DOTA Button at the lower right.\n3. Click the Custom Lobbies and click browse \nLobby name: {}  \nLobby Password: {}'.format(arg2, arg3))
                    await user.send('\n\nIf you cannot join the lobby please type #leavelobby at the channel where you signed up')
                
                #mainchannel
                lobbymain =  client.get_channel(main_lobby_channel_id)

                await lobbymain.send(hostname + ' lobby has started! To all participants, please check the private message from DFZDotaHostBot for the instructions')

                hostname =''
                slot = 0
                members = []
                membersId = []

            else:
                await ctx.channel.send(ctx.author.mention + 'Lobby is not yet full')


@client.command()
async def leavelobby(ctx):
    if ctx.channel.name == main_lobby_channel:

        global slot
        global members
        global membersId
        global max_slot

        member = ctx.author.name
        memberId = ctx.author.id
        
        if memberId in membersId:
            members.remove(member)
            membersId.remove(memberId)
            slot = slot - 1
            strslot = str(slot)
            
            await ctx.channel.send(ctx.author.mention +' has left the lobby '+ hostname + ' to join the match type #joinlobby ' + hostname + ' (' +  strslot + '/' + str(max_slot) + ')')
        else:
            await ctx.channel.send(ctx.author.mention + 'you are not in a lobby')

@client.command()
async def deletelobby(ctx):
    if ctx.channel.name == admin_lobby_channel:

        global hostname
        global slot
        global members
        global membersId

        await ctx.channel.send(ctx.author.mention +' deleted the lobby: ' + hostname)
        hostname =''
        slot = 0
        members = []
        membersId = []
    


client.run('NjMxODQwMzQ3NDMzMjA1Nzky.XbbP-g.nQdcd2kcpTRI-LJUb-iNlNlGhK8') # Add bot token here
