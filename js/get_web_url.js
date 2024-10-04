// alert(window.location.href);
// alert(document.URL);

// let var_name = 'abcd';

// let n = 120;

// this[var_name] = n;

// console.log(this[var_name]);

function getFileExtention(string_val){
    extention = string_val.split('.').at(-1);
    console.log(extention);
}

getFileExtention("text.js");