/* _______________________
Command use toast message:

Alert({
	type: "Your type you want",
	title: "Your title!",
	text: "Your text.",
	buttonLeft: "Content for button left",
	classButtonLeft: "Class for button left", (optional)
	buttonRight: "Content for button right",
	classButtonRight: "Class for button right", (optional)
	coin: "Coin for reward the game", (optional)
})
_______________________*/

const alert = document.createElement('div');
alert.classList.add('alert');
document.body.prepend(alert);
const icons = {
    empty: 'fa-solid fa-hourglass alertbox__icon--empty',
    congrats: 'fa-solid fa-award',
    email: 'fa-solid fa-envelope',
    error: 'fa-solid fa-xmark',
    success: 'fa-solid fa-check',
    danger: 'fa-solid fa-bolt',
    info: 'fa-solid fa-circle-info',
    warning: 'fa-solid fa-triangle-exclamation',
};

function Alert({
                   type = 'empty',
                   title = 'SOMETHING WENT WRONG!',
                   text = 'Nothing here.',
                   buttonLeft = '',
                   classButtonLeft = '',
                   buttonRight = '',
                   classButtonRight = '',
                   coin = null,
               }) {
    const alertBox = document.createElement('div');
    alertBox.classList.add('alertbox', `alertbox--${type}`);
    alertBox.innerHTML = `<div class="alertbox__icon"><i class="${icons[type]}"></i></div>
								<div class="alertbox__title">
									<h2>${title}</h2>
								</div>
								<div class="alertbox__text">${text}</div>
                                ${buttonLeft !== '' ? `<div class="${classButtonLeft} btn btn--size-s">${buttonLeft}</div>` : ''}
                                ${buttonRight !== '' ? `<div class="${classButtonRight} btn btn--size-s">${buttonRight}</div>` : ''}`;
    // if (buttonLeft !== '' || buttonRight !== '' || classButtonLeft !== '' || classButtonRight !== '') {
    //     alertBox.innerHTML += `<div class="alertbox__btn btns">
    //         ${buttonLeft !== '' ? `<div class="${classButtonLeft} btn btn--size-s">${buttonLeft}</div>` : ''}
    //         ${buttonRight !== '' ? `<div class="${classButtonRight} btn btn--size-s">${buttonRight}</div>` : ''}
    //     </div>`;
    // }
    alert.prepend(alertBox);
    if (coin !== null) {
        const alertText = document.querySelector('.alertbox__text');
        alertText.innerHTML = `${text}<span>${coin} Coin</span>`;
    }
}
