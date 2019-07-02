$(function(){
  var output = "<div class='row'>";
  $.getJSON("https://popowa.github.io/kdmg/output.json", function(data){
      for(var i=0;i < data.length;i++){
         if((i%3)==0) {
            output += "</div><div class='row'>" + "<div class='col-sm-3'>" + data[i].html + "</div>";
         } else {
            output += "<div class='col-sm-3'>" + data[i].html + "</div>";
         }
      }
      output += "</div>";
    $('.main').append(output);
    });
});
