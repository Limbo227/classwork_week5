#Data #1:
colors = {
"black": {
"category": "hue",
"type": "primary",
"code": {
"rgba": [255,255,255,1],
"hex": "#000"
}
},
"white": {
"category": "value",
"type": "primary",
"code": {
"rgba": [0,0,0,1],
"hex": "#FFF"
}
},
"red": {
"category": "hue",
"type": "primary",
"code": {
"rgba": [255,0,0,1],
"hex": "#FF0"
}
},
"blue": {
"category": "hue",
"type": "primary",
"code": {
"rgba": [0,0,255,1],
"hex": "#00F"
}
},
"yellow": {
"category": "hue",
"type": "primary",
"code": {
"rgba": [255,255,0,1],
"hex": "#FF0"
}
},
"green": {
"category": "hue",
"type": "secondary",
"code": {
"rgba": [0,255,0,1],
"hex": "#0F0"
}
}
}

#Data #2:
data = {
"markers": [
{
"name": "Rixos The Palm Dubai",
"location": [25.1212, 55.1535],
},
{
"name": "Shangri-La Hotel",
"location": [25.2084, 55.2719]
},
{
"name": "Grand Hyatt",
"location": [25.2285, 55.3273]
}
]
}
# #1
# class Laptop:
#     def __init__(self, name, cpu, ram, graph_card, hdd, screensize):
#         self.name = name
#         self.cpu = cpu
#         self.ram = ram
#         self.graph_card = graph_card
#         self.hdd = hdd
#         self.screensize = screensize
#
#     def get_dict(self):
#         dict1 = {
#             'Название ноутбука': self.name,
#             'Процессор': self.cpu,
#             'Оперативная память': f'{self.ram} гб',
#             'Видеокарта': self.graph_card,
#             'Размер диска': self.hdd,
#             'Диагональ экрана': self.screensize,
#         }
#         return dict1
#
#     def output(self):
#         some_dict = Laptop.get_dict(self).items()
#         for k, v in some_dict:
#             print(k, ':', v)
#
#
# mac_pro = Laptop('Macbook AIR PRO','Intel 5', 16, 'GTX 2060ti', 1028, 25)
# mac_pro.output()



##2
# class Data:
#
#     def get_tuple(self,dict1):
#         keys1_tuple = tuple(dict1.keys())
#         values1_tuple = tuple(dict1.values())
#         print('Ключи: ', keys1_tuple,'Значении: ', values1_tuple)
#     def get_list(self,dict1):
#         keys1_list = list(dict1.keys())
#         values1_list= list(dict1.values())
#         print('Ключи: ', keys1_list,'Значении: ', values1_list)
#     def get_set(self,dict1):
#         keys1_set = set(dict1.keys())
#         values1_set = set(dict1.values())
#         print('Ключи: ', keys1_set,'Значении: ', values1_set)
#
# my_class = Data()
# my_class.get_list(colors)

##3
class Hotels:

    def __init__(self,data):
        self.data = data

    def get_namesHotels(self):
        names_hotels = []
        for x in self.data['markers']:
            name = x.get('name')
            names_hotels.append(name)
        return names_hotels
    def get_dictionary(self):
        names_tuple = tuple(self.get_namesHotels())
        locations_list = []
        dictionary = dict()
        for x in self.data['markers']:
            location = x.get('location')
            locations_list.append(location)
        locations_tuple = tuple(locations_list)
        dictionary.update({'name':names_tuple, 'location':locations_tuple})
        return dictionary
    def update_dictionary(self):
        for x in range(3):
            self.data['markers'][x].update({'status':1})
        return self.data
output = Hotels(data)
print(output.get_namesHotels())
print(output.get_dictionary())
print(output.update_dictionary())
