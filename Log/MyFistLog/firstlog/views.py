from django.shortcuts import render
import logging.config

from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
import schedule
import time
#custom intance
logger = logging.getLogger('django')
print(logger)
#logger1 = logging.getLogger('django.request')
#logger2 = logging.getLogger('django.server')

# Create your views here.
def flog(request):
     #context={'f1':'fyfuy'}
     logger.info('pankaj info')
     logger.debug('my 1st log debug')
     logger.warning('my 1st warning')
     logger.error('my 1st log error')

     n = int(input('enter first number'))
     n1 = int(input('enter 2nd number'))
     try:
          result = n / n1
          print(result)
          logger.info('successfully print result')

     except ZeroDivisionError as s:
          #logger.critical(str(s))
          logger.exception('exception please enter non zero value')
     return render(request, 'base.html')

'''# Standard instance of a logger with __name__
stdlogger = logging.getLogger(__name__)
# Custom instance logging with explicit name
dbalogger = logging.getLogger('dba')


def index(request):
     stdlogger.debug("Entering index method")
     return render(request, 'base.html')


def contactform(request):
     stdlogger.info("Call to contactform method")

     try:
          stdlogger.debug("Entering store_id conditional block")
          # Logic to handle store_id
     except Exception as e:
          stdlogger.exception(e)

     stdlogger.info("Starting search on DB")
     try:
          stdlogger.info("About to search db")
          # Loging to search db
     except Exception as e:
          stdlogger.error("Error in searchdb method")
          dbalogger.error("Error in searchdb method, stack %s" % (e))
     return render(request, 'base.html')'''

"""def sendmail(request):
     subject='Test massage'
     massage='this mail from my django '
     sendfrom='settings.EMAIL_HOST_USER'
     toaddress=['gtghule8605@gmail.com',]
     fail_silently = False,
     send_mail(subject,massage,sendfrom,toaddress,fail_silently)
     return render(request,'index.html')

"""

