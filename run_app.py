from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
#from rasa_telegram_connector import TelegramInput
from rasa_core.channels.telegram import TelegramInput
from rasa_core.utils import EndpointConfig

import logging
logging.basicConfig(level=logging.DEBUG)

nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/nlu')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")


agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter, action_endpoint = action_endpoint)


input_channel = TelegramInput(
        # you get this when setting up a bot
        access_token="",
        # this is your bots username
        verify="RasalinaBot",
        # the url your bot should listen for messages
        webhook_url="matabares.ngrok.io/webhooks/telegram/webhook")


agent.handle_channels([input_channel], 5004, serve_forever=True)