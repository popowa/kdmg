//https://qiita.com/kouh/items/dfc14d25ccb4e50afe89
//http://www.webdesignleaves.com/wp/jquery/1340/
//var fs = require('fs');
//var twitter = JSON.parse(fs.readFileSync('./output.json', 'utf8'));
// vanilla JS
// init with element
var grid = document.querySelector('.grid');
var msnry = new Masonry( grid, {
  // options...
  itemSelector: '.grid-item',
  columnWidth: 200
});

// init with selector
var msnry = new Masonry( '.grid', {
  // options...
});
