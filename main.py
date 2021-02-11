import json

with open('BotConfig.json') as f:
  configuration = json.load(f)
bot_token = configuration['BotToken']

# print(bot_token)




def BootBot():

    # booting services

    pass


if __name__ == "__main__":
    BootBot()





















