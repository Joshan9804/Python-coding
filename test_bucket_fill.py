from bucket_fill import fill
from bucket_fill import show_image
from bucket_fill import stringify_image
from bucket_fill import load_image



def test_pattern_smiley(pattern="data/smiley.txt"):
	image = load_image(pattern)
	print("Before filling:")
	show_image(image)

	image_filled = fill(image=image, seed_point=(1,1))
	print("-" * 25)
	print("After filling:")
	show_image(image_filled)
	
def test_pattern_bar(pattern="data/bar.txt"):
	image = load_image(pattern)
	print("Before filling:")
	show_image(image)

	image_filled = fill(image=image, seed_point=(1,1))
	print("-" * 25)
	print("After filling:")
	show_image(image_filled)
	
def test_pattern_largest_matrix(pattern="data/largest_matrix.txt"):
	image = load_image(pattern)
	print("Before filling:")
	show_image(image)

	image_filled = fill(image=image, seed_point=(1,1))
	print("-" * 25)
	print("After filling:")
	show_image(image_filled)

def test_pattern_simply_try(pattern="data/simple_try.txt"):
	image = load_image(pattern)
	print("Before filling:")
	show_image(image)

	image_filled = fill(image=image, seed_point=(1,1))
	print("-" * 25)
	print("After filling:")
	show_image(image_filled)

def test_pattern_smallest_matrix(pattern="data/smallest_matrix.txt"):
	image = load_image(pattern)
	print("Before filling:")
	show_image(image)

	image_filled = fill(image=image, seed_point=(0,0))
	print("-" * 25)
	print("After filling:")
	show_image(image_filled)

def test_pattern_snake(pattern="data/snake.txt"):
	image = load_image(pattern)
	print("Before filling:")
	show_image(image)

	image_filled = fill(image=image, seed_point=(0,0))
	print("-" * 25)
	print("After filling:")
	show_image(image_filled)

if __name__ == '__main__':
    test_pattern_smiley(pattern="data/smiley.txt")
    test_pattern_bar(pattern="data/bar.txt")
    test_pattern_largest_matrix(pattern="data/largest_matrix.txt") 
    test_pattern_simply_try(pattern="data/simple_try.txt")
    test_pattern_smallest_matrix(pattern="data/smallest_matrix.txt")
    test_pattern_snake(pattern="data/snake.txt")