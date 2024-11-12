#include <gio/gio.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <sys/socket.h>

int main(void) {
    GError *error = NULL;
    GDBusConnection *connection;
    GVariant *result;

    // Connect to system bus
    connection = g_bus_get_sync(G_BUS_TYPE_SYSTEM, NULL, &error);
    if (error != NULL) {
        g_printerr("Failed to connect to system bus: %s\n", error->message);
        g_error_free(error);
        return 1;
    }

    // Create socketpair
    int sockets[2];
    if (socketpair(AF_UNIX, SOCK_STREAM, 0, sockets) == -1) {
        g_printerr("Failed to create socket pair\n");
        g_object_unref(connection);
        return 1;
    }

    // Write the required message to one end
    const char *message = "Please give me flag2\n";
    write(sockets[1], message, strlen(message));
    close(sockets[1]);  // Close write end

    // Create GUnixFDList with the read end of the socket
    GUnixFDList *fd_list = g_unix_fd_list_new();
    gint index = g_unix_fd_list_append(fd_list, sockets[0], &error);
    if (error != NULL) {
        g_printerr("Failed to append fd: %s\n", error->message);
        g_error_free(error);
        close(sockets[0]);
        g_object_unref(connection);
        return 1;
    }

    // Call GetFlag2 method
    result = g_dbus_connection_call_with_unix_fd_list_sync(
        connection,
        "cn.edu.ustc.lug.hack.FlagService",        // bus name
        "/cn/edu/ustc/lug/hack/FlagService",       // object path
        "cn.edu.ustc.lug.hack.FlagService",        // interface name
        "GetFlag2",                                // method name
        g_variant_new("(h)", index),               // parameters
        G_VARIANT_TYPE("(s)"),                     // reply type
        G_DBUS_CALL_FLAGS_NONE,
        -1,
        fd_list,                                   // fd_list
        NULL,                                      // out_fd_list
        NULL,
        &error);

    if (error != NULL) {
        g_printerr("Failed to call GetFlag2: %s\n", error->message);
        g_error_free(error);
        g_object_unref(fd_list);
        g_object_unref(connection);
        return 1;
    }

    // Extract and print the flag
    const gchar *flag;
    g_variant_get(result, "(&s)", &flag);
    printf("Flag2: %s\n", flag);

    // Cleanup
    g_variant_unref(result);
    g_object_unref(fd_list);
    g_object_unref(connection);
    close(sockets[0]);

    return 0;
}
