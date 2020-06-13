from flask import Flask, request, session
from datetime import datetime, timedelta
from twilio.twiml.messaging_response import MessagingResponse

SECRET_KEY = 'a secret key'
app = Flask(__name__)
app.config.from_object(__name__)


def find_requests(msg):
    dici = {}
    dici['eat'] = ['comer', 'comida', 'fome', 'food', 'jantar', 'almoco', 'almoço', 'lanche', 'lanchar']
    dici['sleep'] = ['sono', 'dormir', 'descansar', 'sleep', 'deitar', 'parar']
    dici['bathroom'] = ['banheiro', 'mijar', 'banho', 'limpar', 'lavar']
    match_lst = []
    for key,value in dici.items():
        for word in value:
            if msg == word:
                match_lst.append(str(word))
    return match_lst


@app.route("/", methods=['POST'])
def sms_reply():
    msg = request.form.get('Body')
    phone_no = request.form.get('From')
    reply =''
    match_lst = []
    step = session.get('step', 0)
    req = session.get('req', '')
    step += 1
        #Case mandar mensagem introdutoria
    if step == 1:
        reply = "Oi! Eu sou seu chapa do zap. Quero melhorar sua experiência na estrada. O que você procura?"
    elif not req:
        # Case usuario pediu serviço
        match_lst = find_requests(msg)
        if len(match_lst) > 0:
            req = match_lst[0]
            reply = "Entendi você quer " +match_lst[0]+ " Onde você está?"
        else:
            reply = "Não entendi o que você quer"
            step -= 1
    elif step >1:
        reply = "localizar" + str(req)
    # Create reply
    resp = MessagingResponse()
    resp.message(reply)
    session['step'] = step
    session['req'] = req
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)