let result = arguments[arguments.length - 1];

wait_for_dom(() => {
    result(
        document.querySelector("#body .pagination ul li:nth-last-child(2) span").getAttribute("pageindex")
    );
});
