const model = document.getElementById('main2');
const open = document.getElementById('upload-text');
const field = document.getElementById('input-post')
const btn = document.getElementById('submit-post-id');
let windowsContainer = document.getElementById('windows-container');
const userContentH = document.getElementById('user-content');
let audioVideo = document.getElementById('videoId')

// window.onload = function(){
//    windowsContainer.style.height = userContentH.offsetHeight  + 650 + 'px'
// }

open.addEventListener('click', () => {
    model.classList.replace('main2', 'show12345');

});

function myFunction() {
    model.classList.replace('show12345', 'main2')
}

let b = document.querySelector('button');
setTimeout(() => b.focus(), 100);
setTimeout(() => b.blur(), 1000);

$("video").click(function(e){

        // get click position
        var clickY = (e.pageY - $(this).offset().top);
        var height = parseFloat( $(this).height() );

        // avoids interference with controls
        if(y > 0.82*height) return;

        // toggles play / pause
        this.paused ? this.play() : this.pause();

    });


// const video = document.querySelector("video");
// let playState = null;

// const observer = new IntersectionObserver((entries) => {
//   entries.forEach((entry) => {
//     if (!entry.isIntersecting) {
//       video.pause();
//       playState = false;
//     } else {
//       video.play();
//       playState = true;
//     }
//   });
// }, {});
//
// observer.observe(video);
//
// const onVisibilityChange = () => {
//   if (document.hidden || !playState) {
//     video.pause();
//   } else {
//     video.play();
//   }
// };
//
// document.addEventListener("visibilitychange", onVisibilityChange);

