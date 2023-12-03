document.addEventListener('DOMContentLoaded', function() {
    loadFilters();
    fetchInternships();

    document.getElementById('apply-filters').addEventListener('click', applyFilter);
});

function loadFilters() {
    fetch('/filters/')
    .then(response => response.json())
    .then(filters => {
        populateFilter('filter-type', filters.types);
        populateFilter('filter-location', filters.locations);
        populateFilter('filter-duration', filters.durations);
    });
}

function fetchInternships(query = '') {
    let url = `/internships/${query ? '?query_text=' + query : ''}`;
    fetch(url)
    .then(response => response.json())
    .then(responseData => {
        const { data, extracted_criteria } = responseData;
        displayInternships(data);
        if (query) {
            updateFilters(extracted_criteria);
        }
    });
}

function populateFilter(filterId, options) {
    const filter = document.getElementById(filterId);
    options.forEach(option => {
        let optionElement = document.createElement('option');
        optionElement.value = option;
        optionElement.textContent = option;
        filter.appendChild(optionElement);
    });
}

function applyFilter() {
    const userQuery = document.getElementById('user-query').value;
    fetchInternships(userQuery);
}

function updateFilters(criteria) {
    if (criteria["Type of Internship"]) {
        document.getElementById('filter-type').value = criteria["Type of Internship"];
    }
    if (criteria["Place"]) {
        document.getElementById('filter-location').value = criteria["Place"];
    }
    if (criteria["Duration"]) {
        document.getElementById('filter-duration').value = criteria["Duration"];
    }
}

function displayInternships(internships) {
    const container = document.getElementById('internships-container');
    container.innerHTML = '';

    internships.forEach(internship => {
        const card = document.createElement('div');
        card.className = 'internship-card';

        Object.entries(internship).forEach(([key, value]) => {
            const div = document.createElement('div');
            div.className = 'card-content';
            div.textContent = `${key}: ${value}`;
            card.appendChild(div);
        });

        container.appendChild(card);
    });
}