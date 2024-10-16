const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const burger = urlParams.get("burger")

function createSpecialOption(specialName) {
    const label = document.createElement('label');

    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.classList.add('special-option');
    checkbox.value = specialName;

    label.appendChild(checkbox);

    label.append(` ${specialName}`);

    return label;
}

function loadSpecialOptions() {
    fetch('/api/getSpecials?burger=' + burger)
        .then(response => response.json())
        .then(specials => {
            const specialsContainer = document.getElementById('specials-container');

            specials.forEach(special => {
                const specialOption = createSpecialOption(special);
                specialsContainer.appendChild(specialOption);
            });
        })
        .catch(error => console.error('Error fetching specials:', error));
}

document.addEventListener('DOMContentLoaded', loadSpecialOptions);

function getSelectedSpecials() {
    const selectedSpecials = [];
    const checkboxes = document.querySelectorAll('.special-option');

    checkboxes.forEach(checkbox => {
        if (checkbox.checked) {
            selectedSpecials.push(checkbox.value);
        }
    });

    return selectedSpecials;
}

function submitOrder() {
    const specials = getSelectedSpecials();

    const orderData = {
        order: {
            burger: burger,
            specials: specials
        }
    };

    fetch('/api/newOrder', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(orderData)
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Error placing order');
        }
    })
    .then(data => {
        console.log('Order placed successfully:', data);
        alert("Success!")
        window.location.href = "/";
    })
    .catch(error => {
        console.error('Error:', error);
        alert("There was an error!")
    });
}

document.getElementById('order-btn').addEventListener('click', submitOrder);
