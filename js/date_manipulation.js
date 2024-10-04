function leap_year(year=1970){
  let div = year % 100 === 0 ? year % 400 === 0 : year % 4 === 0;
  return div;
}

// console.log(leap_year(2016));
// console.log(leap_year(2020));
// console.log(leap_year(1700));
// console.log(leap_year(1800));