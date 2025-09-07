from lexical_analyzer import LexicalAnalyzer

def main():
    """Main function to run lexical analyzer from txt file"""
    
    print("LEXICAL ANALYZER WITH SYMBOL TABLE")
    print("="*60)
    print("This program reads C code from 'input_code.txt' file")
    print("and generates a symbol table in 'symbol_table_output.txt'")
    print("-"*60)
    
    # Create analyzer
    analyzer = LexicalAnalyzer()
    
    # Analyze code from input file
    tokens = analyzer.analyze_from_file('input_code.txt')
    
    if tokens:
        print("\nAnalysis completed successfully!")
        print("Check 'symbol_table_output.txt' for detailed symbol table")
    else:
        print("Analysis failed or no code found!")

if __name__ == "__main__":
    main()