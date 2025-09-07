# Lexical Analyzer with TXT File Input

A C language lexical analyzer that reads code from a text file and generates a symbol table.

## How to Use

1. **Add your C code** to `input_code.txt` file
2. **Run the analyzer**:
   ```bash
   python main.py
   ```
3. **Check results** in `symbol_table_output.txt`

## Features

- Reads C code from `input_code.txt`
- Recognizes C language tokens (keywords, identifiers, operators, etc.)
- Generates symbol table exactly as shown in academic examples
- Saves detailed analysis to `symbol_table_output.txt`

## Token Types Recognized

- **Datatype**: int, float, char, double, void
- **Keywords**: if, else, for, while, printf, etc.
- **Identifiers**: Variable and function names
- **Constants**: Numbers (integers and floats)
- **Operators**: Arithmetic (+, -, *, /), Assignment (=), Relational (>, <, ==)
- **Separators**: ;, :, ,
- **Brackets**: (), {}
- **String/Char Literals**: "text", 'c'

## Files

- `input_code.txt` - Put your C code here
- `main.py` - Run this to start analysis
- `lexical_analyzer.py` - Main analyzer logic
- `symbol_table.py` - Symbol table management
- `symbol_table_output.txt` - Generated analysis results"# Lexical-Analyzer" 
