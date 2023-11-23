const btnSubmit = document.querySelector('.btn-submit')

btnSubmit.addEventListener('click', function () {
    const email = document.getElementById('email')
    const policyCheck = document.getElementById('policy_check')

    let message = policyCheck ? 'Vui lòng đồng ý với chính sách của chúng tôi!' : null

    if (policyCheck.checked) {
        sendDataToResetPassword(email.value)

        email.value = ""
        policyCheck.checked = false
    } else {
        toast({
            title: 'Quên mật khẩu', message: message, type: 'error',
        })
    }
})