//dones't work
$(function(){
  window.twttr = (function(d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0],
      t = window.twttr || {};
    if (d.getElementById(id)) return t;
    js = d.createElement(s);
    js.id = id;
    js.src = "https://platform.twitter.com/widgets.js";
    fjs.parentNode.insertBefore(js, fjs);

    t._e = [];
    t.ready = function(f) {
      t._e.push(f);
    };

    return t;
  }(document, "script", "twitter-wjs"));

  //init twitter
  twttr.widgets.load()

  $.getJSON("http://kdmg.popowa.com/output_2.json", function(data){
    for(var i in data){
        $( ".grid" ).append( "<div class=\"grid-item\" id=\"king-" + i + "\"></div>");
      twttr.widgets.createTweet(
        data[i].url,
        document.getElementById("king-"+i),
        {conversation: 'none',dnt: 'true'}
      );
    }
  });
  twttr.ready(function (twttr) {
    twttr.events.bind('loaded', function (event) {
      var $grid = $('.grid').masonry({
        itemSelector: '.grid-item',
        columnWidth: '.grid-sizer',
        percentPosition: true,
        isFitWidth: true
      });

    });
  });
});//function
