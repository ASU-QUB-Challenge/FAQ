package com.allstate;

import java.io.Console;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        // write your code here
        ChatBot chatBot = new ChatBot();

        System.out.println("Welcome to ChatBot v0.0");
        System.out.print("User: ");

        Scanner sc = new Scanner(System.in);

        while (sc.hasNextLine()) {
            String userInput = sc.nextLine();
            System.out.println(chatBot.Diagnose(userInput));
            System.out.print("User: ");
        }
    }
}
