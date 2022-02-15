$(document).ready(function () {
	const url = "https://swapi-api.hbtn.io/api/films/?format=json"
	$.getJSON(url, function (response) {
		const movieList = response.results;
		for (movie of movieList) {
			const title = movie.title;
			$("#list_movies").append(`<li>${title}</li>`);
		};
	});
});
