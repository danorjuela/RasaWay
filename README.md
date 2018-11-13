# Bot del clima 

Bot del clima hecho en rasa

## Entrenar NLU

``` python nlu_model.py ```

### Entrenar Core

1. ejecutar servidor de acciones personalizadas 

``` python -m rasa_core_sdk.endpoint --actions actions ```  

2. en un nuevo terminal ejecutar el entrenamiento

``` python dialogue_management_model.py```  
 
### Usar el entrenamiento en linea:

1. ejecutar servidor de acciones personalizadas 

``` python -m rasa_core_sdk.endpoint --actions actions ``` 

2. ejecutar Script de entrenamiento

``` python train_online.py ```  







