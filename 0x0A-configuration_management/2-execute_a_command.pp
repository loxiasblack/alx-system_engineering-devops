# creat a script that kill the process
exec { "killmenow":
    command => "pkill killmenow",
    path    => ['/bin', '/usr/bin', '/sbin', '/usr/sbin'],
}
