def check_key(d, key):
    return key in d

def get_value(d, key):
    return d.get(key, "Kalit topilmadi")

info = {'name': 'Ali', 'age': 25, 'city': 'Toshkent'}
print(check_key(info, 'age'))      # True
print(get_value(info, 'age'))      # 25
print(get_value(info, 'phone'))    # Kalit topilmadi
