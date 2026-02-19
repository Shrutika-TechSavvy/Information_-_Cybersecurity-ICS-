
public class RailFenceCipher {

    static String encrypt(String text, int r) {
        String cipher = "";
        int c = text.length();
        char[][] mat = new char[r][c];

        //Filling the matrix with placeholder
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                mat[i][j] = ' ';

            }
        }

        int temp = 0; //Row
        boolean down = true;

        for (int i = 0; i < c; i++) {
            mat[temp][i] = text.charAt(i);
            if (temp == 0) {
                down = true;
            } else if (temp == r - 1) {
                down = false;
            }

            if (down) {
                temp++;
            } else {
                temp--;
            }
        }

        //Reading the row wise
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (mat[i][j] != ' ') {
                    cipher += mat[i][j];
                }
            }
        }

        return cipher;
    }

    static String decrypt(String cipher, int r) {
        int c = cipher.length();
        char[][] mat = new char[r][c];

        //Fill the matrix with placeholder
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                mat[i][j] = ' ';
            }
        }

        //Marking the zigzag ptah
        int temp = 0;
        boolean down = true;

        for (int i = 0; i < c; i++) {

            mat[temp][i] = '*';

            if (temp == 0) {
                down = true; 
            }else if (temp == r - 1) {
                down = false;
            }

            if (down) {
                temp++; 
            }else {
                temp--;
            }
        }

        //filling the cipher text ro-wise
        int index = 0;
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (mat[i][j] == '*' && index < c) {
                    mat[i][j] = cipher.charAt(index++);
                }
            }
        }

        // read zig-zag to get original text
        String text = "";
        temp = 0;
        down = true;

        for (int i = 0; i < c; i++) {
            text += mat[temp][i];

            if (temp == 0) {
                down = true; 
            }else if (temp == r - 1) {
                down = false;
            }

            if (down) {
                temp++; 
            }else {
                temp--;
            }
        }

        return text;
    }

        public static void main(String[] args) {

        String text = "HELLOWORLD";
        int rails = 3;

        String encrypted = encrypt(text, rails);
        System.out.println("Encrypted: " + encrypted);

        String decrypted = decrypt(encrypted, rails);
        System.out.println("Decrypted: " + decrypted);
    }
}

