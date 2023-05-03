window.onload=function(){
    const clock = document.querySelector('#time');
    function getTime(){
        const time = new Date();
        const hour = time.getHours();
        const minutes = time.getMinutes();
        const seconds = time.getSeconds();
        clock.innerHTML = hour +":" + minutes + ":"+seconds;
    }
    function init(){
        setInterval(getTime, 1000);
    }
    init();
}
