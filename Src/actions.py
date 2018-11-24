from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class ActionWeather(Action):
	def name(self):
		return 'action_weather'
		
	def run(self, dispatcher, tracker, domain):
		from apixu.client import ApixuClient
		api_key = '----' #your apixu key
		client = ApixuClient(api_key)

		loc = tracker.get_slot('location')
		print (loc)

		try:
			current = client.getCurrentWeather(q=loc)
			country = current['location']['country']
			city = current['location']['name']
			condition = current['current']['condition']['text']
			temperature_c = current['current']['temp_c']
			humidity = current['current']['humidity']
			wind_mph = current['current']['wind_mph']

			response = """Actualmente en {}. La temperatura es {} grados, La humedad  {}% y la velocidad del viento es {} mph.""".format( city, temperature_c, humidity, wind_mph)
		except:
			response = "no pude encontrar esa localizacion, podrias revisar la escritura"

		dispatcher.utter_message(response)
		return [SlotSet('location',None)]



