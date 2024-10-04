let num = Math.floor(Math.random() * 11) + 1;

var gnum = parseInt(prompt('Guess the number between 1 and 10 inclusive'));

if(gnum === num){
    alert("Mathed");
}else{
    alert("Not Mached the number is "+ num);
}
