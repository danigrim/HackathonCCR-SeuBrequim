from flask import Flask, request, session
from datetime import datetime, timedelta
from twilio.twiml.messaging_response import MessagingResponse
import re

SECRET_KEY = 'a secret key'
app = Flask(__name__)
app.config.from_object(__name__)


def find_requests(msg_arr):
    dici = {}
    dici['eat'] = {'comer', 'comida', 'fome', 'food', 'jantar', 'almoco', 'almoço', 'lanche', 'lanchar', 'lanchinho', 'comidinha', 'rango', 'alimentacao', 'come'}
    dici['sleep'] = {'sono', 'dormir', 'descansar', 'sleep', 'deitar', 'parar', 'dormidinha', 'soneca', 'cama'}
    dici['bathroom'] = {'banheiro', 'mijar', 'banho', 'limpar', 'lavar'}
    dici['help'] = {'ajuda', 'sos', 'suporte', 'socorro', 'acidente', 'perigo', 'seguranca', 'atendimento'}
    match_lst = []
    for key,value in dici.items():
        for word in msg_arr:
            if word in value:
                match_lst.append(str(word))
    return match_lst


def find_street_name(road_index, msg_arr):
    road_name = ''
    if road_index > 0:
        for i in range(road_index, len(msg_arr)):
            if msg_arr[i].isdigit() or re.match('(KM|km|Km|Kilometro|KILOMETRO)', msg_arr[i]):
                return road_name
            else:
                road_name = road_name + ' ' + msg_arr[i]
    else:
        common_words = {'dentro', 'perto', 'estou', 'longe', 'aqui', 'fora', 'mim', 'voce', 'sabe'}
        for word in msg_arr:
            if word not in common_words and word.isalpha():
                return road_name


def get_location(msg_arr):
    location_dict = {}
    for i, word in enumerate(msg_arr):
        if word.isdigit():
            location_dict['km'] = word
        #case BR-xxx
        elif re.match('(BR|BR-|Br-|bR-|br|br-)[0-9]*3', word):
            location_dict['rodoviaria'] = msg_arr[i]
    road_type = {'rodoviária', 'rodoviaria', 'rodovia', 'rua', 'estrada', 'avenida', 'rodov', 'estr'}
    road_index = -1
    for ind, word in enumerate(msg_arr):
        if word in road_type:
            if ind < (len(msg_arr)-1):
                    road_index = ind + 1
    if not location_dict.get('rodoviaria', ''):
        location_dict['rodoviaria'] = find_street_name(road_index, msg_arr)
    return location_dict


@app.route("/", methods=['POST'])
def sms_reply():
    msg = request.form.get('Body').lower()
    msg_arr = msg.split(' ')
    phone_no = request.form.get('From')
    reply = ''
    match_lst = []
    step = session.get('step', 0)
    req = session.get('req', '')
    loc = session.get('loc', {})
        #Case mandar mensagem introdutoria
    if len(req) == 0 or len(loc)==0:
        # Case usuario pediu serviço
        match_lst = find_requests(msg_arr)
        if len(match_lst) > 0:
            req = match_lst[0]
            reply = "Entendi, você quer " + match_lst[0] + " ! Por gentileza, me informe a rodoviaria e km onde você se encontra"
            step += 1
        elif step > 0 and len(req)==0:
            reply = "Não entendi o que você quer"
    if step == 0:
        reply = "Oi! Eu sou seu chapa do zap. Quero melhorar sua experiência na estrada. O que você procura?"
        step += 1
    elif len(req) > 0 and len(reply) == 0:
        loc = get_location(msg_arr)
        street_name = loc.get('rodoviaria', 0)
        km = loc.get('km', 0)
        if not km or not street_name:
            reply = "Não encontrei essa localizacao"
        else:
            reply = "Aqui está " + str(req) + " na rodoviaria " + str(street_name) + " e no Km " + str(km) + ". Obrigada pela confianca!"
            step = 0
            loc = {}
            req = ''
    # Create reply
    resp = MessagingResponse()
    resp.message(reply)
    session['step'] = step
    session['req'] = req
    session['loc'] = loc
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)