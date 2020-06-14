def validate(value):
    if value < 0 or value > 100:
        print("Invalid value!")
    else:
        print("Valid value!")
        
while True:
    value = int(input("Write the value (0-100): "))
    validate(value)
