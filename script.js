// Navbar Toggle
const toggleBtn = document.querySelector(".navbar-toggler");
const navbarCollapse = document.querySelector(".navbar-collapse");

toggleBtn.addEventListener("click", () => {
    navbarCollapse.classList.toggle("show");
});

// Dropdown Toggle
const dropdownToggle = document.querySelector(".dropdown-toggle");
const dropdownMenu = document.querySelector(".dropdown-menu");

dropdownToggle.addEventListener("click", (e) => {
    e.preventDefault();
    dropdownMenu.classList.toggle("show");
});

// Close dropdown when clicking outside
document.addEventListener("click", (e) => {
    if (
        !dropdownToggle.contains(e.target) &&
        !dropdownMenu.contains(e.target)
    ) {
        dropdownMenu.classList.remove("show");
    }
});

// Search Form
const searchForm = document.querySelector("form");
const searchInput = document.querySelector(".form-control");

searchForm.addEventListener("submit", (e) => {
    e.preventDefault();

    const query = searchInput.value.trim();

    if (query !== "") {
        alert(`Searching for: ${query}`);
        searchInput.value = "";
    } else {
        alert("Please enter something to search.");
    }
});