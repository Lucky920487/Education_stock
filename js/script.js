document.querySelectorAll(".auth-box form").forEach((form) => {
  form.addEventListener("submit", (e) => {
    e.preventDefault();
    alert("Form submitted!");
  });
});