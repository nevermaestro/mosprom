const button1 = document.getElementById("click");
function handleClick(){
    document.getElementById("chart").textContent = "PLEASE NO";
}

const apiUrl = 'http://127.0.0.1:5000/api/orgs';

usefulArrayNames = [];
usefulArrayRevenue = [];
async function fetchData() {
    try {
        const response = await fetch(apiUrl);
        
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        
        const data = await response.json();
        
        if (!data.orgs || data.orgs.length === 0) {
            throw new Error("No organizations found in the data.");
        }

        data.orgs.forEach(element => {
            usefulArrayNames.push(element.Название);
            usefulArrayRevenue.push(element.Выручка);
        });
    } catch (error) {
        console.error('There was a problem with your fetch operation:', error);
    }
}
async function initChart() {
    // Show loading message
    document.getElementById('loading').style.display = 'block'; 

    // Fetch data
    await fetchData(); 

    // Hide loading message and show chart canvas only if data is available
    if (usefulArrayNames.length > 0 && usefulArrayRevenue.length > 0) {
        document.getElementById('loading').style.display = 'none';
        document.getElementById('myChart').style.display = 'block';

        const ctx = document.getElementById('myChart').getContext('2d');
        
        const myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: usefulArrayNames, // Use fetched names
                datasets: [{
                    label: 'Revenue',
                    data: usefulArrayRevenue, // Use fetched revenue
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        // Add more colors as needed
                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        // Add more colors as needed
                    ],
                    borderWidth: 1,
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    } else {
        document.getElementById('loading').innerText = "No data available.";
    }
}

document.addEventListener('DOMContentLoaded', function () {
    initChart(); // Call the function to initialize the chart
});