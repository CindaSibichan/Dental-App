// // Notification modal
// document.addEventListener("DOMContentLoaded", function() {
//     // Get the notification message from Django messages framework
//     var notificationMessage = "{{ notification_message }}";

//     if (notificationMessage) {
//         // Display the modal
//         document.getElementById("noti_modal").classList.remove("hidden");
//         document.getElementById("notificationMessage").innerText = notificationMessage;
//     }

//     // Close modal functionality
//     document.getElementById("closeBtn").addEventListener("click", function() {
//         document.getElementById("noti_modal").classList.add("hidden");
//     });

//     document.getElementById("buttonClose").addEventListener("click", function() {
//         document.getElementById("noti_modal").classList.add("hidden");
//     });
// });