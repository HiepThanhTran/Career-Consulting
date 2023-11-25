function applyJob(userID, jobID) {
    fetch('/job/apply-job/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify({
            userID: userID.toString(),
            jobID: jobID.toString(),
        })
    }).then(response => response.json())
        .then(data => {
            const baseUrl = window.location.origin
            window.location.href = new URL(data.redirect_to, baseUrl).href
        })
}