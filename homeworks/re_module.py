import re 

class PasswordValidator:
    
    LOWER_CASE_PATTERN = r"[a-z]"
    UPPER_CASE_PATTERN = r"[A-Z]"
    SYMBOLS_PATTERN = r"[!@#$%^&*]"
    NUMBERS_PATTERN = r"[0-9]"

    def __init__(self):
        self.pattern_lower = re.compile(self.LOWER_CASE_PATTERN)
        self.pattern_upper = re.compile(self.UPPER_CASE_PATTERN)
        self.pattern_symbols = re.compile(self.SYMBOLS_PATTERN)
        self.pattern_numbers = re.compile(self.NUMBERS_PATTERN)
        self.password = None

    def get_pass(self):
        self.password = input("Enter your password: ")
        return self.password
    
    
    def check_valid_password(self):
        has_lower = bool(self.pattern_lower.search(self.password))
        has_upper = bool(self.pattern_upper.search(self.password))
        has_symb = bool(self.pattern_symbols.search(self.password))
        has_num = bool(self.pattern_numbers.search(self.password))
        min_length = len(self.password) >= 8
        
        if has_lower and has_upper and has_symb and has_num and min_length:
            return True

    
    def __str__(self):
        if self.check_valid_password():
            return f"Your password '{self.password}' is valid"
        
        return f"Your password '{self.password}' is not valid"
    
validator = PasswordValidator()
validator.get_pass()
print(validator)