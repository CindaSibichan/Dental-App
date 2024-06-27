// Notification modal
document.addEventListener('DOMContentLoaded', () => {
    const openModal = document.getElementById('noti-open-model');
    const closeModal = document.getElementById('closeBtn');
    const modalNoti = document.getElementById('noti_modal');
    const buttonClose = document.getElementById('buttonClose');

    openModal.addEventListener('click', () => {
        modalNoti.classList.add('active');
    });

    closeModal.addEventListener('click', () => {
        modalNoti.classList.remove('active');
        
    });
    buttonClose.addEventListener('click', () => {
        modalNoti.classList.remove('active');
    });

    // Optional: Close the modal when clicking outside of it
    window.addEventListener('click', (e) => {
        if (e.target == modalNoti) {
            modal.classList.remove('active');
        }
    });
});


