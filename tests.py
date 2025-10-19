from spider import parse_args

DEFAULT_DIR = "./data/"
TEST_DIR_PATH = "test/path"
test_cases = [
	{
		"args": [],
		"expected": (False, 1, None, DEFAULT_DIR)
	},
	{
		"args": ["-r"],
		"expected": (True, 5, None, DEFAULT_DIR)
	},
	{
		"args": ["r"],
		"expected": (False, 1, None, DEFAULT_DIR)
	},
	{
		"args": ["-r", "-l"],
		"expected": (True, -1, None, DEFAULT_DIR)
	},
	{
		"args": ["-r", "-l", "3"],
		"expected": (True, 3, None, DEFAULT_DIR)
	},
	{
		"args": ["-r", "-l", "a"],
		"expected": (True, -1, None, DEFAULT_DIR)
	},
	{
		"args": ["-l"],
		"expected": (False, 1, None, DEFAULT_DIR)
	},
	{
		"args": ["-l", "3"],
		"expected": (False, 1, None, DEFAULT_DIR)
	},
	{
		"args": ["-l", "a"],
		"expected": (False, 1, None, DEFAULT_DIR)
	},
	{
		"args": ["-p"],
		"expected": (False, 1, None, "")
	},
	{
		"args": ["-p", "./test/path/"],
		"expected": (False, 1, None, "./test/path/")
	},
	{
		"args": ["-p", ".//////////sdf/sd/f/sdf"],
		"expected": (False, 1, None, "")
	},
	{
		"args": ["-p", "."],
		"expected": (False, 1, None, ".")
	},
	{
		"args": ["-r", "-l"],
		"expected": (True, -1, None, DEFAULT_DIR)
	},
	{
		"args": ["-r", "-l", 6],
		"expected": (True, 6, None, DEFAULT_DIR)
	},
	{
		"args": ["-l", 6, "-r"],
		"expected": (True, 6, None, DEFAULT_DIR)
	},
	{
		"args": ["-r", 6, "-l"],
		"expected": (True, -1, None, DEFAULT_DIR)
	},
	{
		"args": ["-r", 6, "-l"],
		"expected": (True, -1, None, DEFAULT_DIR)
	},
	{
		"args": ["-r", 6, "-l", 7],
		"expected": (True, 7, None, DEFAULT_DIR)
	},
	{
		"args": ["-r", "-l", 1],
		"expected": (True, 1, None, DEFAULT_DIR)
	},
	{
		"args": ["-l", 1, "-r"],
		"expected": (True, 1, None, DEFAULT_DIR)
	},
	{
		"args": ["-r", "-p"],
		"expected": (True, 5, None, "")
	},
	{
		"args": ["-r", "-p", TEST_DIR_PATH],
		"expected": (True, 5, None, TEST_DIR_PATH)
	},
	{
		"args": ["-p", TEST_DIR_PATH, "-r"],
		"expected": (True, 5, None, TEST_DIR_PATH)
	},
	{
		"args": ["-p", TEST_DIR_PATH, "-l"],
		"expected": (False, 1, None, TEST_DIR_PATH)
	},
	{
		"args": ["-p", TEST_DIR_PATH, "-l", 10],
		"expected": (False, 1, None, TEST_DIR_PATH)
	},
	{
		"args": ["-r", "-p", TEST_DIR_PATH, "-l", 10],
		"expected": (True, 10, None, TEST_DIR_PATH)
	},
	{
		"args": ["-r", "-l", "-3"],
		"expected": (True, -1, None, DEFAULT_DIR)
	},
]

for i, case in enumerate(test_cases):
	actual = parse_args(case["args"])
	try:
		assert actual == case["expected"], f"Expected {case['expected']}, got {actual}"
		print(f"Test case {i}: OK!")
	except AssertionError as e:
		print(f"Test case {i}: NOK! {e}")