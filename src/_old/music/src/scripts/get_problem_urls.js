let result = arguments[arguments.length - 1];

wait_for_dom(() => {
    let urls = [];
    document.querySelectorAll("#pageContent table.problems tr > td:nth-child(2) > div:first-child > a").forEach((elem) => {
        urls.push(elem.href);
    });

    result(urls);
});
