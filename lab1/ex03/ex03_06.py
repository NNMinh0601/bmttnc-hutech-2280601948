def xoa_phan_tu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False
    
my_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_delete = 'b'
result = xoa_phan_tu(my_dict, key_to_delete)
if result:
    print("Phan tu da duoc xoa tu dictionary: ", my_dict)
else:
    print("Khong tim thay phan tu de xoa trong dictionary.")

