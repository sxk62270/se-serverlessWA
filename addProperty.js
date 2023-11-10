const resource_url =
  "https://vkkm38khe4.execute-api.us-east-1.amazonaws.com/dev/property";
const form = document.getElementById("create-property-form");
form.addEventListener("submit", (e) => {
  e.preventDefault();
  const formData = new FormData(form);
  // print the form values
  //for (var i of formData.entries()) {
  //  console.log(i[0] + ", " + i[1]);
  //}
  /**
   * We can't pass the `FormData` instance directly to `fetch`
   * as that will cause it to automatically format the request
   * body as "multipart" and set the `Content-Type` request header
   * to `multipart/form-data`. We want to send the request body
   * as JSON, so we're converting it to a plain object and then
   * into a JSON string.
   *
   * @see https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST
   * @see https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/fromEntries
   * @see https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify
   */
  const plainFormData = Object.fromEntries(formData.entries());
  const fetchOptions = {
    method: "POST",
    mode: "cors",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(plainFormData),
  };
  fetch(resource_url, fetchOptions);
  form.reset();
});