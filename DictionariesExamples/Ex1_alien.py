## Using  dictionaries
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
assert type(alien_0.get("x_position")) is int
assert type(alien_0.get("y_position")) is int
assert type(alien_0.get("speed") is str)

print(f"Original position: ({alien_0['x_position']}, {alien_0['y_position']})")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
elif alien_0['speed'] == 'fast':
    x_increment = 3
else:
    print(f"Invalid speed group: {alien_0['speed']}")
    exit()

# The new position is the old position plus the increment.
alien_0['x_position'] += x_increment
print(f"New position: ({alien_0['x_position']}, {alien_0['y_position']})")
