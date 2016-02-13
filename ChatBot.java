package com.allstate;

public class ChatBot {

    public int responseNum = 0;

    public String Diagnose(String input) {
        responseNum++;
        String initString = "ChatBot #" + Integer.toString(responseNum) + ": >>>";
        String response = "Not Implemented";

        return initString + response;
    }
}
