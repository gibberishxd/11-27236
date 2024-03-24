from square_generator.square_generator import SquareGenerator

square_gen = SquareGenerator()
start = 1
end = 10
squares_list = square_gen.generate_squares(start, end)
print(f"List of squares from {start} to {end}: {squares_list}")
