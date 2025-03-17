import InsectClass as i

housefly = i.Insect('housefly',2,4)
mosquito = i.Insect('mosquito',2,6)

housefly.calc_flight()
mosquito.calc_flight()


print(f"The {mosquito.get_name()} can fly up to {mosquito.get_flight()} miles.")
print(f"The {housefly.get_name()} can fly up to {housefly.get_flight()} miles.")