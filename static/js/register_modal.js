
// Register modal
document.addEventListener('DOMContentLoaded', (event) => {
    const modal = document.getElementById('modal');
    const openModalBtn = document.getElementById('openmodal');
    const closeModalBtn = document.getElementById('closeModalBtn');
    const subscriptField = document.getElementById('id_subscript');
    const daysField = document.getElementById('days');
    const amountField = document.getElementById('amount');
    const registrationDateField = document.getElementById('register_date');
    const buttonReset = document.getElementById('buttonReset');
    const hospitalForm = document.getElementById('hospitalmodal');
    
    
    openModalBtn.addEventListener('click', () => {
        modal.classList.add('active');
    });

    closeModalBtn.addEventListener('click', () => {
        modal.classList.remove('active');
    });

    buttonReset.addEventListener('click', (event) => {
        event.preventDefault(); 
        
        // Show confirmation dialog
        const confirmReset = confirm("Are you sure you want to reset the form?");
        
        if (confirmReset) {
          
            hospitalForm.reset(); 
            modal.classList.add('active'); 
        }
    });
    subscriptField.addEventListener('change', (event) => {
        const value = event.target.value;

        daysField.classList.add('hidden');
        amountField.classList.add('hidden');
        registrationDateField.classList.add('hidden');
        registrationDateField.removeAttribute('required');

        if (value === 'Temporary') {
            daysField.classList.remove('hidden');
        } else if (value === 'Permanent') {
            amountField.classList.remove('hidden');
            registrationDateField.classList.remove('hidden');
            registrationDateField.setAttribute('required', 'required');
        }
    });

    // const form = document.getElementById('hospitalmodal');
    hospitalForm.addEventListener('submit', (event) => {
        console.log('Form submitted');
        // event.preventDefault(); // Prevent actual form submission

        // Close the modal
        // modal.classList.remove('active');

        

       
        // Delay the success message display
        setTimeout(() => {
            // Create a success message element
            const successMessage = document.createElement('div');
            successMessage.classList.add('bg-green-600', 'text-white', 'p-4', 'fixed', 'bottom-0', 'z-50', 'right-0', 'm-4', 'rounded-md', 'shadow-md');
            successMessage.textContent = 'Hospital Registered Successfully!';

            // Append the success message to the document body
            document.body.appendChild(successMessage);

            // Remove the success message after 10 seconds
            setTimeout(() => {
                successMessage.remove();
            }, 8000);
        }, 200); // Adjust the delay as needed
    });
});

