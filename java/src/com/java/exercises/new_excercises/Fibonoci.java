package com.java.exercises.new_excercises;

import java.util.List;
import java.util.ArrayList;

public class Fibonoci {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		List<Integer> arr = fibSer();
		System.out.println(arr);
	}
	public static List<Integer> fibSer(){
		List<Integer> fibArr = new ArrayList<Integer>();
		int fib = 0;
		int fibTemp = 0;
		int fibPre = 0;
		while(fib<50) {
			if(fib == 0) {
				fib = 1;
				fibTemp = 0;
				fibPre = 0;
				fibArr.add(0);
				fibArr.add(fib);
			}else if(fib !=0) {
				fibTemp = fib;
				fib = fib + fibPre;
				fibPre = fibTemp;
				if(fib < 50) {
					fibArr.add(fib);
				}
			}
		}
		
		return fibArr;
	}

}
