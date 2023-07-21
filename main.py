import discord,os,asyncio,csv,googletrans
from discord.ext import commands

translator = googletrans.Translator()
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents,command_prefix="* ")
token = #token
version="B-1.0.0"




# Initial Setting Code
Gllen_member=[]
csvfile = open('premium.csv', 'r', encoding='utf-8')
read_file = csv.reader(csvfile)
for line in read_file:
    line_list=[]
    for i in line:
        line_list.append(int(i))
    Gllen_member.append(line_list)
csvfile.close()

for i in range(len(Gllen_member)):
    if Gllen_member[i][1]==0:
        Gllen_member[i][1]="Gllen Developer"
    elif Gllen_member[i][1]==1:
        Gllen_member[i][1]="Gllen Member"
    elif Gllen_member[i][1]==2:
        Gllen_member[i][1]="Gllen Hyper"
    elif Gllen_member[i][1]==3:
        Gllen_member[i][1]="Gllen Friends"
    elif Gllen_member[i][1]==529:
        Gllen_member[i][1]="Gllen Supporter"
    else:
        Gllen_member[i][1]="Gllen에 가입하지 않음"
    
    if Gllen_member[i][2]==0:
        Gllen_member[i][2]='Developer'
    elif Gllen_member[i][2]==1:
        Gllen_member[i][2]='Member'
    elif Gllen_member[i][2]==2:
        Gllen_member[i][2]='Propheta AI+'
    elif Gllen_member[i][2]==3:
        Gllen_member[i][2]='Propheta Hyper'
    elif Gllen_member[i][2]==52901:
        Gllen_member[i][2]='Beta Tester(AI+)'
    elif Gllen_member[i][2]==52902:
        Gllen_member[i][2]='Beta Tester(Hyper)'
    else:
        Gllen_member[i][1]='Propheta에 가입하지 않음'
    
    if Gllen_member[i][3]==-1:
        Gllen_member[i][3]="Unlimited"


"""⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌"""
# Function Setting

async def bt(games): #discord setting
    await bot.wait_until_ready()

    while not bot.is_closed():
        for g in games:
            await bot.change_presence(status = discord.Status.online, activity = discord.Game(g))
            await asyncio.sleep(10)



async def Member_S(id): #member searching
    global Gllen_member
    member_info=await bot.fetch_user(id)
    for i in range(len(Gllen_member)):
        print(Gllen_member[i])
        if int(id)==Gllen_member[i][0]:
            return [member_info,Gllen_member[i][1],Gllen_member[i][2],Gllen_member[i][3]]
    return [member_info,"Gllen에 가입하지 않음","ProPheta에 가입하지 않음",0]

async def emset(ctx,embed): #embed setting
    global Gllen_member
    member=await Member_S(int(ctx.author.id))
    embed.color=0x2cf6e5
    if ctx.author.avatar!=None:
        embed.set_footer(icon_url=ctx.author.avatar, text='{} ({})'.format(ctx.author,member[2]))
    else:
        embed.set_footer(text='{} ({})'.format(ctx.author,member[2]))
    return embed


"""⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌"""
# Main Command Interaction Code

@bot.event
async def on_ready():
    os.system('echo \033[32mPropheta {} Online\033[0m'.format(version))
    os.system('echo \033[34m{}\033[0m'.format(bot.user.name))
    os.system('echo \033[34m{}\033[0m'.format(bot.user.id))
    os.system('echo \033[35m================\033[0m')
    await bt(['Propheta {} ㅣ VM 24H Server'.format(version)])

@bot.slash_command(description="자신의 정보 확인")
async def 정보(ctx):
    global Gllen_member
    member=await Member_S(ctx.author.id)
    print(member)
    embed = discord.Embed(title="정보", description="information of `{}`".format(member[0].name))
    embed = await emset(ctx,embed)
    embed.add_field(name="이름", value=member[0].name, inline=True)
    embed.add_field(name="Tag", value="#"+str(member[0].discriminator), inline=True)
    embed.add_field(name="계정 생성 시간", value=(str(member[0].created_at))[:-13], inline=True)
    embed.add_field(name="Gllen ㅣ Propheta Tier", value=f"```ansi\n\033[33m{member[1]}\033[0m ㅣ \033[33m{member[2]}\033[0m```", inline=False)
    embed.add_field(name="AI Use Limits", value=f"```fix\n{member[3]}\n```", inline=False)
    await ctx.respond(embed=embed)

@bot.slash_command(description="Google Translator를 이용한 번역")
async def 번역(ctx, content: discord.commands.Option(str, "번역할 내용")):
    detected_str=translator.detect(content)
    print(detected_str)
    detected_lang=detected_str.lang
    print(detected_lang)
    if detected_lang=='ko':
        trans_lang='en'
        embed = discord.Embed(title="Propheta Translate", description="Mode: `{}` => `{}`".format("ko","en"))
        embed = await emset(ctx,embed)
        trans_content = translator.translate(content, src='ko', dest='en')
    elif detected_lang=='en':
        trans_lang='ko'
        embed = discord.Embed(title="Propheta Translate", description="Mode: `{}` => `{}`".format("en","ko"))
        embed = await emset(ctx,embed)
        trans_content = translator.translate(content, src='en', dest='ko')
    else:
        await ctx.respond("이해할 수 없는 언어입니다.")
        return
    embed.add_field(name="`Input`({})".format(detected_lang), value=f"```fix\n{content}```", inline=False)
    embed.add_field(name="`Output`({})".format(trans_lang), value=f"```fix\n{trans_content.text}```", inline=False)
    print(trans_lang,trans_content,embed)
    await ctx.respond(embed=embed)


"""⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌⨌"""
# Discord Bot running Code

bot.run(token)
