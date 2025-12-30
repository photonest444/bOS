# tag: fourteam-bos-root-encrypter

class WordCipher:
    """
    A class for encrypting and decrypting messages using a keyword-based cipher.
    """
    
    def __init__(self, keyword=None):
        """
        Initialize the cipher with an optional keyword.
        
        Args:
            keyword (str, optional): The encryption key. Defaults to None.
        """
        self.keyword = keyword
        self._validate_keyword()
    
    def _validate_keyword(self):
        """Validate the keyword, setting a default if none provided."""
        if self.keyword is None or self.keyword.strip() == "":
            self.keyword = "SECRET"
        else:
            # Remove spaces and ensure consistent case for key processing
            self.keyword = self.keyword.upper().replace(" ", "")
            
            # Ensure keyword only contains letters
            if not self.keyword.isalpha():
                raise ValueError("Keyword must contain only letters")
    
    def _extend_key(self, text_length):
        """
        Extend the keyword to match the length of the text.
        
        Args:
            text_length (int): Length of the text to encrypt/decrypt.
            
        Returns:
            str: Extended key matching text length.
        """
        if text_length == 0:
            return ""
        
        # Repeat the keyword until it's at least as long as the text
        extended_key = (self.keyword * (text_length // len(self.keyword) + 1))[:text_length]
        return extended_key
    
    def _char_shift(self, char, key_char, encrypt=True):
        """
        Shift a single character based on the key character.
        
        Args:
            char (str): Character to shift.
            key_char (str): Key character for shifting.
            encrypt (bool): True for encryption, False for decryption.
            
        Returns:
            str: Shifted character.
        """
        if not char.isalpha():
            # Non-alphabetic characters remain unchanged
            return char
        
        # Determine shift value based on key character (A=0, B=1, ..., Z=25)
        shift = ord(key_char) - ord('A')
        
        if not encrypt:
            # For decryption, shift in the opposite direction
            shift = -shift
        
        # Check if character is uppercase or lowercase
        is_upper = char.isupper()
        char_code = ord(char.upper())
        
        # Apply shift with wrap-around
        shifted_code = ((char_code - ord('A') + shift) % 26) + ord('A')
        
        # Convert back to appropriate case
        result = chr(shifted_code)
        if not is_upper:
            result = result.lower()
        
        return result
    
    def encrypt(self, plaintext):
        """
        Encrypt a plaintext message using the keyword.
        
        Args:
            plaintext (str): The message to encrypt.
            
        Returns:
            str: The encrypted message.
        """
        if not plaintext:
            return ""
        
        # Extend the key to match the text length
        extended_key = self._extend_key(len(plaintext))
        
        # Encrypt each character
        encrypted_chars = []
        key_index = 0
        
        for i, char in enumerate(plaintext):
            if char.isalpha():
                # Use corresponding key character for alphabetic characters
                encrypted_char = self._char_shift(char, extended_key[key_index], encrypt=True)
                key_index += 1
            else:
                # Non-alphabetic characters remain unchanged
                encrypted_char = char
            
            encrypted_chars.append(encrypted_char)
        
        return ''.join(encrypted_chars)
    
    def decrypt(self, ciphertext):
        """
        Decrypt a ciphertext message using the keyword.
        
        Args:
            ciphertext (str): The message to decrypt.
            
        Returns:
            str: The decrypted message.
        """
        if not ciphertext:
            return ""
        
        # Extend the key to match the text length
        extended_key = self._extend_key(len(ciphertext))
        
        # Decrypt each character
        decrypted_chars = []
        key_index = 0
        
        for i, char in enumerate(ciphertext):
            if char.isalpha():
                # Use corresponding key character for alphabetic characters
                decrypted_char = self._char_shift(char, extended_key[key_index], encrypt=False)
                key_index += 1
            else:
                # Non-alphabetic characters remain unchanged
                decrypted_char = char
            
            decrypted_chars.append(decrypted_char)
        
        return ''.join(decrypted_chars)
    
    def set_keyword(self, keyword):
        """
        Set or change the encryption keyword.
        
        Args:
            keyword (str): The new encryption key.
        """
        self.keyword = keyword
        self._validate_keyword()


def encrypt_message(message, keyword):
    """
    Simple function to encrypt a message with a keyword.
    
    Args:
        message (str): Message to encrypt.
        keyword (str): Encryption key.
        
    Returns:
        str: Encrypted message.
    """
    cipher = WordCipher(keyword)
    return cipher.encrypt(message)


def decrypt_message(ciphertext, keyword):
    """
    Simple function to decrypt a message with a keyword.
    
    Args:
        ciphertext (str): Encrypted message.
        keyword (str): Encryption key.
        
    Returns:
        str: Decrypted message.
    """
    cipher = WordCipher(keyword)
    return cipher.decrypt(ciphertext)


# Example usage and testing
if __name__ == "__main__":
    # Example 1: Basic usage
    print("=== Example 1: Basic Usage ===")
    keyword = "PYTHON"
    message = "Hello, World! This is a secret message."
    
    cipher = WordCipher(keyword)
    encrypted = cipher.encrypt(message)
    decrypted = cipher.decrypt(encrypted)
    
    print(f"Keyword: {keyword}")
    print(f"Original: {message}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    print()
    
    # Example 2: Using helper functions
    print("=== Example 2: Using Helper Functions ===")
    secret_key = "SECRETKEY"
    text = "Meet me at midnight"
    
    encrypted_text = encrypt_message(text, secret_key)
    decrypted_text = decrypt_message(encrypted_text, secret_key)
    
    print(f"Key: {secret_key}")
    print(f"Original: {text}")
    print(f"Encrypted: {encrypted_text}")
    print(f"Decrypted: {decrypted_text}")
    print()
    
    # Example 3: Case sensitivity test
    print("=== Example 3: Case Sensitivity ===")
    cipher2 = WordCipher("CIPHER")
    mixed_case = "Python Programming IS Fun!"
    result = cipher2.encrypt(mixed_case)
    print(f"Original: {mixed_case}")
    print(f"Encrypted: {result}")
    print(f"Decrypted: {cipher2.decrypt(result)}")
    print()
    
    # Example 4: Test with special characters and numbers
    print("=== Example 4: Special Characters and Numbers ===")
    cipher3 = WordCipher("KEY")
    complex_msg = "Message 123: Don't forget the 5:30 meeting! #important"
    encrypted_complex = cipher3.encrypt(complex_msg)
    print(f"Original: {complex_msg}")
    print(f"Encrypted: {encrypted_complex}")
    print(f"Decrypted: {cipher3.decrypt(encrypted_complex)}")