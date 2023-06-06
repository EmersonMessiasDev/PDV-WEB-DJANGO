from django.contrib import messages
import constants  # Substitua com a localização real do seu módulo constants

has_error = False

if v_codigo <= 0:
    messages.add_message(request, messages.ERROR, constants.INVALID_CODE_ERROR)
    has_error = True
else:
    produto.codigo = v_codigo

if v_descricao == '':
    messages.add_message(request, messages.ERROR, constants.INVALID_DESC_ERROR)
    has_error = True
else:
    produto.descricao = v_descricao

if v_valor <= 0 or v_valor == '':
    messages.add_message(request, messages.ERROR, constants.INVALID_VAL_ERROR)
    has_error = True
else:
    produto.valor = v_valor

if v_quantidade == '':
    messages.add_message(request, messages.ERROR, constants.INVALID_QTY_ERROR)
    has_error = True
else:
    produto.quantidade = v_quantidade

if has_error:
    return redirect('pdvWeb:atualizacao_produto', produto.id)
else:
    produto.save()
    messages.add_message(request, messages.SUCCESS, constants.UPDATE_SUCCESS)
    return redirect('pdvWeb:produtos')