var y0 = {a};
var y1 = {b};


var trace1 = {
  y: y0,
  type: 'box'
};

var trace2 = {
  y: y1,
  type: 'box'
};

var data = [trace1, trace2];

Plotly.newPlot('boxChart', data);

