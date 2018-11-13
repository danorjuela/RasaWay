from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weathernlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-447570327334-446111098707-448087355143-7816d5215f0fe387a47288e29b57dc1d', #app verification token
							'xoxb-447570327334-448087356887-JcwRgqNVA40tVUYEIVREbq1n', # bot verification token
							'jHoAxJLk1eWUrdza6QoTvARJ', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))