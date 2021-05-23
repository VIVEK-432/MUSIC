function Fame(){
  var greeting;
  var time = new Date().getHours();


  if(time<10){
    greeting="Good @"
  }else if (time < 20) {
    greeting="$ morning";
  }
  else {
    greeting="Evening #";
  }
  document.getElementById("game").innerHTML=greeting;
}
