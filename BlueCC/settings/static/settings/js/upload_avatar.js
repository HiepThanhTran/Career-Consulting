const boxUpload = document.querySelector('.box-upload')
const boxUploadBody = document.querySelector('.box-upload__body')
const buttonChangeAvatar = document.querySelector('.buton_change_avatar')
const inputAvatarFile = document.getElementById('input_avatar')
const avatarLabel = document.querySelector('#avatar_form > p > label')
const label = document.querySelector('.not-cv > label')
const previewAvatar = document.querySelector('.not-cv img')
const iconUpload = document.querySelector('.icon_upload')

window.addEventListener('beforeunload', function (event) {
    const avatarForm = document.getElementById('avatar_form')
    const formData = new FormData(avatarForm);

    if (avatarForm.dirty && !window.confirm('Bạn có chắc chắn muốn rời khỏi trang?')) {
        event.preventDefault();
        event.returnValue = '';
    }
});

buttonChangeAvatar.addEventListener('click', () => {
    inputAvatarFile.value = ""
    boxUpload.style.display = 'flex'
})

inputAvatarFile.addEventListener('change', () => {
    avatarLabel.textContent += inputAvatarFile.files.item(0).name
    label.style.display = 'none'
    previewAvatar.style.display = 'block'
    iconUpload.style.display = 'none'
    previewAvatar.src = URL.createObjectURL(inputAvatarFile.files.item(0))
})

boxUpload.addEventListener('click', () => {
    boxUpload.style.display = 'none'
    label.style.display = 'block'
    previewAvatar.style.display = 'none'
    iconUpload.style.display = 'block'
    inputAvatarFile.value = ""
    avatarLabel.textContent = "Avatar:  "
})

boxUploadBody.addEventListener('click', (event) => {
    event.stopPropagation();
})