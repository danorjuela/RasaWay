from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
#from rasa_telegram_connector import TelegramInput
from rasa_core.channels.telegram import TelegramInput
from rasa_core.utils import EndpointConfig

import logging
logging.basicConfig(level=logging.DEBUG)

nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weathernlu')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter, action_endpoint = action_endpoint)


input_channel = TelegramInput(
        # you get this when setting up a bot
        access_token="",
        # this is your bots username
        verify="RasalinaBot",
        # the url your bot should listen for messages
        webhook_url="matabares.ngrok.io/webhooks/telegram/webhook")


#input_channel = SlackInput('xoxp-447570327334-446111098707-448087355143-7816d5215f0fe387a47288e29b57dc1d', #app verification token
#							'xoxb-447570327334-448087356887-JcwRgqNVA40tVUYEIVREbq1n', # bot verification token
#							'jHoAxJLk1eWUrdza6QoTvARJ', # slack verification token
#							True)

# set serve_forever=False if you want to keep the server running


agent.handle_channels([input_channel], 5004, serve_forever=True,)