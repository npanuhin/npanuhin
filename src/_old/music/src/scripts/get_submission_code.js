let result = arguments[arguments.length - 1];

wait_for_dom(() => {
    result(document.getElementById("program-source-text").innerText);
});
