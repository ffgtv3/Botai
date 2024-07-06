import discord
import os

# Загружаем данные из файла data.txt
with open("data.txt", "r") as f:
    data = f.read().splitlines()

# Создаем экземпляр бота
client = discord.Client()

# Обрабатываем события
@client.event
async def on_ready():
    print(f"Бот {client.user} подключился к Discord!")

@client.event
async def on_message(message):
    # Игнорируем сообщения от самого бота
    if message.author == client.user:
        return

    # Обрабатываем сообщения, начинающиеся с префикса "!"
    if message.content.startswith("!"):
        command = message.content[1:]
        if command == "data":
            # Отправляем данные из data.txt в ответ на сообщение
            await message.channel.send("\n".join(data))
        elif command == "интересно":
            # Отправляем ответ с интересным фактом в чат с ID 1259185689623396573
            channel = client.get_channel(1259185689623396573)
            await channel.send("Знаете ли вы, что население Земли составляет около 8 миллиардов человек?")

# Запуск бота
client.run(os.environ['MTI1ODcxODA0NDAzNzg0MTAyMw.GZ07-j.-voDcRbRk3rRD97TGmZ0s_Qw3FddlDIY50otuY'])
