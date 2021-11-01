function send(form){
	//https://www.car.gov.br/#/consultar/

	let numbCar = form.numbCar.value;
	//let action = form.action = 'https://www.car.gov.br/#/consultar/' + numbCar;
	window.open('https://www.car.gov.br/#/consultar/' + numbCar, '_blank');

}