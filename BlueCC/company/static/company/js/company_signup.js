const btnSubmit = document.querySelector('.btn-submit')

btnSubmit.addEventListener('click', function () {
    const companyName = document.getElementById('company_name')
    const email = document.getElementById('email')
    const phone = document.getElementById('phone')
    const password = document.getElementById('password')
    const passwordConfirm = document.getElementById('confirm')
    const policyCheck = document.getElementById('policy_check')

    const regex = /^(?!.*@gmail\.com$).+@.+\..+$/

    let message = !regex.test(email.value) ? 'Vui lòng sử dụng email doanh nghiệp' : (password === passwordConfirm ? 'Mật khẩu không khớp!' :
        (policyCheck ? 'Vui lòng đồng ý với chính sách của chúng tôi!' : null))

    if (regex.test(email.value) && password.value === passwordConfirm.value && policyCheck.checked) {
        sendDataToSignupCompany(companyName.value, email.value, phone.value, password.value)

        companyName.value = ""
        email.value = ""
        phone.value = ""
        password.value = ""
        passwordConfirm.value = ""
        policyCheck.checked = false
    } else {
        toast({
            title: 'Đăng ký tài khoản doanh nghiệp', message: message, type: 'error',
        })
    }
})