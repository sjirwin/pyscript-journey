def main():
    print('"Hello World!" from local PyScript!!')

try:
    main()
except Exception as x:
    print(f"Error starting client script: {x}")
