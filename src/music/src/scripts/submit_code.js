let language = arguments[0];
let code = arguments[1];

wait_for_dom(() => {
    let form = document.querySelector("#pageContent form.submit-form");

    let select_elem = form.querySelector("select[name='programTypeId']");

    // Search all select options for the one with the text that matches the language
    for (let option of select_elem.options) {
        if (option.text === language) {
            select_elem.value = option.value;
            break;
        }
    }

    // Toggle editor off
    document.getElementById("toggleEditorCheckbox").checked = true;

    // Set the code
    document.getElementById("sourceCodeTextarea").value = code;

    create_dummy_element();

    // Submit the form
    form.submit();
});
