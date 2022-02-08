# # #1
# class Factory:
#     def engine(self):
#         return 'Двигатель создан'
#     def bridge(self):
#         return 'Ходовая часть создана'
#
# #2
#
# class Toyota(Factory):
#     def wheels(self):
#         return "Колёса готовы"
#     def window(self):
#         return "Стёкла готовы"
#
# list_1 = []
# result = Toyota()
# list_1.append(result.engine())
# list_1.append(result.bridge())
# list_1.append(result.wheels())
# list_1.append(result.window())
# print(list_1)

##3
# class Zoo:
#     pass
#
# z = Zoo()
# z.animal1 = 'tiger'
# z.animal2 = 'begemot'
# z.animal3 = 'jiraf'
# z.animal1 = 'lion'
# z.animal4 = [z.animal2, z.animal3]
# z.animal3 = 'snake'
