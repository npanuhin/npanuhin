function create_dummy_element() {
    cf_dummy_element = document.createElement("div");
    cf_dummy_element.id = "cf_dummy_element";
    document.body.append(cf_dummy_element);

    wait_for_elem("#cf_dummy_element");
}
