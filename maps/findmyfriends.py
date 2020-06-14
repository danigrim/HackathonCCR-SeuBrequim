friends_dict = {
    'Padaria E Confeitaria Central de Barueri' : ['user0', 'user1', 'user2'],
    'Tapiocaria La Santa' : ['user0', 'user1', 'user2'],
    'Esquina 76' : ['user3', 'user4',],
    'Caffè Mio' : ['user5', 'user6']
}


def find_friends(selection):
    if selection in friends_dict:
        return len(friends_dict.get(selection))
