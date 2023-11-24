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
})
_______________________*/

var alert = document.createElement('div');
alert.classList.add('alert', 'alert--hidden');
document.body.prepend(alert);
const icons = {
   empty: 'fa-solid fa-hourglass alertbox__icon--empty',
   congrats: 'fa-solid fa-award',
};
function Alert({
   type = '',
   title = '',
   text = '',
   textButtonLeft = '',
   textButtonRight = '',
}) {
   alert.classList.remove('alert--hidden');
   const alertBox = document.createElement('div');
   alertBox.classList.add('alertbox', `alertbox--${type}`);
   alertBox.innerHTML = `<div class="alertbox__icon"><i class="${icons[type]}"></i></div>
								<div class="alertbox__title"><h2>${title}</h2></div>
								<div class="alertbox__text">${text}</div>
								<div class="alertbox__btn btns">
									${textButtonLeft ? <div onclick="removeAlertBox();" class="buttons buttons--size-s">${textButtonLeft}</div> : ""}
									${textButtonRight ? <div onclick="removeAlertBox();" class="buttons buttons--size-s">${textButtonRight}</div> : ""}
								</div>`;
   alert.prepend(alertBox);
}
function removeAlertBox() {
   alert.replaceChildren();
   alert.classList.add('alert--hidden');
}

function createAlert(type, title, text, ...butons) {
   Alert({
      type: type,
      title: title,
      text: text,
      textButtonLeft: 'Back to lobby',
      textButtonRight: 'New game',
   });
}
