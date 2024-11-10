use std::ffi::CString;
use zbus::{Connection, Result, dbus_proxy};
use nix::unistd::{pipe, write};
use zbus::zvariant::Fd;

#[dbus_proxy(
    interface = "cn.edu.ustc.lug.hack.FlagService",
    default_path = "/cn/edu/ustc/lug/hack/FlagService"
)]

trait FlagService {
    fn GetFlag1(&self, input: &str) -> Result<String>;
    fn GetFlag2(&self, input: Fd) -> Result<String>;
    fn GetFlag3(&self) -> Result<String>;
}

fn set_process_name(name: &str) {
    let c_name = CString::new(name).unwrap();
    unsafe {
        libc::prctl(libc::PR_SET_NAME, c_name.as_ptr() as usize, 0, 0, 0);
    }
}

#[tokio::main]
async fn main() -> Result<()> {
    let connection = Connection::system().await?;
    let proxy = FlagServiceProxy::new(&connection).await?;

    // Flag 1
    
    let flag1 = proxy.GetFlag1("Please give me flag1").await?;
    println!("{flag1}");

    // Flag 2

    let (read_fd, write_fd) = pipe().expect("Failed to create pipe");
    write(write_fd, b"Please give me flag2\n").expect("Failed to write to pipe");
    nix::unistd::close(write_fd).expect("Failed to close write end of pipe");

    let fd = Fd::from(read_fd);
    let flag2 = proxy.GetFlag2(fd).await?;
    println!("{flag2}");

    // Flag 3
    set_process_name("getflag3");
    let flag3 = proxy.GetFlag3().await?;
    println!("{flag3}");

    Ok(())

}