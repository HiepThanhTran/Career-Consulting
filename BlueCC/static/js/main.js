const getCookie = (name) => {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
};

function sendVerificationEmail(email, message = '') {
    fetch('/api/verification-email/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest', //Necessary to work with request.is_ajax()
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify({
            email: email,
        }),
    }).then(response => response.json())
        .then(data => {
            if (data.message !== '') {
                toast({
                    title: 'Xác thực tài khoản',
                    message: data.message,
                    type: 'success',
                })
            }
        })
        .catch(error => {
            toast({
                title: 'Xác thực tài khoản',
                message: 'Có lỗi xảy ra khi gửi email xác thực!',
                type: 'error',
            })
        });
}