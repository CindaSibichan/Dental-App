
// notification modal
// document.addEventListener("DOMContentLoaded", function() {
//     // Check if the modal has already been shown today
//     if (!localStorage.getItem('modalShown')) {
//         var expiredMessages = '{{ expired_hospitals_messages|escapejs }}'; // Use escapejs filter to safely output the string

//         // Split the message string into individual messages
//         var messagesList = expiredMessages.split('\n');

//         // Check if there are any expired hospital messages
//         if (messagesList.length > 0) {
//             // Display the modal
//             document.getElementById("noti_modal").classList.remove("hidden");

//             // Set the notification message
//             var notificationElement = document.getElementById("notificationMessage");
//             notificationElement.innerHTML = ''; // Clear existing content
//             messagesList.forEach(function(message) {
//                 var p = document.createElement('p'); // Create a new paragraph element for each message
//                 p.textContent = message; // Set the message text
//                 notificationElement.appendChild(p); // Append the paragraph to the notification element
//             });
//         }

//         // Mark the modal as shown
//         localStorage.setItem('modalShown', 'true');
//     }

//     // Close modal functionality
//     document.getElementById("closeBtn").addEventListener("click", function() {
//         document.getElementById("noti_modal").classList.add("hidden");
//     });

//     document.getElementById("buttonClose").addEventListener("click", function() {
//         document.getElementById("noti_modal").classList.add("hidden");
//     });
// });
