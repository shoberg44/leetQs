import os
import re
import subprocess
import sys
import unittest
from pathlib import Path


CURRENT_DIR = Path(__file__).resolve().parent
MAIN_PY = CURRENT_DIR / "main.py"


def find_test_pairs(directory: Path):
    """
    Finds all test files matching the input schema (e.g. 001-input.txt, 001-input.text)
    and pairs each with its corresponding output file (e.g. 001-output.txt, 001-output.text, 001-output.py).
    """
    pairs = []
    if not directory.exists():
        return pairs

    # Match files containing 'input' (e.g. 001-input.txt, 01-input.text, etc.)
    input_files = sorted(
        [f for f in directory.iterdir() if f.is_file() and re.search(r"input", f.name, re.IGNORECASE)],
        key=lambda f: f.name,
    )

    for in_file in input_files:
        # Generate possible output file names by replacing 'input' with 'output'
        # e.g. 001-input.txt -> 001-output.txt
        output_name = re.sub(r"input", "output", in_file.name, flags=re.IGNORECASE)
        base_output_name = re.sub(r'\.(txt|text|py)$', '', output_name, flags=re.IGNORECASE)
        out_candidates = [
            directory / output_name,
            directory / f"{base_output_name}.txt",
            directory / f"{base_output_name}.text",
            directory / f"{base_output_name}.py",
        ]

        # Use the first existing candidate
        out_file = next((candidate for candidate in out_candidates if candidate.is_file()), None)
        if out_file:
            pairs.append((in_file, out_file))

    return pairs


def normalize_output(text: str) -> str:
    """Normalize line endings and strip whitespace on each line for consistent comparison."""
    return "\n".join(line.rstrip() for line in text.strip().splitlines())


class Tester(unittest.TestCase):
    def _run_single_test(self, input_file: Path, output_file: Path):
        self.assertTrue(MAIN_PY.is_file(), f"Target script '{MAIN_PY}' not found.")

        input_text = input_file.read_text(encoding="utf-8")
        expected_output = output_file.read_text(encoding="utf-8")

        try:
            result = subprocess.run(
                [sys.executable, str(MAIN_PY)],
                input=input_text,
                text=True,
                capture_output=True,
                cwd=str(CURRENT_DIR),
                timeout=5,
            )
        except subprocess.TimeoutExpired:
            self.fail(f"Test case '{input_file.name}' timed out after 5 seconds.")

        if result.returncode != 0:
            self.fail(
                f"Execution failed with return code {result.returncode} for '{input_file.name}'.\n"
                f"--- Error Output (stderr) ---\n{result.stderr}\n"
                f"--- Standard Output (stdout) ---\n{result.stdout}"
            )

        actual_norm = normalize_output(result.stdout)
        expected_norm = normalize_output(expected_output)

        self.assertEqual(
            actual_norm,
            expected_norm,
            msg=(
                f"\nTest case '{input_file.name}' failed!\n"
                f"--- Input ---\n{input_text.rstrip()}\n"
                f"--- Expected Output ---\n{expected_output.rstrip()}\n"
                f"--- Actual Output ---\n{result.stdout.rstrip()}\n"
            ),
        )

    def run_all(self):
        """Run all test cases sequentially using subtests."""
        pairs = find_test_pairs(CURRENT_DIR)
        self.assertTrue(len(pairs) > 0, f"No test input/output pairs found in {CURRENT_DIR}")
        for in_file, out_file in pairs:
            with self.subTest(case=in_file.name):
                self._run_single_test(in_file, out_file)


# Dynamically generate individual test methods on Tester for IDE test explorer and granular CLI runs
_test_pairs = find_test_pairs(CURRENT_DIR)
if _test_pairs:
    for _in_file, _out_file in _test_pairs:
        _safe_name = re.sub(r"[^a-zA-Z0-9_]", "_", _in_file.stem)
        _method_name = f"test_{_safe_name}"

        def _make_test(in_path: Path, out_path: Path, name: str):
            def test_method(self):
                self._run_single_test(in_path, out_path)
            test_method.__name__ = name
            test_method.__doc__ = f"Test with {in_path.name} against {out_path.name}"
            return test_method

        setattr(Tester, _method_name, _make_test(_in_file, _out_file, _method_name))
else:
    def test_no_cases(self):
        self.fail(f"No test input/output pairs found in {CURRENT_DIR}")
    setattr(Tester, "test_no_cases", test_no_cases)


if __name__ == "__main__":
    unittest.main()