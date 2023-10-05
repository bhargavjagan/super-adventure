interface Notification {
    notifyUser(): void;
}

class SMSNotification implements Notification {
    public notifyUser(): void {
        console.log('notify use');
    }
}

class PushNotification implements Notification {
    public notifyUser(): void {
        console.log('notify push notification');
    }
}

class EmailNotification implements Notification {
    public notifyUser(): void {
        console.log('notify email notification');    
    }
}

abstract class NotificationFactory {
    abstract createNotification(): Notification;
    
}