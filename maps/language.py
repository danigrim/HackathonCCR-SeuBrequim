# Defines words to predict request

googleMapsPlaces = {
    #'eat': ['meal_delivery', 'meal_takeaway', 'restaurant', 'bakery', 'cafe', 'supermarket'],
    'eat': ['restaurants'],
    'sleep': ['gas_station', 'bus_station', 'parking', 'transit_station', 'train_station'],
    'bathroom': ['gas_station', 'restaurant'],
    'help': ['fire_station', 'police' ]
}


positives = {'sim', 'quero', 'positivo', 's', 'yes', 'siim', 'pode'}
negatives = {'não', 'nao', 'nada', 'errado', 'talvez', 'naao', 'naoo', 'N'}
common_words = {'dentro', 'perto', 'estou', 'longe', 'aqui', 'fora', 'mim', 'voce', 'sabe'}
road_words = {'rodoviária', 'rodoviaria', 'rodovia', 'rua', 'estrada', 'avenida', 'rodov', 'estr'}

servicesDict = {
'eat' : {'comer', 'comida', 'alimentação', 'restaurantes', 'alimentacao', 'fome', 'food', 'jantar', 'almoco', 'almoço', 'almoçar', 'lanche', 'lanchar', 'lanchinho', 'comidinha', 'rango', 'alimentacao', 'come'},
'sleep': {'sono', 'paradas', 'dormir', 'parada', 'descansar', 'sleep', 'deitar', 'parar', 'dormidinha', 'soneca', 'cama'},
'bathroom' : {'banheiros', 'banheiro', 'mijar', 'banho', 'limpar', 'lavar'},
'help' : {'ajuda', 'sos', 'suporte', 'socorro', 'acidente', 'perigo', 'seguranca', 'atendimento'}
}
