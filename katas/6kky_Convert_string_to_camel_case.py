""" Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).
Examples

to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior" """

def to_camel_case(text):        
    arr = text.replace('-', '_').split('_')     
    return ''.join(arr[i].capitalize() if i !=0 else arr[i] for i in range(len(arr)))

print(to_camel_case(''))
# '', "An empty string was provided but not returned"
print(to_camel_case("the_stealth_warrior"))
# "theStealthWarrior", "to_camel_case('the_stealth_warrior') did not return correct value"
print(to_camel_case("The-Stealth-Warrior"))
# "TheStealthWarrior", "to_camel_case('The-Stealth-Warrior') did not return correct value"
print(to_camel_case("A-B-C"))
# "ABC", "to_camel_case('A-B-C') did not return correct value")