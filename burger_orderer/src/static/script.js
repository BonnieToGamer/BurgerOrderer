document.querySelectorAll('.burgers').forEach(burger => {
    //Lägger till klickad burgare och tar bort de andra från UI
    burger.addEventListener('click', function() {
        document.querySelectorAll('.burgers').forEach(b => {
            if (b !== this) {
                b.style.display = 'none'; 
            }
        });

        //lägger till "active" klassen till .burgers
        this.classList.add('active');
        
        //lägger till specials UI
        document.querySelector('.specials-container').style.display = 'grid';
        
        //Order Button
        const newOrderButton = document.createElement('button');
        newOrderButton.textContent = 'Order';
        newOrderButton.classList.add('order-btn');
        //Lägger till order button i UI
        this.appendChild(newOrderButton);

        newOrderButton.addEventListener('click', function() {
            window.location.href = '/views/order'; 
        });

        //Data collection
        newOrderButton.addEventListener('click', function() {

            const selectedBurger = {
                name: burger.querySelector('.burger-name').textContent
            };

            const selectedSpecials = [];
            document.querySelectorAll('.special-option').forEach(option => {
                if (option.checked) {
                    selectedSpecials.push(option.value); 
                }
            });
        });
    });
});

