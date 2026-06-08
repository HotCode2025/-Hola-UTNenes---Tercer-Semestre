const username = document.getElementById('username');
const password = document.getElementById('password');
const form = document.getElementById('loginForm');

if (form) {
    form.addEventListener('submit', e => {
        e.preventDefault();

        if (username.value === '' || password.value === '') {
            alert('Completa los campos');
            return;
        }

        window.location.href = `login.html?username=${username.value}`;
    });
}

const signUpBtn = document.getElementById('sign');
const forgetBtn = document.getElementById('forget');

signUpBtn.addEventListener('click', e => {
        e.preventDefault();
        alert('YOU ARE SIGNING UP');

    });


forgetBtn.addEventListener('click', e => {
        e.preventDefault();
        alert('TRY NOT TO FORGET THIS, ITS IMPORTANT!');
    });




