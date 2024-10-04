package com.java.exercises;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Calendar;

public class DisplayDate {

	public static void dateDis() {
		DateFormat format = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");
		Calendar cal = Calendar.getInstance();
		System.out.println("Date is: " + format.format(cal.getTime()));
	}
}
