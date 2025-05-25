let submission_index = arguments[0];
let result = arguments[arguments.length - 1];

wait_for_dom(() => {
    // let submission_id = document.querySelector("#pageContent table.status-frame-datatable tr:not(.first-row) > td:first-child > a");
    let submission_id = document.querySelector(`#pageContent table.status-frame-datatable tr:not(.first-row):nth-child(${submission_index + 2}) > td:first-child > a`);

    if (submission_id === null) {
        result(null);
        return;
    }

    result([
        submission_id.getAttribute("submissionid"),
        // document.querySelector("#pageContent table.status-frame-datatable tr:not(.first-row) > td:nth-child(5)").textContent
        document.querySelector(`#pageContent table.status-frame-datatable tr:not(.first-row):nth-child(${submission_index + 2}) > td:nth-child(5)`).textContent
    ]);
});
