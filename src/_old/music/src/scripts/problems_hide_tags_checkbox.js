// wait_for_elem("#change-hide-tag-status");

wait_for_dom(() => {
    if (document.getElementById("change-hide-tag-status").checked) {

        create_dummy_element();

        document.getElementById("change-hide-tag-status").click();
    }
});
