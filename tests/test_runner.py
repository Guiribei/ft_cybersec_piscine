from src.spider import parse_args, DEFAULT_DIR
from tests import negative_tests, positive_tests

from pathlib import Path


# Text Formatting
BOLD = "\033[1m"
RED = "\033[31m"
GREEN_BOLD = "\033[1;32m"
YELLOW_BOLD = "\033[1;33m"
RESET = "\033[0m"
LINE_SIZE = 80


def run_positive_tests(test_cases):
    failed_tests_count = 0
    for i, case in enumerate(test_cases, 1):
        try:
            actual = parse_args(case["args"])
            assert (
                actual == case["expected_result"]
            ), f"Expected {case['expected_result']}, got {actual}"
            print(f"Test {i} - {case['name']}: {GREEN_BOLD}OK!{RESET}")
        except AssertionError as e:
            print(
                f"Test {i} - {case['name']}: {BOLD}{RED}NOK!{RESET} {type(e).__name__}: {e}"
            )
            failed_tests_count += 1
        except Exception as e:
            print(
                f"Test {i} - {case['name']}: {BOLD}{RED}NOK!{RESET} Unexpected exception: {e}"
            )
            failed_tests_count += 1

    return failed_tests_count


def run_negative_tests(test_cases):
    failed_tests_count = 0
    for i, test in enumerate(test_cases, 1):
        try:
            parse_args(test["args"])
            print(f"Test {i} {test['name']}: {BOLD}{RED}NOK!{RESET} Expected exception")
            failed_tests_count += 1
        except test["expected_exception"]:
            print(f"Test {i} {test['name']}: {GREEN_BOLD}OK!{RESET}")
        except Exception as e:
            print(
                f"Test {i} {test['name']}: {BOLD}{RED}NOK!{RESET} Unexpected exception: {type(e).__name__} (`{e}`); Expected: {test['expected_exception'].__name__}"
            )
            failed_tests_count += 1
    return failed_tests_count


def print_header_oneliner(string):
    print("\n" + "-" * LINE_SIZE)
    print(f"{BOLD}{string:=^{LINE_SIZE}}{RESET}")
    print("-" * LINE_SIZE)


def print_test_report(failed_tests_count):
    # Header
    print_header_oneliner(" TEST REPORT ")

    # Body
    total_test_cases = len(positive_tests) + len(negative_tests)
    print(f"{BOLD}TOTAL TEST CASES: {total_test_cases}{RESET}")
    print(f"{BOLD}FAILED TEST CASES: {RED}{failed_tests_count}{RESET}")

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
    print("-" * LINE_SIZE)


# Run tests
print(f"{BOLD}RUNNING TEST SUITE...{RESET}")

failed_tests_count = 0
print_header_oneliner(" RUNNING POSITIVE TESTS ")
failed_tests_count += run_positive_tests(positive_tests)
print_header_oneliner(" RUNNING NEGATIVE TESTS ")
failed_tests_count += run_negative_tests(negative_tests)

print_test_report(failed_tests_count)
