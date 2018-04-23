document.addEventListener("DOMContentLoaded", function(event) {
  var table_contents = document.getElementsByTagName('td')
  for (var i = 0; i < table_contents.length; i++) {
      current_node = table_contents.item(i)
      if (current_node.innerText == 1){
        current_node.style.color = "#09d009"
        current_node.innerText = 'Rise'
      } else if (current_node.innerText == 0){
        current_node.style.color = "red"
        current_node.innerText = 'Drop'
      }
  }

  if (document.getElementsByClassName('pred-table').length == 1){
    var company_hour_graph = document.getElementById('company_hour_graph')
    var company_day_graph = document.getElementById('company_day_graph')
    var company_week_graph = document.getElementById('company_week_graph')
    var company_month_graph = document.getElementById('company_month_graph')
    if (location.hash == ''){
      var current_open_graph = company_hour_graph
      company_hour_graph.style.display = "block"
    }else if (location.hash == '#day'){
      var current_open_graph = company_day_graph
      company_day_graph.style.display = "block"
    }else if (location.hash == '#week'){
      var current_open_graph = company_week_graph
      company_week_graph.style.display = "block"
    }else if (location.hash == '#month'){
      var current_open_graph = company_hour_graph
      company_month_graph.style.display = "block"
    }

  }

  window.onhashchange = function() {
       var company_hour_graph = document.getElementById('company_hour_graph')
       var company_day_graph = document.getElementById('company_day_graph')
       var company_week_graph = document.getElementById('company_week_graph')
       var company_month_graph = document.getElementById('company_month_graph')

      if(location.hash == ''){
          company_hour_graph.style.display = "block"
          company_day_graph.style.display = "none"
          company_week_graph.style.display = "none"
          company_month_graph.style.display = "none"
       }else if (location.hash == '#day'){
         company_hour_graph.style.display = "none"
         company_day_graph.style.display = "block"
         company_week_graph.style.display = "none"
         company_month_graph.style.display = "none"
       }else if (location.hash == '#week'){
         company_hour_graph.style.display = "none"
         company_day_graph.style.display = "none"
         company_week_graph.style.display = "block"
         company_month_graph.style.display = "none"
       }else if (location.hash == '#month'){
         company_hour_graph.style.display = "none"
         company_day_graph.style.display = "none"
         company_week_graph.style.display = "none"
         company_month_graph.style.display = "block"
       }
  }


});
