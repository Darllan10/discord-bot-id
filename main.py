import discord
from discord import app_commands
from discord.ext import commands
import random
import os

intents = discord.Intents.default()
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)
tree = bot.tree

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")
    try:
        synced = await tree.sync()
        print(f"Comandos sincronizados: {len(synced)}")
    except Exception as e:
        print(f"Erro: {e}")

@tree.command(name="pedir", description="Gera um ID e muda seu nome.")
async def pedir(interaction: discord.Interaction):
    member = interaction.user
    random_id = random.randint(1, 999)
    nome = member.display_name
    if "|" in nome:
        nome = nome.split("|", 1)[-1].strip()
    novo_nome = f"{random_id}|{nome}"

    try:
        await member.edit(nick=novo_nome)
        await interaction.response.send_message(f"✅ Seu ID é `{novo_nome}`", ephemeral=True)
    except discord.Forbidden:
        await interaction.response.send_message("❌ Sem permissão para mudar seu nick!", ephemeral=True)

bot.run(os.getenv("TOKEN"))
