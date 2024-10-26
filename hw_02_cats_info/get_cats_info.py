path = "hw_02_cats_info/cats_info.txt"


def get_cats_info(path):
    """
    Reads a text file containing cat information and returns a list of dictionaries for each cat.

    Each line in the file should contain a unique identifier, name, and age of a cat, separated by commas.

    Parameters:
        path (str): Path to the text file containing cat data.

    Returns:
        list: A list of dictionaries with keys 'id', 'name', and 'age' representing each cat's data.

    Exceptions:
        - FileNotFoundError: If the specified file is not found.
        - ValueError: If the age value is not an integer.
        - Prints error messages for lines with invalid format or missing fields.

    Example:
        Given a file with the following content:

            60b90c1c13067a15887e1ae1,Tayson,3
            60b90c2413067a15887e1ae2,Vika,1
            60b90c2e13067a15887e1ae3,Barsik,2

        The function will return:

            [
                {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": 3},
                {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": 1},
                {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": 2},
            ]
    """
    cats_info = []
    try:
        with open(path, mode="r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()

                if not line:
                    print(f"Warning: Line {line_number} is empty and was skipped.")
                    continue

                parts = line.split(",")

                if len(parts) != 3:
                    print(
                        f"Warning: Line {line_number} has an invalid format: '{line}'. Expected 3 parts separated by commas."
                    )
                    continue

                cat_id, name, age_str = parts

                try:
                    age = int(age_str)
                    cats_info.append({"id": cat_id, "name": name, "age": age})
                except ValueError:
                    print(print("Info about cat is incorrect"))

    except FileNotFoundError:
        print(
            f"Error: File not found at path '{path}'. Please check the file path and try again."
        )
    except IOError:
        print(
            f"Error: An IO error occurred while trying to read the file at path '{path}'."
        )
    except Exception as e:
        print(f"Unexpected error: {e}")

    return cats_info


print(get_cats_info(path))
