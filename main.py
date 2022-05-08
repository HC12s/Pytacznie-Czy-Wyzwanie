import discord
from discord_components import DiscordComponents, ComponentsBot, Button, SelectOption, Select
from discord.ext import commands
from data.botdata import *
from data.embeds import *
from data.devdata import teamids
client = commands.Bot(command_prefix=prefix)
client.remove_command('help')
DiscordComponents(client)




@client.event
async def on_ready():
    print("Bot is ready!")
    await client.change_presence(activity=discord.Streaming(name="Wpisz pcw!help", url="https://www.twitch.tv/Valorant"))


@client.command()
async def help(ctx):
    await ctx.send(embed=embed, components =[
    [Button(label="1", style="2", custom_id="one"), Button(label="2", style="2", custom_id="two")]])
    while True:
        try:
            interaction = await client.wait_for("button_click", check = lambda i: i.custom_id == "one")
            await interaction.send(content = "JD", ephemeral=False)
            interaction1 = await client.wait_for("button_click", check=lambda i: i.custom_id == "two")
            await interaction1.send(content = "Haha xD", ephemeral=False)
        except:
            await ctx.send("error")
















@client.command()
async def helpadmin(ctx):
    if str(ctx.author.id) in teamids:
        await ctx.send(embed=embedadmin, delete_after=15)
        await ctx.send(
            components=[
                discord_ui.Button(style=discord_ui.ButtonStyle.red, label='Click me!')
            ]
        )
        interaction = await client.wait_for('button_click', check=lambda i: i.component.label.startswith('Click me!'))
        await interaction.send('You clicked the button!')



@client.command()
async def button(ctx):
    await ctx.send(
        "This is a Button!",
        components = [
            discord_ui.Button(style=ButtonStyle.red, label ='Click me!')
        ]
    )
    interaction = await client.wait_for('button_click', check=lambda i: i.component.label.startswith('Click me!'))
    await interaction.send('You clicked the button!')


client.run(token)
