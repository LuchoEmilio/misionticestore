google.charts.load("current", { packages : [ 'corechart' ]});
 
google.charts.setOnLoadCallback(drawChart);
function drawChart() {
     
    //Aquí se representa el nombre de columna, el dato y el color
    var data = google.visualization.arrayToDataTable([ 
                [ "Element", "Euros", { role : "style"} ], 
                [ "2014", 12820756, "pink" ], 
                [ "2015", 13171807, "silver" ],
                [ "2016", 13259769, "gold" ],
                [ "2017", 14063444, "blue" ],
                [ "2018", 14945692, "green" ],]);
 
    var view = new google.visualization.DataView(data);
    view.setColumns(
        [ 0, 1, {
            calc : "stringify",
            sourceColumn : 1,
            type : "string",
            role : "annotation"
        }, 2 ]);
 
    //Aquí se añade el título y tamaño del gráfico
    var options = {
        title : "Gastos internos en I+D en Euros.",
        width : 600,
        height : 300,
        bar : { groupWidth : "95%" },
        legend : { position : "none" },
    };
     
    var chart = new google.visualization.ColumnChart(document.getElementById("columnchart_values"));
    chart.draw(view, options);
}
 
function getValueAt(column, dataTable, row) {
    return dataTable.getFormattedValue(row, column);
}