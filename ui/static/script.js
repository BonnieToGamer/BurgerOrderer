document.querySelectorAll('.burgers').forEach(burger => {
    burger.addEventListener('click', function() {
        // Remove 'active' class and remove "Order" button from other burgers
        document.querySelectorAll('.burgers').forEach(b => {
            b.classList.remove('active');
            const existingButton = b.querySelector('.order-btn');
            if (existingButton) existingButton.remove(); // Remove any existing buttons
        });

        // Add 'active' class to the clicked burger
        this.classList.add('active');

        // Create and add the "Order" button
        const orderButton = document.createElement('button');
        orderButton.textContent = 'Order';
        orderButton.classList.add('order-btn');

        // Append the button to the burger container
        this.appendChild(orderButton);

        // Handle click event on the "Order" button
        orderButton.addEventListener('click', function() {
            // Redirect to another page (e.g., order.html)
            window.location.href = '/views/order'; // Adjust the path as needed
        });
    });
});
