friends_dict = {
    'Pizzaria Sportello' : ['user0', 'user1', 'user2'],
    'Armazém da Pizza' : ['user3', 'user4', 'user5'],
    'House of Pizza' : ['user6', 'user7', 'user8'],
    'Papitus Burguer' : ['user 9', 'useer 10']
}


def find_friends(selection):
    if selection in friends_dict:
        return len(friends_dict.get(selection))
