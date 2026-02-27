import java.util.Scanner;
import java.math.BigInteger;

public class RSA{
    public static void main(String a[]){
        //Step 1.1
        Scanner sc = new Scanner(System.in);
        int p =sc.nextInt();
        int q = sc.nextInt();
        //Step 1.2
        int n = p * q;
        //Step 1.3
        int phi = (p-1) * (q-1);
        System.out.println("phi = " + phi);
        //Step 1.4
        int e = 17;
        //Step 1.5 - we want the d such that (d * e) mod phi = 1
        int d = 0;   
        //Finding the d
        for (int i = 1; i < phi; i++){
            if((i * e) % phi == 1) {
                d = i;
                break;
            }
        }

        System.out.println("d = " + d);
        // Print keys
        System.out.println("Public Key (n, e): (" + n + ", " + e + ")");
        System.out.println("Private Key (n, d): (" + n + ", " + d + ")");

        int M = 65;
        System.out.println("Original message : "+M);

        int C = 1;
        for(int i = 0; i< e; i++){
            C = (C * M) % n;
        }

        System.out.println("The encrypted message :" + C);


        int decrypted = 1;
        for(int i = 0; i < d; i++){
            decrypted =( decrypted * C ) % n;
        }

        System.out.println("Decrypted Message (M): " + decrypted);

    }
}