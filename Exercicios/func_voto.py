#Recebe o ano de nascimento
#Retorna um valor literal indicando voto obrigatório, opcional ou negado.

from datetime import datetime

def voto(ano=datetime.now().year):
    """
    :param ano: ano de nascimento
    """
    s = ''
    global id 
    id = datetime.now().year - ano
    if 18<= id < 65:
        s = f'Com {id} anos: voto obrigatório'
        return s
        
    elif 16<= id <18 or id>65:
        s = f'Com {id} anos: voto opcional'
        return s
    
    else:
        s = f'Com {id} anos: não vota'
        return s



id = 0
v1 = voto(int(input('Ano de nascimento: ')))
print(v1)
