function random_bg_color() {
    const arr = ["red","blue","green"]
    const x = Math.floor(Math.random() * 3);
    const bgColor = arr[x]
    console.log(bgColor);
    document.body.style.background = bgColor;
    
}

random_bg_color();