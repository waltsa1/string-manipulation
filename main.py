import re


# This function capitalizes every nth alphanumeric character of the given string.
# Alphanumeric characters are defined as [a-z][A-Z][0-9], excluding the underscore (_).
# @param str_in - The string to capitalize.
# @param n = The multiple of the character to capitalize. E.g., if n=3, capitalize every third letter.
def capitalize_nth_letter(str_in, n):
    # We can't capitalize a character in a position longer than the input string.
    # Raise an exception.
    if n > len(str_in):
        raise Exception("Position to capitalize, {}, "
                        "exceeds the length of the input string, {}.".format(n, len(str_in)))

    # Can't capitalize a character with a negative index!
    # Raise an exception.
    if n < 0:
        raise Exception("Position to capitalize, {}, is a negative number.".format(n))

    # Make the entire string lower case as "Characters other than each nth should be down-cased."
    str_in = str_in.lower()

    # Variable to keep track of which alphanumeric character we're on.
    alphanumeric_count = 0

    # Regex pattern to check for alphanumber characters, sans the underscore.
    # "For the purposes of counting and capitalizing every three characters, consider only alphanumeric
    # characters, ie [a-z][A-Z][0-9]."
    alphanumeric_pattern = "[a-zA-Z0-9]"

    # Variable to build our output string
    str_out = ''

    # Look at the characters in the string.
    for char in str_in:

        # Check for alphanumeric characters
        if re.search(alphanumeric_pattern, char):

            # Increment the alphanumeric_count so we know if we've seen an alphanumeric character
            alphanumeric_count += 1

            # If n is 0, capitalize the first letter and break
            if n == 0:
                str_out = str_in[0].capitalize() + str_in[1:]
                break
            elif alphanumeric_count % n == 0:
                # If our alphanumeric character count is a multiple of n, capitalize the character
                # and append it to the output string
                char = char.capitalize()
                str_out += char
            else:
                # Our alphanumeric_count is not a multiple of n,
                # so append the character as-is the output string.
                str_out += char
        else:
            # The current character of the input string is not alphanumeric,
            # so append teh character as-is to the output string.
            str_out += char

    print(str_out)
    return str_out


# Just in case someone wants to run it on the command line
# Please see test_capitalization.py for unit tests
if __name__ == '__main__':
    capitalize_nth_letter('Aspiration.com', 3)
