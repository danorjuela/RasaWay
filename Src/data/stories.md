## fallback story
* out_of_scope
   - action_default_fallback
  
## greet
* greet
   - utter_greet

## goodbye
* goodbye
   - utter_goodbye

## story001
* intent_star
   - utter_greet
* informacionDia
   - action_informacion_dia
* pedidoTipo{"tipo": "Baratisimo"}
   - slot{"tipo": "Baratisimo"}
   - utter_tamano
* pedidoTamano{"tamano": "15"}
   - slot{"tamano": "15"}
   - utter_pan
* pedidoPan{"pan": "Avena"}
   - slot{"pan": "Americano"}
   - utter_queso
* pedidoQueso{"queso": "Americano"}
   - slot{"queso": "Americano"}
   - utter_adicion_queso
* pedidoQuesoAdional{"quesoAdicional": "Americano"}
   - slot{"quesoAdicional": "Americano"}
   - utter_coccion
* pedidoCoccion{"coccion": "Frio"}
   - slot{"coccion": "Frio"}
   - action_vegetal_adicional
* pedidoVegetales{"vegetal": "Lechuga"}
   - slot{"vegetal": "Lechuga"}
   - action_vegetal_adicional
* pedidoVegetales{"vegetal": "Tomate"}
   - slot{"vegetal2": "Tomate"}
   - action_vegetal_adicional
* pedidoVegetales{"vegetal": "Pepino"}
   - slot{"vegetal": "Pepino"}
   - action_vegetal_adicional
* pedidoVegetales{"vegetal": "Pepiillos"}
   - slot{"vegetal": "Pepiillos"}
   - action_vegetal_adicional
* pedidoVegetales{"vegetal": "Pimenton"}
   - slot{"vegetal": "Pimenton"}
   - action_vegetal_adicional
* pedidoVegetales{"vegetal": "Cebolla"}
   - slot{"vegetal": "Cebolla"}
   - action_vegetal_adicional
* pedidoVegetales{"vegetal": "Aceitunas"}
   - slot{"vegetal7": "Aceitunas"}
   - action_vegetal_adicional
* pedidoVegetales{"vegetal": "Jalapechos"}
   - slot{"vegetal": "Jalapechos"}
   - action_vegetal_adicional
   - action_salsa_adicional
* pedidoSalsas{"salsa": "BBQ"}
   - slot{"salsa": "BBQ"}
   - action_salsa_adicional
* pedidoSalsas{"salsa": "Chipote"}
   - slot{"salsa": "Chipote"}
   - action_salsa_adicional
* pedidoSalsas{"salsa": "Mayonesa"}
   - slot{"salsa": "Mayonesa"}
   - action_salsa_adicional
   - utter_combo
* pedido
   - utter_gaseosa
* pedidoGaseosa{"gaseosa": "Pepsi"}
   - slot{"gaseosa": "Pepsi"}
   - utter_galleta
* pedidoGalletas{"galleta": "Chocolate"}
   - slot{"galleta": "Chocolate"}
   - utter_papas
* pedidoPapas{"papas": "BBQ"}
   - action_informacion_sub
   - action_confirmar_sub


## story002
* intent_star
   - utter_greet
* informacionDia
   - action_informacion_dia
* pedidoTipo{"tipo": "Baratisimo"}
   - slot{"tipo": "Baratisimo"}
   - utter_tamano
* pedidoTamano{"tamano": "15"}
   - slot{"tamano": "15"}
   - utter_pan
* pedidoPan{"pan": "Avena"}
   - slot{"pan": "Americano"}
   - utter_queso
* pedidoQueso{"queso": "Americano"}
   - slot{"queso": "Americano"}
   - utter_adicion_queso
* negacion
   - utter_coccion
* pedidoCoccion{"coccion": "Frio"}
   - slot{"coccion": "Frio"}
   - action_vegetal_adicional
* pedidoVegetales{"vegetal": "Lechuga"}
   - slot{"vegetal": "Lechuga"}
   - action_vegetal_adicional
* pedidoVegetales{"vegetal": "Tomate"}
   - slot{"vegetal2": "Tomate"}
   - action_vegetal_adicional
* pedidoVegetales{"vegetal": "Pepino"}
   - slot{"vegetal": "Pepino"}
   - action_vegetal_adicional
* pedidoVegetales{"vegetal": "Pepiillos"}
   - slot{"vegetal": "Pepiillos"}
   - action_vegetal_adicional
* pedidoVegetales{"vegetal": "Pimenton"}
   - slot{"vegetal": "Pimenton"}
   - action_vegetal_adicional
* pedidoVegetales{"vegetal": "Cebolla"}
   - slot{"vegetal": "Cebolla"}
   - action_vegetal_adicional
* pedidoVegetales{"vegetal": "Aceitunas"}
   - slot{"vegetal7": "Aceitunas"}
   - action_vegetal_adicional
* pedidoVegetales{"vegetal": "Jalapechos"}
   - slot{"vegetal": "Jalapechos"}
   - action_vegetal_adicional
   - action_salsa_adicional
* pedidoSalsas{"salsa": "BBQ"}
   - slot{"salsa": "BBQ"}
   - action_salsa_adicional
* pedidoSalsas{"salsa": "Chipote"}
   - slot{"salsa": "Chipote"}
   - action_salsa_adicional
* pedidoSalsas{"salsa": "Mayonesa"}
   - slot{"salsa": "Mayonesa"}
   - action_salsa_adicional
   - utter_combo
* pedido
   - utter_gaseosa
* pedidoGaseosa{"gaseosa": "Pepsi"}
   - slot{"gaseosa": "Pepsi"}
   - utter_galleta
* pedidoGalletas{"galleta": "Chocolate"}
   - slot{"galleta": "Chocolate"}
   - utter_papas
* pedidoPapas{"papas": "BBQ"}
   - action_informacion_sub
   - action_confirmar_sub


## story003
* intent_star
   - utter_greet
* informacionDia
   - action_informacion_dia
* pedidoTipo{"tipo": "Baratisimo"}
   - slot{"tipo": "Baratisimo"}
   - utter_tamano
* pedidoTamano{"tamano": "15"}
   - slot{"tamano": "15"}
   - utter_pan
* pedidoPan{"pan": "Avena"}
   - slot{"pan": "Americano"}
   - utter_queso
* pedidoQueso{"queso": "Americano"}
   - slot{"queso": "Americano"}
   - utter_adicion_queso
* negacion
   - utter_coccion
* pedidoCoccion{"coccion": "Frio"}
   - slot{"coccion": "Frio"}
   - action_vegetal_adicional
* pedidoVegetales{"vegetal": "Lechuga"}
   - slot{"vegetal": "Lechuga"}
   - action_vegetal_adicional
* negacion
   - action_salsa_adicional
* pedidoSalsas{"salsa": "BBQ"}
   - slot{"salsa": "BBQ"}
   - action_salsa_adicional
* pedidoSalsas{"salsa": "Chipote"}
   - slot{"salsa": "Chipote"}
   - action_salsa_adicional
* pedidoSalsas{"salsa": "Mayonesa"}
   - slot{"salsa": "Mayonesa"}
   - action_salsa_adicional
   - utter_combo
* pedido
   - utter_gaseosa
* pedidoGaseosa{"gaseosa": "Pepsi"}
   - slot{"gaseosa": "Pepsi"}
   - utter_galleta
* pedidoGalletas{"galleta": "Chocolate"}
   - slot{"galleta": "Chocolate"}
   - utter_papas
* pedidoPapas{"papas": "BBQ"}
   - action_informacion_sub
   - action_confirmar_sub


## story004
* intent_star
   - utter_greet
* informacionDia
   - action_informacion_dia
* pedidoTipo{"tipo": "Baratisimo"}
   - slot{"tipo": "Baratisimo"}
   - utter_tamano
* pedidoTamano{"tamano": "15"}
   - slot{"tamano": "15"}
   - utter_pan
* pedidoPan{"pan": "Avena"}
   - slot{"pan": "Americano"}
   - utter_queso
* pedidoQueso{"queso": "Americano"}
   - slot{"queso": "Americano"}
   - utter_adicion_queso
* negacion
   - utter_coccion
* pedidoCoccion{"coccion": "Frio"}
   - slot{"coccion": "Frio"}
   - action_vegetal_adicional
* pedidoVegetales{"vegetal": "Lechuga"}
   - slot{"vegetal": "Lechuga"}
   - action_vegetal_adicional
* negacion
   - action_salsa_adicional
* pedidoSalsas{"salsa": "BBQ"}
   - slot{"salsa": "BBQ"}
   - action_salsa_adicional
* negacion
   - utter_combo
* pedido
   - utter_gaseosa
* pedidoGaseosa{"gaseosa": "Pepsi"}
   - slot{"gaseosa": "Pepsi"}
   - utter_galleta
* pedidoGalletas{"galleta": "Chocolate"}
   - slot{"galleta": "Chocolate"}
   - utter_papas
* pedidoPapas{"papas": "BBQ"}
   - action_informacion_sub
   - action_confirmar_sub



## story005
* intent_star
   - utter_greet
* informacionDia
   - action_informacion_dia
* pedidoTipo{"tipo": "Baratisimo"}
   - slot{"tipo": "Baratisimo"}
   - utter_tamano
* pedidoTamano{"tamano": "15"}
   - slot{"tamano": "15"}
   - utter_pan
* pedidoPan{"pan": "Avena"}
   - slot{"pan": "Americano"}
   - utter_queso
* pedidoQueso{"queso": "Americano"}
   - slot{"queso": "Americano"}
   - utter_adicion_queso
* negacion
   - utter_coccion
* pedidoCoccion{"coccion": "Frio"}
   - slot{"coccion": "Frio"}
   - action_vegetal_adicional
* pedidoVegetales{"vegetal": "Lechuga"}
   - slot{"vegetal": "Lechuga"}
   - action_vegetal_adicional
* negacion
   - action_salsa_adicional
* pedidoSalsas{"salsa": "BBQ"}
   - slot{"salsa": "BBQ"}
   - action_salsa_adicional
* negacion
   - utter_combo
* negacion
   - action_informacion_sub


## story006
* intent_star
   - utter_greet
* informacionMenu
   - utter_menu
* pedidoTipo{"tipo": "Baratisimo"}
   - slot{"tipo": "Baratisimo"}
   - utter_tamano
* pedidoTamano{"tamano": "15"}
   - slot{"tamano": "15"}
   - utter_pan
* pedidoPan{"pan": "Avena"}
   - slot{"pan": "Americano"}
   - utter_queso
* pedidoQueso{"queso": "Americano"}
   - slot{"queso": "Americano"}
   - utter_adicion_queso
* pedidoQuesoAdional{"quesoAdicional": "Americano"}
   - slot{"quesoAdicional": "Americano"}
   - utter_coccion
* pedidoCoccion{"coccion": "Frio"}
   - slot{"coccion": "Frio"}
   - action_vegetal_adicional
* pedidoVegetales{"vegetal": "Lechuga"}
   - slot{"vegetal": "Lechuga"}
   - action_vegetal_adicional
* pedidoVegetales{"vegetal": "Tomate"}
   - slot{"vegetal2": "Tomate"}
   - action_vegetal_adicional
* pedidoVegetales{"vegetal": "Pepino"}
   - slot{"vegetal": "Pepino"}
   - action_vegetal_adicional
* pedidoVegetales{"vegetal": "Pepiillos"}
   - slot{"vegetal": "Pepiillos"}
   - action_vegetal_adicional
* pedidoVegetales{"vegetal": "Pimenton"}
   - slot{"vegetal": "Pimenton"}
   - action_vegetal_adicional
* pedidoVegetales{"vegetal": "Cebolla"}
   - slot{"vegetal": "Cebolla"}
   - action_vegetal_adicional
* pedidoVegetales{"vegetal": "Aceitunas"}
   - slot{"vegetal7": "Aceitunas"}
   - action_vegetal_adicional
* pedidoVegetales{"vegetal": "Jalapechos"}
   - slot{"vegetal": "Jalapechos"}
   - action_vegetal_adicional
   - action_salsa_adicional
* pedidoSalsas{"salsa": "BBQ"}
   - slot{"salsa": "BBQ"}
   - action_salsa_adicional
* pedidoSalsas{"salsa": "Chipote"}
   - slot{"salsa": "Chipote"}
   - action_salsa_adicional
* pedidoSalsas{"salsa": "Mayonesa"}
   - slot{"salsa": "Mayonesa"}
   - action_salsa_adicional
   - utter_combo
* pedido
   - utter_gaseosa
* pedidoGaseosa{"gaseosa": "Pepsi"}
   - slot{"gaseosa": "Pepsi"}
   - utter_galleta
* pedidoGalletas{"galleta": "Chocolate"}
   - slot{"galleta": "Chocolate"}
   - utter_papas
* pedidoPapas{"papas": "BBQ"}
   - action_informacion_sub
   - action_confirmar_sub


## story007
* intent_star
   - utter_greet
* pedidoTipo{"tipo": "Baratisimo"}
   - slot{"tipo": "Baratisimo"}
   - utter_tamano
* pedidoTamano{"tamano": "15"}
   - slot{"tamano": "15"}
   - utter_pan
* pedidoPan{"pan": "Avena"}
   - slot{"pan": "Americano"}
   - utter_queso
* pedidoQueso{"queso": "Americano"}
   - slot{"queso": "Americano"}
   - utter_adicion_queso
* pedidoQuesoAdional{"quesoAdicional": "Americano"}
   - slot{"quesoAdicional": "Americano"}
   - utter_coccion
* pedidoCoccion{"coccion": "Frio"}
   - slot{"coccion": "Frio"}
   - action_vegetal_adicional
* pedidoVegetales{"vegetal": "Lechuga"}
   - slot{"vegetal": "Lechuga"}
   - action_vegetal_adicional
* pedidoVegetales{"vegetal": "Tomate"}
   - slot{"vegetal2": "Tomate"}
   - action_vegetal_adicional
* pedidoVegetales{"vegetal": "Pepino"}
   - slot{"vegetal": "Pepino"}
   - action_vegetal_adicional
* pedidoVegetales{"vegetal": "Pepiillos"}
   - slot{"vegetal": "Pepiillos"}
   - action_vegetal_adicional
* pedidoVegetales{"vegetal": "Pimenton"}
   - slot{"vegetal": "Pimenton"}
   - action_vegetal_adicional
* pedidoVegetales{"vegetal": "Cebolla"}
   - slot{"vegetal": "Cebolla"}
   - action_vegetal_adicional
* pedidoVegetales{"vegetal": "Aceitunas"}
   - slot{"vegetal7": "Aceitunas"}
   - action_vegetal_adicional
* pedidoVegetales{"vegetal": "Jalapechos"}
   - slot{"vegetal": "Jalapechos"}
   - action_vegetal_adicional
   - action_salsa_adicional
* pedidoSalsas{"salsa": "BBQ"}
   - slot{"salsa": "BBQ"}
   - action_salsa_adicional
* pedidoSalsas{"salsa": "Chipote"}
   - slot{"salsa": "Chipote"}
   - action_salsa_adicional
* pedidoSalsas{"salsa": "Mayonesa"}
   - slot{"salsa": "Mayonesa"}
   - action_salsa_adicional
   - utter_combo
* pedido
   - utter_gaseosa
* pedidoGaseosa{"gaseosa": "Pepsi"}
   - slot{"gaseosa": "Pepsi"}
   - utter_galleta
* pedidoGalletas{"galleta": "Chocolate"}
   - slot{"galleta": "Chocolate"}
   - utter_papas
* pedidoPapas{"papas": "BBQ"}
   - action_informacion_sub
   - action_confirmar_sub



