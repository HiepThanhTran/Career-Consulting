function sendVerificationEmail(email) {
    fetch('/api/verification-email/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
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

function sendDataToServer(url, method, body, successMessage, errorMessage) {
    showLoadingModal();

    fetch(url, {
        method: method,
        headers: {
            'Content-Type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify(body)
    }).then(response => response.json())
        .then(data => {
            if (data.redirect_to) {
                const baseUrl = window.location.origin
                window.location.href = new URL(data.redirect_to, baseUrl).href
            } else if (data.message) {
                sendVerificationEmail(body.email)
                toast({
                    title: data.message_status ? successMessage : errorMessage,
                    message: data.message,
                    type: data.message_status ? 'success' : 'error'
                })
            }
        })
        .catch(error => {
            toast({
                title: errorMessage,
                message: 'Có lỗi xảy ra trong quá trình xử lý dữ liệu. Vui lòng thử lại!',
                type: 'error',
            });
            console.log(error);
        })
        .finally(() => {
            hideLoadingModal();
        });
}