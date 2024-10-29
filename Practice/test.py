# try:
#     file= open("file.t","w")
#     try:
#         file.write("witing...")
#     finally:
#         print("cleaning up...")
#         file.close()
# except IOError:
#     print("Error: can\'t find file or read file")

# class CumstomError(RuntimeError):
#     def  __init__(self, arg) -> None:
#         self.args = arg,


# def temp_convert(var):
#     raise CumstomError("This is  a custome error")

# try:
#     temp_convert("av")
# except CumstomError as e:
#     print(e.args[0])


class InvalidAgeError(Exception):
    def __init__(self, age, message="Age must be between 18 and 100") -> None:
        self.age = age
        self.message = message
        super().__init__(self.message)

def set_age(age):
    if age < 18 or age > 100:
        raise InvalidAgeError(age)


# try:
#     set_age(150)
# except InvalidAgeError as e:
#     print(print(f"Invalid age: {e.age}, {e.message}"))

try:
    open("nofile.txt")
except OSError as exc:
    raise RuntimeError from exc