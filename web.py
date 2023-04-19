# https://www.youtube.com/watch?v=R26iojTwUv8
# https://pythonacademy.com.br/blog/como-usar-o-fastapi-para-construir-apis-no-python
# uvicorn web:app --reload - comando para rodar o servidor

# Rodar html no retorno da fastAPI
# https://eugeneyan.com/writing/how-to-set-up-html-app-with-fastapi-jinja-forms-templates/

import time
import logging
from fastapi import FastAPI
from datetime import datetime

# Registro de
logging.basicConfig(
    level=logging.WARNING,
    filename='logs.txt',
    filemode='a',
    encoding='utf-8',
    format='%(asctime)s : %(levelname)s : %(message)s'
)

# FastAPI
app = FastAPI()

# https://patineteavela.com/python/2021/01/16/como-localizar-datas-corretamente-usando-python-e-pytz.html
# https://www.freecodecamp.org/news/how-to-get-the-current-time-in-python-with-datetime/#:~:text=You%20can%20get%20the%20current%20time%20in%20a%20particular%20timezone,with%20another%20module%20called%20pytz%20.&text=You%20can%20then%20check%20for,all%20timezones%20of%20the%20world.
Relogio = datetime.now()


@app.get("/")
def site():
    return Relogio


@app.get("/page2/")
def site():
    return {"message": "Pagina 2"}


@app.get("/school_guardian/")
def school_guardian():
    return {"consultar_carros!"}


'''
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
'''


'''
https://testdriven.io/blog/moving-from-flask-to-fastapi/

'''