import json
import requests
from enum import Enum


class APIEnum(Enum):
    ABILITY = 1
    EQUIPMENT = 2
    MODEL = 3
    MODEL_TYPE = 4
    UNIT = 5
    UNIT_TYPE = 6
    CONTINGENT = 7
    CONTINGENT_TYPE = 8
    ARMY = 9
    PLAYER = 10
    SCENARIO = 11


class Rester:

    def __init__(self, uri='http://localhost:8000/armytools/'):
        self.BASE_URI = uri
        self.URI_DICT = {
            APIEnum.ABILITY: 'abilities/',
            APIEnum.EQUIPMENT: 'equipment/',
            APIEnum.MODEL: 'models/',
            APIEnum.MODEL_TYPE: 'modeltypes/',
            APIEnum.UNIT: 'units/',
            APIEnum.UNIT_TYPE: 'unittypes/',
            APIEnum.CONTINGENT: 'contingents/',
            APIEnum.CONTINGENT_TYPE: 'contingenttypes/',
            APIEnum.ARMY: 'armies/',
            APIEnum.PLAYER: 'players/',
            APIEnum.SCENARIO: 'scenarios/'
        }

    def list_request(self, types):
        if isinstance(types, list):
            result = {}
            for t in types:
                response = requests.get(self.BASE_URI + self.URI_DICT[t]).json()
                print(response)
                key = list(response.keys())[0]
                result[key] = response[key]
            return result

        return json.loads(requests.get(self.BASE_URI + self.URI_DICT[types]).json())

