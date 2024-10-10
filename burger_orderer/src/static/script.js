function createBurgerDiv(burgerName, burgerPrice) {
    const burgerDiv = document.createElement('div');
    burgerDiv.classList.add('burgers');

    const burgerLink = document.createElement('a');
    burgerLink.href = '/order?burger=' + burgerName;

    const burgerImage = document.createElement('img');
    burgerImage.src = '../static/Burger1.png'; // Placeholder image
    burgerImage.classList.add('burger-image');
    burgerImage.alt = burgerName;

    burgerLink.appendChild(burgerImage);

    const burgerInfoDiv = document.createElement('div');
    burgerInfoDiv.classList.add('burger-info');

    const burgerNameH3 = document.createElement('h3');
    burgerNameH3.classList.add('burger-name');
    burgerNameH3.textContent = burgerName;

    const burgerPriceDiv = document.createElement('div');
    burgerPriceDiv.classList.add('burger-price');
    burgerPriceDiv.textContent = burgerPrice;

    burgerInfoDiv.appendChild(burgerNameH3);
    burgerInfoDiv.appendChild(burgerPriceDiv);

    burgerDiv.appendChild(burgerLink);
    burgerDiv.appendChild(burgerInfoDiv);

    return burgerDiv;
}

function loadBurgers() {
    fetch('/api/getBurgers')
        .then(response => response.json())
        .then(burgers => {
            const burgerContainer = document.getElementById('burgers-container');

            burgers.forEach(burger => {
                const { name, price } = burger;
                const burgerDiv = createBurgerDiv(name, price);
                burgerContainer.appendChild(burgerDiv); // Append each burger to the container
            });
        })
        .catch(error => console.error('Error fetching burgers:', error));
}

document.addEventListener('DOMContentLoaded', loadBurgers);
