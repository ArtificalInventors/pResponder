package com.example.presponder;

import android.app.Application;
import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.os.Build;

public class addnotif extends Application {
    public static final String  CHANNEL_1_ID = "mednotif";
    public static final String CHANNEL_2_ID = "panicnotif";

    @Override
    public void onCreate() {
        super.onCreate();

        createNotificationChannels();
    }

    private void createNotificationChannels(){
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O){
            NotificationChannel channel1 = new NotificationChannel(
                    CHANNEL_1_ID,
                    "Medication Channel",
                    NotificationManager.IMPORTANCE_DEFAULT
            );
            channel1.setDescription(""); // medical info fragment

            NotificationChannel channel2 = new NotificationChannel (
                    CHANNEL_2_ID,
                    "Emergency Channel",
                    NotificationManager.IMPORTANCE_HIGH
            );
            channel2.setDescription("");

            NotificationManager manager = getSystemService(NotificationManager.class);
            manager.createNotificationChannel(channel1);
            manager.createNotificationChannel(channel2);

        }
    }
}