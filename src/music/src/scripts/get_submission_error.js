let result = arguments[arguments.length - 1];

wait_for_dom(() => {
	result(
		document.querySelector("#pageContent form.submit-form span.error.for__source").textContent
	);
});
