from spider import parse_args


# Text Formatting
BOLD = "\033[1m"
RED = "\033[31m"
GREEN_BOLD = "\033[1;32m"
YELLOW_BOLD = "\033[1;33m"
RESET = "\033[0m"

# TEST SUITE
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

print(f"{BOLD}RUNNING TEST SUITE...{RESET}")

total_test_cases = len(test_cases)
failed_tests_count = 0
for i, case in enumerate(test_cases):
	actual = parse_args(case["args"])
	try:
		assert actual == case["expected"], f"Expected {case['expected']}, got {actual}"
		print(f"Test case {i}: {GREEN_BOLD}OK!{RESET}")
	except AssertionError as e:
		print(f"Test case {i}: {BOLD}{RED}NOK!{RESET} {e}")
		failed_tests_count += 1


# Header
print("\n" + "-" * 66)
print(f"{BOLD}{' TEST REPORT ':=^66}{RESET}")
print("-" * 66)


# Body
print(f"{GREEN_BOLD}TOTAL TEST CASES: {total_test_cases}{RESET}")
print(f"{BOLD}{RED}FAILED TEST CASES: {failed_tests_count}{RESET}")

# Compute passing rate safely
if total_test_cases > 0:
    passing_rate = (total_test_cases - failed_tests_count) / total_test_cases * 100
else:
    passing_rate = 0.0

# Choose color based on result
if passing_rate == 100:
    rate_color = GREEN_BOLD
elif passing_rate >= 80:
    rate_color = YELLOW_BOLD
else:
    rate_color = f"{BOLD}{RED}"

print()
print(f"{rate_color}Passing Rate: {passing_rate:.2f}%{RESET}")
print("-" * 66)
