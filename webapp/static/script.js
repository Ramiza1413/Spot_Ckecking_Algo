document.getElementById('signinForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    try {
        const response = await fetch('/signin', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });
        if (response.ok) {
            window.location.href = '/login';
        } else {
            const data = await response.json();
            document.getElementById('message').textContent = data.message;
        }
    } catch (error) {
        console.error('Error:', error);
    }
});

document.getElementById('registerForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    try {
        const response = await fetch('/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });
        if (response.ok) {
            window.location.href = '/login';
        } else {
            const data = await response.json();
            document.getElementById('message').textContent = data.message;
        }
    } catch (error) {
        console.error('Error:', error);
    }
});
