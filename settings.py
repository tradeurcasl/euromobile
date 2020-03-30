# settings.py
import faker

link = 'https://www.euromobile.ru/produkciya/5g-moduli/mv31-w/'
"""Это линк для тестов на странице продуктов"""

linkprice = 'https://www.euromobile.ru/produkciya/5g-moduli/'
'''Можно использовать любой другой раздел каталога, где есть кнопка "узнать цену"
'''
linkservice = 'https://euromobile.ru/service/kompleksnoe-obsluzhivanie-bortovogo-oborudovaniya-passazhirskogo-transporta/'

linkcontact = 'https://www.euromobile.ru/kontakty/evromobajl-rossiya/'

linksolution = 'https://www.euromobile.ru/solutions/bezopasnost/avtomatizirovannaya-sistema-khraneniya-i-uchyeta-sredstv-videokontrolya/'

linkorder = 'https://www.euromobile.ru/produkciya/lte-routery/teltonika-rut-240/'
'''Пока не будет переделан код сайта и, соответственно, локаторы, менять ссылку можно только со сменой икспаса или 
ксс селектора в локаторах, т.к. из-за их отвратительности приходится писать костыльный икспас'''

'''Генерируем рандомные регистрационные данные для вопросов'''
f = faker.Faker()
email = f.email()
name = f.name()
phone = '81234567890'
message = 'напиши тут любое сообщение'
item = 'item name'
quantity = '2'
object = 'object'
company = 'its'
key = '22'