function sendDataToLogin(url, email, password) {
    const urlParams = new URLSearchParams(window.location.search);

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest', //Necessary to work with request.is_ajax()
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify({
            email: email.toString(),
            password: password.toString(),
            params: urlParams.has('next') ? urlParams.get('next') : '/',
        })
    }).then(response => response.json())
        .then(data => {
            if (data.redirect_to) {
                const baseUrl = window.location.origin
                window.location.href = new URL(data.redirect_to, baseUrl).href
            } else {
                sendVerificationEmail(email)
                toast({
                    title: 'Đăng nhập',
                    message: data.message,
                    type: 'error',
                })
            }
        })
        .catch(error => {
            toast({
                title: 'Đăng nhập',
                message: 'Có lỗi xảy ra trong quá trình đăng nhập!',
                type: 'error',
            })
            console.log(error)
        });
}

function sendDataToSignup(fullName, email, password) {
    fetch('/account/signup/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest', //Necessary to work with request.is_ajax()
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify({
            fullName: fullName.toString(),
            email: email.toString(),
            password: password.toString(),
        })
    }).then(response => response.json())
        .then(data => {
            sendVerificationEmail(email)
            toast({
                title: 'Đăng ký thành công',
                message: data.message,
                type: 'success',
            })
        })
        .catch(error => {
            toast({
                title: 'Đăng ký tài khoản',
                message: 'Có lỗi xảy ra khi gửi email!',
                type: 'error',
            })
            console.log(error)
        });
}

function sendDataToResetPassword(email) {
    fetch('/account/reset-password/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest', //Necessary to work with request.is_ajax()
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify({
            email: email.toString(),
        })
    }).then(response => response.json())
        .then(data => {
            toast({
                title: 'Quên mật khẩu',
                message: data.message,
                type: data.message_status ? 'success' : 'error'
            })
        })
        .catch(error => {
            toast({
                title: 'Quên mật khẩu',
                message: 'Có lỗi xảy ra khi gửi email!',
                type: 'error',
            })
            console.log(error)
        })
}

function sendDataToSignupCompany(companyName, email, phone, password) {
    fetch('/company/company-signup/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest', //Necessary to work with request.is_ajax()
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify({
            companyName: companyName.toString(),
            email: email.toString(),
            phone: phone.toString(),
            password: password.toString(),
        })
    }).then(response => response.json())
        .then(data => {
            sendVerificationEmail(email)
            toast({
                title: 'Đăng ký thành công',
                message: data.message,
                type: 'success',
            })
        })
        .catch(error => {
            toast({
                title: 'Đăng ký tài khoản doanh nghiệp',
                message: 'Có lỗi xảy ra trong quá trình đăng ký!',
                type: 'error',
            })
            console.log(error)
        });
}