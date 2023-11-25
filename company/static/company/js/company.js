const textAreas = document.querySelectorAll('.company_description');

if (textAreas) {
    textAreas.forEach(textArea => {
        ClassicEditor
            .create(textArea)
            .then(editor => {

            })
            .catch(error => {
                console.error(error);
            });
    });
}

const inputSearchJD = document.getElementById('searchJD')
const jdName = document.getElementsByClassName('campaign-card__left--title')
const jdCard = document.getElementsByClassName('campaign-card')

function searchJD() {
    const filter = inputSearchJD.value.toUpperCase();

    for (let i = 0; i < jdName.length; i++) {
        if (jdName[i].innerHTML.toUpperCase().indexOf(filter) > -1) {
            jdCard[i].style.display = 'flex'
        } else {
            jdCard[i].style.display = 'none'
        }
    }
}

const buttons = document.getElementsByClassName('btn-remove');

for (let i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener('click', function () {
        showAlertBox(i)
    })
}


function deleteJD(button, jobdescription_id) {
    showLoadingModal()
    fetch('/company/company-recruitment-management-delete/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify({
            jobdescription_id: jobdescription_id
        })
    }).then(response => response.json())
        .then(data => {
            toast({
                title: 'Xoá bài tuyển dụng',
                message: data.message,
                type: data.message_status ? 'success' : 'error',
            })
        })
        .catch(error => {
            toast({
                title: 'Xoá bài tuyển dụng',
                message: 'Có lỗi trong quá trình truyền dữ liệu. Vui lòng thử lại sau ít phút!',
                type: 'error',
            })
            console.log(error)
        })
        .finally(() => {
            hideLoadingModal();
        });

    const campaignCard = button.closest('.campaign-card');

    if (campaignCard) {
        campaignCard.remove()
    }
}
