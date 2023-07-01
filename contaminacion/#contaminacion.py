import discord
import random
consejos=[
        "Apaga las luces cuando salgas de una habitación.",
        "Utiliza bombillas de bajo consumo o LED.",
        "Recicla tus residuos y separa los materiales correctamente.",
        "Usa productos reutilizables en lugar de desechables.",
        "Ahorra agua cerrando el grifo mientras te cepillas los dientes.",
        "Opta por el transporte público o comparte coche para reducir emisiones.",
        "Planta árboles y cuida de los espacios verdes en tu comunidad.",
        "Reduce el consumo de carne y opta por opciones vegetarianas o veganas.",
        "Compra productos locales y de temporada para reducir la huella de carbono del transporte.",
        "Revisa el aislamiento de tu hogar para ahorrar energía en la calefacción o refrigeración."
] 

#La variable intents almacena los privilegios del bot
intents = discord.Intents.default()

#Activar el privilegio de lectura de mensajes
intents.message_content = True

#Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print(f'Se inicio como {client.user}') 

@client.event
async def on_message(message):
    if message.content.startswith('$consejos'):
        consejos = random.choice(consejos)

Tipos_de_contaminacion=[
        "Contaminacion Acustica.",
        "Contaminacion Agricola.",
        "Contaminacion Ambiental.",
        "Contaminacion Antropogenica.",
        "Contaminacion Biologica.",
        "Contaminacion Cruzada.",
        "Contaminacion de los Alimentos.",
        "Contaminacion del agua.",
        "Contaminacion del aire.",
        "Contaminacion del suelo",
        "Contaminacion industrial",
        "Contaminacion Luminica",
        "Contaminacion Natural",
        "Contaminacion Quimica",
        "Contaminacion Radioactiva",
        "Contaminacion Termica",
        "Contaminacion Visual"
] 

#La variable intents almacena los privilegios del bot
intents = discord.Intents.default()

#Activar el privilegio de lectura de mensajes
intents.message_content = True

#Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print(f'Se inicio como {client.user}') 

@client.event
async def on_message(message):
    if message.content.startswith('$contaminacion'):
        Tipos_de_contaminacion = random.choice(Tipos_de_contaminacion)




client.run("token") # TOKEN --> No borrar