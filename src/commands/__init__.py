# import requests
# import os

# bot_token = os.getenv("BOT_TOKEN")
# def update_bot_commands(bot_token, commands):
#     """
#     Update the list of commands for a Telegram bot using the Telegram Bot API.

#     Args:
#         bot_token (str): The token of the Telegram bot.
#         commands (list): A list of dictionaries where each dictionary represents a command
#             with "command" and "description" keys.

#     Returns:
#         bool: True if the update was successful, False otherwise.
#     """
#     url = f'https://api.telegram.org/bot{bot_token}/setMyCommands'
#     data = {"commands": commands}

#     response = requests.post(url, json=data)

#     if response.status_code == 200:
#         print("Commands updated successfully")
#         return True
#     else:
#         print("Command update failed")
#         print(f"{response.json()=}")
#         return False

# # Example usage:
# new_commands = [
#     {"command": "start", "description": "Start the bot"},
#     {"command": "help", "description": "Get help"},
#     # Add more commands as needed
# ]

# update_bot_commands(bot_token, new_commands)