from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


def find_requests(msg):
    dici = {}
    dici['eat'] = ['comer', 'comida', 'fome', 'food', 'jantar', 'almoco', 'almoço']
    dici['sleep'] = ['sono', 'dormir', 'descansar', 'sleep', 'deitar', 'parar']
    dici['bathroom'] = ['banheiro', 'mijar', 'banho', 'limpar', 'lavar']
    match_lst = []
    for key,value in dici.items():
        for word in value:
            if msg == word:
                match_lst.append(str(key))
    return match_lst


@app.route("/", methods=['POST'])
def sms_reply():
    msg = request.form.get('Body')
    phone_no = request.form.get('From')
    reply = ''
    match_lst = []
    if len(msg)>3:
        match_lst = find_requests(msg)
    if len(match_lst) > 0:
        reply = str(match_lst)
    else:
        reply = 'não'
    # Create reply
    resp = MessagingResponse()
    resp.message(reply)
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)