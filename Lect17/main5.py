def main(call):
    print("Hello from main")
    call()

def hello():
    print("Hello from hello!")

def goodbye():
    print("Hello from goodbye!")



func_list = [hello, goodbye, lambda : print("Hello from lambda!")]
for f in func_list:
    main(f)