// TrailMate Main JavaScript

// Initialize the map on the home page
document.addEventListener('DOMContentLoaded', function() {
    // Check if map container exists on the page
    const mapContainer = document.getElementById('map-container');
    if (mapContainer) {
        initializeMap();
    }
});

// Initialize the interactive map
function initializeMap() {
    // Create the map
    const map = L.map('map-container').setView([12.8797, 121.7740], 6);
    
    // Add the OpenStreetMap tile layer
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);
    
    // Fetch mountain data from the API
    fetch('/mountains/data/')
        .then(response => response.json())
        .then(mountains => {
            // Add markers for each mountain
            mountains.forEach(mountain => {
                const marker = L.marker([mountain.latitude, mountain.longitude])
                    .addTo(map)
                    .bindPopup(`
                        <strong>${mountain.name}</strong><br>
                        Elevation: ${mountain.elevation}m<br>
                        Difficulty: ${mountain.difficulty}<br>
                        <a href="/mountains/${mountain.id}/" class="btn btn-sm btn-primary mt-2">View Details</a>
                    `);
                
                // Add click event to show mountain details in sidebar
                marker.on('click', function() {
                    showMountainDetails(mountain.id);
                });
            });
        })
        .catch(error => console.error('Error fetching mountain data:', error));
    
    // Add search control
    const searchControl = document.getElementById('map-search');
    if (searchControl) {
        searchControl.addEventListener('submit', function(e) {
            e.preventDefault();
            const query = document.getElementById('search-query').value;
            searchMountains(query, map);
        });
    }
}

// Show mountain details in the sidebar
function showMountainDetails(mountainId) {
    const sidebar = document.getElementById('map-sidebar');
    if (!sidebar) return;
    
    // Show loading state
    sidebar.innerHTML = '<div class="text-center"><div class="spinner-border text-primary" role="status"></div><p>Loading mountain details...</p></div>';
    
    // Fetch mountain details
    fetch(`/mountains/${mountainId}/`)
        .then(response => response.text())
        .then(html => {
            // Extract the relevant part of the HTML response
            const parser = new DOMParser();
            const doc = parser.parseFromString(html, 'text/html');
            const mountainDetails = doc.querySelector('.mountain-details');
            
            if (mountainDetails) {
                sidebar.innerHTML = '';
                sidebar.appendChild(mountainDetails);
            } else {
                sidebar.innerHTML = `
                    <div class="alert alert-info">
                        <h5>Mountain Information</h5>
                        <p>Click on a mountain marker to view details, or <a href="/mountains/${mountainId}/">view the full page</a>.</p>
                    </div>
                `;
            }
        })
        .catch(error => {
            console.error('Error fetching mountain details:', error);
            sidebar.innerHTML = `
                <div class="alert alert-danger">
                    <h5>Error</h5>
                    <p>Could not load mountain details. Please try again or <a href="/mountains/${mountainId}/">view the full page</a>.</p>
                </div>
            `;
        });
}

// Search mountains on the map
function searchMountains(query, map) {
    if (!query) return;
    
    fetch(`/mountains/search/?q=${encodeURIComponent(query)}`)
        .then(response => response.json())
        .then(results => {
            if (results.length > 0) {
                // Center map on first result
                map.setView([results[0].latitude, results[0].longitude], 10);
                
                // Highlight the result
                L.popup()
                    .setLatLng([results[0].latitude, results[0].longitude])
                    .setContent(`
                        <strong>${results[0].name}</strong><br>
                        Found ${results.length} mountains matching "${query}"<br>
                        <a href="/mountains/search/?q=${encodeURIComponent(query)}">View all results</a>
                    `)
                    .openOn(map);
            } else {
                alert(`No mountains found matching "${query}"`);
            }
        })
        .catch(error => console.error('Error searching mountains:', error));
}

// Handle star rating in review form
document.addEventListener('DOMContentLoaded', function() {
    const ratingInputs = document.querySelectorAll('.rating-input');
    const ratingStars = document.querySelectorAll('.rating-star');
    
    if (ratingStars.length > 0) {
        ratingStars.forEach(star => {
            star.addEventListener('click', function() {
                const value = this.getAttribute('data-value');
                
                // Update hidden input
                ratingInputs.forEach(input => {
                    input.value = value;
                });
                
                // Update star display
                ratingStars.forEach(s => {
                    if (s.getAttribute('data-value') <= value) {
                        s.classList.add('active');
                    } else {
                        s.classList.remove('active');
                    }
                });
            });
        });
    }
});

// Toggle mobile navigation
document.addEventListener('DOMContentLoaded', function() {
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');
    
    if (navbarToggler && navbarCollapse) {
        navbarToggler.addEventListener('click', function() {
            navbarCollapse.classList.toggle('show');
        });
    }
});