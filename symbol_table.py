class SymbolTable:
    """Enhanced symbol table for C language tokens"""
    
    def __init__(self):
        self.table = {}
        
    def insert(self, name, token_type, datatype=None, line_no=1):
        """Insert a symbol into the table"""
        if name not in self.table:
            self.table[name] = {
                'token_type': token_type,
                'datatype': datatype,
                'line_no': line_no,
                'scope': 'global'
            }
            return True
        return False
    
    def lookup(self, name):
        """Look up a symbol in the table"""
        return self.table.get(name, None)
    
    def get_all_symbols(self):
        """Get all symbols as list"""
        return list(self.table.items())
    
    def display_formatted(self):
        """Display symbol table in the exact format shown in images"""
        print("\nSYMBOL TABLE (TOKENS)")
        print("="*50)
        print(f"{'Attributes':<15} {'Token/Datatype':<20}")
        print("-"*50)
        
        if not self.table:
            print("No symbols found")
        else:
            for name, info in self.table.items():
                datatype = info.get('datatype', info['token_type'])
                print(f"{name:<15} {datatype:<20}")
        
        print("="*50)