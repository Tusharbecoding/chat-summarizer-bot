import discord
from discord.ext import commands
import google.genai as genai
import os 
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is now online!")

@bot.command()
async def summarize(ctx, channel: discord.TextChannel = None, last: str = "last", count: int = 20):
    """Summarize messages from a channel. Usage: !summarize #channel last 50"""
    if not channel:
        channel = ctx.channel

    try:
        messages = []
        async for message in channel.history(limit=count):
            if not message.author.bot:
                timestamp = message.created_at.strftime("%H:%M")
                messages.append(f"[{timestamp}] {message.author.display_name}: {message.content}")

        if not messages:
            await ctx.send("No messages found to summarize.")
            return
        messages.reverse()
        conversation = "\n".join(messages)

        prompt = f"""
        Summarize this Discord conversation in a clear, concise format:
        {conversation}
Provide:
1. Main topics discussed
2. Key decisions or conclusions
3. Important information shared
4. Action items (if any)
Keep it brief but informative.
"""
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )
        summary = response.text

        embed = discord.Embed(
            title = f"Summary of #{channel.name}",
            description = f"Last {count} messages",
            color=0x00ff00
        )

        embed.add_field(name="Summary", value=summary[:1024], inline=False)
        embed.set_footer(text=f"Requested by {ctx.author.display_name}")

        await ctx.send(embed=embed)
    
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

@bot.command()
async def tldr(ctx, count: int = 10):
    """Quick summary of current conversation. Usage: !tldr 15"""
    await summarize(ctx, ctx.channel, "last", count)

@bot.command(name="daily-summary")
async def daily_summary(ctx, channel: discord.TextChannel = None):
    """Daily digest of important discussions. Usage: !daily-summary #channel"""
    if not channel:
        channel = ctx.channel

    try:
        yesterday = datetime.utcnow() - timedelta(days=1)
        messages = []
        async for message in channel.history(after=yesterday):
            if not message.author.bot and len(message.content) > 10:
                timestamp = message.created_at.strftime("%H:%M")
                messages.append(f"[{timestamp}] {message.author.display_name}: {message.content}")
            
        if not messages:
            await ctx.send("No significant messages found for last 24 hours.")
            return 
        
        messages.reverse()
        conversation = "\n".join(messages)

        prompt = f"""
Create a daily digest of this Discord channel activity from the last 24 hours:
{conversation}
Format as:
**Daily Summary - {channel.name}**

**Hot Topics:**
- Topic 1
- Topic 2

**Key Points:**
- Point 1  
- Point 2

**Action Items:**
- Item 1
- Item 2

Keep it organized and highlight the most important discussions.
"""
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents = prompt
        )

        summary = response.text

        await ctx.send(f"```\n{summary}\n```")

    except Exception as e:
        await ctx.send(f"Error generating daily summary: {e}")

bot.run(os.getenv("DISCORD_TOKEN"))

