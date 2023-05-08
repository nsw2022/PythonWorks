window.onload=function(){
    const clock = document.querySelector('#time');
    function getTime(){
//        const time = new Date();
//        const hour = time.getHours();
//        const minutes = time.getMinutes();
//        const seconds = time.getSeconds();
//        clock.innerHTML = hour +":" + minutes + ":"+seconds;
        let date = new Date()
        let now = date.toLocaleTimeString();  // 시간 형식
        document.querySelector('#time').innerHTML = now
    }
    function init(){
        setInterval(getTime, 1000);
    }
    init();
}
