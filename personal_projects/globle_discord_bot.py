import discord
from discord.ext import commands, tasks
import datetime
import random
import pytz  # We'll need this for timezone handling

# Bot setup and permissions
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Channel IDs
GENERAL_CHANNEL_ID = 1186811309732405320  # Your #general channel ID
GLOBLE_CHANNEL_ID = 1332448473684906025   # Your #globle channel ID

# Get the EST timezone
eastern = pytz.timezone('US/Eastern')

# Reminder messages
morning_messages = [
    "Good morning! Let's play Globle.",
    "Rise and shine geography lovers! Time for today's Globle puzzle!",
    "Good morning! Challenge your geography skills with today's Globle.",
    "It's a new day with a new Globle puzzle waiting for you!"
]

evening_messages = [
    "It's 6pm! Have you played Globle yet? Play and post your results in #globle!",
    "Evening reminder: Today's Globle is waiting for you! Share your score in #globle!",
    "Geography fans! It's 6pm - still time to play today's Globle puzzle!",
    "Don't forget to play Globle today! Post your results in #globle when you're done!"
]

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    
    # Attempt to get channel objects via IDs
    general_channel = bot.get_channel(GENERAL_CHANNEL_ID)
    globle_channel = bot.get_channel(GLOBLE_CHANNEL_ID)
    
    # Print channel status
    if general_channel:
        print(f"Found #general channel: {general_channel.name}")
    else:
        print("Could not find #general channel!")
    
    if globle_channel:
        print(f"Found #globle channel: {globle_channel.name}")
    else:
        print("Could not find #globle channel!")
    
    # Start the scheduled tasks
    morning_reminder.start()
    evening_reminder.start()

# Task for 9am EST reminder in #globle channel
@tasks.loop(hours=24)
async def morning_reminder():
    channel = bot.get_channel(GLOBLE_CHANNEL_ID)
    if channel:
        # Choose a random message for variety
        message = random.choice(morning_messages)
        await channel.send(message)

# Task for 6pm reminder in #general channel
@tasks.loop(hours=24)
async def evening_reminder():
    channel = bot.get_channel(GENERAL_CHANNEL_ID)
    if channel:
        # Choose a random message for variety
        message = random.choice(evening_messages)
        await channel.send(message)

# Set the time for the morning task to run at 9am EST
@morning_reminder.before_loop
async def before_morning_reminder():
    await bot.wait_until_ready()
    
    # Get current time in EST
    now = datetime.datetime.now(eastern)
    
    # Calculate time until next 9am EST
    future = datetime.datetime.combine(now.date(), datetime.time(9, 0))
    future = eastern.localize(future)
    
    # If it's already past 9am, schedule for tomorrow
    if now.time() >= datetime.time(9, 0):
        future += datetime.timedelta(days=1)
    
    # Convert to UTC for sleep_until (which uses UTC)
    future_utc = future.astimezone(pytz.utc)
    
    print(f"Morning reminder scheduled for: {future} EST")
    await discord.utils.sleep_until(future_utc)

@evening_reminder.before_loop
async def before_evening_reminder():
    await bot.wait_until_ready()
    
    # Get current time in EST
    now = datetime.datetime.now(eastern)
    
    # Calculate time until next 6pm EST
    future = datetime.datetime.combine(now.date(), datetime.time(18, 0))
    future = eastern.localize(future)
    
    # If it's already past 6pm, schedule for tomorrow
    if now.time() >= datetime.time(18, 0):
        future += datetime.timedelta(days=1)
    
    # Convert to UTC for sleep_until
    future_utc = future.astimezone(pytz.utc)
    
    print(f"Evening reminder scheduled for: {future} EST")
    await discord.utils.sleep_until(future_utc)

# Command to test sending a message to #general
@bot.command(name='testgeneral')
async def test_general(ctx):
    channel = bot.get_channel(GENERAL_CHANNEL_ID)
    if channel:
        await channel.send("This is a test message in #general! Time to play Globle!")
        await ctx.send("Test message sent to #general!")
    else:
        await ctx.send("Could not find the #general channel.")

# Command to test sending a message to #globle
@bot.command(name='testgloble')
async def test_globle(ctx):
    channel = bot.get_channel(GLOBLE_CHANNEL_ID)
    if channel:
        await channel.send("This is a test message in #globle! Don't forget to post your results here!")
        await ctx.send("Test message sent to #globle!")
    else:
        await ctx.send("Could not find the #globle channel.")

# Add a manual trigger command for each reminder
@bot.command(name='sendmorning')
async def send_morning(ctx):
    channel = bot.get_channel(GLOBLE_CHANNEL_ID)
    if channel:
        message = random.choice(morning_messages)
        await channel.send(message)
        await ctx.send("Manual morning reminder sent!")
    else:
        await ctx.send("Could not find the #globle channel.")

@bot.command(name='sendevening')
async def send_evening(ctx):
    channel = bot.get_channel(GENERAL_CHANNEL_ID)
    if channel:
        message = random.choice(evening_messages)
        await channel.send(message)
        await ctx.send("Manual evening reminder sent!")
    else:
        await ctx.send("Could not find the #general channel.")

# Run the bot
bot.run('MTM1MjQ5NzY1NjAzNDc1NDYxMA.GNnLUE.Gr-PafFTNzIoYkePvREwEr6NmKwFcsmWdiRvOM')  # Replace with your actual token