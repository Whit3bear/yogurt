""" Implement a function that receives a string, and lets you extend it with repeated calls. When no argument is passed you should return a string consisting of space-separated words you've received earlier.

Note: there will always be at least 1 string; all inputs will be non-empty.

For example:

create_message("Hello")("World!")("how")("are")("you?")() == "Hello World! how are you?"

 """
class create_message(str):
    def __call__(self, s = ''):
        return create_message(f'{self} {s}'.strip())

print(create_message("Hello")("World!")("how")("are")("you?")())
#"Hello World! how are you?")