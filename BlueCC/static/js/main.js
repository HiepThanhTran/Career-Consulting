const getCookie = (name) => {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
};

const showLoadingModal = () => {
    const loadingModal = document.getElementById('loadingModal');
    loadingModal.style.display = 'flex';
};

const hideLoadingModal = () => {
    const loadingModal = document.getElementById('loadingModal');
    loadingModal.style.display = 'none';
};