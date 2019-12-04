const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});

document.getElementById("LOGIN").style.display = "block";
document.getElementById("SIGNUP").style.display = "block";


function cambiarASignUp() {
	document.getElementById("LOGIN").style.display = "none";
	document.getElementById("SIGNUP").style.display = "block";
}

function cambiarALogin() {
	document.getElementById("SIGNUP").style.display = "none";
	document.getElementById("LOGIN").style.display = "block";
}

