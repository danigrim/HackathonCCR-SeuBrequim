welcome_text = " Prazer, eu sou o Seu Brequim! " \
                "Estou aqui para te dar ajudar a encontrar as paradas e serviços de *baixo " \
               "custo* e *alta qualidade* nas estradas. Além disso, se você se sentir em perigo," \
               " me mande um *SOS* que te ajudo a encontrar suporte. Também posso te avisar quando tiver amigos caminhoneiros por perto. Se você quiser" \
                "compartilhar a sua localização com outros caminhoneiros, para fazer" \
               "parte da *comunidade Seu Brequim*, responda “sim”, caso contrário responda “não” e " \
                "só te dou dicas."

thanks_for_sharing = 'Obrigada por compartilhar sua localização. ' \
                    '*Você nunca mais estará sozinho na estrada!*' \
                    'Se estiver procurando serviços de qualidade na estrada é só perguntar ' \
                    'por *restaurantes*, *paradas*, *banheiros*, *SOS*, *serviços médicos* e eu te ajudo!'

thanks_fornot_sharing = 'Tudo bem amigo, pode deixar que não vou compartilhar sua localizacao. ' \
                    'Se estiver procurando serviços de qualidade na estrada é só perguntar ' \
                    'por *restaurantes*, *paradas*, **banheiros**, *SOS*, *serviços médicos* e eu te ajudo!'


def map_reply(req):
    key_word = ''
    if req == 'eat':
        key_word = 'comer'
    elif req == 'help':
        key_word = 'conseguir ajuda'
    elif req =='bathroom':
        key_word = 'ir ao banheiro'
    elif req == 'sleep':
        key_word = 'descansar'
    return " Nessa foto você vê um mapa com os melhores lugares para " + key_word + ". Em" \
                        " ouro está a melhor qualidade e preço." \
                       " Se quiser saber o endereço, distância ou quantos amigos do Brequim estão lá, " \
                       "é só digitar o *numero* ao lado do ponto no mapa."


# Location request
def request_location_message(request):
    key_word = ''
    if request == 'eat':
        key_word = 'comer'
    elif request == 'sleep':
        key_word ='parar e descansar sem custo'
    elif request =='bathroom':
        key_word = 'banheiros gratuitos '
    elif request == 'help':
        key_word = 'pedir ajuda'
    return "Me diga a rodovia e o km que você está, assim posso te enviar os melhores lugares para " + key_word + " perto de você"
