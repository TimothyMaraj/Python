//************************************************/
/*                                                  
// The following uses the Date and Time Lib heavily
// here is the link for the following lib page to learn more 
// about the functions and everything else used
// https://javascript.info/date
//                  
/*
//************************************************/

function time() {

    var currentDate = new Date(); 
    var month = currentDate.getMonth(); 
    var day = currentDate.getDate();
    var year = currentDate.getFullYear();
    
    var currentTime = new Date(); 
    var hour = currentTime.getHours(); 
    var minutes = currentTime.getMinutes(); 
    var sec = currentTime.getSeconds(); 
  
    if(hour > 12 && hour!== 12)
    {
        hour-=12;
        
    }
    else if(hour<=0)
    {
        hour = 12; 
    }
    if(sec < 10)
    {
        sec = "0"+ sec; 
    }
    if(minutes < 10)
    {
        minutes = "0"+ minutes; 
    }
    if(month <= 11)
    {
        month+=1;
    }



    var clock = document.getElementById("current_time");
    clock.textContent = hour + minutes + sec; 
    clock.innerText = "Date/Time:" + month  + "/" + day + "/" + year + " "+ hour +":"+ minutes+ ":" + sec; 
    setTimeout("time()",1000);
  }
  time();