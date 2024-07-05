// Block modal

document.addEventListener('DOMContentLoaded', () => {
    const blockForms = document.querySelectorAll('.blockForm'); 
    const blockBtns = document.querySelectorAll('.blockBtn'); 


    const modal = document.getElementById('confirmationModal');
    const confirmBtn = document.getElementById('confirmBtn');
    const cancelBtn = document.getElementById('cancelBtn');

  
    blockBtns.forEach((blockBtn, index) => {
        blockBtn.addEventListener('click', () => {
          
            modal.classList.remove('hidden');

            
            confirmBtn.addEventListener('click', () => {
                modal.classList.add('hidden');
                blockForms[index].submit(); 
            });
        });
    });

   
    cancelBtn.addEventListener('click', () => {
        modal.classList.add('hidden');
    });
});

// UnBlock modal

document.addEventListener('DOMContentLoaded', () => {
    const unblockForms = document.querySelectorAll('.unblockForm');
    const unblockBtns = document.querySelectorAll('.unblockBtn'); 

 
    const modal = document.getElementById('confirmationUnblockModal');
    const unblockconfirmBtn = document.getElementById('confirmUnblockBtn');
    const unblockcancelBtn = document.getElementById('cancelUnblockBtn');


    unblockBtns.forEach((unblockBtn, index) => {
        unblockBtn.addEventListener('click', () => {
            
            modal.classList.remove('hidden');

           
            unblockconfirmBtn.addEventListener('click', () => {
                modal.classList.add('hidden');
                unblockForms[index].submit(); 
            });
        });
    });

 
    unblockcancelBtn.addEventListener('click', () => {
        modal.classList.add('hidden');
    });
});
