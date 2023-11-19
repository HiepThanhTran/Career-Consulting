from django.templatetags.static import static


def avatar_context(request):
    if request.user.is_authenticated:
        if request.user.avatar:
            avatar_url = static('images/' + str(request.user.avatar))
        else:
            avatar_url = static('images/default-avatar.jpg')
    else:
        avatar_url = static('images/default-avatar.jpg')

    return {'avatar_url': avatar_url}


def location_context(request):
    location_list = [
        'Hà Nội',
        'Hồ Chí Minh',
        'Bình Dương',
        'Bắc Ninh',
        'Đồng Nai',
        'Hưng Yên',
        'Hải Dương',
        'Đà Nẵng',
        'Hải Phòng',
        'An Giang',
        'Bà Rịa-Vũng Tàu',
        'Bắc Giang',
        'Bắc Kạn',
        'Bạc Liêu',
        'Bến Tre',
        'Bình Định',
        'Bình Phước',
        'Bình Thuận',
        'Cà Mau',
        'Cần Thơ',
        'Cao Bằng',
        'Cửu Long',
        'Đắk Lắk',
        'Đắc Nông',
        'Điện Biên',
        'Đồng Tháp',
        'Gia Lai',
        'Hà Giang',
        'Hà Nam',
        'Hà Tĩnh',
        'Hậu Giang',
        'Hoà Bình',
        'Khánh Hoà',
        'Kiên Giang',
        'Kon Tum',
        'Lai Châu',
        'Lâm Đồng',
        'Lạng Sơn',
        'Lào Cai',
        'Long An',
        'Miền Bắc',
        'Miền Nam',
        'Miền Trung',
        'Nam Định',
        'Nghệ An',
        'Ninh Bình',
        'Ninh Thuận',
        'Phú Thọ',
        'Phú Yên',
        'Quảng Bình',
        'Quảng Nam',
        'Quảng Ngãi',
        'Quảng Ninh',
        'Quảng Trị',
        'Sóc Trăng',
        'Sơn La',
        'Tây Ninh',
        'Thái Bình',
        'Thái Nguyên',
        'Thanh Hoá',
        'Thừa Thiên Huế',
        'Tiền Giang',
        'Toàn Quốc',
        'Trà Vinh',
        'Tuyên Quang',
        'Vĩnh Long',
        'Vĩnh Phúc',
        'Yên Bái',
        'Nước Ngoài',
    ]

    return {'location_list': location_list}