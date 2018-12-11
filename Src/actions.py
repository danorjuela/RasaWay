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
		vegetales =  ["lechuga","tomate","pepino","pepinillos","pimenton","cebolla","aceitunas","jalapechos"]
		seteo = []
		v0 = tracker.get_slot('vegetal')
		v1 = tracker.get_slot('vegetal1')
		v2 = tracker.get_slot('vegetal2')
		v3 = tracker.get_slot('vegetal3')
		v4 = tracker.get_slot('vegetal4')
		v5 = tracker.get_slot('vegetal5')
		v6 = tracker.get_slot('vegetal6')
		v7 = tracker.get_slot('vegetal7')
		v8 = tracker.get_slot('vegetal8')

		if v0 is None:
			response = "Puedes elegir entre los siguentes vegetales "
		elif v1 is None and v2 is None and v3 is None and v4 is None  and v5 is None  and v6 is None and v7 is None and v8 is None:
			response = "Puedes elegir 7 vegetales mas"
			vegetales.remove(v0) 
			seteo.append(SlotSet("vegetal1",v0))
		elif v2 is None and v3 is None and v4 is None  and v5 is None  and v6 is None and v7 is None and v8 is None:
			response = "Puedes elegir 6 vegetales mas"
			vegetales.remove(v1)
			vegetales.remove(v0) 
			seteo.append(SlotSet("vegetal2",v0))
		elif v3 is None and v4 is None  and v5 is None  and v6 is None and v7 is None and v8 is None:
			response = "Puedes elegir 5 vegetales mas "
			vegetales.remove(v0)
			vegetales.remove(v1)
			vegetales.remove(v2)
			seteo.append(SlotSet("vegetal3",v0))
		elif  v4 is None  and v5 is None  and v6 is None and v7 is None and v8 is None:
			response = "Puedes elegir 4 vegetales mas "
			vegetales.remove(v0)
			vegetales.remove(v1)
			vegetales.remove(v2)
			vegetales.remove(v3)
			seteo.append(SlotSet("vegetal4",v0))
		elif  v5 is None  and v6 is None and v7 is None and v8 is None:
			response = "Puedes elegir 3 vegetales mas "
			vegetales.remove(v0)
			vegetales.remove(v1)
			vegetales.remove(v2)
			vegetales.remove(v3)
			vegetales.remove(v4)
			seteo.append(SlotSet("vegetal5",v0))
		elif  v6 is None and v7 is None and v8 is None:
			response = "Puedes elegir 2 vegetales mas "
			vegetales.remove(v0)
			vegetales.remove(v1)
			vegetales.remove(v2)
			vegetales.remove(v3)
			vegetales.remove(v4)
			vegetales.remove(v5)
			seteo.append(SlotSet("vegetal6",v0))
		elif v7 is None and v8 is None:
			response = "Puedes elegir 1 vegetales mas "
			vegetales.remove(v0)
			vegetales.remove(v1)
			vegetales.remove(v2)
			vegetales.remove(v3)
			vegetales.remove(v4)
			vegetales.remove(v5)
			vegetales.remove(v6)
			seteo.append(SlotSet("vegetal7",v0))
		elif v8 is None:
			vegetales.remove(v0)
			vegetales.remove(v1)
			vegetales.remove(v2)
			vegetales.remove(v3)
			vegetales.remove(v4)
			vegetales.remove(v5)
			vegetales.remove(v6)
			vegetales.remove(v7)
			seteo.append(SlotSet("vegetal8",v0))
		

		buttons =[]
		for vegetal in vegetales:
				buttons.append({ "title": vegetal , "payload": vegetal })
		if len(buttons)>0:
			buttons.append({ "title": "ninguno" , "payload": "ninguno" })
			dispatcher.utter_button_message(response, buttons)
		return seteo
		
class ActionSalsaAdicional(Action):
	def name(self):
		return 'action_salsa_adicional'
		
	def run(self, dispatcher, tracker, domain):
		salsas =  ["mayonesa","cebolla dulce","mostaza dulce","moztaza","bbq","chipote","rach","ajo"]
		seteo = []
		s0 = tracker.get_slot('salsa')
		s1 = tracker.get_slot('salsa1')
		s2 = tracker.get_slot('salsa2')
		s3 = tracker.get_slot('salsa3')

		if s0 is None:
			response = "Puedes elegir entre las siguientes salsas "
		elif s1 is None and s2 is None and s3 is None:
			response = "Puedes elegir 2 vegetales mas "
			salsa.remove(s0)
			seteo.append(SlotSet("salsa1",s0))
		elif s2 is None and s3 is None:
			response = "Puedes elegir 1 vegetales mas "
			salsa.remove(s0)
			salsa.remove(s1)
			seteo.append(SlotSet("salsa2",s0))
		elif s3 is None:
			salsa.remove(s0)
			salsa.remove(s1)
			seteo.append(SlotSet("salsa2",s0))

		buttons =[]
		for salsa in salsas:
			buttons.append({ "title": salsa , "payload": salsa })
		if len(buttons)>0:
			buttons.append({ "title": "Ninguno" , "payload": "Ninguno" })
			dispatcher.utter_button_message(response, buttons)
		return seteo

class ActionAdicional(Action):
	def name(self):
		return 'action_adicional'
		
	def run(self, dispatcher, tracker, domain):
		salsas =  ["mayonesa","cebolla dulce","mostaza dulce","moztaza","bbq","chipote","rach","ajo"]
		seteo = []
		s0 = tracker.get_slot('salsa')
		s1 = tracker.get_slot('salsa1')
		s2 = tracker.get_slot('salsa2')
		s3 = tracker.get_slot('salsa3')

		if s0 is None:
			response = "Puedes elegir entre las siguientes salsas "
		elif s1 is None and s2 is None and s3 is None:
			response = "Puedes elegir 2 vegetales mas "
			salsa.remove(s0)
			seteo.append(SlotSet("salsa1",s0))
		elif s2 is None and s3 is None:
			response = "Puedes elegir 1 vegetales mas "
			salsa.remove(s0)
			salsa.remove(s1)
			seteo.append(SlotSet("salsa2",s0))
		elif s3 is None:
			salsa.remove(s0)
			salsa.remove(s1)
			seteo.append(SlotSet("salsa2",s0))

		buttons =[]
		for salsa in salsas:
			buttons.append({ "title": salsa , "payload": salsa })
		if len(buttons)>0:
			buttons.append({ "title": "Ninguno" , "payload": "Ninguno" })
			dispatcher.utter_button_message(response, buttons)
		return seteo
