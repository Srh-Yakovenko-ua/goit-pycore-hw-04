from typing import List, Tuple, Optional
import re

pattern = r"-?\d+\.?\d*"


def extract_and_sum_numbers(lines: List[str]) -> float:
    """
    Sum all numbers found in a list of strings.

    Args:
        lines (List[str]): Strings potentially containing numeric values.

    Returns:
        float: Total sum of all numbers found.
    """
    total_sum = 0
    for line in lines:
        matches = re.findall(pattern, line)
        for number in matches:
            total_sum += float(number)

    return total_sum


def total_salary(path: str) -> Optional[Tuple[float, float]]:
    """
    Calculate total and average salary from a file.

    Args:
        path (str): Path to the file with salary data.

    Returns:
        Optional[Tuple[float, float]]: Tuple of total and average salaries, or None on error.

    Raises:
        ValueError: If the data file is empty.
        FileNotFoundError: If the file is not found.
        PermissionError: If reading the file is not permitted.
        Exception: For other file reading errors.
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            employees_list = [line for line in file if line.strip()]

            if not employees_list:
                raise ValueError(
                    "Employee list is empty. Please check the file content."
                )

            total = extract_and_sum_numbers(employees_list)
            average_salary = total / len(employees_list)

            return total, average_salary

    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None, None
    except PermissionError:
        print("No permission to read the file.")
        return None, None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None, None


path = "hw_01_total_salary/text.txt"
total, average = total_salary(path)

print(f"Total salary amount: {total}$, Average salary: {average}$")
