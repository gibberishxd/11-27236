from square_generator.square_generator import SquareGenerator


class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End of the range cannot be less than the start.")
        return [x ** 3 for x in range(start, end + 1)]


cubic_gen = CubicGenerator()
start = 1
end = 10
cubes_list = cubic_gen.generate_squares(start, end)  # Note: We're calling generate_squares, but it generates cubes.
print(f"List of cubes from {start} to {end}: {cubes_list}")
