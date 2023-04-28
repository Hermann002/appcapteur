const ctx = document.getElementById('myChart');

new Chart(ctx, {
  type: 'scatter',
  data: {
    labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
    datasets: [{
        label: 'Scatter Dataset',
        data: [{
          x: -10,
          y: 0
        }, {
          x: 0,
          y: 10
        }, {
          x: 10,
          y: 5
        }, {
          x: 0.5,
          y: 5.5
        }],
        backgroundColor: 'rgb(255, 99, 132)'
    }],
  },
  options: {
    scales: {
      y: {
        beginAtZero: true
      }
    }
  }
});

