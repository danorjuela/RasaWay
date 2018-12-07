import time
import redis


class redisConect():
    def __init__(self):
        """
        incia la conexion con un servidor redis
        """
        self.redisClient = redis.StrictRedis(host='127.0.0.1', port=6379)


    def pub(self,comand,channel = 'rosaliaChannel'):
        """ publica en el servidor redis
        :param comand:
        :type comand: str
        :param channel: especifica el canal de la publicacion
        :type comand: str
        """
        self.redisClient.publish(channel,comand)

    def subs(self,channel = 'rosaliaChannel'):
        """ se subcrbe al servidor redis y empieza a revisar los mensajes
        se recomienda usar este metodo en un thread
        :param channel: especifica el canal a subcribirse
        :type comand: str
        """
        subs = self.redisClient.pubsub()
        subs.subscribe(channel)
        for comandItem in subs.listen():
            if type(comandItem['data']) is not int:
                #nota: poner expresiones regulares AQUI
                mensaje = comandItem['data'].decode('UTF-8')
                print (mensaje)



