// wait_for_elem("#change-hide-solved-status");

// return document.querySelector("#change-hide-solved-status");

wait_for_dom(() => {
    if (!document.getElementById("change-hide-solved-status").checked) {

        create_dummy_element();

        document.getElementById("change-hide-solved-status").click();
    }
});
