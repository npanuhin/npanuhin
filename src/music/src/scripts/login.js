let username = arguments[0];
let password = arguments[1];

// create_dummy_element();

// wait_for_elem("#handleOrEmail")
// wait_for_elem("#password")
// wait_for_elem("#remember")
// wait_for_elem("#enterForm")

wait_for_dom(() => {
    wait_for_elem("#passp-field-login");

    document.getElementById("passp-field-login").value = username;

    wait_for_elem("#passp\\:sign-in");

    document.getElementById("passp:sign-in").click();

    wait_for_elem("#passp-field-passwd");

    document.getElementById("passp-field-passwd").value = password;

    wait_for_elem("#passp\\:sign-in");

    document.getElementById("passp:sign-in").click();
});
