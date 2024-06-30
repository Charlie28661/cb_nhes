import json
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='~cb ', intents=intents)

with open ("settings.json", "r", encoding="utf-8") as setting:
    settings = json.load(setting)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


@bot.command()
async def database_support(ctx):
    with open ("support.json", "r", encoding="utf-8") as support:
        supports = json.load(support)

    for type in supports:
        embed=discord.Embed(title="支援系統資料庫查詢系統", description="XX後台查詢系統")
        embed.add_field(name="類別", value=type["type"], inline=False)
        embed.add_field(name="暱稱 / 貼文編號", value=type["nickname"], inline=False)
        embed.add_field(name="建議 / 申告內容", value=type["content"], inline=False)
        await ctx.send(embed=embed)


if __name__ == '__main__':
    bot.run(settings["token"])