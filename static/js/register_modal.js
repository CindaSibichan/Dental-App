
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
        event.preventDefault(); // Prevent default form submission

        const formData = new FormData(hospitalForm);

        fetch(hospitalForm.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': formData.get('csrfmiddlewaretoken')
            }
        })
        .then(response => response.json())
        .then(data => {
            // Assuming your server returns a success response
            if (data.success) {
                modal.classList.remove('active');
                hospitalForm.reset(); // Clear form fields
                fetch('/updated_hospitals')
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    console.log('Updated hospitals data:', data);
                   
                    // updateTable(data.hospitals);
                     // Check fetched data
                    // Update your UI or table with the fetched data
                    // Example: updateTable(data.hospitals);
                })
                .catch(error => {
                    console.error('Error fetching updated hospitals:', error); // Log fetch error
                });
        

                // Fetch updated hospital data and update UI
              
                // Delay the success message display to ensure the modal is closed
                setTimeout(() => {
                    // Create a success message element
                    const successMessage = document.createElement('div');
                    successMessage.classList.add('bg-green-600', 'text-white', 'p-4', 'fixed', 'bottom-8', 'z-50', 'right-0', 'm-4', 'rounded-md', 'shadow-md');
                    successMessage.textContent = 'Hospital Registered Successfully!';

                    document.body.appendChild(successMessage);
                   

                    // Remove the success message after 10 seconds
                    setTimeout(() => {
                        successMessage.remove();
                        window.location.href = '/dashboard/';
                    }, 2000);
                    
                }, 200);
         
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
    // function updateTable(newHospitalsData) {
    //     const tbody = document.querySelector('#hospitals-table tbody');
    
    //     if (!newHospitalsData || newHospitalsData.length === 0) {
    //         console.error('No data received for updating table.');
    //         return;
    //     }
    
    //     // Loop through each new hospital entry
    //     newHospitalsData.forEach(hospital => {
    //         // Create a new row for each hospital
    //         const row = document.createElement('tr');
    
    //         // For each property in the hospital object, create a new cell and append it to the row
    //         Object.entries(hospital).forEach(([key, value]) => {
    //             const cell = document.createElement('td');
    //             cell.textContent = value; // Set the cell content to the corresponding value
    //             row.appendChild(cell);
    //         });
    
    //         // Append the new row to the table body
    //         tbody.appendChild(row);
    //     });
    // }
    
});
