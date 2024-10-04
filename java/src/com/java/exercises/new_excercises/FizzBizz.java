package com.java.exercises.new_excercises;

public class FizzBizz {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		fizzbizz();
	}
	public static void fizzbizz() {
		for(int i=1; i<51; i++) {
			if(i%5 ==0 && i%3==0) {
				System.out.println("FizzBizz");
			}else if(i%3==0) {
				System.out.println("Fizz");
			}else if(i%5==0) {
				System.out.println("Bizz");
			}else {
				System.out.println(i);
			}
		}
	}

}
