const btnSubmit = document.querySelector('.btn-submit')

btnSubmit.addEventListener('click', function () {
    const email = document.getElementById('email')
    const password = document.getElementById('password')
    const policyCheck = document.getElementById('policy_check')

    const regex = /^(?!.*@gmail\.com$).+@.+\..+$/

    let message = !regex.test(email.value) ? 'Vui lòng sử dụng email doanh nghiệp' :
        (policyCheck ? 'Vui lòng đồng ý với chính sách của chúng tôi!' : null)

    if (regex.test(email.value) && policyCheck.checked) {
        sendDataToLogin('/company/company-login/', email.value, password.value)

        email.value = ""
        password.value = ""
    } else {
        toast({
            title: 'Đăng nhập', message: message, type: 'error',
        })
    }
})