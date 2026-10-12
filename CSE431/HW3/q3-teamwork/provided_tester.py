import os
import re
import subprocess
import sys
import unittest
from pathlib import Path


CURRENT_DIR = Path(__file__).resolve().parent
MAIN_PY = CURRENT_DIR / "main.py"


def find_test_files(directory: Path):
    """
    Finds all test files matching test_*.txt in the directory.
    """
    if not directory.exists():
        return []
    return sorted(
        [f for f in directory.iterdir() if f.is_file() and re.match(r"test_\d+\.txt", f.name, re.IGNORECASE)],
        key=lambda f: f.name,
    )


def parse_test_file(file_path: Path):
    """
    Parses a test file into expected colors and individual robot inputs.
    
    Format:
    Line 1: space-separated expected colors for robot 0 .. N-1
    Then sections separated by '===':
    Each section has 3 lines:
      Line 1: N X
      Line 2: possible colors
      Line 3: other robot colors
    """
    content = file_path.read_text(encoding="utf-8").strip()
    sections = [s.strip() for s in content.split("===") if s.strip()]
    if not sections:
        return [], []

    # First section contains the true assignment on its first line
    first_lines = sections[0].splitlines()
    expected_colors = first_lines[0].split()

    robot_runs = []
    # If the first section had more lines (in case === wasn't before robot 0), handle it,
    # but based on test format: section 0 is just expected colors.
    # Sections 1..N are the robot test inputs.
    for sec in sections[1:]:
        lines = [line.strip() for line in sec.splitlines() if line.strip()]
        if len(lines) >= 3:
            robot_input = "\n".join(lines[:3]) + "\n"
            robot_runs.append(robot_input)

    return expected_colors, robot_runs


class Tester(unittest.TestCase):
    def _run_test_file(self, test_file: Path):
        self.assertTrue(MAIN_PY.is_file(), f"Target script '{MAIN_PY}' not found.")

        expected_colors, robot_runs = parse_test_file(test_file)
        self.assertTrue(
            len(expected_colors) > 0,
            f"Could not parse expected colors from '{test_file.name}'."
        )
        self.assertEqual(
            len(expected_colors),
            len(robot_runs),
            f"Number of expected colors ({len(expected_colors)}) != number of robot runs ({len(robot_runs)}) in '{test_file.name}'."
        )

        results = []
        at_least_one_correct = False

        for robot_id, (expected, robot_input) in enumerate(zip(expected_colors, robot_runs)):
            try:
                proc = subprocess.run(
                    [sys.executable, str(MAIN_PY)],
                    input=robot_input,
                    text=True,
                    capture_output=True,
                    cwd=str(CURRENT_DIR),
                    timeout=5,
                )
            except subprocess.TimeoutExpired:
                self.fail(f"Test case '{test_file.name}' robot {robot_id} timed out after 5 seconds.")

            if proc.returncode != 0:
                self.fail(
                    f"Execution failed with return code {proc.returncode} for '{test_file.name}' robot {robot_id}.\n"
                    f"--- Stderr ---\n{proc.stderr}\n"
                    f"--- Stdout ---\n{proc.stdout}"
                )

            actual = proc.stdout.strip()
            is_correct = (actual == expected)
            if is_correct:
                at_least_one_correct = True
            results.append((robot_id, expected, actual, is_correct))

        summary_lines = [
            f"Robot {rid}: expected='{exp}', got='{act}' -> {'[CORRECT]' if ok else '[WRONG]'}"
            for rid, exp, act, ok in results
        ]
        summary_text = "\n".join(summary_lines)

        self.assertTrue(
            at_least_one_correct,
            msg=(
                f"\nTest case '{test_file.name}' failed! No robot guessed correctly.\n"
                f"--- Results ---\n{summary_text}\n"
            ),
        )

    def run_all(self):
        """Run all test cases sequentially using subtests."""
        test_files = find_test_files(CURRENT_DIR)
        self.assertTrue(len(test_files) > 0, f"No test files found in {CURRENT_DIR}")
        for t_file in test_files:
            with self.subTest(case=t_file.name):
                self._run_test_file(t_file)


# Dynamically generate individual test methods on Tester for IDE test explorer and granular CLI runs
_test_files = find_test_files(CURRENT_DIR)
if _test_files:
    for _test_file in _test_files:
        _safe_name = re.sub(r"[^a-zA-Z0-9_]", "_", _test_file.stem)
        _method_name = f"test_{_safe_name}"

        def _make_test(t_path: Path, name: str):
            def test_method(self):
                self._run_test_file(t_path)
            test_method.__name__ = name
            test_method.__doc__ = f"Test with {t_path.name}"
            return test_method

        setattr(Tester, _method_name, _make_test(_test_file, _method_name))
else:
    def test_no_cases(self):
        self.fail(f"No test files found in {CURRENT_DIR}")
    setattr(Tester, "test_no_cases", test_no_cases)


if __name__ == "__main__":
    unittest.main()