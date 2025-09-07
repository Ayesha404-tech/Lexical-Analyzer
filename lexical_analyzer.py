import re

class LexicalAnalyzer:
    """Lexical analyzer that reads from txt file and generates symbol table"""
    
    def __init__(self): 
        # Define C language keywords
        self.keywords = {
            'int', 'float', 'char', 'double', 'void', 'if', 'else', 
            'while', 'for', 'do', 'switch', 'case', 'default', 
            'break', 'continue', 'return', 'printf', 'scanf',
            'main', 'include', 'define'
        }
        
        # Define token patterns for C language
        self.token_patterns = [
            ('COMMENT', r'//.*|/\*.*?\*/'),  # Single line and multi-line comments
            ('PREPROCESSOR', r'#\s*include\s*<[^>]+>'),
            ('AT_SYMBOL', r'@'),  # @ symbol to ignore
            ('DATATYPE', r'\b(int|float|char|double|void)\b'),
            ('KEYWORD', r'\b(if|else|while|for|do|switch|case|default|break|continue|return|printf|scanf|main|include|define)\b'),
            ('ID', r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),
            ('CONSTANT', r'\b\d+(\.\d+)?\b'),
            ('STRING_LITERAL', r'"[^"]*"'),
            ('CHAR_LITERAL', r"'[^']*'"),
            ('INCREMENT_OP', r'\+\+'),
            ('DECREMENT_OP', r'--'),
            ('ASSIGN_OP', r'='),
            ('ARITHMETIC_OP', r'[+\-*/]'),
            ('RELATIONAL_OP', r'(>=|<=|==|!=|>|<)'),
            ('ROUND_BRACKET', r'[()]'),
            ('CURLY_BRACKET', r'[{}]'),
            ('SEPARATOR', r'[;,:]'),
            ('WHITESPACE', r'[ \t]+'),
            ('NEWLINE', r'\n'),
        ]
        
        # Compile regex
        self.token_regex = '|'.join(f'(?P<{name}>{pattern})' 
                                  for name, pattern in self.token_patterns)
        
        self.symbol_table = {}
        
    def read_code_from_file(self, filename):
        """Read code from txt file"""
        try:
            with open(filename, 'r') as file:
                return file.read()
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found!")
            return ""
    
    def tokenize(self, code):
        """Tokenize the input code"""
        tokens = []
        
        for match in re.finditer(self.token_regex, code):
            token_type = match.lastgroup
            token_value = match.group()
            
            if token_type in ['WHITESPACE', 'NEWLINE', 'COMMENT', 'AT_SYMBOL']:
                continue
                
            # Handle special cases
            if token_type == 'ID':
                if token_value in self.keywords:
                    if token_value in ['int', 'float', 'char', 'double', 'void']:
                        token_type = 'DATATYPE'
                    else:
                        token_type = 'KEYWORD'
                else:
                    # Add to symbol table
                    self.add_to_symbol_table(token_value, 'ID')
            
            tokens.append((token_type, token_value))
        
        return tokens
    
    def add_to_symbol_table(self, name, token_type):
        """Add identifier to symbol table"""
        if name not in self.symbol_table:
            self.symbol_table[name] = token_type
    
    def generate_symbol_table_file(self, tokens, original_code):
        """Generate symbol table in txt file exactly as shown in images"""
        
        with open('symbol_table_output.txt', 'w') as f:
            f.write("LEXICAL ANALYSIS REPORT\n")
            f.write("="*50 + "\n\n")
            
            f.write("INPUT CODE:\n")
            f.write("-"*20 + "\n")
            f.write(original_code + "\n\n")
            
            f.write("TOKENS FOUND:\n")
            f.write("="*30 + "\n")
            for token_type, value in tokens:
                f.write(f"{value:<15} -> {token_type}\n")

            f.write(f"\nTotal tokens: {len(tokens)}\n\n")
            
            f.write("\n" + "="*50 + "\n")
            f.write("SYMBOL TABLE (TOKENS)\n")
            f.write("="*50 + "\n")
            f.write(f"{'ATTRIBUTES':<15} {'TOKEN/DATATYPE':<20}\n")
            f.write("-"*50 + "\n")

            
            
            # Add entries exactly as shown in images
            symbol_entries = []
            
            for token_type, value in tokens:
                if token_type == 'DATATYPE':
                    symbol_entries.append((value, 'Datatype'))
                elif token_type == 'ID':
                    symbol_entries.append((value, 'ID'))
                elif token_type == 'ASSIGN_OP':
                    symbol_entries.append((value, 'Assign_OP'))
                elif token_type == 'CONSTANT':
                    symbol_entries.append((value, 'Constant'))
                elif token_type == 'SEPARATOR':
                    symbol_entries.append((value, 'Separator'))
                elif token_type == 'KEYWORD':
                    symbol_entries.append((value, 'Keyword'))
                elif token_type == 'ROUND_BRACKET':
                    symbol_entries.append((value, 'Round Bracket'))
                elif token_type == 'CURLY_BRACKET':
                    symbol_entries.append((value, 'Curly Bracket'))
                elif token_type == 'INCREMENT_OP':
                        symbol_entries.append((value, 'Increment Operator'))
                elif token_type == 'DECREMENT_OP':
                        symbol_entries.append((value, 'Decrement Operator'))
                elif token_type == 'RELATIONAL_OP':
                    symbol_entries.append((value, 'Relational Operator'))
                elif token_type == 'STRING_LITERAL':
                    symbol_entries.append((value, 'String Literal'))
                
            # Remove duplicates while preserving order
            seen = set()
            unique_entries = []
            for entry in symbol_entries:
                if entry not in seen:
                    seen.add(entry)
                    unique_entries.append(entry)
            
            for attribute, datatype in unique_entries:
                f.write(f"{attribute:<15} {datatype:<20}\n")
            
            f.write("="*50 + "\n")
            f.write(f"Total unique symbols: {len(unique_entries)}\n")
            
    
    def analyze_from_file(self, filename):
        """Main analysis function that reads from file"""
        print("LEXICAL ANALYZER - TXT FILE INPUT")
        print("="*50)
        
        # Read code from file
        code = self.read_code_from_file(filename)
        
        if not code:
            return
        
        print(f"Reading code from: {filename}")
        print("Code content:")
        print("-"*20)
        print(code)
        print("\nAnalyzing...")
        
        # Tokenize
        tokens = self.tokenize(code)
        
        # Display tokens
        print("\nTOKENS GENERATED:")
        print("="*30)
        for token_type, value in tokens:
            print(f"{value:<15} -> {token_type}")
        
        # Generate symbol table file
        self.generate_symbol_table_file(tokens, code)
        
        print(f"\nSymbol table saved to: symbol_table_output.txt")
        print(f"Total tokens found: {len(tokens)}")
        print(f"Total unique identifiers: {len(self.symbol_table)}")
        
        return tokens