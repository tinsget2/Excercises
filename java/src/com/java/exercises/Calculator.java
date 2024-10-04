package com.java.exercises;
import java.util.Scanner;

public class Calculator {
	public static void calculate() {
		try (Scanner input = new Scanner(System.in)) {
			System.out.println("Enter number");		
			float firstNum = input.nextFloat();
			int itrat = 1;
			
			while(itrat == 1){
				System.out.println("Enter operator ");	
				String oprat = input.next();
				char opr = oprat.charAt(0);
				if(opr == '+') {
					System.out.println("Enter another number " + firstNum + " " + opr);		
					float secNum = input.nextFloat();
					firstNum = addition(firstNum, secNum);
				}else if(opr == '-') {
					System.out.println("Enter another number "  + firstNum + " " + opr);		
					float secNum = input.nextFloat();
					firstNum = substraction(firstNum, secNum);
				}else if(opr == '*') {
					System.out.println("Enter another number "  + firstNum + " " + opr);		
					float secNum = input.nextFloat();
					firstNum = multiplication(firstNum, secNum);
				}else if(opr == '/') {
					System.out.println("Enter another number "  + firstNum + " " + opr);		
					float secNum = input.nextFloat();
					firstNum = division(firstNum, secNum);
				}
				System.out.println("To exit enter 0 to continue 1");	
				itrat = input.nextInt();
			}
			
			System.out.println(firstNum);
		}catch(Exception e) {
			System.out.println(e.getMessage());
		}
		
	}
	
	public static float addition(float num1, float num2) {
		float sum = num1 + num2;
		return sum;
	}
	
	public static float multiplication(float num1, float num2) {
		float product = num1 * num2;
		return product;
	}
	
	public static float substraction(float num1, float num2) {
		float sub = num1 - num2;
		return sub;
	}
	
	public static float division(float num1, float num2) {
		float quotient = num1 / num2;
		return quotient;
	}

}
