package com.java.exercises;

public class AreaOfCircle {
	static double PI = Math.PI;
	public static void area(double rad) {		
		double area = PI * rad * rad;
		System.out.printf("Area of a circle is: %f", area);
	}
	
	public static void perimeter(double rad) {
		double peri = 2 * PI * rad;
		System.out.printf("Perimeter of a circle: %.2f", peri);
	}
}
