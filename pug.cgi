#!/usr/bin/node

filename = process.env.PATH_TRANSLATED
console.log("Content-type: text/html")
if(filename === undefined){
  console.log('file not found')
  return 0
}

var pug = require('pug')

try {
  var html = pug.renderFile(filename, {pretty: true})
  console.log(html)
}
catch (err) {
  console.log('')
  console.log('<pre>')
  console.log(err.message)
  console.log('</pre>')
}
