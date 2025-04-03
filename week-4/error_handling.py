# program prompts the user for a file name and handles errors
def main():
    file_name = input("Enter the file name (or nothing to quit): ")

    if file_name:
        try:
            with open(file_name):
                pass
            return f"{file_name} file found\n"
        except Exception:
            return f"{file_name} file not found\n"
    else:
        return


if __name__ == "__main__":
    while True:
        result = main()
        if result is None:
            print("Bye")
            break
        print(result)
