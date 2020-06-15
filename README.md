# CCR Hackathon - Seu Brequim Bot de whatsapp
Hackathon CCR projeto

Nossa solução é um chatbot de whatsapp. Escolhemos o Whatsapp pois, de acordo com pesquisas conduzidas, é a plataforma de preferência dos caminhoneiros. Ao iniciar, o usuário tem duas opções: compartilhar a localização com outros caminhoneiros que usam o chatbot, assim se tornando parte da comunidade Seu Brequim, ou não. Nos dois casos, o usuário pode sempre pedir dicas para o Seu Brequim de lugares para comer, se higienizar, descansar ou pedir ajuda por perto. Com chamadas a API do google Maps, o Seu Brequim obtem as informações e monta um mapa com os lugares em um rádio de 3km, classificados de acordo com o selo de qualidade Seu Brequim. Fazemos chamadas a API do google maps também para obter o endereço exato e distância até o destino. Por fim, o caminhoneiro recebe essas informações via uma imagem e também é notificado se tem outros amigos do Seu Brequim no estabelecimento. 

PARA TESTAR: Esse bot foi desenvolvido usando o trial do Twilio, portanto, só se pode alcançar o número mandando uma mensagem para +1 415 523 8886 com o codigo 'join watch-truth.'. Geramos URLs no ngrok para host nosso bot, e esses URLS duram 8 horas, por isso fora dos horários que o hosting está disponível o bot não pode te responder. Se quiser fazer um teste, por favor mandar uma mensagem para +21 999818357 e irei gerar um novo URL para hospedar o chatbot. 

NOTA: Para esse MVP os dados da qualidade de estabelecimento e o número de usuarios por estabelecimento foram gerados por nós. Claro que, quando o produto estivesse no mercado esses dados seriam alimentados ao sistéma pelos usuários, e nossos selecionados caminhoneiros aprovando lugares. 

