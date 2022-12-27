import json, ast


jdata = {'subscribed_mobile': True, 'country_code': u'RU', 'linked_xbox': True, 'subscribed_xcom': '', 'subscribed_2k': True, 'platforms': [u'xbl', u'steam', u'google', u'twitter', u'twitch'], 'subscribed_coda_intent': '', 'subscribed_msft_aug19': '', 'linked_google': True, 'language_code': u'ru', 'linked_steam': True, 'age_group': 'Adult', 'id': u'821946fb359a42d9b7aeca8acb07b4ae', 'subscribed_bioshock': '', 'first_name': u'\u0410\u043b\u0435\u043a\u0441\u0430\u043d\u0434\u0440', 'subscribed_wwe': '', 'subscribed_gearbox': '', 'subscribed_mafia': True, 'subscribed_daffodil': '', 'age_rating': u'US18', 'is_verified': True, 'email': u'aleksandr.avetyan.2000@gmail.com', 'subscribed_coda': '', 'subscribed_civ': '', 'unsubscribe_list': [u'teen', u'unverified'], 'subscribed_golf': '', 'subscribed_playtest': '', 'linked_fb': False, 'linked_twitter': True, 'subscribed_battleborn': '', 'linked_playstation': False, 'birth_month_day': '', 'linked_nintendo': False, 'linked_twitch': True, 'subscribed_nba': '', 'subscribed_borderlands': '', 'subscribe_list': [u'2k', u'2kmobile', u'mafia'], 'linked_gamecenter': False}

jdata = ast.literal_eval(json.dumps(jdata)) # Removing uni-code chars
print(jdata)