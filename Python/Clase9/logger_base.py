import logging as log # Importacion del modulo
log.basicConfig(level=log.DEBUG,
                format= '%(asctime)s:%(levelname)s [%(filename)s:%(lineno)s] %(message)s', #logging a DEBUG los mensajes.)
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('capa_datos.log'), # Archivo donde se guardan los logs
                    log.StreamHandler() # Agregamos un manejador de flujo para mostrar los logs en la consola.
                ])

if __name__ == '__main__':
    log.debug('Mensaje a nivel debug') 
    log.info('Mensaje a nivel info') 
    log.warning('Mensaje a nivel warning') 
    log.error('Mensaje a nivel error')
    log.critical('Mensaje a nivel critical')