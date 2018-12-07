from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import datetime
import mRedis

class ActionInformacionDia(Action):
	def name(self):
		return 'action_informacion_dia'
		
	def run(self, dispatcher, tracker, domain):
		x = datetime.datetime.now()
		dicdias = {'MONDAY':'Lunes','TUESDAY':'Martes','WEDNESDAY':'Miercoles','THURSDAY':'Jueves', 'FRIDAY':'Viernes','SATURDAY':'Sabado','SUNDAY':'Domingo'}
		anho = x.year
		mes =  x.month
		dia = x.day
		fecha = datetime.date(anho, mes, dia)
		dia = dicdias[fecha.strftime('%A').upper()]
		sub = ""
		if dia == "lunes":
			sub = "Pollo"
		elif dia == "Martes":
			sub = "italianisimo"
		elif dia == "Miercoles":
			sub = "Carne"
		elif dia == "Jueves":
			sub = "Atun"
		elif dia == "Viernes":
			sub = "Italiano BTM"
		elif dia == "Sabado":
			sub = "cerdo BBQ"
		elif dia == "Domingo":
			sub = "Pavo y jamon"
		
		response =  "el subway de hoy " + dia + " es " +  sub 
		#dispatcher.utter_message(response)
		buttons =[]
		buttons.append({ "title": "Si" , "payload": "quiero un "+sub })
		buttons.append({ "title": "No" , "payload": "no quiero el sub del dia" })
		dispatcher.utter_button_message(response + " Desea este sub", buttons)
		
		
		#return [SlotSet('Tipo',sub)]

class ActionInformacionSub(Action):
	def name(self):
		return 'action_informacion_sub'
		
	def run(self, dispatcher, tracker, domain):
		tipo = tracker.get_slot('tipo')
		tamano = tracker.get_slot('tamano')
		pan = tracker.get_slot('pan')
		coccion = tracker.get_slot('coccion')
		queso = tracker.get_slot('queso')
		quesoAdicional = tracker.get_slot('quesoAdicional')

		response =  "el subway que pidio es " + tipo + " de tamaño " + tamano + " en pan " + pan + " en queso " + queso + " con coccion " + coccion 
		buttons =[]
		buttons.append({ "title": "Si" , "payload": "si, quiero ese Sub" })
		buttons.append({ "title": "No" , "payload": "no, no quiero ese" })
		dispatcher.utter_button_message(response + ",Desea este sub", buttons)

class ActionConfirmarSub(Action):
	def name(self):
		return 'action_confirmar_sub'
		
	def run(self, dispatcher, tracker, domain):
		tipo = tracker.get_slot('tipo')
		tamano = tracker.get_slot('tamano')
		pan = tracker.get_slot('pan')
		coccion = tracker.get_slot('coccion')
		queso = tracker.get_slot('queso')
		quesoAdicional = tracker.get_slot('quesoAdicional')

		response =  "el subway que pidio es " + tipo + " de tamaño " + tamano + " en pan " + pan + " en queso " + queso + " con coccion " + coccion 

		redis = mRedis.redisConect()
        redis.pub(response)

		

class ActionVegetalAdicional(Action):
	def name(self):
		return 'action_vegetal_adicional'
		
	def run(self, dispatcher, tracker, domain):

class ActionVegetalAdicional(Action):
	def name(self):
		return 'action_salsa_adicional'
		
	def run(self, dispatcher, tracker, domain):

