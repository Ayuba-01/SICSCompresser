from collections import Counter


class SICSCompresser:
    def __init__(self):
        # Dictionary to store character-to-hex mappings for compression
        self.char_to_hex = {}
        # Dictionary to store hex-to-character mappings for decompression
        self.hex_to_char = {}

    def map_hex_values(self, txt):
        """
        Generates hex values for characters based on their frequency in the text.

        Args:
            txt (str): The text to be mapped.
        """
        # Count the frequency of each character in the text
        char_frequency = Counter(txt)
        # Sort characters by frequency in descending order
        sorted_chars = [char for char, _ in char_frequency.most_common()]

        hex_value = 0  # Start with hex 0
        for char in sorted_chars:
            # Convert hex_value to hex
            if hex_value <= 0xE:
                # Assign simple hex values from 0 to E
                hex_code = f"{hex_value:X}"
            else:
                # For larger hex values
                more_nibbles = (hex_value - 0xF) // 0xE + 1
                terminal_nibble = (hex_value - 0xF) % 0xE
                f_count = "F" * more_nibbles
                hex_code = f_count + f"{terminal_nibble:X}"

            # Update dictionaries
            self.char_to_hex[char] = hex_code
            self.hex_to_char[hex_code] = char

            hex_value += 1

    def compress(self, txt):
        """
        Compresses the input text using the SICS.

        Args:
            txt (str): The text to be compressed.

        Returns:
            str: The compressed text as a hex string.
        """
        self.map_hex_values(txt)

        # Replace characters in the text with their corresponding hex values
        compressed_txt = ""
        for char in txt:
            compressed_txt += self.char_to_hex[char]

        return compressed_txt

    def decompress(self, compressed_txt):
        """
        Decompresses a hex string back to the original text using the SICS.

        Args:
            compressed_txt (str): The compressed hex string.

        Returns:
            str: The decompressed original text.
        """
        # Initialize decompression variables
        decompressed_txt = ""
        current_hex = ""

        for hex_code in compressed_txt:
            if hex_code == 'F':
                # Accumulate the F's
                current_hex += hex_code
            else:
                # Complete the hex code and map it to the original character
                current_hex += hex_code
                decompressed_txt += self.hex_to_char[current_hex]
                # Reset current_hex for the next character
                current_hex = ""

        return decompressed_txt
