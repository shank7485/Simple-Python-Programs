import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class TimeConvert {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String time = in.next();
     
        if(time.charAt(8) == 'P'){
        	String numbr = "";
            int number = Integer.parseInt(Integer.toString(time.charAt(0) - 48) + Integer.toString(time.charAt(1) - 48)) + 12;
            numbr = "" + number;
            for(int i = 2; i < time.length() - 2; i++){
                numbr = numbr + time.charAt(i);
            }
            System.out.println(numbr);
        }
        
        else {
            String out = "";
            for(int i = 0; i < time.length() - 2; i++){
                out = out + time.charAt(i);
            }
            System.out.println(out);
        }
    }
}
