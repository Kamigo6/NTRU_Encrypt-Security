
def char_to_binary_list(char):
    # Convert character to binary string
    binary_str = bin(ord(char))[2:]

    # Calculate the number of zero-padding needed
    padding_len = 8 - len(binary_str)

    # Create a list with zero-padding
    binary_list = [0] * padding_len + [int(bit) for bit in binary_str]

    return binary_list

# Example usage:
character = 'H'
result = char_to_binary_list(character)
print(result)