$(document).ready(function () {
	const url = "https://fourtonfish.com/hellosalut/?lang=fr"
	$.getJSON(url, function (response) {
		console.log(response.hello)
		$("#hello").append(response.hello);
	});
});
