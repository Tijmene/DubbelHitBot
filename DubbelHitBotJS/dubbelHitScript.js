window.value = true;

function checkDubbelHit(temp1, temp2){
	var artist1 = temp1.innerText;
	var artist2 = temp2.innerText;

	console.log(artist1);
	console.log(artist2);

	if (artist1 == artist2 && window.value)
	{
		console.log("TRIGGERED")
		console.log("Global value set to False")
        window.value= false;  
		window.open("http://localhost:5000/DubbelHit");
	}
	if (artist1 != artist2) {
		window.value = true
		console.log("Global value set to True")
	}
}

setInterval(function() {checkDubbelHit(temp1, temp2);}, 100000 * Math.random());



