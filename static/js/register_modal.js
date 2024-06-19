document.addEventListener('DOMContentLoaded', () => {
    const openModalBtn = document.getElementById('openmodal');
    const closeModalBtn = document.getElementById('closeModalBtn');
    const modal = document.getElementById('modal');

    openModalBtn.addEventListener('click', () => {
        modal.classList.add('active');
    });

    closeModalBtn.addEventListener('click', () => {
        modal.classList.remove('active');
    });

    // Optional: Close the modal when clicking outside of it
    window.addEventListener('click', (e) => {
        if (e.target == modal) {
            modal.classList.remove('active');
        }
    });
});


// Notification modal

