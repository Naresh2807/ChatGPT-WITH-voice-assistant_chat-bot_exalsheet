    document.getElementById('contactForm').addEventListener('submit', function(event) {
      event.preventDefault();
      
      var name = document.getElementById('name').value;
      var email = document.getElementById('email').value;
      var message = document.getElementById('message').value;
      
      // Send the form data to the server using AJAX or any other method you prefer
      // You can include additional validation or processing logic here
      
      // Display a success message to the user
      document.getElementById('message').innerHTML = '<p>Thank you for contacting us, ' + name + '! We will get back to you soon.</p>';
      
      // Reset the form fields
      document.getElementById('contactForm').reset();
    });