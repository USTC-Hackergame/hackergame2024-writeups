// ==UserScript==
// @name        Hackergame 2024 ComparingMaster [auto-script]
// @namespace   Hackergame 2024
// @require     https://cdn.jsdelivr.net/npm/jquery@3.2.1/dist/jquery.min.js
// @match       http://202.38.93.141:12122/*
// ==/UserScript==

"use strict";

;(() => {
  let setTimeout_1 = window.setTimeout
  window.setTimeout = function() {
    if(arguments[1] == 200) {
      arguments[1] = 10
    }
    setTimeout_1.apply(this, arguments)
  }
})()

$(() => {
  setInterval(() => {
    let v1 = +$('#value1').text()
    let v2 = +$('#value2').text()
    if(v1 < v2) {
      $('#less-than').click()
    } else {
      $('#greater-than').click()
    }
  }, 10)
})
