let search = document.querySelector("#search");
console.log(search);
let icon = document.querySelector("#search-icon");

icon.onclick = () => {
  search.classList.toggle("active");
  search.focus();
};
