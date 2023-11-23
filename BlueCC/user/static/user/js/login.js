const btnSubmit = document.querySelector('.btn-submit')

btnSubmit.addEventListener('click', function () {
    const email = document.getElementById('email')
    const password = document.getElementById('password')
    const policyCheck = document.getElementById('policy_check')

    let message = policyCheck ? 'Vui lòng đồng ý với chính sách của chúng tôi!' : null

    if (policyCheck.checked) {
        sendDataToLogin('/account/login/', email.value, password.value)

        email.value = ""
        password.value = ""
    } else {
        toast({
            title: 'Đăng nhập', message: message, type: 'error',
        })
    }
})