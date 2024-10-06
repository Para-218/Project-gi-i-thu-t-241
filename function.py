import unicodedata

def remove_accents(input_str):
    # Chuẩn hóa chuỗi thành dạng NFD (tách dấu ra khỏi ký tự gốc)
    nfkd_form = unicodedata.normalize('NFD', input_str)
    
    # Loại bỏ các ký tự thuộc nhóm "Mn" (Mark, Nonspacing), tức là dấu
    no_accent_str = ''.join([char for char in nfkd_form if unicodedata.category(char) != 'Mn'])
    
    # Thay thế các ký tự Đ và đ
    no_accent_str = no_accent_str.replace('Đ', 'D').replace('đ', 'd')
    
    return no_accent_str

def read_file(filename):
    # Mở file txt và đọc nội dung
    with open(filename, 'r', encoding='utf-8') as file:
        # Đọc từng dòng và lưu vào một danh sách
        list_item = file.readlines()

    # Xóa bỏ ký tự xuống dòng (nếu có)
    list_item = [item.strip() for item in list_item]
    return list_item

if __name__ == '__main__':
    print(remove_accents("Việt Nam Đất Nước Côn Người"))
    print(remove_accents("Welcome to Vietnam !"))
    
