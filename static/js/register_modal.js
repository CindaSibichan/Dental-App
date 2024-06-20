// document.addEventListener('DOMContentLoaded', () => {
//     const openModalBtn = document.getElementById('openmodal');
//     const closeModalBtn = document.getElementById('closeModalBtn');
//     const modal = document.getElementById('modal');

//     openModalBtn.addEventListener('click', () => {
//         modal.classList.add('active');
//     });

//     closeModalBtn.addEventListener('click', () => {
//         modal.classList.remove('active');
//     });


//     window.addEventListener('click', (e) => {
//         if (e.target == modal) {
//             modal.classList.remove('active');
//         }
//     });
// });


    document.addEventListener('DOMContentLoaded', (event) => {
        const modal = document.getElementById('modal');
        const openModalBtn = document.getElementById('openmodal');
        const closeModalBtn = document.getElementById('closeModalBtn');
        const subscriptField = document.getElementById('id_subscript');
        const daysField = document.getElementById('days');
        const amountField = document.getElementById('amount');
        const registrationDateField = document.getElementById('register_date');
        const buttonCancel = document.getElementById('buttonCancel');

        openModalBtn.addEventListener('click', () => {
            modal.classList.add('active');
        });

        closeModalBtn.addEventListener('click', () => {
            modal.classList.remove('active');
        });

        buttonCancel.addEventListener('click', () => {
            modal.classList.remove('active');
        });

        subscriptField.addEventListener('change', (event) => {
            const value = event.target.value;

            // Hide all fields initially
            daysField.classList.add('hidden');
            amountField.classList.add('hidden');
            registrationDateField.classList.add('hidden');

            // Show fields based on the selected subscription type
            if (value === 'Temporary') {
                daysField.classList.remove('hidden');
            } else if (value === 'Permanent') {
                amountField.classList.remove('hidden');
                registrationDateField.classList.remove('hidden');
            }
        });
    });



