from spider import main

test_cases = [
	{
		"args": [],
		"expected": (False, 1, None, "./data/")
	},
	{
		"args": ["-r"],
		"expected": (True, 1, None, "./data/")
	},
	{
		"args": ["r"],
		"expected": (False, 1, None, "./data/")
	},
	{
		"args": ["-l"],
		"expected": (False, -1, None, "./data/")
	},
	{
		"args": ["-l", "3"],
		"expected": (False, 3, None, "./data/")
	},
	{
		"args": ["-l", "a"],
		"expected": (False, -1, None, "./data/")
	},
]

for i, case in enumerate(test_cases):
	actual = main(case["args"])
	try:
		assert actual == case["expected"], f"Expected {case['expected']}, got {actual}"
		print(f"Test case {i}: OK!")
	except AssertionError as e:
		print(f"Test case {i}: NOK! {e}")