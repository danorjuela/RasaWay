from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from builtins import str
from flask import Blueprint, request, jsonify

from rasa_core import constants
from rasa_core.channels import InputChannel
from rasa_core.channels.channel import UserMessage, OutputChannel

logger = logging.getLogger(__name__)


class TelegramBot(OutputChannel):
	def __init__(self, token, chat_id):
		self.token = token
		self.chat_id = chat_id
		
	def send_text_message(self, recipient_id, message):
		import telebot
		bot = telebot.TeleBot(self.token)
		bot.send_message(self.chat_id, message) 
        
        
class TelegramInput(InputChannel):
	def __init__(self, access_token , verify, webhook_url, debug_mode=False):
		self.access_token = access_token
		self.debug_mode = debug_mode
		self.verify = verify 
		self.webhook_url = webhook_url
		
	def blueprint(self, on_new_message):
		from flask import Flask, request, Response
		telegram_webhook = Blueprint('telegram_webhook', __name__)
		
		@telegram_webhook.route('/', methods = ['GET'])
		def health():
			return jsonify({'status':'ok'})
			
		@telegram_webhook.route('/webhook', methods = ['POST'])
		def event():
			update = request.get_json()
			#if request.json.get('type') == 'url_verification':
			#	return request.json.get('challenge'), 200
				
			if "message" in update:
				text = update["message"]["text"]
				chat_id = update["message"]["chat"]["id"]
				on_new_message(UserMessage(text, TelegramBot(self.access_token , chat_id)))
			return Response(), 200
			
		return telegram_webhook
				