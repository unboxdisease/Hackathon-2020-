var b1 = document.querySelector("#book");
var status1 = document.querySelector("#free1");
function func()
{
    var countdown = 40* 60 * 1000;
    b1.disabled = true;
    status1.textContent = "In Use";
    b1.textContent = "booked";
    var timerId = setInterval(function(){
        countdown -= 1000;
        var min = Math.floor(countdown / (60 * 1000));
        //var sec = Math.floor(countdown - (min * 60 * 1000));  // wrong
        var sec = Math.floor((countdown - (min * 60 * 1000)) / 1000);  //correct
      
        if (countdown <= 0) {
            status1.textContent = "Free";
            b1.textContent = "Click to reserve";
           clearInterval(timerId);
           //doSomething();
           b1.disabled = false;
           document.querySelector("#time1").innerHTML = "";
        } else {
            document.querySelector("#time1").innerHTML ="Remaining: " + min + "min " + sec + "sec" ;
        }
      
      }, 1000);
}
b1.addEventListener("click",func);

// ..................button 2


var b2 = document.querySelector(".book1");
// alert(b2);
var status2 = document.querySelector("#free2");
function func1()
{
    var countdown1 = 40* 60 * 1000;
    b2.disabled = true;
    status2.textContent = "In Use";
    b2.textContent = "booked";
    var timerId = setInterval(function(){
        countdown1 -= 1000;
        var min = Math.floor(countdown1 / (60 * 1000));
        //var sec = Math.floor(countdown - (min * 60 * 1000));  // wrong
        var sec = Math.floor((countdown1 - (min * 60 * 1000)) / 1000);  //correct
      
        if (countdown1 <= 0) {
            status2.textContent = "Free";
            b2.textContent = "Click to reserve";
           clearInterval(timerId);
           //doSomething();
           b2.disabled = false;
           document.querySelector("#time2").innerHTML = "";
        } else {
            document.querySelector("#time2").innerHTML ="Remaining: " + min + "min " + sec + "sec" ;
        }
      
      }, 1000);
}
b2.addEventListener("click",func1);
