def is_password_valid(password):
    digit=0
    if len(password)<8:
        return False
    elif not any(char.isupper() for char in password):
        return False
    elif not any(char.islower() for char in password):
        return False
    elif len(password)>8:
        for ch in password:
            if ch.isdigit():
                digit+=1
        if digit<=2:
            return False
    else:
        return True
    
     

print(is_password_valid('2abCd345'))

