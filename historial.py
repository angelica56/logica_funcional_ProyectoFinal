import logging

logging.basicConfig(
    filename="escuela.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def registrar_log(mensaje):
    logging.info(mensaje)