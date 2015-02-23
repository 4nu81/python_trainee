import random
import time


my_file1 = """<html>
  <head>
    <!--Load the AJAX API-->
    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">

      // Load the Visualization API and the piechart package.
      google.load('visualization', '1.0', {'packages':['corechart']});

      // Set a callback to run when the Google Visualization API is loaded.
      google.setOnLoadCallback(drawChart);

      // Callback that creates and populates a data table,
      // instantiates the pie chart, passes in the data and
      // draws it.
      function drawChart() {

        // Create the data table.
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Number');
        data.addColumn('number', 'Occurances');
        data.addRows([
"""
my_file2 = """
        ]);

        // Set chart options
        var options = {'title':'throw 2 dices 10.000 times',
                       curveType: 'function',
                       'width':800,
                       legend: { position: 'bottom' },
                       'height':600};


        // Instantiate and draw our chart, passing in some options.
        var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
        chart.draw(data, options);
      }
    </script>
  </head>

  <body>
    <!--Div that will hold the pie chart-->
    <div id="chart_div"></div>
  </body>
</html>
"""



l = {}
i = 0
while i < 100000:
    i += 1
    z1 = random.randint(1,6)
    z2 = random.randint(1,6)
    if z1+z2 in l:
        l[z1 + z2] += 1
    else:
        l[z1 + z2] = 1

rows = []
for i in range(2,13):
    if i in l:
        rows.append('          [{key},{value}],'.format(key = '\''+str(i)+'\'', value = l[i]))

result = my_file1 + '\n'.join(rows) + my_file2


f = open('google.html', 'w')
f.write(result)
f.close()

