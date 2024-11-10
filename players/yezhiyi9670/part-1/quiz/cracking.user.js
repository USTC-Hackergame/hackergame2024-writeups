// ==UserScript==
// @name        Hackergame 2024 Quiz [cracking]
// @namespace   Hackergame 2024
// @require     https://cdn.jsdelivr.net/npm/jquery@3.2.1/dist/jquery.min.js
// @match       http://202.38.93.141:13030/*
// ==/UserScript==

"use strict";

$(() => {
  // RESET use this: localStorage.setItem('crack-index', '0')

  let unpass_str = '本次测验总得分为 0'
  let genDateList = () => {
    let ret = []
    for(let i = 1500; i < 2200; i++) {
      ret.push('' + i)
    }
    return ret
  }
  let trialData = genDateList()
  let $typebox = $('input[name=q6]')

  let isPassed = $('.alert-secondary').text().indexOf(unpass_str) == -1
  let currIndex = +localStorage.getItem('crack-index')

  if(isPassed) {
    alert('Something nontrivial!!1')
    return
  }

  if(currIndex >= trialData.length) {
    alert('nmsl')
    return
  }

  let nextData = trialData[currIndex]
  console.log("Let's try", nextData)
  currIndex += 1
  $typebox.val(nextData)
  localStorage.setItem('crack-index', currIndex.toString())

  setTimeout(() => {
    $('input[type=submit]').trigger('click')
  }, 400)
})
