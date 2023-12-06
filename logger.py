import logging

class Logger():
    __instance = None

    def __new__(cls):
        """ Override the default __new__ method to implement singleton behavior. """
        if cls.__instance is None:
            cls.__instance = super(Logger, cls).__new__(cls)
            cls.__instance.__initialize__()
        return cls.__instance

    def __initialize__(self):
        self.logger = self.__build_logger__()

    def __build_logger__(self) -> logging.Logger:
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        logger.propagate = False

        # Creo un formatter per lo stdout handler, stampo solo il messaggio come un normale print
        stdout_formatter = logging.Formatter('%(message)s')
        # Creo uno stdout handler, imposto il formatter e lo aggiungo al logger
        stdout_handler = logging.StreamHandler()
        stdout_handler.setFormatter(stdout_formatter)
        stdout_handler.setLevel(logging.INFO)  # Si può impositare imposta un livello di registrazione differente per tutti i vari handler
        logger.addHandler(stdout_handler)

        file_formatter = logging.Formatter(
                '%(asctime)s.%(msecs)03d - %(levelname)s - %(name)s - %(funcName)s - %(lineno)d - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
        file_handler = logging.FileHandler('log.log', mode='a') # Uso append, ma si può usare 'w' per sovrascrivere ogni volta il contenuto
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)
        return logger


if __name__ == '__main__':
    logger = Logger().logger
    logger.info('This is a info message!')