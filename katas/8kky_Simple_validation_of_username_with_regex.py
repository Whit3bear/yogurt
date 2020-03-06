import re
def validate_usr(username):
    if 4 > len(username) > 16:
        return False
    
    pattern = '[^a-z0-9_]'
    if re.search(pattern, username):
        return False
    else: 
        return True
    
    

print(validate_usr('asddsa'))
# True
# Test.assert_equals(validate_usr('a'), False)
# Test.assert_equals(validate_usr('Hass'), False)
# Test.assert_equals(validate_usr('Hasd_12assssssasasasasasaasasasasas'), False)
# Test.assert_equals(validate_usr(''), False)
# Test.assert_equals(validate_usr('____'), True)
# Test.assert_equals(validate_usr('012'), False)