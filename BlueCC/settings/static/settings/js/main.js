const btnVerify = document.querySelector('.btn-verify');
const alert = document.querySelector('.my_alert')

btnVerify.addEventListener('click', function () {
    alert.classList.remove('my_alert--hidden')
});

function removeAlertBox() {
    alert.classList.add('my_alert--hidden');
}

// function sendDataToDjango(url, email) {
//     fetch(url, {
//         method: 'post', body: JSON.stringify({
//             'email': email
//         }), headers: {
//             'Content-Type': 'application/json',
//         },
//     })
//         .then(response => response.json())
//         .then(data => {
//             // Xử lý dữ liệu trả về từ Django ở đây
//             console.log(data);
//             // Cập nhật giao diện người dùng tương ứng
//         })
//         .catch(error => {
//             // Xử lý lỗi nếu có
//             console.error('Error:', error);
//         });
// }