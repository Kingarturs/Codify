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
	var cambiarColor = document.getElementById("registro");
  	document.getElementById("LOGIN").style.display = "none";
	cambiarColor.classList.add("SIGNUPANIM");
	document.getElementById("SIGNUP").style.display = "block";
}

function cambiarALogin() {
	var cambiarColor = document.getElementById("inicio");
	document.getElementById("SIGNUP").style.display = "none";
	cambiarColor.classList.add("LOGINANIM");
	document.getElementById("LOGIN").style.display = "block";
}

