function rotate_string(string_val){
  let newString = string_val.at(-1);
  let len = string_val.length;
  //newString = newString + string_val.substring(0,len-1);
  newString = newString + string_val.slice(0, len-1);
  
  return newString;
}

// let rot = "Tinsae";
// for(let i=0; i<6; i++){
//     rot = rotate_string(rot);
//     console.log(rot);
// }


function add_Py(string_val){
    begin_str = string_val.slice(0,2);
    return begin_str === "Py" ? string_val : "Py" + string_val;
}

// console.log(add_Py("Python"));
// console.log(add_Py("thon"));


function string_remove_char(string_val, position){
    let new_string = string_val.slice(0,position) + string_val.slice(position+1);
    return new_string;
}

// console.log(string_remove_char("Tinsae", 3));

function swap_first_and_last_char(string_val){
    first_string = string_val.at(0).toLowerCase();
    last_string = string_val.at(-1).toUpperCase();    
    middle_Str = string_val.slice(1, -1)

    return last_string + middle_Str + first_string;
}

// console.log(swap_first_and_last_char("T"));


const remove_script_in_4th_index = function(string_val){
    // let str_position = string_val.indexOf("Script");
    let str_position = string_val.search(/Script/i)

    if(str_position === 4){
        let new_string = string_val.slice(0, 4) + string_val.slice(10);
        return new_string;
    }else{
        return string_val;
    }
    
}

// console.log(remove_script_in_4th_index("JavaScript"));
// console.log(remove_script_in_4th_index("JavaNoScript"));
// console.log(remove_script_in_4th_index("JavaScriptIsAwesome"));


const reverse_String = function(string_val){
    // let reversed = ""
    // for(st of string_val){
    //     reversed = st + reversed;
    // }

    const reversed = [...string_val].reverse().join("");
    return reversed;    
}

// console.log(reverse_String("Tinsae"));

// console.log(String.fromCharCode("Tin".charCodeAt(0)+1));

const next_letter = function(string_val){
    let str_arr = ""
    let str_len = string_val.length;
    for(let i=0; i<str_len; i++){
        let z_check = string_val.at(i)

        switch(z_check){
            case 'Z':
                str_arr += 'A';
                break;
            case 'z':
                str_arr += 'a';
                break;
            case ' ':
                break;
            default:
                str_arr += String.fromCharCode(string_val.charCodeAt(i) +1);

        }
        
    }
    return str_arr;
}


// console.log(next_letter("Zython"));


function capitalize_first_letters (string_val){
    const str_arr = string_val.split(' ');
    let new_word = "";
    for(str of str_arr){
        new_word += str.at().toUpperCase() + str.slice(1) + " ";
    }
    
    return new_word;
}


console.log(capitalize_first_letters("tinsae getachew"));


