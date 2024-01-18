# creat a script that kill the process
exec { "killmenow":
    command => "pkill -f killmenow",
    path    => ['/bin', '/usr/bin', '/sbin', '/usr/sbin'],
}
