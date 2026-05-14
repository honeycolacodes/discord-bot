import discord
from discord.ext import commands

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# !hello command
@bot.command()
async def hello(ctx):
    await ctx.send(f"Hey {ctx.author.name}! 👋")

# !flip command - flips a coin
@bot.command()
async def flip(ctx):
    import random
    result = random.choice(["Heads 🪙", "Tails 🪙"])
    await ctx.send(result)

# !roll command - rolls a dice
@bot.command()
async def roll(ctx, sides: int = 6):
    import random
    result = random.randint(1, sides)
    await ctx.send(f"🎲 You rolled a {result}!")

# !joke command
@bot.command()
async def joke(ctx):
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
        "Why did the programmer quit? Because they didn't get arrays! 😄",
        "How do you comfort a JavaScript bug? You console it! 💻",
    ]
    import random
    await ctx.send(random.choice(jokes))

# !help command
@bot.command()
async def helpme(ctx):
    help_text = """
**Available Commands:**
`!hello` — Say hello to the bot
`!flip` — Flip a coin
`!roll [sides]` — Roll a dice (default: 6 sides)
`!joke` — Get a random programming joke
    """
    await ctx.send(help_text)

# Replace with your bot token
bot.run("YOUR_BOT_TOKEN_HERE")
