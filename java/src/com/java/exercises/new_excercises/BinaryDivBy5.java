package com.java.exercises.new_excercises;

import java.util.List;
import java.util.ArrayList;

public class BinaryDivBy5 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		divBy5("0100,0011,1010,1001,1100,1001");
	}
	public static void divBy5(String a) {
		String con = "";
		int counter = 0;
		List<String> hold  = new ArrayList<String>();
		for(int i=0; i<a.length(); i++) {
			if(counter <= 3) {
				con += a.charAt(i);
				counter++;
				if(counter==4) {
					int num1 = Integer.parseInt(con, 2);
					if(num1%5==0) {
						hold.add(con);
					}
				}
					
			}else {
				counter = 0;
				con = "";
			}
		}
		
		System.out.println(hold);
	}

}
