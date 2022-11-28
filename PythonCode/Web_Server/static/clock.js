function TimeRender() {

    var currentDate = new Date(); 
    var month = currentDate.getMonth(); 
    
    var currentTime = new Date(); 
    var hour = currentTime.getHours(); 
    var minutes = currentTime.getMinutes(); 
    var sec = currentTime.getSeconds(); 
  
    if(hour > 12)
    {
        hour-=12;
    }

    if(sec < 10)
    {
        sec = "0"+ sec; 
    }
    if(minutes < 10)
    {
        minutes = "0"+ minutes; 
    }


    var clock = document.getElementById("clockDisplay");
    clock.textContent = hour + minutes + sec; 
    clock.innerText = hour +":"+ minutes+ ":" + sec; 
    setTimeout("TimeRender()",1000);
  }
  TimeRender();