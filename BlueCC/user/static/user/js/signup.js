const btnSubmit = document.querySelector('.btn-submit')

btnSubmit.addEventListener('click', function () {
    const fullName = document.getElementById('full_name')
    const email = document.getElementById('email')
    const password = document.getElementById('password')
    const passwordConfirm = document.getElementById('confirm')
    const policyCheck = document.getElementById('policy_check')

    let message = password === passwordConfirm ? 'Mật khẩu không khớp!' : (policyCheck ? 'Vui lòng đồng ý với chính sách của chúng tôi!' : null)

    if (password.value === passwordConfirm.value && policyCheck.checked) {
        sendDataToServer('/account/signup/', 'POST', {
            fullName: fullName.value.toString(),
            email: email.value.toString(),
            password: password.value.toString(),
        }, 'Đăng ký thành công', 'Đăng ký thất bại')

        fullName.value = ""
        email.value = ""
        password.value = ""
        passwordConfirm.value = ""
        policyCheck.checked = false
    } else {
        toast({
            title: 'Đăng ký tài khoản', message: message, type: 'error',
        })
    }
})