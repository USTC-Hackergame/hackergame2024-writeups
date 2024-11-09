// ==UserScript==
// @name         hackergame get secret
// @namespace    http://tampermonkey.net/
// @version      2024-11-05
// @description  noVNC 是吧，通过 dispatchEvent 发一个压缩包过去
// @author       literal
// @match        http://202.38.93.141:12010/
// @icon         none
// @grant        unsafeWindow
// @grant        GM_registerMenuCommand
// ==/UserScript==

(function() {
  'use strict';

  var targetel = null
  function keyboard_input(char){
      targetel.dispatchEvent(new KeyboardEvent('keydown', {key: char}))
      targetel.dispatchEvent(new KeyboardEvent('keyup', {key: char}))
  }


  const payload = `(base64 -d | zstd -d | cpio -i) <<EOF
这里填压缩包内容
EOF
`
  let inject = GM_registerMenuCommand(
      "注入！",
      function () {
          var theframe = document.querySelector('#novnc-iframe')
          targetel = theframe.contentDocument.querySelector('canvas')
          //console.warn(theframe.contentDocument.querySelector)
          //console.warn(theframe.contentDocument.querySelector('canvas'))
          let len = payload.length
          function f(off) {
              if (off >= len) {
                  return
                  // 不知道要怎么玩
                  targetel.dispatchEvent(new KeyboardEvent('keydown', {key: 'Control', ctrlKey: true}))
                  targetel.dispatchEvent(new KeyboardEvent('keydown', {key: 'd', ctrlKey: true}))
                  targetel.dispatchEvent(new KeyboardEvent('keyup', {key: 'Control'}))
                  targetel.dispatchEvent(new KeyboardEvent('keyup', {key: 'd'}))
                  return
              }
              keyboard_input(payload[off])
              setTimeout(f, 2, off+1)
          }
          setTimeout(f, 0, 0)
      },
      "辅助信息"
  )
})();
