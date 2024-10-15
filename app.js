// Cargar los datos desde el archivo CSV
d3.csv("data.csv").then(function(data) {
  
    // Convertir precios a números
    data.forEach(function(d) {
      d.Precio = +d.Precio.replace(/[^\d]/g, '');  // Quitar símbolos y convertir a número
    });
  
    // Crear escalas para el gráfico de barras
    var width = 800, height = 400;
    var margin = {top: 20, right: 20, bottom: 50, left: 50};
  
    var x = d3.scaleBand()
      .domain(data.map(function(d) { return d.Ubicación; }))
      .range([margin.left, width - margin.right])
      .padding(0.1);
  
    var y = d3.scaleLinear()
      .domain([0, d3.max(data, function(d) { return d.Precio; })])
      .nice()
      .range([height - margin.bottom, margin.top]);
  
    // Crear el SVG para el gráfico de barras
    var svgBarras = d3.select("#barras").append("svg")
      .attr("width", width)
      .attr("height", height);
  
    // Agregar barras al gráfico
    svgBarras.selectAll(".bar")
      .data(data)
      .enter().append("rect")
      .attr("class", "bar")
      .attr("x", function(d) { return x(d.Ubicación); })
      .attr("y", function(d) { return y(d.Precio); })
      .attr("height", function(d) { return y(0) - y(d.Precio); })
      .attr("width", x.bandwidth())
      .attr("fill", "steelblue");
  
    // Agregar ejes
    svgBarras.append("g")
      .attr("transform", `translate(0,${height - margin.bottom})`)
      .call(d3.axisBottom(x))
      .selectAll("text")
      .attr("transform", "rotate(-45)")
      .style("text-anchor", "end");
  
    svgBarras.append("g")
      .attr("transform", `translate(${margin.left},0)`)
      .call(d3.axisLeft(y));
  
    
  
  });
  