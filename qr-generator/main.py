import sys


# Check for command line arguments
if len(sys.argv) == 2:
    value = sys.argv[1]
    encodeString(value)
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("No arguments provided")

def encodeString(value):
    print(f"Encoding string: {value}")
    # Encode string
    if value.isnumeric():
        encodeNumeric(value)
    elif value.isalnum():
        encodeAlphaNumeric(value)
    else:
        encodeByte(value)
    # Generate QR code
    # Save QR code
    
    





    
def encodeNumeric(value):
    print(f"Encoding numeric: {value}")
    # Encode numeric
    
def encodeAlphaNumeric(value):
    print(f"Encoding alpha numeric: {value}")
    # Encode alpha numeric
    
def encodeByte(value):
    print(f"Encoding binary: {value}")
    # Encode binary