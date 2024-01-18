#creat a script that kill the process

exec { "killmenow":
    command => "pkill -f killmenow",
    path    => '/usr/bin:/usr/sbin:/bin',
}
