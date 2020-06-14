from flask import Flask, request, session
from datetime import datetime, timedelta
from twilio.twiml.messaging_response import MessagingResponse
import re
from main import flow
from findmyfriends import find_friends
from language import googleMapsPlaces, positives, negatives, common_words, road_words, servicesDict
from message_reply import welcome_text, thanks_for_sharing, thanks_fornot_sharing, map_reply, request_location_message


SECRET_KEY = 'chapa zap key'
app = Flask(__name__)
app.config.from_object(__name__)


def find_requests(msg_arr):
    match_lst = []
    for key,value in servicesDict.items():
        for word in msg_arr:
            if word in value:
                match_lst.append(str(key))
    return match_lst


# Find street name from message
def find_street_name(road_index, msg_arr):
    road_name = ''
    if road_index > 0:
        for i in range(road_index, len(msg_arr)):
            if msg_arr[i].isdigit() or re.match('(KM|km|Km|Kilometro|KILOMETRO)', msg_arr[i]):
                return road_name
            else:
                road_name = road_name + ' ' + msg_arr[i]
    else:
        so_far = ''
        for word in (msg_arr):
            # case BR-xxx
            if re.match('(BR|BR-|Br-|bR-|br|br-)[0-9][0-9][0-9]', word):
                return word
        for i, word in enumerate(msg_arr):
            if word.isdigit() or re.match('(KM|km|Km|Kilometro|KILOMETRO)', msg_arr[i]):
                return so_far
            elif word not in common_words:
                so_far = so_far + word
        return so_far


#final direction to restaurant
def direction_reply(sharing, word, dicas):
    selected = dicas.get(word)[0]
    address = dicas.get(word)[1]
    distance = dicas.get(word)[2]
    friend_count = find_friends(selected)
    if sharing:
        return "Você selecionou o seguinte estabelecimento: " + str(selected) + "O endereco de lá é: " + str(address) + " E está a " + str(distance) + " Tem " + str(friend_count) + \
               " chapas do Seu Brequin lá. Se estiver se sentindo sozinho, tente encontrá-los" + "uto(s)"
    return "Você selecionou o seguinte estabelecimento: " + str(selected) + "O endereco de lá é: " + str(address) + " E está a " + str(distance) + "uto(s)"


# Get location from user message
def get_location(msg_arr):
    location_dict = {}
    for i, word in enumerate(msg_arr):
        if word.isdigit():
            location_dict['km'] = word
    road_index = -1
    for ind, word in enumerate(msg_arr):
        if word in road_words:
            if ind < (len(msg_arr)-1):
                    road_index = ind + 1
    location_dict['rodovia'] = find_street_name(road_index, msg_arr)
    return location_dict


# Location sharing preferences
def share_preference(msg_arr):
    for word in msg_arr:
        if word in negatives:
            return False
        elif word in positives:
            return True
    return False


def re_init_session(session):
    session['step'] = 0
    session['loc'] = {}
    session['req'] = ''
    session['sharing'] = False
    session['first'] = [False, False]
    session['selected'] = ''
    session['dicas'] = {}


# Main rote
@app.route("/", methods=['POST'])
def sms_reply():
    msg = request.form.get('Body').lower()
    msg_arr = msg.split(' ')
    phone_no = request.form.get('From')
    reply = ''
    match_lst = []
    #Conversation data
    step = session.get('step', 0)
    first = session.get('first', [True, True]) #first and second contact messages missing
    req = session.get('req', '')
    loc = session.get('loc', {})
    dicas = session.get('dicas', {})
    selected = session.get('selected', '')
    sharing = session.get('share', False)
    if len(req) > 0 and len(loc) == 0:
        step = 3
    if len(dicas) > 0:
        step = 4
    #First contact message
    if first[0]:
        reply = welcome_text
        first = [False, True]
    #Second contact message
    elif (not first[0]) and first[1]:
        sharing = share_preference(msg_arr)
        if sharing == True:
            reply = thanks_for_sharing
        elif sharing == False:
            reply = thanks_fornot_sharing
        first = [False, False]
    #Returning client
    else:
        if msg_arr[0]=="00":
            re_init_session(session)
            reply ="Sem problemas, vou recomeçar essa sessão"
            resp = MessagingResponse()
            resp.message(reply)
            return str(resp)
        if len(req) == 0:
        #Service requested
            match_lst = find_requests(msg_arr)
            if len(match_lst) > 0:
                req = match_lst[0]
                reply = request_location_message(match_lst[0])
                step += 1
            elif step > 0 and len(req) == 0:
                reply = "Não entendi o que você quer. Tente um pedido"
                req =''
        #Greet returning client
        if step == 0:
            reply = "Oi meu amigo, bom te ver por aqui. O que você procura?"
            step = 1
        elif step == 3:
            #Location provided
            loc = get_location(msg_arr)
            street_name = loc.get('rodovia', 0)
            km = loc.get('km', 0)
            if not km or not street_name:
                reply = "Não encontrei essa localizacao. Tente novamente, ou digite 00 para re iniciar a conversa"
                loc = {}
            else:
                google_places = googleMapsPlaces.get(req)
                origem = "rodovia " + str(street_name) + " km " + str(km)
                places_dict, picture_url = flow(origem, google_places)
                if len(places_dict) == 0:
                    reply = "Infelizmente, não encontrei nada perto de você. Sugiro que dirija mais" \
                            " um pouco, e me chame novamente!"
                else:
                    session['dicas'] = places_dict
                    reply = map_reply(req) + str(places_dict.get("0"))
                    resp = MessagingResponse()
                    msg = resp.message(reply)
                    msg.media(str(picture_url))
                    return str(resp)
        elif step == 4:
            selected = ''
            for word in msg_arr:
                if word.isdigit():
                    selected = dicas.get(word, '')
                    if len(selected) == 0:
                        reply = "Esse número não está no mapa! Digite algum número do mapa, ou 00 para finalizar"
                    else:
                        reply = direction_reply(sharing, word, dicas)
                        # session ended
                        re_init_session(session)
    # Create reply
    resp = MessagingResponse()
    resp.message(reply)
    session['step'] = step
    session['req'] = req
    session['loc'] = loc
    session['first'] = first
    session['sharing'] = sharing
    session['dicas'] = dicas
    session['selected'] = selected
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
