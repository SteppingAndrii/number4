import logging

# logging.basicConfig(level=logging.DEBUG, filename="log.log", filemode="w")
# logging.debug("IM DEBUGGING")
logging.basicConfig(
    level=logging.INFO, 
    filename="log.log", 
    filemode="w", 
    format="%(asctime)s: %(levelname)s - %(message)s"
)

logging.info('The program was launched succesfully')
# logging.debug('debug')
# logging.info('info')
# logging.warning('warning')
# logging.error('error')
# logging.critical('critical')