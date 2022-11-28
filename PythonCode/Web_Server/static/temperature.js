function render_attemp1() {

    // what is the bandwidth on "real time"
    // the write may take 100ms and then the query to display another 100ms 
    // the check for the current time rounded to the nearest second 5-50ms 
    // then that totals at 250 ms in our best case with a 50ms gap between displays

    // limit the writes! to 6 times a second # gives 2 possible hits: aim for a 1/2 hit ratio

    // our goal is 3 sample changes per seconds: 250ms per display is best case
    // what about the worst? 

    // it takes up to 990ms for display is something around the worst case
    // is a general guess
    // the real worst case /best case would need to be tested for becuz write times may vary 
    // further analysis is required 



    //round out to a certain number of decimal places to make it smooth-> Math.round or .toFixed("num of decimal places")

    // burning buildings can reach these temps: https://sf-fire.org/home-fire-facts#:~:text=In%20only%203%201%2F2,the%20people%20in%20those%20rooms.

    var items = Array(71.9,71.89,71.70,71.90,80.8,85.9,80.2,90.5,90.7,90.6,300.9,360.8,1107.89); 
    var item = items[Math.floor(Math.random()*items.length)];
    var temp_element = document.getElementById("temperature")
    temp_element.innerHTML = "Temperature: " + item.toFixed(2) + " degrees";
    
    if(item <= 300)
    {
        temp_element.style.color = "green";
    }
    else if(item <= 999 && item >=300)
    {
        temp_element.style.color = "orange";
    }
    else if(item >= 1000)
    {
        temp_element.style.color = "red";
    }
    else{
        temp_element.style.color = "black";
    }


  }
 setInterval(render_attemp1,300);

 /*

- ok cool i can get the 3 times per second but what about the super range
  in temperatures? 
  1) can i make a loop that will transition to that value smoothly? 
     what is a balance between accuracy in value and smooth transistion

  2) How the fuck do I make a chart with this data? (LIB?)(Online template?)
             - dial 
             - scatter plot -> line chart, 
             - bar chart seems better that will react to current temp 
        







 */