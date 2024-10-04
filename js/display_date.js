let da = new Date();
dayy = da.getUTCDay();
switch(dayy){
    case 0:
        console.log("Monday");
        break;
    case 1:
        console.log("Tuesday");
        break;
    case 2:
        console.log("Wednesday");
        break;
    case 3:
        console.log("Thursday");
        break;
    case 4:
        console.log("Friday");
        break;
    case 5:
        console.log("Saturday");
        break;
    case 6:
        console.log("Sunday");
        break;
    default:
        console.log("Error");
        break;

}

const weekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];

console.log("Current Date: " + da);

console.log("Weekday: "+weekDays[da.getUTCDay()])
console.log("Time: "+ da.getHours()+":"+da.getMinutes()+":"+da.getSeconds())
