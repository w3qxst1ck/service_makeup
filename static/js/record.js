var recordBtns = document.getElementsByClassName('add-record')


for(var i = 0; i < recordBtns.length; i++){
	recordBtns[i].addEventListener('click', function(){		
		var year = this.dataset.year
		var month = this.dataset.month
		var day = this.dataset.day
		var hour = this.dataset.hour
		var service = this.dataset.service
		console.log('hour: ', hour, 'day: ', day, 'month: ', month, 'year: ', year, 'service: ', service)
		addRecord(year, month, day, hour, service)
	})
}


function addRecord(year, month, day, hour, service){

	var url = '/add_record/'

	fetch(url, {
		method: 'POST',
		headers:{
			'Content-Type': 'application/json',
			'X-CSRFToken': csrftoken,
		},
		body: JSON.stringify({'year': year, 'month': month, 'day': day, 'hour': hour, 'service': service})
	})

	.then((response) => {
		return response.json()
	})

	.then((data) => {
		console.log('data: ', data)
	})
}