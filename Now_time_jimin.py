import time
import datetime
import zoneinfo
import pytz
import asyncio
import tasks
from datetime import datetime
from datetime import date
from pytz import timezone

current_time = datetime.now(timezone('Asia/Seoul')).strftime("%H:%M")

global next_time

next_time = 0 

async def set_next_time():
    global next_time
    while True:
        if  datetime.now(timezone('Asia/Seoul')).strftime("%H:%M") > "01:11" and datetime.now(timezone('Asia/Seoul')).strftime("%H:%M") <= "02:22":
            next_time = "02:22"
            break

        if  datetime.now(timezone('Asia/Seoul')).strftime("%H:%M") > "02:22" and datetime.now(timezone('Asia/Seoul')).strftime("%H:%M") <= "03:33":
            next_time = "03:33"
            break

        if  datetime.now(timezone('Asia/Seoul')).strftime("%H:%M") > "03:33" and datetime.now(timezone('Asia/Seoul')).strftime("%H:%M") <= "04:44":
            next_time = "04:44"
            break

        if  datetime.now(timezone('Asia/Seoul')).strftime("%H:%M") > "04:44" and datetime.now(timezone('Asia/Seoul')).strftime("%H:%M") <= "05:55":
            next_time = "05:55"
            break

        if  datetime.now(timezone('Asia/Seoul')).strftime("%H:%M") > "05:55" and datetime.now(timezone('Asia/Seoul')).strftime("%H:%M") <= "10:10":
            next_time = "10:10"
            break

        if  datetime.now(timezone('Asia/Seoul')).strftime("%H:%M") > "10:10" and datetime.now(timezone('Asia/Seoul')).strftime("%H:%M") <= "11:11":
            next_time = "11:11"
            break

        if datetime.now(timezone('Asia/Seoul')).strftime("%H:%M")  > "11:11" and datetime.now(timezone('Asia/Seoul')).strftime("%H:%M") <= "12:12":
            next_time = "12:12"
            break

        if  datetime.now(timezone('Asia/Seoul')).strftime("%H:%M") > "12:12" and datetime.now(timezone('Asia/Seoul')).strftime("%H:%M") <= "13:11":
            next_time = "13:11"
            break

        if  datetime.now(timezone('Asia/Seoul')).strftime("%H:%M") > "13:11" and datetime.now(timezone('Asia/Seoul')).strftime("%H:%M") <= "14:22":
            next_time = "14:22"
            break

        if  datetime.now(timezone('Asia/Seoul')).strftime("%H:%M") > "14:22" and datetime.now(timezone('Asia/Seoul')).strftime("%H:%M") <= "15:33":
            next_time = "15:33"
            break

        if  datetime.now(timezone('Asia/Seoul')).strftime("%H:%M") > "15:33" and datetime.now(timezone('Asia/Seoul')).strftime("%H:%M") <= "16:44":
            next_time = "16:44"
            break

        if datetime.now(timezone('Asia/Seoul')).strftime("%H:%M")  > "16:44" and datetime.now(timezone('Asia/Seoul')).strftime("%H:%M") <= "17:55":
            next_time = "17:55"
            break

        if datetime.now(timezone('Asia/Seoul')).strftime("%H:%M")  > "17:55" and datetime.now(timezone('Asia/Seoul')).strftime("%H:%M") <= "22:10":
            next_time = "22:10"
            break

        if  datetime.now(timezone('Asia/Seoul')).strftime("%H:%M") > "22:10" and datetime.now(timezone('Asia/Seoul')).strftime("%H:%M") <= "23:11":
            next_time = "23:11"
            break

        if  datetime.now(timezone('Asia/Seoul')).strftime("%H:%M") > "23:11":
            next_time = "01:11"
            break
    await cal_time()

async def cal_time():
    global next_time
    set_next_time()
    while True:
        if datetime.now(timezone('Asia/Seoul')).strftime("%H:%M") == next_time:
            await now_time_jimin()
            await asyncio.sleep(70)
            await cal_time()
            break
        else:
            if  datetime.now(timezone('Asia/Seoul')).strftime("%H:%M") != next_time:
                await asyncio.sleep(40)
                await cal_time()
                break

async def now_time_jimin():
    channel = client.get_channel(915862213074493543)
    await channel.send("**<@386099935163973634> 지짐시**")

async def 지짐시(ctx):
    global next_time
    print(datetime.now(timezone('Asia/Seoul')).strftime("%H:%M"), "지짐시 호출됨")
    print(next_time)
    await ctx.channel.send(f'다음 지짐시는 {next_time}입니다.')



#@bot.event #지민 진정 기능
#async def on_message(message):
#    if "ㅅㅂ" in message.content: 
#        msg = await message.channel.send(f"{message.author.mention} 진정")
#        await asyncio.sleep(0.5)
#        await msg.delete()

