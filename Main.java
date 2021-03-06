package com.company;

public class Main {

    public static void main(String[] args) {
        int[][] arr = new int[4][4];
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                arr[i][j] = j + 1 + 4 * i;
                System.out.print(arr[i][j] + "\t");
            }
            System.out.println();
        }
        System.out.println("Hello");
        for (int j = 0; j <= arr.length; j++) {
            for (int i = 0; i < j; i++) {
                if (j % 2 == 0)
                    System.out.print(arr[j - i - 1][i] + " ");
                else
                    System.out.print(arr[i][j - i - 1] + " ");
            }
            System.out.println();
        }
        System.out.println();
        for (int j = arr.length - 1; j >= 0; j--) {
            for (int i = j - 1; i >= 0; i--) {
                if (j % 2 != 0)
                    System.out.print(arr[j - i + (arr.length - j - 1)][arr.length - (j - i)] + " ");
                else
                /*System.out.println("i = " + i + "; j = " + j);
                System.out.println(arr.length + "-1 - " + j + " + " + i);
                System.out.println(j + " - " + i);
                System.out.println("===============");
                int x = arr.length - 1 - (j - i);
                int y = j - i;
                System.out.println("x = " + x);
                System.out.println("y = " + y);
                System.out.println("--------------------");
*/
                    System.out.print(arr[arr.length - (j - i)][j - i + (arr.length - j - 1)] + " ");
            }
            System.out.println();
        }
    }
}
