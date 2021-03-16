

package Cryptography.javacodebad;

import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Scanner;

public class RSA {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        BigInteger N,phiN,e,d,m,c;

        // cipertext c, plaintext m

        System.out.println("Insert N");
        N = new BigInteger (sc.nextLine());

        System.out.println("Input e");
        e = new BigInteger (sc.nextLine());

        System.out.println("Input c");
        c = new BigInteger (sc.nextLine());

        System.out.println("Input phi");
        phiN = new BigInteger (sc.nextLine());

        sc.close();

        d = e.modInverse(phiN);
        m = c.modPow(d, N);

        System.out.println("d = "+d);           
        System.out.println("m = "+m);

        System.out.println("m in base 256 = "+base256(m));
        System.out.println("Convert with ASCII \n"+ Encode256(base256(m)));
    }
    static ArrayList<BigInteger> base256 (BigInteger M) {
        BigInteger base = new BigInteger("256");
        ArrayList<BigInteger> message256 = new ArrayList<BigInteger>();
        BigInteger sisa=M;
        BigInteger k;
        double z = Double.parseDouble(M.toString());
        double p = Math.floor(Math.log(z)/Math.log(256));
        int r = (int) p;
        for (int j=0;j<=r;j++){
            k=sisa.mod(base);
            sisa=sisa.divide(base);
            message256.add(k);
        }
        return message256;
    }

    static String Encode256 (ArrayList<BigInteger> ascii) {
        String ascii256="";
        int g;
        for (int i=0;i<ascii.size();i++) {
            g = Integer.parseInt(""+ascii.get(i));
            ascii256=ascii256+( (char) g );
        }
        return ascii256;
    }
}
