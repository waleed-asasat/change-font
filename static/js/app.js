odoo.define("ChangeFont.ChangeFont", function(require){
  "use strict";

  var ajax = require('web.ajax')

  ajax.jsonRpc('/font/selected', 'call')
    .then(function(result) {
        var style = document.createElement("style");

        var encoded = result.split(' ').join('+')

         style.innerHTML = `
           @import url('https://fonts.googleapis.com/css2?family=${encoded}&display=swap');

           body {
              font-family: '${result}', sans-serif;
           }
         `

        document.head.appendChild(style);
    })
})