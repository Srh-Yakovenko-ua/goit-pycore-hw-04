from typing import List, Tuple, Optional
import re

pattern = r"-?\d+\.?\d*"


def extract_and_sum_numbers(employes: List[str]) -> float:
    """
    Extracts numbers from a list of strings and returns their sum.

    Args:
        lines (List[str]): A list of strings, each potentially containing numeric values.

    Returns:
        float: The total sum of all numbers extracted from the list.
    """
    # Combine all strings into one large string to facilitate searching
    combined_string = " ".join(employes)
    # Use list comprehension to extract all salaries and convert them to floats
    salaries = [float(num) for num in re.findall(pattern, combined_string)]
    return sum(salaries)


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
