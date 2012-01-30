from collective.geo.geographer.geocoder import GeoCoderUtility
from geopy.geocoders.google import GQueryError


test_params = [{'address': "Torino Italy",
                'output': [(u'Turin, Italy',
                                (45.070562099999997, 7.6866186000000001))]},
               {'address': "Serravalle Italy",
                 'output': [(u'Serravalle di Chienti Macerata, Italy',
                                    (43.075758700000002, 12.957291700000001)),
                    (u'46030 Serravalle a Po Mantua, Italy',
                                    (45.071769699999997, 11.0986653)),
                    (u'Serravalle, 50019 Sesto Fiorentino Florence, Italy',
                                    (43.847528799999999, 11.2683242)),
                    (u'Serravalle, 12026 Piasco Cuneo, Italy',
                                    (44.5675697, 7.4256900000000003)),
                    (u'Serravalle, 06046 Norcia Perugia, Italy',
                                    (42.785488399999998, 13.022334499999999)),
                    (u'Serravalle, 54023 Filattiera Massa-Carrara, Italy',
                                    (44.367425699999998, 9.9383029000000001)),
                    (u'Serravalle, Berra Ferrara, Italy',
                                    (44.967833300000002, 12.044703699999999)),
                    (u'Serravalle, Asti, Italy',
                                    (44.947478799999999, 8.1465417999999996)),
                    (u'Serravalle, Bibbiena Arezzo, Italy',
                                    (43.7736485, 11.8429064)),
                    (u'Serravalle, 38061 Ala Trento, Italy',
                                    (45.811786499999997, 11.0141562))]}]


class DummyGeoCoder(GeoCoderUtility):

    def retrieve(self, address=None, google_api=None):  # pylint: disable=W0613
        for item in test_params:
            if address == item['address']:
                return item['output']
        raise GQueryError
