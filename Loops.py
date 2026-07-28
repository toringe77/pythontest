msg = "Hello world!"
print(msg)

i = 1
first_name = 'albert'
last_name = 'einstein'
full_name = f"{first_name} {last_name} {i}"
print(full_name)

bikes = ['trek', 'redline', 'giant']
first_bike = bikes[0]
last_bike = bikes[-1]
print(first_bike)
print(last_bike)

for bike in bikes:
    print(bike)

cars = []
cars.append('volvo')
cars.append('vw')
cars.append('nissan')
print(cars)
for car in cars:
    print(car)

squares = []
for x in range(1, 11):
    squares.append(x**2)
    print(squares)

squares_again = [x**2 for x in range(1,11)]
print(f"Squares again: {squares_again}")

first_squares = squares[:2]
print(first_squares)

copy_of_squares = squares[:]
print(copy_of_squares)

dimensions = (1920, 1080)
resolutions = ('720p', '1080p', '4K')
print(dimensions)
print(resolutions)

print('trek' in bikes)
print('surly' not in bikes)

alien = {'color': 'green', 'points': 5}
print(f"The alien's color is {alien['color']}.")

alien['x_position'] = 0

print(alien)

fav_numbers = {'eric': 7, 'ever': 4, 'erin': 47}
for name, number in fav_numbers.items():
    print(f"{name} loves {number}.")

fav_numbers = {'eric': 7, 'ever': 4, 'erin': 47}
for name in fav_numbers.keys():
    print(f"{name} loves a number.")

print(fav_numbers)
print(fav_numbers.keys())
print(fav_numbers.items())