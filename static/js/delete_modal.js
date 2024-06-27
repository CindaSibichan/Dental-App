// edit modal
document.addEventListener('DOMContentLoaded', function () {
    const editButtons = document.querySelectorAll('#edit-button');
    const editModal = document.getElementById('edit-modal');
    const cancelEdit = document.getElementById('cancel-edit');

    const subscriptInput = document.getElementById('hospital-subscript');
    const daysContainer = document.getElementById('days-container');
    const amountContainer = document.getElementById('amount-container');
    const registrationDateContainer = document.getElementById('registration-date-container');
    function updateFieldVisibility(subscriptionType) {
        if (subscriptionType === 'Permanent') {
            daysContainer.classList.add('hidden');
            amountContainer.classList.remove('hidden');
            registrationDateContainer.classList.remove('hidden');
        } else if (subscriptionType === 'Temporary') {
            daysContainer.classList.remove('hidden');
            amountContainer.classList.add('hidden');
            registrationDateContainer.classList.add('hidden');
        }
    }

    editButtons.forEach(button => {
        button.addEventListener('click', function () {
            const hospitalId = this.getAttribute('data-id');
            const hospitalName = this.getAttribute('data-name');
            const hospitalPhone = this.getAttribute('data-phone');
            const hospitalEmail = this.getAttribute('data-email');
            const hospitalSubscript = this.getAttribute('data-subscript');
            const hospitalDays = this.getAttribute('data-days');
            const hospitalAmount = this.getAttribute('data-amount');
            const hospitalRegistrationDate = this.getAttribute('data-registration-date');

            // Parse the d-m-Y formatted date string
            const [day, month, year] = hospitalRegistrationDate.split('-');
            const parsedDate = new Date(year, month - 1, day); // month - 1 because JavaScript months are 0-indexed

            // Optionally format the parsed date as needed
            const formattedDate = `${parsedDate.getFullYear()}-${parsedDate.getMonth() + 1}-${parsedDate.getDate()}`;

            document.getElementById('hospital-id').value = hospitalId;
            document.getElementById('hospital-name').value = hospitalName;
            document.getElementById('hospital-phone').value = hospitalPhone;
            document.getElementById('hospital-email').value = hospitalEmail;
            document.getElementById('hospital-subscript').value = hospitalSubscript;
            document.getElementById('hospital-days').value = hospitalDays;
            document.getElementById('hospital-amount').value = hospitalAmount;
            document.getElementById('hospital-registration-date').value = formattedDate;

            updateFieldVisibility(hospitalSubscript);

            editModal.classList.remove('hidden');
        });
    });

    subscriptInput.addEventListener('input', function () {
        updateFieldVisibility(this.value);
    });

    cancelEdit.addEventListener('click', function () {
        editModal.classList.add('hidden');
    });
});






// Delete modal
document.addEventListener('DOMContentLoaded', function () {
    // Delete modal setup
    const deleteButtons = document.querySelectorAll('.delete-button'); 
    const deleteModal = document.getElementById('delete-modal');
    const confirmDelete = document.getElementById('confirm-delete');
    const cancelDelete = document.getElementById('cancel-delete');

    deleteButtons.forEach(deleteButton => {
        deleteButton.addEventListener('click', function () {
            deleteModal.classList.remove('hidden');
            const deleteUrl = this.getAttribute('data-href');
            confirmDelete.setAttribute('data-href', deleteUrl);
        });
    });

    confirmDelete.addEventListener('click', function () {
        const deleteUrl = this.getAttribute('data-href');
        window.location.href = deleteUrl;
    });

    cancelDelete.addEventListener('click', function () {
        deleteModal.classList.add('hidden');
    });

});
