import re
from django.contrib import messages
from django.contrib.messages import constants
from .models import *
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
import random
import string


def validar_produto(request, v_codigo, v_descricao, v_valor, v_quantidade ):
    if v_codigo <= 0 or v_codigo < 3:
        messages.add_message(request, messages.ERROR, 'Codigo não pode ficar vazio ou ser menor que 3')
        return False

    if v_descricao.strip() == '':
        messages.add_message(request, messages.ERROR, 'Descrição não pode ficar vazio')
        return False


    if v_valor <= 0 or v_valor == '':
        messages.add_message(request, messages.ERROR, 'Valor não pode ficar vazio')
        return False


    if v_quantidade == '':
        messages.add_message(request, messages.ERROR, 'Quantidade não pode ficar vazio')
        return False
    
    return True



