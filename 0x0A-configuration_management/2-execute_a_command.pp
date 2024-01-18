# manifest that kills a process named killmenow

exec { "killmenow":
    command  => "pkill -f killmenow",
    path     => ['/bin', '/usr/bin', '/sbin', '/usr/sbin'],
    provider => "shell",
    onlyif   => "pgrep -f killmenow",
    return_code => [0, 1],
}
