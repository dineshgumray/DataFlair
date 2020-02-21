// connecting talk and content html and js part
const btn = document.querySelector('.talk');
const content = document.querySelector('.content');

// for craeting the required tags..
const greetings = ['Hi guys', 'Helo', 'Musi Musi'];
//

// creating SpeechRecognition object.
const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = new SpeechRecognition();

// add listener to the btn
btn.addEventListener('click',() => {
    recognition.start();
});

// for starting the mic.
recognition.onstart = function(){
    console.log('Voice is activated, you can speak now');
    const speech = new SpeechSynthesisUtterance();
    speech.text = 'Voice is activated, would you like to call Daisy';
    window.speechSynthesis.speak(speech);
};

// to speak with bot.
recognition.onresult = function(event){
    // console.log(event);
    const current = event.resultIndex;
    const transcript = event.results[current][0].transcript;

    // to show what user speak on webpage.
    // content.textContent = transcript;
    readOutLoad(transcript);

};

// to listen the bot speak.
function readOutLoad(message){

    const speech = new SpeechSynthesisUtterance();

    speech.text = "I don't know what you said.";

    var voices = window.speechSynthesis.getVoices();

     console.log(voices);
    // to change voice to female.
    if(message.includes("yes")){
        speech.voice = voices[4];
        speech.text = "Hi Dinesh";
    }
    
    // to get random message from our given options.
    else if(message.includes("how are you")){

        const finalText = greetings[Math.floor(Math.random()*greetings.length)];
        speech.text = finalText;
    };

    speech.volume = 1;
    speech.rate = 1;
    speech.pitch = 1; 

    // to listen to the voice on webpage
    window.speechSynthesis.speak(speech);
}