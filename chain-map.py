from collections import ChainMap

# We can link multiple dictionaries and can be treated as a single unit
# We can use it to store default values and override when required
# We can use it to store configuration with some default values

car_parts = {'hood': 500, 'engine': 5000, 'front_door': 750}
car_options = {'A/C': 1000, 'Turbo': 2500, 'rollbar': 300}
car_accessories = {'cover': 1000, 'hood_ornament': 150, 'seat_cover': 99}
car_pricing = ChainMap(car_accessories, car_options, car_parts)
print(car_pricing['hood'])


