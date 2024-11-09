import pandas as pd
import numpy as np
import csv

from app_store_scraper import AppStore
import re



#5       https://apps.apple.com/gy/app/deutsche-bank-mobile/id1040475847 #no reviews for tis country
#17      https://apps.apple.com/tt/app/first-citizens-mobile-banking/id553624402 #no reviews for tis country
#  46   'https://apps.apple.com/uy/app/my-heritage/id1441537962',  #No reviews for no country
   


# get and write data to csv file(Apple app store)
bobbank = AppStore(country='uy', app_name='my-heritage', app_id = '1441537962')

bobbank.review(how_many=20000)

commdf = pd.DataFrame(np.array(bobbank.reviews),columns=['review'])
commdf2 = commdf.join(pd.DataFrame(commdf.pop('review').tolist()))

commdf2['date'] = pd.to_datetime(commdf2['date']).dt.strftime('%d/%m/%Y')

commdf2 = commdf2.rename(columns={'date': 'Date of Review', 'review': 'Review Text', 'rating': 'Stars / Rating', 'isEdited': 'isEdited', 'userName':'Reviewer', 'title':'Title'})[['Title', 'Date of Review', 'Stars / Rating', 'Reviewer', 'Review Text']]

commdf2.to_csv('App 46- Apple Reviews.csv', index=False, encoding='utf-8')



# def extract_link_parts(link):
#     # Define the regular expression pattern with Unicode support for app names
#     pattern = r"https://apps\.apple\.com/(?P<country>[a-z]{2})/app/(?P<app_name>[\w\-%]+[^/])/id(?P<id_number>\d+)"
    
#     # Use re.search to match the pattern in the link
#     match = re.search(pattern, link)
    
#     if match:
#         # Return the parts in the correct order for the AppStore constructor
#         return [match.group('country'), match.group('app_name'), match.group('id_number')]
#     else:
#         return None



# def process_links(list_of_links):
#     app_store_objects = []  # Initialize an empty list to store AppStore objects
#     for link in list_of_links:
#         output = extract_link_parts(link)  # Call the function for each link
#         if output:
#             # Unpack the list and create an AppStore object
#             app_store = AppStore(country=output[0], app_name=output[1], app_id=output[2])
#             app_store_objects.append(app_store)  # Append the AppStore object to the list
#         else:
#             app_store_objects.append(None)  # Append None if the link format is incorrect
#     return app_store_objects

# app_urls = [
#     # 'https://apps.apple.com/gy/app/citizens-bank-mobile-banking/id388082488',
#     'https://apps.apple.com/gy/app/deutsche-bank-mobile/id1040475847',
#     'https://apps.apple.com/gy/app/republicmobile-guyana/id1486014233',
#     'https://apps.apple.com/jm/app/scotiabank/id341151570',
#     'https://apps.apple.com/jm/app/onejn/id1577602772',
#     'https://apps.apple.com/jm/app/ncb-mobile/id1435405040',
#     'https://apps.apple.com/my/app/cimb-biz/id6461311433',
#     'https://apps.apple.com/my/app/mae-by-maybank2u/id1481028763',
#     'https://apps.apple.com/my/app/mypb-by-public-bank/id6446102283',
#     'https://apps.apple.com/sg/app/dbs-digibank/id1068403826',
#     'https://apps.apple.com/sg/app/ocbc-singapore/id292506828',
#     'https://apps.apple.com/sg/app/uob-tmrw/id1049286296',
#     'https://apps.apple.com/tt/app/cibc-caribbean-mobile/id1094351996',
#     'https://apps.apple.com/tt/app/first-citizens-mobile-banking/id553624402',
#     'https://apps.apple.com/tt/app/republicmobile-tt/id1572835373',
#     'https://apps.apple.com/pe/app/banco-de-la-nación-banca-móvil/id1316766665', #argentina can't connect
#     'https://apps.apple.com/ar/app/galicia-el-banco-en-tu-celu/id774860115',
#     'https://apps.apple.com/ar/app/bip-m%C3%B3vil/id910702923',
#     'https://apps.apple.com/ar/app/santander-argentina/id626971464',
#     'https://apps.apple.com/cl/app/mi-banco-chile/id1516872542',
#     'https://apps.apple.com/cl/app/bancoestado/id1143576734',
#     'https://apps.apple.com/cl/app/santander-chile/id604982236',
#     'https://apps.apple.com/co/app/banco-de-bogot%C3%A1/id741196012',
#     'https://apps.apple.com/co/app/bancolombia-personas/id565101003',
#     'https://apps.apple.com/co/app/davivienda/id1578380253',
#     'https://apps.apple.com/cr/app/banca-m%C3%B3vil-bac/id465508552',
#     'https://apps.apple.com/cr/app/bcr-comercial/id1489731710',
#     'https://apps.apple.com/cr/app/bn-m%C3%B3vil/id1083667456',
#     # 'https://apps.apple.com/do/app/tarjeta-de-claves-digital-bhd/id1511745609',

#     # 'https://apps.apple.com/do/app/banco-popular-dominicano/id583475424',
#     # 'https://apps.apple.com/do/app/banreservas/id1170610154',
#     # 'https://apps.apple.com/mx/app/santander-superm%C3%B3vil/id498944221',
#     # 'https://apps.apple.com/mx/app/banorte-m%C3%B3vil/id374817863',
#     # 'https://apps.apple.com/mx/app/bbva-m%C3%A9xico/id374824226',
#     # 'https://apps.apple.com/pa/app/banco-general-s-a/id571046666',
#     # 'https://apps.apple.com/pa/app/banistmo-app-personas/id1482789541',
#     # 'https://apps.apple.com/pa/app/banca-m%C3%B3vil-de-bnp/id934819140',
#     # 'https://apps.apple.com/pe/app/banca-m%C3%B3vil-bcp/id777961079',
#     # 'https://apps.apple.com/pe/app/bbva-per%C3%BA/id569453542',
#     # 'https://apps.apple.com/pe/app/interbank-app/id378649517',
#     # 'https://apps.apple.com/uy/app/app-ebrou/id841015703',
#     # 'https://apps.apple.com/uy/app/santander-empresas-uruguay/id6444013090',
#     # 'https://apps.apple.com/uy/app/my-heritage/id1441537962',
#     # 'https://apps.apple.com/bh/app/aub-bahrain/id771724261',
#     # 'https://apps.apple.com/bh/app/albaraka-mobil/id1428860724',
#     # 'https://apps.apple.com/bh/app/arabi-mobile/id1387380275',
#     # 'https://apps.apple.com/kw/app/burgan-bank/id471816688',
#     # 'https://apps.apple.com/kw/app/gulf-bank-mobile-banking/id1577206679',
#     # 'https://apps.apple.com/kw/app/kfh-online/id409153764',
#     # 'https://apps.apple.com/kw/app/nbk-mobile-banking/id451107234',
#     # 'https://apps.apple.com/om/app/bankdhofar/id1638910529',
#     # 'https://apps.apple.com/om/app/bank-muscat-mobile-banking/id763499293',
#     # 'https://apps.apple.com/om/app/nbo/id939103611',
#     # 'https://apps.apple.com/qa/app/cbq-mobile/id388934616',
#     # 'https://apps.apple.com/qa/app/al-rayan-mobile/id492875448',
#     # 'https://apps.apple.com/qa/app/qib-mobile/id587428616',
#     # 'https://apps.apple.com/qa/app/qnb-mobile/id426172922',
#     # 'https://apps.apple.com/ae/app/adcb/id547172388',
#     # 'https://apps.apple.com/ae/app/dib-mobile/id739758144',
#     # 'https://apps.apple.com/ae/app/enbd-x/id1497518128',
#     # 'https://apps.apple.com/ae/app/fab-mobile-banking/id1383237548'
# ]

# results = process_links(app_urls)
# for index, apps in enumerate(results):
#     bobbank = apps
#     bobbank.review(how_many=100000)

#     commdf = pd.DataFrame(np.array(bobbank.reviews),columns=['review'])
#     commdf2 = commdf.join(pd.DataFrame(commdf.pop('review').tolist()))

#     commdf2['date'] = pd.to_datetime(commdf2['date']).dt.strftime('%d/%m/%Y')

#     commdf2 = commdf2.rename(columns={'date': 'Date of Review', 'review': 'Review Text', 'rating': 'Stars / Rating', 'isEdited': 'isEdited', 'userName':'Reviewer', 'title':'Title'})[['Title', 'Date of Review', 'Stars / Rating', 'Reviewer', 'Review Text']]

#     commdf2.to_csv(f'App {index+1}- Apple Reviews.csv', index=False, encoding='utf-8')










