function area_triangle_sss(a=0, b=0, c=0){
    let s = (a + b + c)/2
    let s_outof_srt = s*(s-a)*(s-b)*(s-c);
    let area = Math.sqrt(s_outof_srt)
    return area
}

console.log(area_triangle_sss(5, 6, 7));