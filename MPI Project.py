def extract_even_numbers(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            numbers = file.readline().split()
            even_numbers = [num for num in numbers if int(num) % 2 == 0]

        with open(output_file, 'w') as file:
            file.writelines(" ".join(even_numbers))
    except Exception as e:
        print(f"An error occurred: {e}")
extract_even_numbers('arr.txt', 'output_file.txt')