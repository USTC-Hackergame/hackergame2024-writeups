#include <gio/gio.h>
#include <stdio.h>

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
