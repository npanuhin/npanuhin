wait_for_dom(() => {
    document.getElementById("verdictName").value = "OK";

    create_dummy_element();

    document.querySelector("form.status-filter").submit();
});
