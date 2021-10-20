import discord, random
from discord import voice_client
from discord.ext import commands
from youtube_dl import YoutubeDL # cmd 창에서 미리 pip install 필요
import time
import asyncio
import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from discord.utils import get
from discord import FFmpegPCMAudio

bot = commands.Bot(command_prefix='!') # 항상 앞에 '!'를 붙이는 것을 원칙으로 함

@bot.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(bot.user.name)
    print('connection was succesful')
    await bot.change_presence(status=discord.Status.online, activity=None)

@bot.command()
async def 주사위(ctx, number:int):
    await ctx.send(embed = discord.Embed(title = '주사위', description = f'주사위를 굴려 {random.randint(1,int(number))}이(가) 나왔습니다. (1~{number})', color = 0x00ff00))

@bot.command()
async def 로또(ctx):
    await ctx.send(embed = discord.Embed(title = '로또', description = f'이번주 예상 당첨 번호는 {random.randint(1, 46)}, {random.randint(1, 46)}, {random.randint(1, 46)}, {random.randint(1, 46)}, {random.randint(1, 46)}, {random.randint(1, 46)}이(가) 나왔습니다.', color = 0x00ff00))

@bot.command()
async def 공지(ctx):
    await ctx.send(embed = discord.Embed(title = '모임날짜', description = f'이번주 게임 모임 날짜는 금요일로 선정되었습니다.', color = 0x00ff00))

@bot.command()
async def 명령어(ctx):
    await ctx.send(embed = discord.Embed(title = '명령어', description = '!설명, !공지, !주사위 + (숫자), !로또, [노래듣고 싶을때 !들어와 -> !URL재생 + (듣고싶은 노래 URL)], !나가', color = 0x00ff00))

@bot.command()
async def 설명(ctx):
    await ctx.send(embed = discord.Embed(title = '설명', description = '해당 봇은 현준이가 그냥 재미 삼아 만든 것이므로 그냥 갖고 놀면 됩니다.', color = 0x00ff00))

@bot.command()
async def 들어와(ctx):
    try:
        global vc
        vc = await ctx.message.author.voice.channel.connect()
    except:
        try:
            await vc.move_to(ctx.message.author.voice.channel)
        except:
            await ctx.send("현재 채널에 아무도 없습니다.")

@bot.command()
async def 나가(ctx):
    try:
        await vc.disconnect()
    except:
        await ctx.send("전 채널에 아직 들어가지 않았는걸요?")


@bot.command()
async def URL재생(ctx, *, url):
    YDL_OPTIONS = {'format': 'bestaudio','noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    if not vc.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        await ctx.send(embed = discord.Embed(title= "노래 재생", description = "현재 " + url + "을(를) 재생하고 있습니다.", color = 0x00ff00))
    else:
        await ctx.send("노래가 이미 재생되고 있습니다!")

bot.run('Token Number')