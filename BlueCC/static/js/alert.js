const btnVerify = document.querySelector('.btn-verify');
const alert = document.querySelector('.my_alert')

if (btnVerify) {
    btnVerify.addEventListener('click', function () {
        alert.classList.remove('my_alert--hidden')
    });
}

function removeAlertBox() {
    alert.classList.add('my_alert--hidden');
}