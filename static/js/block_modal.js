// Block modal

document.addEventListener('DOMContentLoaded', () => {
    const blockForms = document.querySelectorAll('.blockForm'); // Select all forms with class .blockForm
    const blockBtns = document.querySelectorAll('.blockBtn'); // Select all buttons with class .blockBtn

    // Modal elements
    const modal = document.getElementById('confirmationModal');
    const confirmBtn = document.getElementById('confirmBtn');
    const cancelBtn = document.getElementById('cancelBtn');

    // Add event listeners to each block button
    blockBtns.forEach((blockBtn, index) => {
        blockBtn.addEventListener('click', () => {
            // Show confirmation modal
            modal.classList.remove('hidden');

            // Set up form submission on confirmation
            confirmBtn.addEventListener('click', () => {
                modal.classList.add('hidden');
                blockForms[index].submit(); // Submit the corresponding form
            });
        });
    });

    // Handle cancel button click
    cancelBtn.addEventListener('click', () => {
        modal.classList.add('hidden');
    });
});

// UnBlock modal

document.addEventListener('DOMContentLoaded', () => {
    const unblockForms = document.querySelectorAll('.unblockForm'); // Select all forms with class .blockForm
    const unblockBtns = document.querySelectorAll('.unblockBtn'); // Select all buttons with class .blockBtn

    // Modal elements
    const modal = document.getElementById('confirmationUnblockModal');
    const unblockconfirmBtn = document.getElementById('confirmUnblockBtn');
    const unblockcancelBtn = document.getElementById('cancelUnblockBtn');

    // Add event listeners to each block button
    unblockBtns.forEach((unblockBtn, index) => {
        unblockBtn.addEventListener('click', () => {
            // Show confirmation modal
            modal.classList.remove('hidden');

            // Set up form submission on confirmation
            unblockconfirmBtn.addEventListener('click', () => {
                modal.classList.add('hidden');
                unblockForms[index].submit(); // Submit the corresponding form
            });
        });
    });

    // Handle cancel button click
    unblockcancelBtn.addEventListener('click', () => {
        modal.classList.add('hidden');
    });
});
