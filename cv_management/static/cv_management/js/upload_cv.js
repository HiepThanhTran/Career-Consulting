const inputCVFile = document.getElementById('file-upload-cv')
const iconUpload = document.querySelector('.icon_upload')
const textUpload = document.querySelector('.not-cv')
const previewCV = document.getElementById('preview_cv')
const cvLabel = document.getElementById('cv_label')
const boxUploadMain = document.querySelector('.box-upload-main')

inputCVFile.addEventListener('change', () => {
    previewCV.src = URL.createObjectURL(inputCVFile.files.item(0))
    previewCV.style.display = 'block'
    cvLabel.textContent = 'CV: ' + inputCVFile.files.item(0).name
    cvLabel.style.display = 'block'
    iconUpload.style.display = 'none'
    textUpload.style.display = 'none'
    boxUploadMain.style.display = 'flex'
})