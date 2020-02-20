// Load the model with this optional parameter.
const modelParams = {
    flipHorizontal: true,   // flip e.g for video 
    imageScaleFactor: 0.7,  // reduce input image size for gains in speed.
    maxNumBoxes: 20,        // maximum number of boxes to detect
    iouThreshold: 0.5,      // ioU threshold for non-max suppression
    scoreThreshold: 0.79,    // confidence threshold for predictions.
  }
 
// to detect navigator media for a given browser. 
navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia;

// loading required fields to html page.
const video = document.querySelector("#video");
const audio = document.querySelector("#audio");
const canvas = document.querySelector("#canvas");
const context = canvas.getContext('2d');
let model;

// to start the vedio
handTrack.startVideo(video)
    .then(status => {
        if (status){
            navigator.getUserMedia({video:{}}, stream => {
                video.srcObject = stream;
                // setInterval(runDetection,1000);
                runDetection();
        },
        err => console.log(err)
        );
    }
})

// fun() to detect the hand
function runDetection(){
    model.detect(video)
        .then(predictions=>{
            console.log(predictions);
            if(predictions.length > 0){
                // for playing audio sound if hand is detected on screen.
                //audio.play();
            }
            requestAnimationFrame(runDetection);
            // model.renderPredictions(predictions, canvas, context, video);
    });
}

// for loading the handtrack opensource model.
handTrack.load(modelParams).then(lmodel => {
    model = lmodel;
})