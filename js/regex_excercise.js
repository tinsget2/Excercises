const test_begining  = function(string_val, test_str){
    let searchPattern  = new RegExp('^' + test_str, 'i'); // = /^Java/i
    return searchPattern.test(string_val)
}


console.log(test_begining("Savascript", "Java"));