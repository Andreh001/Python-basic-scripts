"""
Libreria a utilizar: Discord.py (1.7.x o superior)

Comandos para instalar

pip install discord

Si no funciona ese comando, puedes probar con estos:
    
python -m pip install discord

py -m pip install discord

Si estás en Linux:
    
python3 -m pip install discord
o
pip3 install discord
"""

import discord
from discord.ext import commands


token = "INGRESA TU TOKEN ACA"

bot = commands.Bot(command_prefix="!") # Prefijo del bot para los comandos


#----------#
# COMANDOS #
#----------#

"""
COMANDO 1, SUMA DE 2 NÚMEROS

Name = Nombre del comando, debe ser idéntico en el async def.
Aliases = Lista de todos los alias del comando, es decir, el acortador del comando.

Valores dentro del paréntesis

ctx = Representa al uso del bot.
num1 y num2 = Son los datos que debe recibir el comando para ser ejecutado, ejemplo:
    
!suma 10 20
("!" es el prefijo por defecto, si lo cambias deberás usar el que utilizaste)

Lo mismo para los otros comandos.
"""
@bot.command(name="suma", aliases=["sm", "sum"])
async def suma(ctx, num1: int, num2: int):
    sumatotal = num1 + num2
    await ctx.send("Resultado = {}".format(sumatotal))

@bot.command(name="multiplicar", aliases=["mult", "multipl"])
async def multiplicar(ctx, numero1: float, numero2: float):
    total = numero1 * numero2
    await ctx.send("Resultado = {}".format(total))

@bot.command(name="purge")
async def purge(ctx, cantidad = 0):
    if cantidad == 1:
        await ctx.channel.purge(limit=1)
        await ctx.send("¡Se eliminó **{}** mensaje con éxito!".format(cantidad), delete_after=10)
    elif cantidad > 1:
        await ctx.channel.purge(limit=cantidad)
        await ctx.send("¡Se eliminaron **{}** mensajes con éxito!".format(cantidad), delete_after=10)

"""
Lo que realiza este evento, es verificar si un mensaje
enviado por un usuario o bot comienza con algo en específico.

En este caso, si el mensaje comienza con "Hola" u "hola", el
bot enviará el mensaje que se encuentra con comillas.
"""
@bot.event
async def on_message(message):
    mensaje = message.content.startswith
    enviar_mensaje = message.channel.send
    if mensaje("Hola") or mensaje("hola"):
        await enviar_mensaje("Hola, ¡soy el bot!")

"""
Actividad del Bot

discord.ActivityType.playing = Tipo de actividad "Jugando".
discord.ActivityType.streaming = Tipo de actividad "Transmitiendo".
discord.ActivityType.listening = Tipo de actividad "Escuchando".
discord.ActivityType.watching = Tipo de actividad "Viendo".

name = Texto que se mostrará en la actividad

Si la actividad fuera playing y el texto fuera "Programar"
El mensaje en la actividad del bot sería: Jugando a Programar

"""
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Bot Básico - https://github.com/Andreh001"))
    print("Sesión iniciada como {}".format(bot.user)) # Muestra el nombre de usuario del bot con el su hashtag.

bot.run(token, bot=True, reconnect=True)