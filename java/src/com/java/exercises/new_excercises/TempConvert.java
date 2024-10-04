package com.java.exercises.new_excercises;

import java.util.Scanner;

public class TempConvert {
	public static void main(String[] args) {
		try (// TODO Auto-generated method stub\
		Scanner input = new Scanner(System.in)) {
			System.out.println("Enter temprature ex 10F or 10C");
			String a = input.nextLine();
			String val="";
			if(a.contains("F")) {
				int pos = a.indexOf("F");
				String aa = a.substring(0, pos);
				int tem = Integer.parseInt(aa);
				int val1=faratoceli(tem);
				val = val1+"C";
			}else if(a.contains("C")) {
				int pos = a.indexOf("C");
				String aa = a.substring(0, pos);
				int tem = Integer.parseInt(aa);
				int val1=celitofara(tem);
				val = val1+"F";
			}
			System.out.println(val);
		} catch (NumberFormatException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	public static int celitofara(int a) {
		float f = a*9;
		float f1 = f/5;
		float f2 = f1+32;
		int ff = Math.round(f2);
		return ff;
	}
	
	public static int faratoceli(int a) {
		float c = a-32;
		float c1 = c/9;
		float c2 = c1*5;
		int cc = Math.round(c2);
		return cc;
	}
}
