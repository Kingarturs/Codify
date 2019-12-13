const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const logInButton = document.getElementById('login');
const registro = document.getElementById('registro');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});

logInButton.addEventListener('click', () => {

	username = document.getElementById("emailIn").value;
	password = document.getElementById("passwordIn").value;

	$.ajax({
		method: "POST",
		url: "/token-login/",
		data: {
			username: username,
			password: password,
		},
		success: function(data){
			username = data['user'];
			$.ajax({
				method: "POST",
				url: "/index/mkdir",
				data: {
					user:username,
				},
				success: function(data){	
					localStorage.setItem("usuario",username);
				},
				
			});
			window.location = "/index";
		},
		
	});
});

registro.addEventListener('click', () => {

	username = document.getElementById("registroName").value;
	email = document.getElementById("registroEmail").value;
	password = document.getElementById("registroPassword").value;

	$.ajax({
		method: "POST",
		url: "/rest/users/",
		data: {
			username: username,
			email: email,
			password: password,
		},
		success: function(data){
			window.location = "/login";
		},
		
	});

});